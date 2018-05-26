---
Description: When the client has finished communicating with any server or has finished using the additional credentials passed to the AcquireCredentialsHandle function, the client must call the FreeCredentialsHandle function.
ms.assetid: fa943e9b-d379-441f-8c6e-f0a0f5f7f1a3
title: Ending an SSPI Session
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Ending an SSPI Session

After the client and server have finished communicating, both sides call the [**DeleteSecurityContext**](/windows/win32/Sspi/nf-sspi-deletesecuritycontext?branch=master) function with their respective context handles. When the client has finished communicating with any server or has finished using the additional credentials passed to the [**AcquireCredentialsHandle**](/windows/win32/Sspi/?branch=master) function, the client must call the [**FreeCredentialsHandle**](/windows/win32/Sspi/nf-sspi-freecredentialshandle?branch=master) function. When the server is ready to shut down and before unloading the DLL, the server must call **DeleteSecurityContext**.

 

 



