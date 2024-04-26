# copy,clear,pop,get,uptade,items,values,keys

t={}
t["ism"]="Bekzod"
w=t.copy()
t["yosh"]=13
# w.clear
w={"ism":"Bekzod","yosh":13,"friend":"Akmal"}
ism=w.pop("ism")
print(ism) #"Bekzod"

#get: malumot olish 2xil
#1 xil sodaroq usul
print(w["ism"])
print(w["yosh"])
# print(w["sinf"]) #error,chunki w ni ichida "sinf" degan key yoq

#2xil ->get() bilan-> yaxshiroq usul
print(w.get("ism"))
print(w.get("yosh"))
print(w.get("sinf")) #None,chunki ichida "sinf"degan key yoq
print(w.get("maktab","58-maktab"))
print(w.get("friend","Alex"))


l={"ism":"lutfullo","familiya":"to\'rayev","kasb":"futbolist"}

#keys
print(l.keys()) #["ism","familiya","kasb"]
#values
print(l.values()) #["lutfullo","to\'rayev","futbolist"]
#items->(keys,values)
print(l.items()) #[("ism":"lutfullo","familiya":"to\'rayev","kasb":"futbolist")]
e