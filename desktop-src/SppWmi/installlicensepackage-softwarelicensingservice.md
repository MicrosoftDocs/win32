---
title: InstallLicensePackage method of the SoftwareLicensingService class
description: Installs a license package for the current product.
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 92f48128-cdcf-42ee-a359-cbeaf845ec02
keywords:
- InstallLicensePackage method Windows Management Instrumentation
- InstallLicensePackage method Windows Management Instrumentation , SoftwareLicensingService class
- SoftwareLicensingService class Windows Management Instrumentation , InstallLicensePackage method
topic_type:
- apiref
api_name:
- SoftwareLicensingService.InstallLicensePackage
api_location:
- SppWmi.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# InstallLicensePackage method of the SoftwareLicensingService class

Installs a license package for the current product.

## Syntax


```mof
uint32 InstallLicensePackage(
  [in] string LicensePackage
);
```



## Parameters

<dl> <dt>

*LicensePackage* \[in\]
</dt> <dd>

Specifies the license package to install.

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

 

 





