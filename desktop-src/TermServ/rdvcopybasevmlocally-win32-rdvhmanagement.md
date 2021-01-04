---
title: RdvCopyBaseVmLocally method of the Win32_RdvhManagement class
description: Copies a local base virtual machine to a specified remote desktop virtualization (RDV) host server.
ms.assetid: 13c0c629-42c6-4689-9740-f13f31688e42
ms.tgt_platform: multiple
keywords:
- RdvCopyBaseVmLocally method Remote Desktop Services
- RdvCopyBaseVmLocally method Remote Desktop Services , Win32_RdvhManagement class
- Win32_RdvhManagement class Remote Desktop Services , RdvCopyBaseVmLocally method
topic_type:
- apiref
api_name:
- Win32_RdvhManagement.RdvCopyBaseVmLocally
api_location:
- TSVmHostWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RdvCopyBaseVmLocally method of the Win32\_RdvhManagement class

Copies a local base virtual machine to a specified remote desktop virtualization (RDV) host server.

## Syntax


```mof
uint32 RdvCopyBaseVmLocally(
  [in] string BaseVmLocation,
  [in] string FarmName,
  [in] string GoldCacheLocation
);
```



## Parameters

<dl> <dt>

*BaseVmLocation* \[in\]
</dt> <dd>

The base virtual machine location.

</dd> <dt>

*FarmName* \[in\]
</dt> <dd>

The name of the host farm to copy to.

</dd> <dt>

*GoldCacheLocation* \[in\]
</dt> <dd>

The gold cache location.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

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

 

 





