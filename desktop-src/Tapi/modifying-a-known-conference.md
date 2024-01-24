---
description: The following code fragment illustrates modification of a conferences time span. The default time span is thirty minutes. In this fragment, the time span is set to one year.
ms.assetid: 7f05d62e-2bcc-4d98-8a71-97ed20a12af2
title: Modifying a Known Conference
ms.topic: article
ms.date: 05/31/2018
---

# Modifying a Known Conference

\[Rendezvous IP Telephony Conferencing controls and interfaces are not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The following code fragment illustrates modification of a conference's time span. The default time span is thirty minutes. In this fragment, the time span is set to one year.

This fragment assumes that [connecting to an ILS server](connecting-to-an-ils-server.md) has already been performed and that a [conference directory enumeration](enumerating-conference-directories.md) has been performed to obtain the directory entry that will be modified.

This fragment also assumes this is not a multicast conference. Changing the times on a multicast conference requires notification of the multicast address allocation server. See [Acquiring a Multicast Address](acquiring-a-multicast-address.md) for an example of working with multicast addressing.


```C++
// If ( hr != S_OK ) process the error here. 
```



## Related topics

<dl> <dt>

[**ITDirectoryObjectConference**](/windows/desktop/api/Rend/nn-rend-itdirectoryobjectconference)
</dt> </dl>

 

 



