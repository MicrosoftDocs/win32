---
title: ProvisioningEnumerateJobs method of the Win32_RDMSVirtualDesktopCollection class
description: Enumerates virtual desktop provisioning jobs for this service.
ms.assetid: 4bd2b03f-ba8c-483e-af09-270424f9b1ed
ms.tgt_platform: multiple
keywords:
- ProvisioningEnumerateJobs method Remote Desktop Services
- ProvisioningEnumerateJobs method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , ProvisioningEnumerateJobs method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.ProvisioningEnumerateJobs
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ProvisioningEnumerateJobs method of the Win32\_RDMSVirtualDesktopCollection class

Enumerates virtual desktop provisioning jobs for this service.

## Syntax


```mof
uint32 ProvisioningEnumerateJobs(
  [in]  uint32 JobType,
  [in]  string CollectionAlias,
  [out] string JobGuids[]
);
```



## Parameters

<dl> <dt>

*JobType* \[in\]
</dt> <dd>

An integer that specifies the type of job to enumerate.

This parameter can be set to one of the following values:

<dt>

0
</dt> <dd>

Running jobs

</dd> <dt>

1
</dt> <dd>

Completed jobs

</dd> </dl> </dd> <dt>

*CollectionAlias* \[in\]
</dt> <dd>

The alias of the virtual desktop collection to enumerate. The default value for this parameter is FALSE, which specifies that all running jobs are to be enumerated.

</dd> <dt>

*JobGuids* \[out\]
</dt> <dd>

An array that contains the **GUIDs** of provisioning jobs to enumerate.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\CIMv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[**Win32\_RDMSVirtualDesktopCollection**](win32-rdmsvirtualdesktopcollection.md)
</dt> </dl>

 

 





