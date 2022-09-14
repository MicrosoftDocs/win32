---
title: RdvCreateUserDiskTemplate method of the Win32_RdvhManagement class
description: Creates a user disk template, with the specified maximum size, at the specified location.
ms.assetid: b8ca8b8c-58fd-44fc-9a88-5d7d41ef96a2
ms.tgt_platform: multiple
keywords:
- RdvCreateUserDiskTemplate method Remote Desktop Services
- RdvCreateUserDiskTemplate method Remote Desktop Services , Win32_RdvhManagement class
- Win32_RdvhManagement class Remote Desktop Services , RdvCreateUserDiskTemplate method
topic_type:
- apiref
api_name:
- Win32_RdvhManagement.RdvCreateUserDiskTemplate
api_location:
- TSVmHostWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RdvCreateUserDiskTemplate method of the Win32\_RdvhManagement class

Creates a user disk template, with the specified maximum size, at the specified location.

## Syntax


```mof
uint32 RdvCreateUserDiskTemplate(
  [in] string UserDisksStorageUrl,
  [in] uint32 UserDiskMaxSizeInGB
);
```



## Parameters

<dl> <dt>

*UserDisksStorageUrl* \[in\]
</dt> <dd>

Location of the user disk storage.

</dd> <dt>

*UserDiskMaxSizeInGB* \[in\]
</dt> <dd>

Maximum size of the user disk, in GB.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Remarks

All user disks created using this template will have the same maximum size as the template.

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                  |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                             |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                   |
| MOF<br/>                      | <dl> <dt>TSVmHost.mof</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>TSVmHostWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_RdvhManagement**](win32-rdvhmanagement.md)
</dt> </dl>

 

 





