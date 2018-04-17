items = ["Derek", "Tesey", "Gabi", "Izzy", "Roxie", "Maui"]

def rehash(oldhash, table_size):
    return (oldhash+1) % table_size
#get the hash value for the string
def weighted_ord_hash(string, table_size):
    hash_val = 0
    for position in range(len(string)):
        hash_val = hash_val + (ord(string[position]) * position)
    return hash_val % table_size
#now that the hash value has been attained
#travers the list and place into the hash table
def lp_hash(item_list, table_size):
    #create table as dictionary object
    lp_hash_table = dict([(i,None) for i,x in enumerate(range(table_size))])
    #traverse through the dictionary list
    for item in item_list:
        i = weighted_ord_hash(item, table_size)
        #place into the current slot
        print("%s hashed == %s \n" %(item, i))
        if lp_hash_table[i] == None:
            lp_hash_table[i] = item
        #if slot is full:
        elif lp_hash_table[i] != None:
            #move item to the next available slot
            print("Collision, attempting linear probe \n")
            next_slot = rehash(i, table_size)
            print("Setting next slot to %s \n" % next_slot)
            while lp_hash_table[next_slot] != None:
                #if the next slot is not available it will try another slot
                next_slot = rehash(next_slot, len(lp_hash_table.keys()))
                print("Next slot was not empty, trying next slot %s \n" % next_slot)
            if lp_hash_table[next_slot] == None:
                lp_hash_table[next_slot] = item
    return lp_hash_table
#print the values and the has table
print(lp_hash(items, 6))