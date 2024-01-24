---
title: InitialProgram method of the Win32_TSEnvironmentSetting class
description: The InitialProgram method sets startup program properties such as the name, working directory, and path of the program to start immediately after logon to the Remote Desktop Session Host (RD Session Host) server.
ms.assetid: e53621cf-ade8-4301-acc0-232866e88488
ms.tgt_platform: multiple
keywords:
- InitialProgram method Remote Desktop Services
- InitialProgram method Remote Desktop Services , Win32_TSEnvironmentSetting class
- Win32_TSEnvironmentSetting class Remote Desktop Services , InitialProgram method
topic_type:
- apiref
api_name:
- Win32_TSEnvironmentSetting.InitialProgram
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# InitialProgram method of the Win32\_TSEnvironmentSetting class

The **InitialProgram** method sets startup program properties such as the name, working directory, and path of the program to start immediately after logon to the Remote Desktop Session Host (RD Session Host) server.

## Syntax


```mof
uint32 InitialProgram(
  [in] string InitialProgramPath,
  [in] string Startin
);
```



## Parameters

<dl> <dt>

*InitialProgramPath* \[in\]
</dt> <dd>

The name and path of the startup program.

</dd> <dt>

*Startin* \[in\]
</dt> <dd>

The path to the working directory of the startup program.

</dd> </dl>

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

 

