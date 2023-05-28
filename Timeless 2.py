import csv
import os
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from difflib import SequenceMatcher
import datetime
# Open the first CSV file
with open("Online Store Items Sales.csv") as f:
    # Read the contents of the CSV files
    csv_reader1 = csv.reader(f)
    header1 = next(csv_reader1)

# Open the second CSV file
with open("Online Store Project Items for Sale ALTERNATIVE SHOP A.csv") as f:
    # Read the contents of the CSV file
    csv_reader2 = csv.reader(f)
    header2 = next(csv_reader2)

# Open the third CSV file
with open("Online Store Project Items for Sale ALTERNATIVE SHOP B.csv") as f:
    # Read the contents of the CSV file
    csv_reader3 = csv.reader(f)
    header3 = next(csv_reader3)
   

# Open the fourth CSV file
with open("Online Store Project Items for Sale.csv") as f:
    # Read the contents of the CSV file
    csv_reader4 = csv.reader(f)
    header4 = next(csv_reader4)

# Open the fifth CSV file
with open("Online Store Project Sets of Items for Sale.csv", encoding = 'utf-8') as f:
    # Read the contents of the CSV file
    csv_reader5 = csv.reader(f)
    header5 = next(csv_reader5)


app = Flask(__name__)
@app.route('/')
def index():    
 print(all)
 return render_template('index.html', results=all, results2 = all2)


def search_query(query):
    results = search_csv(query)
    
    # Print search results
    if not results:
        return None
    results_list = []
    for i, (filename, header, matches) in enumerate(results):
        match_info = (i+1, filename, header, matches)
        results_list.append(match_info)
    return results_list

            
@app.route('/search', methods=['POST'])
def search():
    
        # Call search_query() with input data
    results = search_query(request.form['search_input']
)
    print(results)
    
    return render_template('search_results.html', results=results, enumerate=enumerate)


def search_file(filename, query):
    with open(filename) as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader) # Skip the header row
        matches = []
        for row in csv_reader:
            if any(query.lower() in cell.lower() for cell in row):
                matches.append(row)
        return header, matches 


def search_csv(query):
    csv_files = ["Online Store Items Sales.csv",
                "Online Store Project Items for Sale ALTERNATIVE SHOP A.csv",
                "Online Store Project Items for Sale ALTERNATIVE SHOP B.csv",
                "Online Store Project Items for Sale.csv",
                "Online Store Project Sets of Items for Sale.csv"]
    all_matches = []
    for filename in csv_files:
        if not os.path.exists(filename):
            print(f"File {filename} not found.")
            continue
        header, matches = search_file(filename, query)
        if matches:
            all_matches.append([filename, header, matches])
    return all_matches

def search_csv4(query):
    filename = "Online Store Project Items for Sale.csv"
    header, matches = search_file(filename, query)
    all_matches=[]
    all_matches.append([filename, header, matches])
    return all_matches 

def search_csv5(query):
    filename = "Online Store Project Sets of Items for Sale.csv"
    header, matches = search_file(filename, query)
    all_matches=[]
    all_matches.append([filename, header, matches])
    return all_matches 



@app.route('/add_items', methods=['POST'])
def add_items():
    print(request.form)
    file = request.form.get('file_to_append_to')
    if '1' in file:
        print(request.form)
        print("i")
        add_items1(request)
    if '2' in file:
        print(request.form)
        print("n")
        add_items2(request)
    if '3' in file:
        print(request.form)
        print("g")
        add_items3(request)
    if '4' in file:
        print(request.form)
        print("e")
        add_items4(request)
    return redirect(url_for('index'))
        

def add_items1(request):
    print("hello2")
    item_id=[]
    item_id.append(request.form.get('item.id'))
    # Iterate over each CSV file
    with open("Online Store Items Sales.csv", mode='a', newline='') as file:
        # Create a CSV writer
        csv_writer = csv.writer(file)
        csv_writer.writerow(item_id)


def add_items2(request):
    print("hello3")
    item_id=[]
    item_id.append(request.form.get('item.id'))
    with open("Online Store Project Items for Sale ALTERNATIVE SHOP A.csv", mode='a', newline='') as file:
        # Create a CSV writer
        csv_writer = csv.writer(file)
        csv_writer.writerow(item_id)


def add_items3(request):
    print("hello4")
    item_id=[]
    item_id.append(request.form.get('item.id'))

    with open("Online Store Project Items for Sale ALTERNATIVE SHOP B.csv", mode='a', newline='') as file:
        # Create a CSV writer
        csv_writer = csv.writer(file)
        csv_writer.writerow(item_id)



def add_items4(request):
    print("hello")
    item_id = request.form.get('item.id')
    item_desc = request.form.get('item.desc')
    item_price = request.form.get('item.price')
    item_list = [item_id, item_desc, item_price]
                        
    with open("Online Store Project Items for Sale.csv", mode='a', newline='') as file:
        # Create a CSV writer
        csv_writer = csv.writer(file)
        csv_writer.writerow(item_list)
    all[0][2].append(item_list)

    
@app.route('/add_sets', methods=['POST'])
def add_sets():     
    set_id= request.form.get('set-id')
    set_desc = request.form.get('set-desc')
    set_price = request.form.get('set-price')
    iset_no = request.form.get('iset-no')
    items_ids = request.form.get('items-id')
    additional_items = []
    for key, value in request.form.items():
        if key.startswith('add-id'):
            additional_items.append(value)
    set_list = [set_id, set_desc,set_price,iset_no, items_ids, additional_items]
    with open("Online Store Project Sets of Items for Sale.csv", mode='a', newline='') as file:
        # Create a CSV writer
        csv_writer = csv.writer(file)
        # Write the new set to the CSV file
        csv_writer.writerow(set_list)
    all2[0][2].append(set_list)
    # Add a confirmation message to be displayed to the user
    return redirect(url_for('index'))


 
def delete(filename, id):
    tempfile = filename + '.temp'
    with open(filename, 'r') as f, open(tempfile, 'w', newline='') as temp:
        reader = csv.reader(f)
        writer = csv.writer(temp)
        header = next(reader)
        writer.writerow(header)
        for row in reader:
            if row and row[0] != id:
                writer.writerow(row)
    os.remove(filename)
    os.rename(tempfile, filename)


@app.route('/delete_item', methods=['POST'])

def delete_item():
    id_to_delete = request.form.get('delete_id')
    temp_id = id_to_delete
    with open('Online Store Project Items for Sale.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip the header row
        for row in reader:
            if row[0] == temp_id:
                description = row[1]
                price = row[2]
                break
        best_match_id = None
        best_match_score = 0
        excluded_ids = [12517, 12540, 12542, 12717, 12719, 12722, 12725, 12704, 12705, 12706, 12707, 12709, 12584, 12589, 12591]
        for row in reader:
            if int(row[0]) in excluded_ids:
                continue
            seq_matcher = SequenceMatcher(None, description, row[1])
            #description_similarity = fuzz.ratio(description, row[1])
            #price_similarity = fuzz.ratio(price, row[2])
            price_similarity = SequenceMatcher(None, price, row[2])
            similarity_score = seq_matcher.ratio() + price_similarity.ratio()
            if similarity_score > best_match_score and int(row[0]) not in excluded_ids:
                best_match_score = similarity_score
                best_match_id = row[0]
                
    csv_files = ["Online Store Items Sales.csv",
                "Online Store Project Items for Sale ALTERNATIVE SHOP A.csv",
                "Online Store Project Items for Sale ALTERNATIVE SHOP B.csv",
                "Online Store Project Items for Sale.csv",
                "Online Store Project Sets of Items for Sale.csv"]
    for filename in csv_files:
        if not os.path.exists(filename):
            continue
        if filename == "Online Store Project Sets of Items for Sale.csv":
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
            for row in range(len(data)):
                for col in range(len(data[row])):
                    if data[row][col] == id_to_delete:
                        data[row][col] = best_match_id
            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        elif filename == "Online Store Items Sales.csv":
            with open(filename, 'r') as f:
                reader = csv.reader(f)
                data = list(reader)
            for row in range(len(data)):
                if row == 0:  # Skip the header row
                    continue
                if data[row][0] == id_to_delete:
                    current_date = datetime.datetime.now().strftime('%d/%m/%Y')
                    data[row][1] = current_date

            with open(filename, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(data)
        else:
            delete(filename, id_to_delete)

    return redirect(url_for('index'))


@app.route('/delete_set', methods=['POST'])
def delete_set():
    set_id = request.form.get('set-id')
    filename = "Online Store Project Sets of Items for Sale.csv"
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        rows = []
        for row in reader:
            if row[0] == set_id:
                continue  # skip the row if the value matches the first column
            rows.append(row)
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return redirect(url_for('index'))


#delete_item_from_csv()
if __name__ == '__main__':
    all = search_csv4("")  
    all2 = search_csv5("")
    app.run(debug=True)
    
