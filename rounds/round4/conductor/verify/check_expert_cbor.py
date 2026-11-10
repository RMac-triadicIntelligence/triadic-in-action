import hashlib,sys
hx="b818000101000200030004f6054006400782000008f6098200000a8200000bf60cf60df60e000ff61082000011f6120013f6140115001682000017f6"
b=bytes.fromhex(hx)
print("len",len(b))
print("sha(tag||cbor)",hashlib.sha256(b"RNR07:STATE:"+b).hexdigest())
print("sha(cbor)",hashlib.sha256(b).hexdigest())
print("sha(tag-no-colon||cbor)",hashlib.sha256(b"RNR07:STATE"+b).hexdigest())
# minimal decode of the top-level map
i=0
def head(i):
    ib=b[i]; mj=ib>>5; ai=ib&31; i+=1
    if ai<24: return mj,ai,i
    n={24:1,25:2,26:4,27:8}[ai]; return mj,int.from_bytes(b[i:i+n],'big'),i+n
def item(i):
    mj,n,i=head(i)
    if mj==0: return n,i
    if mj==1: return -1-n,i
    if mj in(2,3): return b[i:i+n],i+n
    if mj==4:
        out=[]
        for _ in range(n): v,i=item(i); out.append(v)
        return out,i
    if mj==5:
        d={}
        for _ in range(n):
            k,i=item(i); v,i=item(i); d[k]=v
        return d,i
    if mj==7: return {20:False,21:True,22:None}[n],i
v,j=item(0); print("decoded",v); print("consumed",j,"of",len(b))
