---
title: CreateJob method of the MDM\_AppInstallJob class
description: Creates a job to manage the installation, upgrade, or uninstallation of an application on a device.
ms.assetid: 5ee99bd5-893e-4df9-9619-0dbd71eb888d
keywords:
- CreateJob method MDM App Management
- CreateJob method MDM App Management , MDM_AppInstallJob class
- MDM_AppInstallJob class MDM App Management , CreateJob method
topic_type:
- apiref
api_name:
- MDM_AppInstallJob.CreateJob
api_location:
- MDMAppProv.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CreateJob method of the MDM\_AppInstallJob class

\[The MDM Application Provider is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use the [EnterpriseAppManagement Configuration Service Provider (CSP)](https://msdn.microsoft.com/library/windows/hardware/dn904955).\]

Creates a job to manage the installation, upgrade, or uninstallation of an application on a device.

## Syntax


```mof
uint32 CreateJob(
  [in] string JobData
);
```



## Parameters

<dl> <dt>

*JobData* \[in\]
</dt> <dd>

The data for the job.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                    |
| Minimum supported server<br/> | None supported<br/>                                                                 |
| Namespace<br/>                | Root\\CIMv2\\mdm<br/>                                                               |
| MOF<br/>                      | <dl> <dt>MDMAppProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MDMAppProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MDM\_AppInstallJob**](mdm-appinstalljob.md)
</dt> </dl>

 

 





