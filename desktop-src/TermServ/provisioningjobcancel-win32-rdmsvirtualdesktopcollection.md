---
title: ProvisioningJobCancel method of the Win32_RDMSVirtualDesktopCollection class
description: Cancels a virtual desktop provisioning job.
ms.assetid: 933ea0f3-b916-4e70-89de-597f9eb23976
ms.tgt_platform: multiple
keywords:
- ProvisioningJobCancel method Remote Desktop Services
- ProvisioningJobCancel method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , ProvisioningJobCancel method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.ProvisioningJobCancel
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ProvisioningJobCancel method of the Win32\_RDMSVirtualDesktopCollection class

Cancels a virtual desktop provisioning job.

## Syntax


```mof
uint32 ProvisioningJobCancel(
  [in] string JobGuid
);
```



## Parameters

<dl> <dt>

*JobGuid* \[in\]
</dt> <dd>

The **GUID** that uniquely identifies the provisioning job to cancel.

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

 

 





