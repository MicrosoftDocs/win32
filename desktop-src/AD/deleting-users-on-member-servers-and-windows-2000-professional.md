---
title: Deleting Users on Member Servers and Windows 2000 Professional
description: This topic shows how to delete a user from a member server or computer running on Windows 2000 Professional.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 0c94c08b-46cb-494e-89f8-a21bfb20e34c
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- users AD , deleting a user on member servers and Windows 2000 Professional
- Active Directory, using, users, deleting users on member servers and Windows 2000 Professional
- deleting a user
- server, deleting a user
- deleting users on member servers and windows 2000 professional AD
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Deleting Users on Member Servers and Windows 2000 Professional

This topic shows how to delete a user from a member server or computer running on Windows 2000 Professional.

**To delete a user**

1.  Bind to the computer using the following rules:
    1.  Use an account with sufficient rights to access that computer.
    2.  Use the following binding string format using the WinNT provider, computer name, and an extra parameter to tell ADSI that it is binding to a computer: "WinNT://<computer name&gt;,<computer&gt;". The "<computer name&gt;" parameter is the name of the computer whose groups you want to access. This parameter notifies ADSI that it is binding to a computer and allows the WinNT provider parser to skip some ambiguity resolution queries to determine what type of object you are binding to.
    3.  Bind to the [**IADsContainer**](https://msdn.microsoft.com/library/aa705985) interface.
2.  Specify "user" as the class using [**IADsContainer.Delete**](https://msdn.microsoft.com/library/aa705988) to delete the user.

    Be aware that you do not need to call [**IADs.SetInfo**](https://msdn.microsoft.com/library/aa746354) to commit the change to the container. The [**IADsContainer.Delete**](https://msdn.microsoft.com/library/aa705988) call commits the deletion of the user directly to the directory.

 

 




