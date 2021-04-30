---
title: SetColorDepthPolicy method of the Win32_TSClientSetting class
description: The SetColorDepthPolicy method sets the ColorDepthPolicy property for the class.
ms.assetid: 7a8c2b51-5f7a-4188-aae0-0b2d47d043bd
ms.tgt_platform: multiple
keywords:
- SetColorDepthPolicy method Remote Desktop Services
- SetColorDepthPolicy method Remote Desktop Services , Win32_TSClientSetting class
- Win32_TSClientSetting class Remote Desktop Services , SetColorDepthPolicy method
topic_type:
- apiref
api_name:
- Win32_TSClientSetting.SetColorDepthPolicy
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetColorDepthPolicy method of the Win32\_TSClientSetting class

The **SetColorDepthPolicy** method sets the **ColorDepthPolicy** property for the class.

## Syntax


```mof
uint32 SetColorDepthPolicy(
  [in] uint32 ColorDepthPolicy
);
```



## Parameters

<dl> <dt>

*ColorDepthPolicy* \[in\]
</dt> <dd>

Flag disabling or enabling the **SetColorDepthPolicy** property, which specifies whether to override the user's maximum color setting.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

Enable the property.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

Disable the property.

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

[**Win32\_TSClientSetting**](win32-tsclientsetting.md)
</dt> </dl>

 

