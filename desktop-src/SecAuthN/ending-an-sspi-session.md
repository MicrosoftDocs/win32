---
description: When the client has finished communicating with any server or has finished using the additional credentials passed to the AcquireCredentialsHandle function, the client must call the FreeCredentialsHandle function.
ms.assetid: fa943e9b-d379-441f-8c6e-f0a0f5f7f1a3
title: Ending an SSPI Session
ms.topic: article
ms.date: 05/31/2018
---

# Ending an SSPI Session

After the client and server have finished communicating, both sides call the [**DeleteSecurityContext**](/windows/desktop/api/Sspi/nf-sspi-deletesecuritycontext) function with their respective context handles. When the client has finished communicating with any server or has finished using the additional credentials passed to the [**AcquireCredentialsHandle**](/windows/win32/api/sspi/nf-sspi-acquirecredentialshandlea) function, the client must call the [**FreeCredentialsHandle**](/windows/desktop/api/Sspi/nf-sspi-freecredentialshandle) function. When the server is ready to shut down and before unloading the DLL, the server must call **DeleteSecurityContext**.

 

 
