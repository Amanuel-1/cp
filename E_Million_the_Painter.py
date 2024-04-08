n = int(input())
s = input()
possible  =0


if possible==0:
    for i in range(n):
        j=i
        if i>0 and s[i-1]==s[i]:
            continue
        elif (s[i]=="?" and i==0) or (i>1  and s[i]=="?" and s[i-1]!=s[i] ):
            start = i-1
            while j<n and s[j]=="?":
                j+=1
            end  =j-1
            
            leng  = end-start+1

            if leng==1:
                
            elif leng>1:
                possible =True

if "?" not in s:
    possible=True
for i in range(1,len(s)-1):
    if s[i]!="?" and s[i]==s[i-1]:
        possible  =False
        break


if possible:
    print("Yes")
else:
    print("No")

            
    


        

# n = int(input())
# s = input()


# start,end  = 0,0
# possible  =-1
# pai  =0
# indi =0

# if possible==0:
#     i,j  = 0,0
#     while i<len(s):
#         j=i
#         if s[i]=="?":
#             if i==0:
#                 possible =True
                
#             start  =i-1 if i!=0 else i-1

            

#             while j<n and s[j]=="?":

#                 j+=1
            
#             end  =j-1
        
#             # if (s[start] ==s[end] and j-i+1 >2) or s[start]!=s[end]:
#             #     possible =True
#             # elif j-i+1 ==1:

#             leng  = j-i
#             print('lskdjfaslk')
#             if leng==1 and s[start]!=s[end]:
#                 possible =True
#             elif leng>1:
#                 possible =True
#             i=j
#         else:
#             i+=1
# for i in range(1,len(s)):
#     if s[i]!="?" and s[i]==s[i-1]:
#         possible= False
