---
title: NetShell and Command Abbreviation
description: NetShell commands can be abbreviated to the shortest unambiguous string.
ms.assetid: f367bb91-4502-4a73-9786-a9999e2d0dc1
keywords:
- command abbreviation NetSh
- components NetSh , command abbreviation
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NetShell and Command Abbreviation

NetShell commands can be abbreviated to the shortest unambiguous string. This enables administrators to perform a type of shorthand for NetShell commands. For example, the following two lines achieve the same result:

``` syntax
netsh interface ip> show ip interface
netsh interface ip> sh ip int
```

This functionality is provided by the [**MatchToken**](/windows/previous-versions/Netsh/nf-netsh-matchtoken?branch=master) function provided by the NetShell API. Programmers creating NetShell helpers can use the **MatchToken** function to implement command abbreviation for NetShell commands.

 

 




