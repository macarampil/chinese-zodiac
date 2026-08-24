 Annex B 
Computational Thinking Exercise: "Smart Vending Machine" 
Section:          Sodium                                                  Score:____________
 C# / Name:   Maria Carampil, Erikah Zozobrado, Eziah Baylon 
 Date:    8/20/2026   
Scenario 
Your school installs a vending machine to provide snacks and drinks. However, students encounter several issues: 
● Sometimes the machine does not give the correct change. ● Items run out, but the machine doesn’t notify anyone. 
● Students press the wrong buttons and get the wrong item. 
● The machine is slow when multiple students use it in succession. 
Your task is to decompose this problem into smaller, manageable parts that could be solved with computational thinking (CT) Skills. 


Step 1: Identify the Big Problem 
Main Problem:  The machine does not work properly and efficiently.
 Step 2: Identify three to four Sub-Problems 
Please list possible sub-problems: 
5. The machine does not indicate when products are out of stock or when it is empty. 

6. The machine becomes slow or laggy when many students use it consecutively. 

7. The machine does not have a proper program to calculate and give the correct/exact change. 

8. The machine does not have a cancel or order-confirmation option to prevent students from accidentally purchasing the wrong item. 


Step 3: Define Computational Thinking Approaches 
For each sub-problem, apply CT skills:
Sub-Problem 
CT Skill 
Example Solution
The machine does not indicate when products are out of stock or when it is empty.
Pattern Recognition
The machine can keep track of how many items are left, when there are no more items, it can automatically show an “Out of Stock” message.
The machine becomes slow or laggy when many students use it consecutively.
Decomposition 
The machine can divide its tasks into smaller parts, like accepting the payment, checking the order, and giving the item. This can help the machine work faster and avoid becoming too slow.
The machine does not have a proper program to calculate and give the correct/exact change.
Algorithm Design 
The machine can follow a simple step-by-step process, it checks how much money the student paid, compares it with the item's price, and then calculates and gives the correct change.
The machine does not have a cancel or order-confirmation option to prevent students from accidentally purchasing the wrong item.
Abstraction 
The machine can show the selected item and its price before the purchase, it can also have “Confirm” and “Cancel” buttons so students can check their order before buying.



Step 4: Draw a flowchart or write a pseudocode for the identified sub-problem (Your group could use a separate sheet of paper)

START

Display "Welcome to the Vending Machine"

Check if the selected item is available

IF the item is not available THEN
    Display "Out of Stock"
    Ask the student to choose another item
    RETURN to the main menu

ELSE
    Display the selected item and its price
    Ask the student to confirm the order

    IF the student chooses CANCEL THEN
        Display "Order Cancelled"
        RETURN to the main menu

    ELSE
        Ask the student to enter payment

        IF payment is less than the item price THEN
            Display "Insufficient Payment"
            Return the payment
            Ask the student to try again

        ELSE
            Calculate change = payment - item price
            Give the correct change
            Give the selected item
            Display "Thank you for your purchase!"

            Update the number of items remaining

            IF no items are left THEN
                Display "Out of Stock"
            END IF

        END IF
    END IF
END IF

END




Rubrics For Grading 
Total Points: 20pts 
Criteria & Levels of Performance 
Criteria 
Excellent (4) 
Good (3) 
Fair (2) 
N.I. (1)
Identification of 
Sub-Problem s
Identifies 3+ clear, relevant 
sub-problems that directly connect to the scenario.
Identifies 2–3 mostly relevantsub-problems.
Identifies 1–2 vague or 
partially 
relevant 
sub-problems.
Struggles to identify 
sub-problems or lists 
unrelated 
issues.
Application ofCT Strategies
Correctly applies appropriate CT strategies 
(abstraction, 
decomposition, pattern recognition, algorithm design) to each 
sub-problem with clear reasoning.
Applies CT 
strategies to most 
sub-problems, with minor 
errors or 
limited 
explanation.
Applies CT 
strategies 
inconsistently, with weak or unclear 
reasoning.
Rarely appliesCT strategies or misuses 
them.
Flowchart / Pseudocode 
X 2
Flowchart / 
Pseudocode is 
complete, logical, and easy to follow; shows clear steps and decision 
points.
Flowchart / 
Pseudocode ismostly 
complete and logical, with minor gaps or unclear steps.
Flowchart / 
Pseudo Code ispartially 
complete, 
missing key 
steps or 
connections.
Flowchart / 
Pseudocode is incomplete, confusing, or missing 
entirely.
Reflection / Explanation
Provides thoughtful reflection on how decomposition 
helps 
problem-solving and identifies CT skills used with strong justification.
Provides 
adequate 
reflection with some 
justification of CT skills.
Provides limitedreflection with weak or genericjustification.
Provides 
minimal or no reflection.
 



