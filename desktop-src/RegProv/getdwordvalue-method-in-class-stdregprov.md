---
title: GetDWORDValue method of the StdRegProv class
description: The GetDWORDValue method returns the data value for a named value whose data type is REG\_DWORD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a7a64c2c-a260-41a3-9fdf-d1869c0c7db3'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetDWORDValue method", "GetDWORDValue method, StdRegProv class", "StdRegProv class, GetDWORDValue method"]
topic_type:
- apiref
api_name:
- StdRegProv.GetDWORDValue
api_location:
- Stdprov.dll
api_type:
- COM
---

# GetDWORDValue method of the StdRegProv class

The **GetDWORDValue** method returns the data value for a named value whose data type is **REG\_DWORD**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetDWORDValue(
  [in]  uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in]  string sSubKeyName,
  [in]  string sValueName,
  [out] uint32 uValue
);
```



## Parameters

<dl> <dt>

*hDefKey* \[in\]
</dt> <dd>

A registry tree, also known as a hive, that contains the *sSubKeyName* path. The default value is **HKEY\_LOCAL\_MACHINE**.

The following trees are defined in WinReg.h.

<dt>

<span id="HKEY_CLASSES_ROOT"></span><span id="hkey_classes_root"></span>

**HKEY\_CLASSES\_ROOT** (2147483648)


</dt> <dd></dd> <dt>

<span id="HKEY_CURRENT_USER"></span><span id="hkey_current_user"></span>

**HKEY\_CURRENT\_USER** (2147483649)


</dt> <dd></dd> <dt>

<span id="HKEY_LOCAL_MACHINE"></span><span id="hkey_local_machine"></span>

**HKEY\_LOCAL\_MACHINE** (2147483650)


</dt> <dd></dd> <dt>

<span id="HKEY_USERS"></span><span id="hkey_users"></span>

**HKEY\_USERS** (2147483651)


</dt> <dd></dd> <dt>

<span id="HKEY_CURRENT_CONFIG"></span><span id="hkey_current_config"></span>

**HKEY\_CURRENT\_CONFIG** (2147483653)


</dt> <dd></dd> <dt>

<span id="HKEY_DYN_DATA"></span><span id="hkey_dyn_data"></span>

**HKEY\_DYN\_DATA** (2147483654)


</dt> <dd></dd> </dl> </dd> <dt>

*sSubKeyName* \[in\]
</dt> <dd>

A path that contains the named values.

</dd> <dt>

*sValueName* \[in\]
</dt> <dd>

A named value whose data value you are retrieving. Specify an empty string to get the default named value.

</dd> <dt>

*uValue* \[out\]
</dt> <dd>

A **DWORD** data value for the named value.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

The majority of registry values that hold useful information for a system administrator are made up of either alphanumeric characters (**REG\_SZ**) or numbers (**REG\_DWORD**). String values in the registry are often clearly interpretable words, such as the name of a component manufacturer. Registry values of other types, like binary values, cannot be interpreted quite so readily.

You can read **REG\_SZ** and **REG\_DWORD** values by using the [**GetStringValue**](getstringvalue-method-in-class-stdregprov.md) and the **GetDWORDValue** methods, respectively.

## Examples

The following VBScript code example shows how to read and display the value in the **DWORD** registry value **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Control**\\**CrashControl**\\**AutoReboot**.


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strComputer = "."
Set StdOut = WScript.StdOut
Set oReg=GetObject( _
    "winmgmts:{impersonationLevel=impersonate}!\\" &amp;_ 
    strComputer & "\root\default:StdRegProv")
strKeyPath = "SYSTEM\CurrentControlSet\Control\CrashControl"
strValueName = "AutoReboot"
oReg.GetDWORDValue HKEY_LOCAL_MACHINE,strKeyPath,strValueName,dwValue
WScript.Echo "SYSTEM\CurrentControlSet\Control\" _
    & "CrashControl\AutoReboot" _
    & " = " & dwValue
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default<br/>                                                                |
| Header<br/>                   | <dl> <dt>Upnphost.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>RegEvent.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Stdprov.dll</dt> </dl>  |



## See also

<dl> <dt>

[**StdRegProv**](stdregprov.md)
</dt> <dt>

[Modifying the System Registry](https://msdn.microsoft.com/library/aa392388)
</dt> <dt>

[WMI Tasks: Registry](https://msdn.microsoft.com/library/aa394600)
</dt> </dl>

 

 





