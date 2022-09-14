---
title: SetDisableForcibleLogoff method of the Win32_TerminalServiceSetting class
description: SetDisableForcibleLogoff method of the Win32_TerminalServiceSetting class - This method is not supported.
ms.assetid: 1b7ac0f2-c242-4ca8-bc4d-8111e63851eb
ms.tgt_platform: multiple
keywords:
- SetDisableForcibleLogoff method Remote Desktop Services
- SetDisableForcibleLogoff method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , SetDisableForcibleLogoff method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.SetDisableForcibleLogoff
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetDisableForcibleLogoff method of the Win32\_TerminalServiceSetting class

This method is not supported.

**Windows Vista and Windows Server 2008:** Enables or disables whether an administrator logged onto the console can be forcibly logged off.

## Syntax


```mof
uint32 SetDisableForcibleLogoff(
  [in] uint32 DisableForcibleLogoff
);
```



## Parameters

<dl> <dt>

*DisableForcibleLogoff* \[in\]
</dt> <dd>

Flag disabling or enabling the **DisableForcibleLogoff** property, which determines whether an administrator that is logged on to the console can be forcibly logged off.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Disable the property. The connected administrator can be forcibly logged off.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Enable the property. The connected administrator cannot be forcibly logged off.

</dd> </dl> </dd> </dl>

## Return value

Returns Success on success; otherwise, returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| End of client support<br/>    | Windows Vista<br/>                                                                |
| End of server support<br/>    | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md)
</dt> </dl>

 

 





