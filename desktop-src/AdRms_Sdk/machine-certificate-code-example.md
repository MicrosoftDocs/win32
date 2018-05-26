---
Description: The following topics together make up a sample that shows how to activate a computer for a logged-on user.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e67bd9c0-8253-49c6-81cb-56c4e45df513
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: Machine Certificate Code Example
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Machine Certificate Code Example

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The following topics together make up a sample that shows how to activate a computer for a logged-on user. Activation creates a machine certificate and saves it in the certificate store. The sample shows how to perform activation locally rather than by using an activation service on an AD RMS server. For a more complete example that shows how to locate an activation service, refer to the MachineActivation sample included with the Microsoft Windows Software Development Kit (SDK).

Note also that the following sample checks whether the computer has already been activated before proceeding. Reactivating an already activated computer overwrites the machine certificate which in turn will require a new rights account certificate. You should always check whether a computer has been activated before attempting to activate it.

-   [ComputerActivation\_Main.cpp](computeractivation-main-cpp.md)
-   [ComputerActivation\_Callback.cpp](computeractivation-callback-cpp.md)
-   [ComputerActivation.h](computeractivation-h.md)

## Related topics

<dl> <dt>

[Activating a Computer](activating-a-computer.md)
</dt> <dt>

[Machine Certificates](machine-certificates.md)
</dt> <dt>

[Machine Certificate Store](machine-certificate-store.md)
</dt> </dl>

 

 



