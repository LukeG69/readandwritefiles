def main():
    infile = open('clients.txt', 'r')

    n = 1

    for line in infile:
        
        print(str(n) + '. ' + line.rstrip())
        n = n + 1
    
    infile.close

main()