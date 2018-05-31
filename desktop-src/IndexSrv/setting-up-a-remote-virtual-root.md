---
title: Setting Up a Remote Virtual Root
description: Setting Up a Remote Virtual Root
ms.assetid: 8adf7ac3-5e68-4fc3-abef-4db5b28b810b
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting Up a Remote Virtual Root

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

When specifying the logon ID for a remote virtual root, type both the domain name and the user name, separated by a backslash (\):

*domain\\username*

If you do not give the domain name, Indexing Service will not index the remote virtual roots. Note that the domain name may actually be the name of the computer, if the account is local to that computer.

User IDs associated with remote virtual-root setup must have interactive logon permission on the computer running Indexing Service. For example, if /*Vroot1* on *index\_server* points to \\\\*Computername\\Share\\Folder1\\Folder2* and the user ID is *domain\\user*, then *domain\\user* must have interactive logon privilege on *index\_server*. The simplest way to achieve this is to add *domain\\user* to the Guests group on *index\_server*.

 

 




