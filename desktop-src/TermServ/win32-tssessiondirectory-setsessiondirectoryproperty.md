---
title: SetSessionDirectoryProperty method of the Win32_TSSessionDirectory class
description: Sets the SessionDirectoryLocation property or the SessionDirectoryClusterName property for the class.
ms.assetid: 728e1991-294f-4b80-86f8-a0c2cfd10e9c
ms.tgt_platform: multiple
keywords:
- SetSessionDirectoryProperty method Remote Desktop Services
- SetSessionDirectoryProperty method Remote Desktop Services , Win32_TSSessionDirectory class
- Win32_TSSessionDirectory class Remote Desktop Services , SetSessionDirectoryProperty method
topic_type:
- apiref
api_name:
- Win32_TSSessionDirectory.SetSessionDirectoryProperty
api_location:
- TSCfgWmi.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# SetSessionDirectoryProperty method of the Win32\_TSSessionDirectory class

Sets the **SessionDirectoryLocation** property or the **SessionDirectoryClusterName** property for the class.

## Syntax


```mof
uint32 SetSessionDirectoryProperty(
  [in] string PropertyName,
  [in] string Value
);
```



## Parameters

<dl> <dt>

*PropertyName* \[in\]
</dt> <dd>

Type: **string**

Specifies the property that the method is setting.

<dt>

<span id="SessionDirectoryLocation"></span><span id="sessiondirectorylocation"></span><span id="SESSIONDIRECTORYLOCATION"></span>

<span id="SessionDirectoryLocation"></span><span id="sessiondirectorylocation"></span><span id="SESSIONDIRECTORYLOCATION"></span>**SessionDirectoryLocation**


</dt> <dd>

The method is setting the **SessionDirectoryLocation** property.

</dd> <dt>

<span id="SessionDirectoryClusterName"></span><span id="sessiondirectoryclustername"></span><span id="SESSIONDIRECTORYCLUSTERNAME"></span>

<span id="SessionDirectoryClusterName"></span><span id="sessiondirectoryclustername"></span><span id="SESSIONDIRECTORYCLUSTERNAME"></span>**SessionDirectoryClusterName**


</dt> <dd>

The method is setting the **SessionDirectoryClusterName** property.

</dd> </dl> </dd> <dt>

*Value* \[in\]
</dt> <dd>

Type: **string**

The new value for the property specified by the *PropertyName* parameter.

</dd> </dl>

## Return value

Type: **uint32**

Returns 0 on success, otherwise returns a WMI error code. Refer to [Remote Desktop Services WMI Provider Error Codes](terminal-services-wmi-provider-error-codes.md) for a list of these values. The method returns an error if the setting is under group policy control.

## Remarks

Managed Object Format (MOF) files contain the definitions for Windows Management Instrumentation (WMI) classes. MOF files are not installed as part of the Microsoft Windows Software Development Kit (SDK). They are installed on the server when you add the associated role by using the Server Manager. For more information about MOF files, see [Managed Object Format (MOF)](/windows/desktop/WmiSdk/managed-object-format--mof-).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMv2\\TerminalServices<br/>                                                |
| MOF<br/>                      | <dl> <dt>TSCfgWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>TSCfgWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_TSSessionDirectory**](win32-tssessiondirectory.md)
</dt> </dl>

 

