
class solution(object):

   def totalparents(cls,input1,input2,input3):





       map2={}
       for i in range(input1):
           if  input3[i] in map2:
               map2[input3[i]]+=1

           else:
               map2[input3[i]]=1



       sum=0
       if input2==0:
           sum=sum+map2[-1]
       for k,v in map2.items():

            if   k!=-1 and v>=input2:
                sum=sum+1




       return sum






input1=int(input())
input2=int(input())
input3=[int(items) for items in input().split()]

s=solution()

print(s.totalparents(input1,input2,input3))

