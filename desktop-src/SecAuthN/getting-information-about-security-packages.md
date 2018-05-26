---
Description: When a client begins, it selects a security package for its transactions with a server and then contacts that server. A server selects one or more security packages and waits for a client connection.
ms.assetid: eaed162b-ef07-4295-93d9-6be91232a82e
title: Getting Information About Security Packages
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Getting Information About Security Packages

When a client begins, it selects a [*security package*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-package-gly) for its transactions with a server and then contacts that server. A server selects one or more security packages and waits for a client connection.

For specific information about the SSPI security packages available with a particular SSP, the [**EnumerateSecurityPackages**](/windows/win32/Sspi/nf-sspi-enumeratesecuritypackagesa?branch=master) function can be called to retrieve a [**SecPkgInfo**](/windows/win32/Sspi/ns-sspi-_secpkginfoa?branch=master) structure.

To retrieve the output structure, the caller passes to the function the address of a pointer to the type of the return structure. The function allocates memory and returns the data to the caller by assigning the address of the return data buffer to the argument. The SSPI convention is that the function allocates memory for the structure, and the calling application frees that memory using [**FreeContextBuffer**](/windows/win32/Sspi/nf-sspi-freecontextbuffer?branch=master).

Calling the [**QuerySecurityPackageInfo**](/windows/win32/Sspi/nf-sspi-querysecuritypackageinfoa?branch=master) function retrieves the attributes of a [*security package*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-security-package-gly). Both server and client can call the **QuerySecurityPackageInfo** function to get the maximum length of the security token from the **cbMaxToken** member of the [**SecPkgInfo**](/windows/win32/Sspi/ns-sspi-_secpkginfoa?branch=master) structure. For an example, see the call to the **QuerySecurityPackageInfo** function shown in [Using SSPI with a Windows Sockets Server](using-sspi-with-a-windows-sockets-server.md).

For more information on package functions, see [Package Management](authentication-functions.md#package-management).

 

 



