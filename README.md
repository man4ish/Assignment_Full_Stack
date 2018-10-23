Task1.
Algorithm Used for fragments assembler
1. Find the maximum overlaps between all possible pairs of fragments (ignore self pairing).
2. Store the overlaps in dictionary of amount of overlaps between pairs and value (fragment1, fragement2 , start position of overlap on fragment1).
3. Pick the overlap with maximum amount from dictionary and join the fragments.
4. convert the urlendoded string into normal string.

Usage: 
python merge_fragment_assembler.py 	&lt; infile	&gt; <br>
 
or
<br>

python merge_fragment_assembler.py <br>
Enter fragments:

Task2. webservice task

(1) To start the web service <br>
python merge_fragment_webservice.py <br><br>
(2) To get the output:
curl http://localhost:5000/todos --data-urlencode "output=&lt;fragments&gt;" -X POST -v    (Please refer to run.sh script) <br>
click on http://localhost:5000/todos to get the response on web.


Tests:
<br><br>
Task1. Java shuffled text
<br>
python merge_fragment_assembler.py  Java_shuffled_.txt
<br>
Output:<br>
// Sample program <br>
public class HelloWorld {<br>
    public static void main(String[] args) {<br>
        // Prints "Hello, World" to the terminal window.<br>
        System.out.println("Hello, World");<br>
    }<br>
}<br>

Similarly it works for shakeshpere and lpsum txt while with pyhton shuffled text output is bit shuffled.
