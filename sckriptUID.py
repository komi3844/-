with open('chitay.txt', 'r') as f, open("zapisi.sql", "w") as file:
    content = f.readlines()
    content = [x.strip() for x in content]
    print(len(content))
    for i in content:
        x = sep='\n'
        file.write(f"INSERT INTO ***** (***, ***, ***) VALUES ('{i}', '***','***');{x}".format(i, x))
