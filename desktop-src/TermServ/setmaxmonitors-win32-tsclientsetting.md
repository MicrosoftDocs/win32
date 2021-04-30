---
title: SetMaxMonitors method of the Win32_TSClientSetting class
description: Sets the MaxMonitors property.
ms.assetid: 1c8266e1-ff2b-4fbc-af70-6f7b4499d88c
ms.tgt_platform: multiple
keywords:
- SetMaxMonitors method Remote Desktop Services
- SetMaxMonitors method Remote Desktop Services , Win32_TSClientSetting class
- Win32_TSClientSetting class Remote Desktop Services , SetMaxMonitors method
topic_type:
- apiref
api_name:
- Win32_TSClientSetting.SetMaxMonitors
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetMaxMonitors method of the Win32\_TSClientSetting class

Sets the **MaxMonitors** property.

## Syntax


```mof
uint32 SetMaxMonitors(
  [in] uint32 MaxMonitors
);
```



## Parameters

<dl> <dt>

*MaxMonitors* \[in\]
</dt> <dd>

Specifies the new maximum number of monitors supported by the server. The minimum value is 1 and the maximum value is 10.

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

 

 





