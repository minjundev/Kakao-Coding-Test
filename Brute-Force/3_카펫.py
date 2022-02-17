def solution(brown, yellow):
    area = brown + yellow
    row = 2
    while True :
        row += 1
        col = row
        while row*col <= area :
            if row*col == area and brown == 2*(col + row-2) :
                return [col,row]
            col += 1
