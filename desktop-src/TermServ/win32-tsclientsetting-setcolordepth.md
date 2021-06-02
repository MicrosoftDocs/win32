---
title: SetColorDepth method of the Win32_TSClientSetting class
description: The SetColorDepth method sets the ColorDepth property for the class.
ms.assetid: 1ab8ac41-cbbf-4077-b91e-692856ccba42
ms.tgt_platform: multiple
keywords:
- SetColorDepth method Remote Desktop Services
- SetColorDepth method Remote Desktop Services , Win32_TSClientSetting class
- Win32_TSClientSetting class Remote Desktop Services , SetColorDepth method
topic_type:
- apiref
api_name:
- Win32_TSClientSetting.SetColorDepth
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetColorDepth method of the Win32\_TSClientSetting class

The **SetColorDepth** method sets the **ColorDepth** property for the class.

## Syntax


```mof
uint32 SetColorDepth(
  [in] uint32 ColorDepth
);
```



## Parameters

<dl> <dt>

*ColorDepth* \[in\]
</dt> <dd>

The new value for the **ColorDepth** property.

<dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

8 bits per pixel

</dd> <dt>

<span id="2"></span>

<span id="2"></span>**2**


</dt> <dd>

15 bits per pixel

</dd> <dt>

<span id="3"></span>

<span id="3"></span>**3**


</dt> <dd>

16 bits per pixel

</dd> <dt>

<span id="4"></span>

<span id="4"></span>**4**


</dt> <dd>

24 bits per pixel

</dd> <dt>

<span id="5"></span>

<span id="5"></span>**5**


</dt> <dd>

32 bits per pixel

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

 

