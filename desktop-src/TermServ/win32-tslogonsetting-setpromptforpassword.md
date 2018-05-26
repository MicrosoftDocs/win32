---
title: SetPromptForPassword method of the Win32\_TSLogonSetting class
description: The SetPromptForPassword method sets the PromptForPassword property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eeeed374-4a8a-4014-833c-d931be3ef455
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- SetPromptForPassword method Remote Desktop Services
- SetPromptForPassword method Remote Desktop Services , Win32_TSLogonSetting class
- Win32_TSLogonSetting class Remote Desktop Services , SetPromptForPassword method
topic_type:
- apiref
api_name:
- Win32_TSLogonSetting.SetPromptForPassword
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetPromptForPassword method of the Win32\_TSLogonSetting class

The **SetPromptForPassword** method sets the **PromptForPassword** property.

## Syntax


```mof
uint32 SetPromptForPassword(
  [in] uint32 PromptForPassword
);
```



## Parameters

<dl> <dt>

*PromptForPassword* \[in\]
</dt> <dd>

Flag disabling or enabling the **PromptForPassword** property.

<dt>

0
</dt> <dd>

Disables password-prompting.

</dd> <dt>

1
</dt> <dd>

Enables password-prompting.

</dd> </dl> </dd> </dl>

## Return value

Returns Success on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

<dl> <dt>

**FALSE** (0)
</dt> <dt>

**TRUE** (1)
</dt> </dl>

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](https://msdn.microsoft.com/library/aa823192).

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSLogonSetting**](win32-tslogonsetting.md)
</dt> </dl>

 

 





