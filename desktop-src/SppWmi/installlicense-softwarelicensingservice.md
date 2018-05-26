---
title: InstallLicense method of the SoftwareLicensingService class
description: Installs a license for the current product.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 99de56e8-cf5c-4b45-958e-8bd80997f574
keywords:
- InstallLicense method Windows Management Instrumentation
- InstallLicense method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , InstallLicense method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.InstallLicense
api_location:
- SppWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# InstallLicense method of the SoftwareLicensingService class

Installs a license for the current product.

## Syntax


```mof
uint32 InstallLicense(
  [in] string License
);
```



## Parameters

<dl> <dt>

*License* \[in\]
</dt> <dd>

Specifies the license to install.

</dd> </dl>

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>SppWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>SppWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**SoftwareLicensingService**](softwarelicensingservice.md)
</dt> </dl>

 

 





