---
title: SetDWORDValue method of the StdRegProv class
description: Sets the data value for a named value whose data type is REG\_DWORD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7ede899e-b6ae-4b46-b29a-0ced74b40a3a'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetDWORDValue method", "SetDWORDValue method, StdRegProv class", "StdRegProv class, SetDWORDValue method"]
topic_type:
- apiref
api_name:
- StdRegProv.SetDWORDValue
api_location:
- Stdprov.dll
api_type:
- COM
---

# SetDWORDValue method of the StdRegProv class

The **SetDWORDValue** method sets the data value for a named value whose data type is **REG\_DWORD**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetDWORDValue(
  [in] uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in] string sSubKeyName,
  [in] string sValueName,
  [in] uint32 uValue = 
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


</dt> <dd></dd> </dl> </dd> <dt>

*sSubKeyName* \[in\]
</dt> <dd>

A key that contains the named value to be set.

</dd> <dt>

*sValueName* \[in\]
</dt> <dd>

A named value whose data value you are setting. You can specify an existing named value (update) or a new named value (create). Specify an empty string to set the data value for the default named value.

</dd> <dt>

*uValue* \[in\]
</dt> <dd>

A **DWORD** data value.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

Changing the values of registry entries is a common registry management task. The most challenging aspect of that task is determining which entries you need to change, and to which values they must be changed. After you have this information, you must choose the appropriate Registry Provider methods for making the change.

To change a string value (**REG\_SZ**), you use the [**SetStringValue**](setstringvalue-method-in-class-stdregprov.md) method; to change a numeric value (**DWORD**), you use the **SetDWORDValue** method. Each of these methods takes four parameters:

-   A constant that specifies the subtree in which the value being changed is located.
-   The path to the subkey in which the value is located.
-   The name of the entry with the value to be changed.
-   The new value.

These parameters are similar to the parameters used to read registry entries. The only difference is that when registry entries are read, the fourth parameter represents the value read from the registry; when registry entries are configured, the fourth parameter represents the new value being written to the registry.

Be certain to investigate whether other methods of configuration are available before deciding to script direct changes to the registry.

> \[!Caution\]  
> Regardless of where you obtain your information, always back up the registry before modifying it in any way.

 

## Examples

The following VBScript code example shows how to create **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**NewKey**\\**Example DWORD Value** and write a value of type **REG\_DWORD** to it. If **NewKey** already exists then the value is added to it. You can use a registry editor such as regedt32 to view the results of the script.


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strComputer = "."
Set oReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\default:StdRegProv")
strKeyPath = "SOFTWARE\NewKey"
strValueName = "Example DWORD Value"
oReg.SetDWORDValue _ 
    HKEY_LOCAL_MACHINE,strKeyPath,strValueName,250
If Err = 0 Then
   oReg.GetDWORDValue _
       HKEY_LOCAL_MACHINE,strKeyPath,strValueName,dwValue
   WScript.Echo _
       "HKEY_LOCAL_MACHINE\SOFTWARE\NewKey\Example DWORD Value contains " & dwValue
Else 
   WScript.Echo "Error in creating key and DWORD value = " & Err.Number
End If
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default<br/>                                                                |
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

 

 





