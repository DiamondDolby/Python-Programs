def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    total_adult_cost = no_of_adults * 37550.0
    total_children_cost = no_of_children * 37550.0 * 1/3
    
    total_ticket_cost_before_discount = (total_adult_cost + total_children_cost) * 1.07
    
    total_ticket_cost = total_ticket_cost_before_discount * 0.9
    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program

# total_ticket_cost=calculate_total_ticket_cost(5,2)

total_ticket_cost=calculate_total_ticket_cost(3,1)

print("Total Ticket Cost:",total_ticket_cost)   
