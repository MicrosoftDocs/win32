---
title: SetClientWallPaper method of the Win32_TSEnvironmentSetting class
description: The SetClientWallPaper method sets the ClientWallPaper property.
ms.assetid: 08c41df4-5a3c-4799-bb64-61f414814d0c
ms.tgt_platform: multiple
keywords:
- SetClientWallPaper method Remote Desktop Services
- SetClientWallPaper method Remote Desktop Services , Win32_TSEnvironmentSetting class
- Win32_TSEnvironmentSetting class Remote Desktop Services , SetClientWallPaper method
topic_type:
- apiref
api_name:
- Win32_TSEnvironmentSetting.SetClientWallPaper
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetClientWallPaper method of the Win32\_TSEnvironmentSetting class

The **SetClientWallPaper** method sets the **ClientWallPaper** property.

## Syntax


```mof
uint32 SetClientWallPaper(
  [in] uint32 ClientWallPaper
);
```



## Parameters

<dl> <dt>

*ClientWallPaper* \[in\]
</dt> <dd>

Flag disabling or enabling the **ClientWallPaper** property, which specifies whether the background (or wallpaper) image is displayed on the client.

<dt>

<span id="0"></span>

<span id="0"></span>**0**


</dt> <dd>

The background (or wallpaper) image is not displayed on the client.

</dd> <dt>

<span id="1"></span>

<span id="1"></span>**1**


</dt> <dd>

The background (or wallpaper) image is displayed on the client.

</dd> </dl> </dd> </dl>

## Return value

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

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

[**Win32\_TSEnvironmentSetting**](win32-tsenvironmentsetting.md)
</dt> </dl>

 

