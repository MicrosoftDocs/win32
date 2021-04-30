---
title: SetFallbackPrintDriverType method of the Win32_TerminalServiceSetting class
description: The SetFallbackPrintDriverType method sets the FallbackPrintDriverType property for the class.
ms.assetid: be738134-199a-41a6-b2f8-cccfa14fa02b
ms.tgt_platform: multiple
keywords:
- SetFallbackPrintDriverType method Remote Desktop Services
- SetFallbackPrintDriverType method Remote Desktop Services , Win32_TerminalServiceSetting class
- Win32_TerminalServiceSetting class Remote Desktop Services , SetFallbackPrintDriverType method
topic_type:
- apiref
api_name:
- Win32_TerminalServiceSetting.SetFallbackPrintDriverType
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetFallbackPrintDriverType method of the Win32\_TerminalServiceSetting class

The **SetFallbackPrintDriverType** method sets the **FallbackPrintDriverType** property for the class.

## Syntax


```mof
uint32 SetFallbackPrintDriverType(
  [in] uint32 FallbackPrintDriverType
);
```



## Parameters

<dl> <dt>

*FallbackPrintDriverType* \[in\]
</dt> <dd>

Sets the **FallbackPrintDriverType** property which allows or denies new Remote Desktop Services connections.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

No fallback drivers.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Best guess.

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

Best guess. If no match is found, fallback to Hewlett-Packard Printer Control Language (PCL).

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

Best guess. If no match is found, fallback to Postscript (PS).

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4**


</dt> <dd>

Best guess. If no match is found, show both PS and PCL drivers.

</dd> </dl> </dd> </dl>

## Return value

Returns Success on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

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

 

