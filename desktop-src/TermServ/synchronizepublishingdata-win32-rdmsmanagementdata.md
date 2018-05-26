---
title: SynchronizePublishingData method of the Win32\_RDMSManagementData class
description: Synchronizes the specified set of publishing data for Remote Desktop Management Services (RDMS).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 0476ce12-9b08-418c-83c2-208275574f5b
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- SynchronizePublishingData method Remote Desktop Services
- SynchronizePublishingData method Remote Desktop Services , Win32_RDMSManagementData class
- Win32_RDMSManagementData class Remote Desktop Services , SynchronizePublishingData method
topic_type:
- apiref
api_name:
- Win32_RDMSManagementData.SynchronizePublishingData
api_location:
- RDMS.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SynchronizePublishingData method of the Win32\_RDMSManagementData class

Synchronizes the specified set of publishing data for Remote Desktop Management Services (RDMS).

## Syntax


```mof
uint32 SynchronizePublishingData(
  [in] string Context
);
```



## Parameters

<dl> <dt>

*Context* \[in\]
</dt> <dd>

The context information of the publishing data to synchronize.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSManagementData**](win32-rdmsmanagementdata.md)
</dt> </dl>

 

 





