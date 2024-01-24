---
title: Creating Local Groups
description: Only local groups can be created for member servers and Windows 2000 Professional.
ms.assetid: 76cbac51-d8ba-4114-9951-060273be52f3
ms.tgt_platform: multiple
keywords:
- Creating Local Groups AD
ms.topic: article
ms.date: 05/31/2018
---

# Creating Local Groups

Only local groups can be created for member servers and Windows 2000 Professional.

**To create a local group for a member server or computer running Windows 2000 Professional**

1.  Bind to the computer using the following rules:
    1.  Use an account with sufficient rights to access that computer.
    2.  Use the following binding string format using the WinNT provider, computer name, and an extra parameter to instruct ADSI that it is binding to a computer: "WinNT://\<computer name\>,&lt;computer&gt;".

        The "&lt;computer name&gt;" parameter is the name of the computer groups to access.

        In the binding string, the "&lt;computer&gt;" parameter instructs ADSI that it is binding to a computer. ADSI makes this data available to the WinNT provider's parser so that it can skip some ambiguity-resolution queries to determine what type of object you are binding to.

    3.  Bind to the [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) interface.

2.  Specify "localGroup" as the class using [**IADsContainer.Create**](/windows/desktop/api/iads/nf-iads-iadscontainer-create) to add the group.
    > [!Note]  
    > If you specify "group" as the class, ADSI uses "localGroup". Do not specify the class as "globalGroup". Groups of class "globalGroup" cannot be created on member servers or a computer running Windows NT Workstation/Windows 2000 Professional. If you specify "globalGroup", [**IADsContainer.Create**](/windows/desktop/api/iads/nf-iads-iadscontainer-create) creates the group in the property cache, but [**IADs.SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo) does not write the group to the security database and it does not return an error.

     

3.  Write the group to the computer security database using [**IADs.SetInfo**](/windows/desktop/api/iads/nf-iads-iads-setinfo).

 

 
