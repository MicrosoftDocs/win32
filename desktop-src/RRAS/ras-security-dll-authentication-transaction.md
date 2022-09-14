---
title: RAS Security DLL Authentication Transaction
description: Windows NT/Windows 2000 RAS server calls the security DLL's RasSecurityDialogBegin function to begin an authentication of a remote user.
ms.assetid: e6549812-d906-4163-b9c8-86f8f1cb1ad3
ms.topic: article
ms.date: 05/31/2018
---

# RAS Security DLL Authentication Transaction

Windows NT/Windows 2000 RAS server calls the security DLL's [**RasSecurityDialogBegin**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogbegin) function to begin an authentication of a remote user. The RAS server is blocked and cannot accept any other calls until **RasSecurityDialogBegin** returns. For this reason, **RasSecurityDialogBegin** should copy the input parameters, create a thread to perform the authentication, and return as quickly as possible.

The thread created by the security DLL uses the [**RasSecurityDialogSend**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogsend) and [**RasSecurityDialogReceive**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogreceive) functions to communicate with the remote computer. These functions are not available for static import from any library. Instead, the security DLL must use the [**LoadLibrary**](/windows/win32/api/libloaderapi/nf-libloaderapi-loadlibrarya) and [**GetProcAddress**](/windows/win32/api/libloaderapi/nf-libloaderapi-getprocaddress) functions to dynamically link to these functions in RASMAN.DLL.

During an authentication transaction, the RAS connection manager on the remote computer displays a terminal window. The thread of the security DLL calls [**RasSecurityDialogSend**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogsend) to send a message to display in the terminal window. The thread then calls [**RasSecurityDialogReceive**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogreceive) to receive the input that the remote user types in the terminal window. The thread can make any number of **RasSecurityDialogSend** calls, with each call followed by a **RasSecurityDialogReceive** call. After each call to **RasSecurityDialogReceive**, the thread must call one of the wait functions, such as [**WaitForSingleObject**](/windows/win32/api/synchapi/nf-synchapi-waitforsingleobject), to wait for the asynchronous send and receive operations to be completed. The RAS server signals an event object when the receive operation has been completed or when an optional time-out interval has elapsed.

When the thread has finished authenticating the remote user, it calls the [**RasSecurityDialogComplete**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogcomplete) function. This call passes a [**SECURITY\_MESSAGE**](/windows/desktop/api/Rasshost/ns-rasshost-security_message) structure containing the results of the authentication transaction to the RAS server. The RAS server then performs a cleanup sequence that includes a call to the DLL's [**RasSecurityDialogEnd**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogend) function. This gives the security DLL an opportunity to perform any necessary cleanup.

The security DLL can call the [**RasSecurityDialogGetInfo**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialoggetinfo) function to retrieve information about the port associated with an authentication transaction. **RasSecurityDialogGetInfo** fills in a [**RAS\_SECURITY\_INFO**](/windows/desktop/api/Rasshost/ns-rasshost-ras_security_info) structure that indicates the state of the last [**RasSecurityDialogReceive**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogreceive) call for the port.

 

 