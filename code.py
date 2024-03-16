l,r=0,len(h)-1
s=0
while l<r:
  area=(r-l)*min(h[l],h[r])
  s=max(area,s)
  if h[l]<h[r]:
    l+=1
  else:
    r-=1
