---
Description: The server sends the client a reference to their shared security context using the opaque directive of the Digest challenge.
ms.assetid: 543c4bed-b224-4da7-9746-12c9993a40af
title: Authenticating Subsequent Requests Using Microsoft Digest
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Authenticating Subsequent Requests Using Microsoft Digest

The server sends the client a reference to their shared [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly) using the opaque directive of the Digest challenge. After a successful authentication, the client must specify this value in subsequent requests to the target server. Including the opaque value in requests for resources that are accessible using the existing security context eliminates the need to re-authenticate at the domain controller. Such requests are re-authenticated at the server, using the Digest [*session key*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-session-key-gly) cached after the initial authentication.

The following diagram illustrates the steps taken by client and server during a subsequent request for access-protected resources.

![authenticating subsequent requests using microsoft digest](images/digest2.png)

To request additional resources after a successful authentication, the client calls the Microsoft Digest [**MakeSignature**](/windows/win32/Sspi/nf-sspi-makesignature?branch=master) function to generate a Digest challenge response. The opaque value is included in the opaque directive of the challenge response sent to the server as an Authorization header (shown as HTTP Request).

The server calls the [**AcceptSecurityContext (Digest)**](/windows/win32/Sspi/?branch=master) function to determine whether there is an existing [*security context*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-context-gly) for the client. When an existing context is found, the function returns SEC\_E\_COMPLETE\_NEEDED to indicate the server must then call the [**CompleteAuthToken**](/windows/win32/Sspi/nf-sspi-completeauthtoken?branch=master) function. This function performs the client authentication using the Digest [*session key*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-session-key-gly) cached during the [initial authentication](initial-authentication-using-microsoft-digest.md) instead of re-authenticating at the domain controller.

 

 



