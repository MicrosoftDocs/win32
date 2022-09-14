---
title: Enumerating Local Groups
description: On member servers and computers running on Windows 2000 Professional, you can enumerate all local groups.
ms.assetid: edbabbe5-13e1-42f6-8e73-f8e18ba4866b
ms.tgt_platform: multiple
keywords:
- Enumerating Local Groups AD
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Local Groups

On member servers and computers running on Windows 2000 Professional, you can enumerate all local groups.

Only local groups can be created on member servers and Windows 2000 Professional. However, those local groups can contain:

-   Universal and Global groups from the forest that contains the domain to which the computer is a member.
-   Domain local groups from that computer's domain.
-   Users from any domain in the forest.

**To enumerate the local groups on a member server or computer running Windows 2000 Professional**

1.  Bind to the computer using the following rules:
    1.  Use an account with sufficient rights to access that computer.
    2.  Use the following binding string format using the WinNT provider, computer name, and an extra parameter to instruct ADSI that it is binding to a computer: "WinNT://\<computer name\>,&lt;computer&gt;".

        "The \<computer name\>" parameter is the name of the computer group to access. This parameter instruct ADSI that it is binding to a computer and allows the WinNT provider's parser to skip some ambiguity-resolution queries to determine what type of object you are binding to.

    3.  Bind to the [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) interface.

2.  Set a filter that contains "groups" using the [**IADsContainer.Filter**](/windows/desktop/api/iads/nn-iads-iadscontainer) property. This enables you to enumerate the container and retrieve only groups.
3.  Enumerate the group objects, using the [**IADsContainer::get\_\_NewEnum**](/windows/desktop/api/iads/nf-iads-iadscontainer-get__newenum) method.
4.  For each the group object, use the [**IADsGroup**](/windows/desktop/api/iads/nn-iads-iadsgroup) interface to read the name and members of the group.

 

 
