---
Description: The Active Directory Rights Management Services (AD RMS) functions use a specific data type to provide opaque handles to issuance licenses. This data type is declared in the Msdrmdefs.h header file that is included with this SDK.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 485a747c-a5bc-4ed0-a8f8-da64e011316f
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
title: DRMPUBHANDLE
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DRMPUBHANDLE

\[The AD RMS SDK leveraging functionality exposed by the client in Msdrm.dll is available for use in Windows Server 2008, Windows Vista, Windows Server 2008 R2, Windows 7, Windows Server 2012, and Windows 8. It may be altered or unavailable in subsequent versions. Instead, use [Active Directory Rights Management Services SDK 2.1](https://msdn.microsoft.com/library/hh535290), which leverages functionality exposed by the client in Msipc.dll.\]

The Active Directory Rights Management Services (AD RMS) functions use a specific data type to provide opaque handles to issuance licenses. This data type is declared in the Msdrmdefs.h header file that is included with this SDK.


```C++
typedef ULONG DRMPUBHANDLE;
```



## Remarks

When you use managed code, use the .NET Framework managed data type **IntPtr** to represent the handles that are needed by the AD RMS functions. To pass in a null handle that does not need to be modified, you can pass in **IntPtr.Zero** instead of declaring a new **IntPtr** variable and initializing it to zero. To copy this variable, use the [**DRMDuplicatePubHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmduplicatepubhandle) function. When your application is finished with this handle, it should call [**DRMClosePubHandle**](/previous-versions/windows/desktop/api/Msdrm/nf-msdrm-drmclosepubhandle) to close all resources used by this handle and clean up sensitive memory.

## Requirements



|                    |                                                                                        |
|--------------------|----------------------------------------------------------------------------------------|
| Product<br/> | Rights Management Services client 1.0 SP2 or later<br/>                          |
| Header<br/>  | <dl> <dt>Msdrmdefs.h</dt> </dl> |



## See also

<dl> <dt>

[AD RMS Functions](ad-rms-functions.md)
</dt> <dt>

[AD RMS Structures](ad-rms-structures.md)
</dt> </dl>

 

 




