from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hotel_booking_form():
    if request.method == 'POST':
        # Retrieve form data
        customer_name = request.form['customer_name']
        check_in_date = request.form['check_in_date']
        total_days = int(request.form['total_days'])
        total_persons = int(request.form['total_persons'])
        room_type = request.form['room_type']
        amenities = request.form.getlist('amenities')
        advance_amount = int(request.form['advance_amount'])

        # Room Rates and Additional Charges
        room_rates = {
            'Delux Room': 2500,
            'Suite Room': 4000
        }
        amenities_rates = {
            'AC': 1000,
            'Locker': 300
        }
        extra_person_charge = 1000

        # Calculate costs
        room_rate = room_rates.get(room_type, 0)
        amenities_cost = sum(amenities_rates.get(amenity, 0) for amenity in amenities)
        total_room_cost = room_rate * total_days
        total_amenities_cost = amenities_cost * total_days
        total_extra_cost=((total_persons)-2)*extra_person_charge
        total_cost = total_room_cost + total_amenities_cost + total_extra_cost
        balance = total_cost - advance_amount

        # Render the results
        return f'''
        <table border:1px solid black border-collapse: collapse>
            <h2>Hotel Booking Registration Form</h2><hr>
            <h3>Customer Info</h3><hr>
            <p>Customer Name: {customer_name}</p>
            <p>Check-in Date: {check_in_date}</p>
            <p>Total No of Days: {total_days}</p>
            <p>Total No of Persons: {total_persons}</p><hr>
            <h3>Room Information</h3><hr>
            <p>Room Type: {room_type}</p>
            <p>Amenities: {', '.join(amenities)}</p><hr>
            <h3>Advance Payment</h3><hr>
            <p>Advance Amount: {advance_amount}</p><hr>
            <h3>Total Cost Calculation</h3><hr>
            <p>Total Room Cost: {total_room_cost}</p>
            <p>Total Amenities Cost: {total_amenities_cost}</p>
            <p>Total Extra Cost: {total_extra_cost}</p>
            <p>Total Cost: {total_cost}</p><hr>
            <h3>Balance Amount</h3><hr>
            <p>Balance: {balance}</p><hr>
            </table>
        '''
    else:
        # Display the form
        return '''  
            <form method="POST">
            <style>
                table{
                    border:1px solid black;
                    border-collapse: collapse;
                }
                #tabA,#tabB,#tabC,#tabD {
                    background-color: black;
                    color: white;
                }
                .image {
                width: 1px;
                height: 1px;
            }
            </style>
            <table style="width: 100%" >
                <tr>
                    <th style="padding: 10px"><h2>Hotel Booking Registration Form</h2></th>
                </tr>
                </table><br>
                <table style="width: 100%" id="tabA">
                <tr>
                    <th style="padding: 10px"><h3>Customer Info</h3></th>
                </tr>
                </table><br>
                <center>
                <table style="width: 100%">
                <tr>
                <td style="padding: 10px"><label for="customer_name">Customer Name:</label></td> 
                <td style="padding: 10px"><input type="text" id="customer_name" name="customer_name" required>  text</td>
                </tr>
                <tr>
                <td style="padding: 10px"><label for="check_in_date">Check-in Date:</label></td>
                <td style="padding: 10px"><input type="date" id="check_in_date" name="check_in_date" required>  date</td>
                </tr>
                <tr>
                <td style="padding: 10px"><label for="total_days">Total No of Days:</label></td>
                <td style="padding: 10px"><input type="number" id="total_days" name="total_days" required>  number</td>
                </tr>
                <tr>
                <td style="padding: 10px"><label for="total_persons">Total No of Persons:</label></td>
                <td style="padding: 10px"><input type="number" id="total_persons" name="total_persons" required>  number</td>
                </tr>
                </table></center>
                <br>
                <table style="width: 100%" id="tabB">
                <tr>
                    <th style="padding: 10px"><h3>Room Type</h3></th>
                </tr>
                </table><br>
                <table >
                <tr>
                <table style="width: 100%">
                <tr>
                    <td ><center>
                    <img src=https://www.primoresorts.in/wp-content/uploads/2018/06/super-deluxe-room.jpg alt="Deluxe room" width="300" height="200">
                    <br>
                    <input type="radio" id="room_type" name="room_type" value="Delux Room">Delux Room
                    </center>
                    </td>
                    
                    <td><center>
                    <img src=data:image/jpeg;base64,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 alt="Suite room" width="300" height="200">
                    <br>
                    <input type="radio" id="room_type" name="room_type" value="Suite Room">Suite Room
                    </center>
                    </td>
                </tr>
                </table>
                <br>
                <table style="width: 100%" id="tabC">
                <tr>
                    <th style="padding: 10px"><h3>Room Amenities</h3></th>
                </tr>
                </table><br>
                <table style="width: 100%">
                <tr>
                    <td><center>
                    <img src=https://imgeng.jagran.com/images/2023/feb/Best%20AC%20Under%2045000%20In%20India1677590831379.jpg alt="A/C" width="300" height="200">
                    <br>
                    <input type="checkbox" id="ac" name="amenities" value="AC">
                    <label for="ac">AC</label></center>
                    </td>
                    
                    <td><center>
                    <img src=data:image/jpeg;base64,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 alt="Locker" width="300" height="200">
                    <br>
                    <input type="checkbox" id="locker" name="amenities" value="Locker">
                    <label for="locker">Locker</label></center>
                    </td>
                </tr>
                </table>

                <table style="width: 100%" id="tabD">
                <tr>
                    <th style="padding: 10px"><h3>Advance Payment</h3></th>
                </tr>
                </table><br>
                <center>
                <table style="width: 100%">
                <label for="advance_amount" style="padding-right: 5px">Advance Amount:</label>
                <input type="number" id="advance_amount" name="advance_amount" required>
                </table><br>
                </center>
                
                <center><input type="submit" value="Submit"></center>
            </form>
        '''

if __name__ == '__main__':
    app.run(debug=True)

