---
title: Enumerating Users on Member Servers and Windows 2000 Professional
description: This topic shows how to enumerate all users, in a local security database, on member servers and computers running on Windows 2000 Professional.
ms.assetid: 56c20e8a-2861-4cd9-8058-271c89db7ec9
ms.tgt_platform: multiple
keywords:
- Enumerating Users on Member Servers and Windows 2000 Professional AD
- users AD , Enumerating Users on Member Servers and Windows 2000 Professional
- Active Directory, Using, Users, Enumerating Users on Member Servers and Windows 2000 Professional
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Users on Member Servers and Windows 2000 Professional

This topic shows how to enumerate all users, in a local security database, on member servers and computers running on Windows 2000 Professional.

**To enumerate the users**

1.  Bind to the computer using the following rules:
    1.  Use an account that has sufficient rights to access that computer.
    2.  Use the following binding string format using the WinNT provider, computer name, and an extra parameter to instruct ADSI that it is binding to a computer: "WinNT://<computer name>,&lt;computer&gt;". The "&lt;computer name&gt;" parameter is the name of the computer for whose groups to access. This parameter instructs ADSI that it is binding to a computer and enables the WinNT provider parser to skip some ambiguity resolution queries to determine what type of object you are binding to.
    3.  Bind to the [**IADsContainer**](/windows/desktop/api/iads/nn-iads-iadscontainer) interface.
2.  Add "user" to the [**IADsContainer.Filter**](/windows/desktop/ADSI/iadscontainer-property-methods) property. This causes the enumeration to only contain objects that have the "user" object class.
3.  Enumerate the objects. For each user object, use the [**IADs**](/windows/desktop/api/iads/nn-iads-iads) or [**IADsUser**](/windows/desktop/api/iads/nn-iads-iadsuser) interface methods to read the user properties.

 

 
