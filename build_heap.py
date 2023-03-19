# python3

def build_heap(data):
    swaps = []
    # TODO: Creat heap and heap sort
    for i in range((len(data))//2,-1,-1):
        while True:
            lb=2*i+1
            kr=2*i+2
            minim=i
            if lb<len(data) and data[lb]<data[minim]:
                minim=lb
            if kr<len(data) and data[kr]<data[minim]:
                minim=kr
            if minim!=i:
                data[i],data[minim]=data[minim],data[i]
                swaps.append((i,minim))
            if minim==i:
                break
    # try to achieve  O(n) and not O(n2)
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    text=input("ievadi I vai F:")
    if 'F' in text:
        fails=input("faila nosaukums:")
        with open("./tests/" + fails) as f:  
                    n = int(f.readline())
                    data = list(map(int, f.readline().split()))
                     
    # input from keyboard
    elif 'I' in text:
        n = int(input())
        data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
