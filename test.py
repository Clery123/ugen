import sys
import subprocess
import io
def test(arg1, arg2):
    print(arg1)
    print(arg2)
    lstF = ['1234:Jozef:Miloslav:Hurban:Legal','4567:Milan:Rastislav:Stefanik:Defence','4563:Jozef::Murgas:Development']
    listA = ['123:123:123','222:113:aaa:aaa','555:555:555:555']
    with open(arg2, 'w') as f: #fill test data with correct inputs
        for li in lstF:
            f.write(li+'\n')
        f.close()

    p = subprocess.run('py '+arg1+' -o output.txt '+arg2, shell=True) #run script
    fil = open(arg2, "r")
    listTemp = []

    for x in fil: 
        listTemp.append(x)
    fil.close()

    with open('test_report.txt','w') as j: #fll report with data
        for li in listTemp:
            j.write(li+'\n')
        j.close()

    with open(arg2, 'w') as f: #fill test data with random input
        for li in listA:
            f.write(li+'\n')
        f.close()
    
    p = subprocess.getoutput('py '+arg1+' -o output.txt '+arg2) #run script and get output
    with open('test_report.txt','a') as j: #append report with data
        j.write(p)
        j.close()    



if __name__ == "__main__":
    test(sys.argv[1], sys.argv[2])