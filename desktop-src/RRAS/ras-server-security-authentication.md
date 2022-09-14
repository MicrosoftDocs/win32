---
title: RAS Server Security Authentication
description: When a Windows NT/Windows 2000 RAS server receives a call, it invokes the RasSecurityDialogBegin function of the registered RAS security DLL, if there is one.
ms.assetid: dd9469ec-9bb1-4444-af5b-72e3ba8b4cb2
ms.topic: article
ms.date: 05/31/2018
---

# RAS Server Security Authentication

When a Windows NT/Windows 2000 RAS server receives a call, it invokes the [**RasSecurityDialogBegin**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogbegin) function of the registered RAS security DLL, if there is one. This call notifies the security DLL to begin its authentication of the remote user. The RAS server calls **RasSecurityDialogBegin** before performing its PPP or RAS authentication.

The [**RasSecurityDialogBegin**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogbegin) call passes the following information to the security DLL:

-   A port handle to identify the connection.
-   Pointers to buffers to use when communicating with the remote user.
-   A pointer to a [**RasSecurityDialogComplete**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogcomplete) function to call when the authentication has been completed.

The port handle and buffer pointers are valid until the security DLL calls [**RasSecurityDialogComplete**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogcomplete) to terminate the authentication transaction.

The [**RasSecurityDialogComplete**](/windows/desktop/api/Rasshost/nf-rasshost-rassecuritydialogcomplete) notifies the RAS server of the results of the security DLL's authentication of the remote user. If the security DLL reports success, the RAS server proceeds with its PPP and RAS authentication of the remote user. If the security DLL reports that the remote user failed the authentication, or that an error occurred, the RAS server hangs up and logs the error or failed authentication in the event log.

 

 




