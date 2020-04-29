def co(arr,elm,l,r,sc=-1):
    mid=l+(r-l)/2
    if elm == arr[mid] and sc==-1:
        co(arr,elm,l)
    if elm==arr[mid] and arr[mid-1]!=arr[mid] and sc==1:
