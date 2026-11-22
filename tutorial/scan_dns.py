#!/data/data/com.termux/files/usr/bin/python
#Created By Bebey
#pip install dnspython

#=========================
import dns.resolver

domain = "example.com"

res = dns.resolver.Resolver(configure=False)
res.nameservers = ["8.8.8.8"]

results_ipv4 = res.resolve(domain,"A")

for _ipv4 in results_ipv4:
    print(_ipv4)


'''
"A" = mencari ipv4
"AAAA" = mencari ipv6
"NS" = mencari name server
"MX" = mencari mail server
"TXT" = menampilkan informasi TXT
"SOA" = informasi administrasi DNS zone
"PTR" = reverse dns (ip ke hostname)
"CNAME" = menampilkan alias domain
"SRV" = informasi layanan dan port
"CAA" = menentukan CA yg di di izinkan menerbitkan sertifikat
'''
