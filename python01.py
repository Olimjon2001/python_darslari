a=int(input("Istalgan raqamli  son kiriting\t:a="))
b=int(input("Istalgan raqamli son kiriting\t:b="))
yi=a+b # a va b sonlar yig'indisi
ko=a*b # a va b sonlar ko'paytmasi
ay=a-b # a va b sonlar ayermasi
bo=a/b # ikki son bo'linmasi
da=a**b # a sonni b inchi darajasi
mod=a%b # a sonni b ga bo'lgandagi qoldiq
bo=a//b # a sonni b ga bo'lgandagi bo'linma
model_a=abs(a-b) # a sonni b songa ayerganimizdagi model
model_b=abs(b-a) # b sonni a songa ayerganimizdagi model
a_type=type(a) # a sonni data type 
b_type=type(b)  # b sonni data type

print("a+b\t=",ay,"a*b\t=",ko,"a-b=",ay,"a/b=",bo,"a**b=",da,"qoldiq\t:",mod,"bo'linma\t:",bo)
print("a-b ni module\t:",model_a,"b-a sonni modeli\t:",model_b)
print("a sonni data type\t",a_type,"b sonni data type\t", b_type)





