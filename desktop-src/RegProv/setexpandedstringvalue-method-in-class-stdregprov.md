---
title: SetExpandedStringValue method of the StdRegProv class
description: The SetExpandedStringValue method sets the data value for a named value whose data type is REG\_EXPAND\_SZ.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c6067c2d-b16a-4db8-8834-012cd8669819
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetExpandedStringValue method
- SetExpandedStringValue method, StdRegProv class
- StdRegProv class, SetExpandedStringValue method
topic_type:
- apiref
api_name:
- StdRegProv.SetExpandedStringValue
api_location:
- Stdprov.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetExpandedStringValue method of the StdRegProv class

The **SetExpandedStringValue** method sets the data value for a named value whose data type is **REG\_EXPAND\_SZ**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetExpandedStringValue(
  [in] uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in] string sSubKeyName,
  [in] string sValueName,
  [in] string sValue = 
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

*sValue* \[in\]
</dt> <dd>

An expanded string data value. The environment variable specified in the string must exist for the string to be expanded when you call [**GetExpandedStringValue**](getexpandedstringvalue-method-in-class-stdregprov.md).

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

Expanded strings are strings that can include variables; these variables are resolved when an application or a service uses the value. For example, the value of an entry that references a file might include the variable %systemroot%. When a service, such as the Event Log, references the entry, the %systemroot% variable is replaced by the name of the directory containing the Windows system files (for example, C:\\Windows). On a different computer, one with Windows installed on drive D, this same registry value might be replaced by D:\\Windows.

If you need to create an entry that includes a value that might change, such as the path environment variable or the location of the current user's profile, you can use the **SetExpandedStringValue** method.

## Examples

The [Create Expanded String Values](https://Gallery.TechNet.Microsoft.Com/bea49a18-2a51-46d6-b41e-efe6927cc54e) VBScript sample uses WMI to create an expanded string value under the **HKLM\\SOFTWARE\\System Admin Scripting Guide** portion of the registry.

The following VBScript code example shows how to use the **SetExpandedStringValue** method. The script first creates a new key then creates a new expanded string value under the key.


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strComputer = "."
Set objReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\"&amp;_
    strComputer & "\root\default:StdRegProv")
' Create a new key
strKeyPath = "Software\MyKey\MySubKey"
Return = objReg.CreateKey(HKEY_LOCAL_MACHINE, strKeyPath)
If (Return = 0) And (Err.Number = 0) Then   
    Wscript.Echo _
        "HKEY_LOCAL_MACHINE\Software\MyKey\MySubKey created"
Else
    Wscript.Echo "CreateKey failed. Error = " & Err.Number
End If
' Create an expanded string and give it a value
strValueName = "Expanded String Value Name"
strValue = "%ExpandedStringValue%"
' Write expanded string value
Return = objReg.SetExpandedStringValue( _
    HKEY_LOCAL_MACHINE,strKeyPath,strValueName,strValue)
If (Return = 0) And (Err.Number = 0) Then   
    Wscript.Echo "SetExpandedStringValue succeeded"
Else
    Wscript.Echo _
        "SetExpandedStringValue failed. Error = " & Err.Number
End If
```



## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\default<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RegEvent.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Stdprov.dll</dt> </dl>  |



 

 





