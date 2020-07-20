orig_list = ['300', '2', '12', '44', '1', '1', '4', '10', '7', '1', '78', '123', '55']
new_list = [orig_list[i] for i in range(1, len(orig_list)) if int(orig_list[i - 1]) < int(orig_list[i])]
print(f'Original list: {orig_list}')
print(f'New list: {new_list}')