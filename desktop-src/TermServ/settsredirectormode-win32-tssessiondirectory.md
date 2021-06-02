---
title: SetTSRedirectorMode method of the Win32_TSSessionDirectory class
description: Sets the value to indicate whether the server will act as a Remote Desktop Services redirector.
ms.assetid: abdb92df-1e49-4445-ba02-bb83fd1ca541
ms.tgt_platform: multiple
keywords:
- SetTSRedirectorMode method Remote Desktop Services
- SetTSRedirectorMode method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , SetTSRedirectorMode method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.SetTSRedirectorMode
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetTSRedirectorMode method of the Win32\_TSSessionDirectory class

Sets the value to indicate whether the server will act as a Remote Desktop Services redirector.

## Syntax


```mof
uint32 SetTSRedirectorMode(
  [in] uint32 TSRedirValue
);
```



## Parameters

<dl> <dt>

*TSRedirValue* \[in\]
</dt> <dd>

Type: **uint32**

Specifies if the server will act as a Remote Desktop Services redirector. This can be one of the following values.

<dt>

0
</dt> <dd>

The server will act as a Remote Desktop Services redirector.

</dd> <dt>

1
</dt> <dd>

The server will not act as a Remote Desktop Services redirector.

</dd> </dl> </dd> </dl>

## Return value

Type: **uint32**

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                       |
| End of client support<br/>    | None supported<br/>                                                               |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                       |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSSessionDirectory**](win32-tssessiondirectory.md)
</dt> </dl>

 

