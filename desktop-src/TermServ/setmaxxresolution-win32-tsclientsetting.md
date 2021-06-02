---
title: SetMaxXResolution method of the Win32_TSClientSetting class
description: Sets the MaxXResolution property.
ms.assetid: c1e00bab-ab32-4cf6-8121-950184bd8a01
ms.tgt_platform: multiple
keywords:
- SetMaxXResolution method Remote Desktop Services
- SetMaxXResolution method Remote Desktop Services , Win32_TSClientSetting class
- Win32_TSClientSetting class Remote Desktop Services , SetMaxXResolution method
topic_type:
- apiref
api_name:
- Win32_TSClientSetting.SetMaxXResolution
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetMaxXResolution method of the Win32\_TSClientSetting class

Sets the **MaxXResolution** property.

## Syntax


```mof
uint32 SetMaxXResolution(
  [in] uint32 MaxXResolution
);
```



## Parameters

<dl> <dt>

*MaxXResolution* \[in\]
</dt> <dd>

The new maximum X resolution supported by the server. The minimum value is 200 and maximum value is 4096.

</dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the user's connection settings are overridden by the server.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSClientSetting**](win32-tsclientsetting.md)
</dt> </dl>

 

 





