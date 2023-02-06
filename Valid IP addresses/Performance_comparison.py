import timeit
from valid_IP_generator import construct_all_valid_IPs
from ChatGPT_solution import restoreIpAddresses

# Provide a random list of possible inputs
list_of_possible_inputs: list = ["00222", "21345698", "09123675", "56812154", "5052", "7854236", "78", "75934", "098453", "2132504537"]
tot_time_mine: float = 0.0
tot_time_gpt: float = 0.0

# For each of the inputs, calculate the time taken by the two functions
for input in list_of_possible_inputs:
  tot_time_mine += timeit.timeit(lambda: construct_all_valid_IPs(input), number=10000)
  tot_time_gpt += timeit.timeit(lambda: restoreIpAddresses(input), number=10000)
  # If there is a mismatch between the two outputs, signal a problem
  if not construct_all_valid_IPs(input).sort() == restoreIpAddresses(input).sort():
    print("Something went wrong")

print(f"Total time taken by my code is {tot_time_mine} seconds.")  
print(f"Total time taken by GPT's code is {tot_time_gpt} seconds.") 