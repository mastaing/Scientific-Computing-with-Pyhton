def arithmetic_arranger (problems,answer=False) :
    if len(problems) > 5 :
        
        return "Error: Too many problems."
    else :   
        
        for line in problems:    
            if "/"  in line :
                
                return  "Error: Operator must be '+' or '-'."
                
            elif "*" in line :
                
                return  "Error: Operator must be '+' or '-'."
                            
            else :
                parts = line.replace(" ","").split("+")
                if len(parts) != 2 :
                    parts = line.replace(" ","").split("-")
                
                
                operand1, operand2 = parts 
                try :
                    int(operand1) and int(operand2)

                except :
                    
                    return "Error: Numbers must only contain digits."
                    
                if len(operand1) > 4 or len(operand2) > 4 :
                    
                    return "Error: Numbers cannot be more than four digits."

                
        
        
        
        
        first_line = ""
        second_line = ""
        last_line = ""
        answer_line = ""
               

        for i in problems :
            
            parts = i.split()
            
            operands1 = parts[0]
            operator = parts[1]
            operands2 = parts [2]
            
            if operator == "+" :
                result = int(operands1) + int(operands2)
                result = str(result)
            else :
                result = int(operands1) - int(operands2)
                result = str(result)

            big_operands = max(len(operands1), len(operands2)) 
            
                
            first_line += operands1.rjust(big_operands+2) + "    "
            second_line += operator + " " + operands2.rjust(big_operands) + "    "
            last_line += "-" * (big_operands + 2) + "    "
            answer_line += result.rjust(big_operands + 2) + "    "
    
    if answer == False : 
        
        arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + last_line.rstrip()

    else :
        arranged_problems = arranged_problems = first_line.rstrip() + "\n" + second_line.rstrip() + "\n" + last_line.rstrip() + "\n" + answer_line.rstrip()

    return arranged_problems



                      
                
print(arithmetic_arranger(['98 + 3g5', '3801 - 2', '45 + 43', '123 + 49']))
            

