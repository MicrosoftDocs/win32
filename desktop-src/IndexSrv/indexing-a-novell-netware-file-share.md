---
title: Indexing a Novell NetWare File Share
description: Indexing a Novell NetWare File Share
ms.assetid: cc4c42eb-bc3f-4964-98de-8803932f6a28
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Indexing a Novell NetWare File Share

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

If you have Novell NetWare file servers, Indexing Service can index their contents as well. To do this, install and run Microsoft Gateway Service for NetWare. For details about installing Gateway Service for NetWare, see the documentation for that service.

Install Gateway Service for NetWare on the computer running Indexing Service. For details refer to the Gateway Service documentation. Indexing Service indexes the files on Novell NetWare file shares in one of two ways:

-   Through gateway redirection.
-   Through a UNC share.

**To index files using gateway redirection**

1.  Create a gateway to the NetWare share. Assume, for example, that the gateway assigns the drive letter Z to the remote NetWare share.
2.  Add a virtual root in IIS pointing to drive Z. All documents on the remote NetWare share will be indexed by Indexing Service.

You can also index files on NetWare volumes by using a UNC share. You can create this UNC share whether the server is part of a domain or not, as shown in the following examples.

For these examples, assume the following:

-   The UNC name for the share is \\\\NovellServer\\Share1.
-   Indexing Service is running on a computer named Server A.
-   Server A is on Domain A when the server is part of a domain.
-   The user ID is WebUser, which can be any valid user ID.

If Server A is part of a domain, follow these steps:

1.  Create an account called WebUser on Domain A. This account should have the form DomainA\\WebUser.
2.  Give to the DomainA\\WebUser account on Server A.
3.  Make sure that DomainA\\WebUser has Read permission on \\\\NovellServer\\Share1.
4.  Create a virtual root in IIS pointing to \\\\NovellServer\\Share1. Specify DomainA\\WebUser for the user name, and assign an appropriate password. Be sure to specify Domain A followed by a backslash (\) and then the actual user ID.

If Server A is not part of a domain, follow these steps:

1.  Create an account called WebUser on ServerA. This account should have the form ServerA\\WebUser.
2.  Give to the ServerA\\WebUser account on Server A.
3.  Make sure that ServerA\\WebUser has Read permission on \\\\NovellServer\\Share1.
4.  Create a virtual root in IIS pointing to \\\\NovellServer\\Share1. Specify ServerA\\WebUser for the user name, and assign an appropriate password. Be sure to specify Server A followed by a backslash (\) and then the actual user ID.

Indexing Service then indexes the remote UNC \\\\NovellServer\\Share1. If you want to index more remote NetWare files shares, repeat steps 3 and 4 for each of the shares.

 

 




