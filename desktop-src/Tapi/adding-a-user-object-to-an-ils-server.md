---
description: The following code fragment illustrates publishing a user object in an ILS server. After a user object is published, remote parties can use the user object to make calls to the specified user.
ms.assetid: 8b68886c-0df5-4005-bcd5-1a18336f5192
title: Adding a User Object to an ILS Server
ms.topic: article
ms.date: 05/31/2018
---

# Adding a User Object to an ILS Server

\[ Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The following code fragment illustrates publishing a user object in an ILS server. After a user object is published, remote parties can use the user object to make calls to the specified user.

This fragment assumes that [connecting to an ILS server](connecting-to-an-ils-server.md) has already been performed.


```C++
hr = pDirectory->AddDirectoryObject(pDirectoryObject);
```



## Related topics

<dl> <dt>

[**ITDirectory**](/windows/desktop/api/Rend/nn-rend-itdirectory)
</dt> <dt>

[**ITDirectoryObject**](/windows/desktop/api/Rend/nn-rend-itdirectoryobject)
</dt> <dt>

[**ITDirectoryObjectUser**](/windows/desktop/api/Rend/nn-rend-itdirectoryobjectuser)
</dt> </dl>

 

 



