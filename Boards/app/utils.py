def getGroup(user):
    if user.groups.filter(name="Admin").count() > 0:
        usergroup = "Admin"
    elif user.groups.filter(name="Moderator").count() > 0:
        usergroup = "Moderator"
    else:
        usergroup = "User"
    return usergroup
