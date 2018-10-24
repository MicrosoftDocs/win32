---
title: SendMessage, PostMessage, and Related Functions
description: This section describes considerations about forwarding messages using SendMessage, PostMessage, and related functions with touch messages.
ms.assetid: 9fba2013-17a3-499c-80dc-627e89c0edaf
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SendMessage, PostMessage, and Related Functions

This section describes considerations about forwarding messages using [SendMessage](http://msdn.microsoft.com/library/ms644950.aspx), [PostMessage](http://msdn.microsoft.com/library/ms644944(VS.85).aspx), and related functions with touch messages.

If a touch message is forwarded using [SendMessage](http://msdn.microsoft.com/library/ms644950.aspx), [PostMessage](http://msdn.microsoft.com/library/ms644944(VS.85).aspx), or some other related function, the touch input handle is closed. If you have retrieved the information contained referenced by a touch input handle through a call to [**GetTouchInputInfo**](/windows/desktop/api/winuser/nf-winuser-gettouchinputinfo), that data will remain valid until you free the memory.

An application that receives touch messages forwarded through one of these mechanisms owns the touch input handle it receives in the message *LPARAM* and is responsible for closing it. If you don't close the handle with a call to [**CloseTouchInputHandle**](/windows/desktop/api/winuser/nf-winuser-closetouchinputhandle), pass the message to [DefWindowProc](http://go.microsoft.com/fwlink/p/?linkid=136637), or forward the message using [SendMessage](http://msdn.microsoft.com/library/ms644950.aspx), [PostMessage](http://msdn.microsoft.com/library/ms644944(VS.85).aspx), or some related function, you will have a memory leak.

> [!Note]  
> Touch messages are subject to normal User Interface Privilege Isolation (UIPI) rules when they are forwarded.

 

## Functions related to SendMessage and PostMessage

The following functions that can affect the state of the touch input handle.

-   [SendMessage](http://msdn.microsoft.com/library/ms644950.aspx)
-   [PostMessage](http://msdn.microsoft.com/library/ms644944(VS.85).aspx)
-   SendNotifyMessage
-   SendMessageCallback
-   SendMessageTimeout
-   PostThreadMessage

## Related topics

<dl> <dt>

[Functions](mtfunctions.md)
</dt> <dt>

[DefWindowProc](http://go.microsoft.com/fwlink/p/?linkid=136637)
</dt> </dl>

 

 




