---
title: SetSingleSession method of the Win32_TerminalServiceSetting class
description: The SetSingleSession method sets the SingleSession property for the class.
ms.assetid: 67ccfa9d-86a5-4501-9d61-c7f1677ec3d5
ms.tgt_platform: multiple
keywords:
- SetSingleSession method Remote Desktop Services
- SetSingleSession method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , SetSingleSession method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.SetSingleSession
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetSingleSession method of the Win32\_TerminalServiceSetting class

The **SetSingleSession** method sets the **SingleSession** property for the class.

## Syntax


```mof
uint32 SetSingleSession(
  [in] uint32 SingleSession
);
```



## Parameters

<dl> <dt>

*SingleSession* \[in\]
</dt> <dd>

Flag disabling or enabling the **SingleSession** property, which determines whether users are limited to one or more Remote Desktop Services sessions.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Disable the property.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Enable the property.

</dd> </dl> </dd> </dl>

## Return value

Returns Success on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values.

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TerminalServiceSetting**](win32-terminalservicesetting.md)
</dt> </dl>

 

