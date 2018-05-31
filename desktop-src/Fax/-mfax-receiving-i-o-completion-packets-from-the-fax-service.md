---
Description: This topic describes how to receive I/O completion packets from the fax service in the Microsoft Win32 environment.
ms.assetid: 210879a2-b732-4591-a32b-6d1e79be0181
title: Receiving I/O Completion Packets from the Fax Service
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Receiving I/O Completion Packets from the Fax Service

This functionality is currently available only in the Microsoft Win32 environment. It is not available in the legacy Component Object Model (COM) implementation environment. But it is available in the [Extended COM](-mfax-fax-service-extended-com-reference.md) environment.

When a client application calls the [**FaxInitializeEventQueue**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxinitializeeventqueue) function, it can specify notification using I/O completion packets instead of notification messages. The application does this by passing a valid handle to an I/O completion port in the *CompletionPort* parameter, and a value in the *CompletionKey* parameter. If the application specifies I/O completion packets, the fax service does not open an impersonation token for the application. In this situation no additional coding is necessary, because completion packets can cross desktops.

To notify the client of asynchronous events, the fax service calls the [PostQueuedCompletionStatus](http://msdn.microsoft.com/library/en-us/fileio/base/postqueuedcompletionstatus.asp) function. The client must call the [GetQueuedCompletionStatus](http://msdn.microsoft.com/library/en-us/fileio/base/getqueuedcompletionstatus.asp) function to retrieve the I/O completion packet. The I/O completion packet contains a [**FAX\_EVENT**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_eventa) structure.

 

 



