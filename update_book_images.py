from pathlib import Path

root = Path('C:/Users/HP/Photo-Lab/ECommerce-SOAP-MERN')
src = Path(r'C:\Users\HP\OneDrive\Desktop\Books\books_collection\img')
dst = root / 'images' / 'book-covers'
dst.mkdir(parents=True, exist_ok=True)
files = list(src.glob('*.png'))
print('Found', len(files), 'cover files')
for f in files:
    target = dst / f.name
    target.write_bytes(f.read_bytes())
print('Copied cover images to', target.parent)

mapping = {
    1: 'To_Kill_a_Mockingbir_1.png',
    2: '1984_2.png',
    3: 'Pride_and_Prejudice_3.png',
    4: 'The_Great_Gatsby_4.png',
    5: 'Moby-Dick_5.png',
    6: 'The_Hobbit_6.png',
    7: 'Harry_Potter_and_the_7.png',
    8: 'The_Catcher_in_the_R_8.png',
    9: 'The_Alchemist_9.png',
    10: 'The_Da_Vinci_Code_10.png',
    11: 'The_Lord_of_the_Ring_11.png',
    12: 'Brave_New_World_12.png',
    13: 'The_Kite_Runner_13.png',
    14: 'Life_of_Pi_14.png',
    15: 'The_Book_Thief_15.png',
    16: 'The_Hunger_Games_16.png',
    17: 'The_Fault_in_Our_Sta_17.png',
    18: 'Gone_Girl_18.png',
    19: 'The_Chronicles_of_Na_19.png',
    20: 'Dracula_20.png',
    21: 'Frankenstein_21.png',
    22: 'The_Odyssey_22.png',
    23: 'Crime_and_Punishment_23.png',
    24: 'War_and_Peace_24.png',
    25: 'The_Shining_25.png',
}
for filename in ['soap-simple.html', 'product-detail.html']:
    path = root / filename
    text = path.read_text(encoding='utf-8')
    for book_id, file_name in mapping.items():
        size = '420/560' if filename == 'soap-simple.html' else '900/1200'
        old = f'https://picsum.photos/seed/book{book_id}/{size}'
        new = f'images/book-covers/{file_name}'
        text = text.replace(old, new)
    path.write_text(text, encoding='utf-8')
    print('Updated', filename)
