---
title: SchedulePatch method of the Win32_RDMSVirtualDesktopCollection class
description: Schedules a software update provisioning job that installs software updates on the virtual machines in a virtual desktop collection.
ms.assetid: 780d5709-9e7d-41d9-a4d0-b5d021615655
ms.tgt_platform: multiple
keywords:
- SchedulePatch method Remote Desktop Services
- SchedulePatch method Remote Desktop Services , Win32_RDMSVirtualDesktopCollection class
- Win32_RDMSVirtualDesktopCollection class Remote Desktop Services , SchedulePatch method
topic_type:
- apiref
api_name:
- Win32_RDMSVirtualDesktopCollection.SchedulePatch
api_location:
- RDMS.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SchedulePatch method of the Win32\_RDMSVirtualDesktopCollection class

Schedules a software update provisioning job that installs software updates on the virtual machines in a virtual desktop collection.

## Syntax


```mof
uint32 SchedulePatch(
  [in] DATETIME StartTime,
  [in] DATETIME ForceLogOffTime,
  [in] string   JobInputXml
);
```



## Parameters

<dl> <dt>

*StartTime* \[in\]
</dt> <dd>

> [!Note]  
> The system will not log off users of the virtual machines until the time specified in the *ForceLogOffTime* parameter.

 

The date and time to install the updates.

</dd> <dt>

*ForceLogOffTime* \[in\]
</dt> <dd>

The date and time on which the system will log off users of the virtual machines.

</dd> <dt>

*JobInputXml* \[in\]
</dt> <dd>

An XML formatted string that contains the software update job information.

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

 

 





