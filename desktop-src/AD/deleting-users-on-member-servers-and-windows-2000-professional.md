---
title: Deleting Users on Member Servers and Windows 2000 Professional
description: This topic shows how to delete a user from a member server or computer running on Windows 2000 Professional.
ms.assetid: 0c94c08b-46cb-494e-89f8-a21bfb20e34c
ms.tgt_platform: multiple
keywords:
- users AD , deleting a user on member servers and Windows 2000 Professional
- Active Directory, using, users, deleting users on member servers and Windows 2000 Professional
- deleting a user
- server, deleting a user
- deleting users on member servers and windows 2000 professional AD
ms.topic: article
ms.date: 05/31/2018
---

# Deleting Users on Member Servers and Windows 2000 Professional

This topic shows how to delete a user from a member server or computer running on Windows 2000 Professional.

**To delete a user**

1.  Bind to the computer using the following rules:
    1.  Use an account with sufficient rights to access that computer.
    2.  Use the following binding string format using the WinNT provider, computer name, and an extra parameter to tell ADSI that it is binding to a computer: "WinNT://\<computer name\>,&lt;computer&gt;". The "&lt;computer name&gt;" parameter is the name of the computer whose groups you want to access. This parameter notifies ADSI that it is binding to a computer and allows the WinNT provider parser to skip some ambiguity resolution queries to determine what type of object you are binding to.
    3.  Bind to the [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) interface.
2.  Specify "user" as the class using [**IADsContainer.Delete**](/windows/desktop/api/iads/nf-iads-iadscontainer-delete) to delete the user.

    Be aware that you do not need to call [**IADs.SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) to commit the change to the container. The [**IADsContainer.Delete**](/windows/desktop/api/iads/nf-iads-iadscontainer-delete) call commits the deletion of the user directly to the directory.

 

 
