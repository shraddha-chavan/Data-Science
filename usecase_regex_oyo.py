import re
oyo_data='''
1. OYO12345 - Deluxe Room in Mumbai - 1500/night - 4.2
2. OYO67890 - Premium Suit in Delhi - 2500/night - 4.8
3. OYO54321 - Standard Room in Bengalore - 1200/night - 3.9
4. OYO09876 - Economy Room in Chennai -999/night - 4.2
'''
pattern=(r"(OYO\d+)\s-\s([\w\s]+)\sin\s([\w\s]+)\s-\s(\d+)/night\s-\s(\d\.\d)") 

'''
🔍 Explanation of the Pattern:

Group	             Pattern	Captures
1	OYO\d+	         OYO ID     (e.g., OYO12345)
2	[\w\s]+	         Room type  (e.g., Deluxe Room)
3	[\w\s]+	         City name  (e.g., Mumbai)
4	\d+	            Price per night   (e.g., 1500)
5	\d\.\d	        Rating (    e.g., 4.2)
'''
matches=re.findall(pattern,oyo_data)
for oyo_id, room_type, city, price, rating in matches:
    print(f"ID: {oyo_id} | Type: {room_type} | City: {city} | Price: {price} | Rating: {rating}")


########################################################################################################################################



