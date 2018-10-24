---
title: Deleting Local Groups
description: This topic shows how to delete a local group from a member server or computer running on Windows 2000 Professional.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 030da25a-a606-4521-a243-d902c772fd00
ms.tgt_platform: multiple
keywords:
- Deleting Local Groups AD
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Deleting Local Groups

This topic shows how to delete a local group from a member server or computer running on Windows 2000 Professional.

**To delete a local group**

1.  Bind to the computer using the following rules:
    1.  Use an account with sufficient rights to access that computer.
    2.  Use the following binding string format using the WinNT provider, computer name, and an extra parameter to instruct ADSI that it is binding to a computer: "WinNT://<computer name>,<computer>". The "<computer name>" parameter is the name of the computer group to access. This parameter instruct ADSI that it is binding to a computer and allows the WinNT provider's parser to skip some ambiguity-resolution queries to determine what type of object you are binding to.
    3.  Bind to the [**IADsContainer**](https://msdn.microsoft.com/library/aa705985) interface.
2.  Specify "group" as the class using [**IADsContainer.Delete**](https://msdn.microsoft.com/library/aa705988)to delete the group.

    You do not need to call [**IADs.SetInfo**](https://msdn.microsoft.com/library/aa746354) to commit the change to the container. The [**IADsContainer.Delete**](https://msdn.microsoft.com/library/aa705988) call commits the deletion of the group directly to the directory.

 

 




