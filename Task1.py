from flask import Flask,json,request,jsonify
app = Flask(__name__)

@app.route('/getcustomer')
def getcustomer():
    '''with open('customer.json')  as f:
        data = json.load(f)
        return { 'result': data}
    return {'result' : 'Nodata found'}'''
    resp = '''Failed START OF NEW DEBUGOM Debug file: /usr/tmp/l4010047.dbgom message is: This Customer's PO Number is referenced by another orderom message index is: 1om message is: Item with inventory_item_id=100000 is not defined in Item validation Org 707.om message index is: 2Failed'''
    if resp.find('Success') != -1:
        status = 'Success'
    elif resp.find('Failed') != -1:
        status = 'Failed'

    return status 

@app.route('/getcustomer1/<given_no>')
def getcustomer1(given_no):
    with open('customer.json')  as f:
        data = json.load(f)  
        print(data)
        print(type(data))                                                                                                                      
        print(data[0]['cno'])  
        res = [x for x in data if x['cno'] == given_no ]
        print(type(res))
        return { 'result': res}
    return {'result' : 'Nodata found'}

@app.route('/getcustomer2',methods=['GET','POST'])
def getcustomer2():
        obj = request.get_json()
        print(obj)
        return obj

if __name__ == "__main__":
    app.run(debug=True)