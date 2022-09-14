---
title: QueryOfflineInformation method of the Win32_TSVm class
description: Retrieves the properties of the current virtual desktop server (VDS), but only when the server is offline.
ms.assetid: f6ce74cb-a4a4-4e05-a0a7-bac0b7f52c45
ms.tgt_platform: multiple
keywords:
- QueryOfflineInformation method Remote Desktop Services
- QueryOfflineInformation method Remote Desktop Services , Win32_TSVm class
- Win32_TSVm class Remote Desktop Services , QueryOfflineInformation method
topic_type:
- apiref
api_name:
- Win32_TSVm.QueryOfflineInformation
api_location:
- TSVmHostWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# QueryOfflineInformation method of the Win32\_TSVm class

Retrieves the properties of the current virtual desktop server (VDS), but only when the server is offline.

## Syntax


```mof
uint32 QueryOfflineInformation(
  [out] string  Build,
  [out] string  CurrentVersion,
  [out] string  InstallationType,
  [out] string  EditionId,
  [out] string  SysPrepImageState,
  [out] string  SysPrepMode,
  [out] sint32  ProcArch,
  [out] boolean fIsVmbusCapable,
  [out] boolean fIsRdvIcInstalled
);
```



## Parameters

<dl> <dt>

*Build* \[out\]
</dt> <dd>

On a success, returns the build version of the VDS.

</dd> <dt>

*CurrentVersion* \[out\]
</dt> <dd>

On a success, returns the current version of the VDS.

</dd> <dt>

*InstallationType* \[out\]
</dt> <dd>

On a success, returns the installation type of the VDS.

</dd> <dt>

*EditionId* \[out\]
</dt> <dd>

On a success, returns the edition ID of the VDS.

</dd> <dt>

*SysPrepImageState* \[out\]
</dt> <dd>

On success, returns the system prep image state of the VDS.

</dd> <dt>

*SysPrepMode* \[out\]
</dt> <dd>

On a success, returns the system prep mode of the VDS.

</dd> <dt>

*ProcArch* \[out\]
</dt> <dd>

On a success, returns a value indicating the processor architecture.

<dt>

0
</dt> <dd>

x86

</dd> <dt>

1
</dt> <dd>

amd64

</dd> </dl> </dd> <dt>

*fIsVmbusCapable* \[out\]
</dt> <dd>

on a success, indicates whether the system is VMBus-capable.

</dd> <dt>

*fIsRdvIcInstalled* \[out\]
</dt> <dd>

On a success, indicates if RDVIC is installed.

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

[**Win32\_TSVm**](win32-tsvm.md)
</dt> </dl>

 

 





