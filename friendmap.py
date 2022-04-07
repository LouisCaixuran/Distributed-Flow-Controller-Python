# some pseudocodes about the friend map app

# person storage node
person_node = {
    name: "Alice",
    label_name: "xxx", # draw_map won't show this person's name in the map if protected
    address: "Madison, WI",
    label_address: "xxx", # draw_map won't show this person if 
    private_key: "xxx",
    public_key: "xxx"
}

# friends relationship storage node
relationship_node = {
    relationship: {
        "xxx": "xxx" # public key mapping
    },
    label: "xxx" # public
}

# intermediate result of friends storage node
result_node = {
    connected: ['xxx'], # public key list, friends connected with Alice
    label: "xxx"
}



def get_friend_map(public_key): # might use argv to get all the parameters
    # new result node
    result = {}
    result.connected = []
    result.label = 'public' # show it to everyone, even not friend

    for key in relationship_node.relationship: # access relationship storage node
        if key == public_key:
            result.connected += [relationship_node.relationship["key"]]


def draw_map(): # might use some visualization and take into consideration of different labels
    