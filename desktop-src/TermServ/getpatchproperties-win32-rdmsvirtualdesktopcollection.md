---
title: GetPatchProperties method of the Win32_RDMSVirtualDesktopCollection class
description: Retrieves the properties of a software update provisioning job for the virtual machines in a virtual desktop collection.
ms.assetid: 9f228d89-0613-49c7-8169-48491c3a2d9b
ms.tgt_platform: multiple
keywords:
- GetPatchProperties method Remote Desktop Services
- GetPatchProperties method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , GetPatchProperties method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.GetPatchProperties
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# GetPatchProperties method of the Win32\_RDMSVirtualDesktopCollection class

Retrieves the properties of a software update provisioning job for the virtual machines in a virtual desktop collection.

## Syntax


```mof
uint32 GetPatchProperties(
  [out] DATETIME StartTime,
  [out] DATETIME ForceLogOffTime,
  [out] string   JobGuid,
  [out] uint32   State
);
```



## Parameters

<dl> <dt>

*StartTime* \[out\]
</dt> <dd>

The date and time to install the updates.

</dd> <dt>

*ForceLogOffTime* \[out\]
</dt> <dd>

The date and time on which the system will log off users of the virtual machines.

</dd> <dt>

*JobGuid* \[out\]
</dt> <dd>

A **GUID** that uniquely identifies the provisioning job.

</dd> <dt>

*State* \[out\]
</dt> <dd>

The state of the provisioning job.

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

 

 





