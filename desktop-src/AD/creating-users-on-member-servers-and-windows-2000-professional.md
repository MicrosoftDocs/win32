---
title: Creating Users on Member Servers and Windows 2000 Professional
description: This topic describes steps used to create a user on a member server or computer running Windows 2000 Professional.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 714a36d4-3407-426f-b4e9-27ec399f742a
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- Creating Users on Member Servers and Windows 2000 Professional AD
- users AD , creating a user on member servers and Windows 2000 Professional
- Active Directory, using, users, creating a user on member servers and Windows 2000 Professional
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Users on Member Servers and Windows 2000 Professional

**To create a user**

1.  Bind to the computer using the following rules:
    1.  Use an account that has sufficient rights to access that computer.
    2.  Use the following binding string format using the WinNT provider, computer name, and an extra parameter to tell ADSI that it is binding to a computer: "WinNT://&lt;computer name&gt;,&lt;computer&gt;". The "&lt;computer name&gt;" computer is the name of the computer whose groups you want to access. This parameter tells ADSI that it is binding to a computer and allows the WinNT provider's parser to skip some ambiguity resolution queries to determine what type of object you are binding to.
    3.  Bind to the [**IADsContainer**](https://msdn.microsoft.com/library/aa705985) interface.
2.  Specify "user" as the class using [**IADsContainer.Create**](https://msdn.microsoft.com/library/aa705987) to add the user.
3.  Write the user to the computer's security database using [**IADs.SetInfo**](https://msdn.microsoft.com/library/aa746354).

 

 




