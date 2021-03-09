---
title: EnvironmentVariables method of the Win32_TSExpandEnvironmentVariables class
description: Expands system-defined environment variables. | EnvironmentVariables method of the Win32_TSExpandEnvironmentVariables class
ms.assetid: eff0dcdf-ef98-4730-9b0c-4f44250a607b
ms.tgt_platform: multiple
keywords:
- EnvironmentVariables method Remote Desktop Services
- EnvironmentVariables method Remote Desktop Services , Win32_TSExpandEnvironmentVariables class
- Win32_TSExpandEnvironmentVariables class Remote Desktop Services , EnvironmentVariables method
topic_type:
- apiref
api_name:
- Win32_TSExpandEnvironmentVariables.EnvironmentVariables
api_location:
- TsPubWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# EnvironmentVariables method of the Win32\_TSExpandEnvironmentVariables class

Expands system-defined environment variables.

## Syntax


```mof
uint32 EnvironmentVariables(
  [in]  string OriginalString,
  [out] string ExpandedString
);
```



## Parameters

<dl> <dt>

*OriginalString* \[in\]
</dt> <dd>

A string that contains the environment variables to expand.

</dd> <dt>

*ExpandedString* \[out\]
</dt> <dd>

A string with the environment variables expanded.

</dd> </dl>

## Remarks

You must be a member of the Administrators group to call this method.

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>Tsallow.mof</dt> </dl>  |
| DLL<br/>                      | <dl> <dt>TsPubWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSExpandEnvironmentVariables**](win32-tsexpandenvironmentvariables.md)
</dt> </dl>

 

