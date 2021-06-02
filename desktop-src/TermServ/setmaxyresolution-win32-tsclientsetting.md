---
title: SetMaxYResolution method of the Win32_TSClientSetting class
description: Sets the MaxYResolution property.
ms.assetid: a8399c7c-6b3a-464f-8112-8838257ccf06
ms.tgt_platform: multiple
keywords:
- SetMaxYResolution method Remote Desktop Services
- SetMaxYResolution method Remote Desktop Services , Win32_TSClientSetting class
- Win32_TSClientSetting class Remote Desktop Services , SetMaxYResolution method
topic_type:
- apiref
api_name:
- Win32_TSClientSetting.SetMaxYResolution
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetMaxYResolution method of the Win32\_TSClientSetting class

Sets the **MaxYResolution** property.

## Syntax


```mof
uint32 SetMaxYResolution(
  [in] uint32 MaxYResolution
);
```



## Parameters

<dl> <dt>

*MaxYResolution* \[in\]
</dt> <dd>

The new maximum Y resolution supported by the server. The minimum value is 200 and the maximum value is 2048.

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

 

 





