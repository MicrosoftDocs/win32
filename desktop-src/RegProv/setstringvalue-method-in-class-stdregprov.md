---
title: SetStringValue method of the StdRegProv class
description: The SetStringValue method sets the data value for a named value whose data type is REG\_SZ.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: dc4a9eee-52a2-4584-86ea-8df4ce2e24b5
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetStringValue method
- SetStringValue method, StdRegProv class
- StdRegProv class, SetStringValue method
topic_type:
- apiref
api_name:
- StdRegProv.SetStringValue
api_location:
- Stdprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetStringValue method of the StdRegProv class

The **SetStringValue** method sets the data value for a named value whose data type is **REG\_SZ**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetStringValue(
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

The following trees are defined in Winreg.h.

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

A data value.

</dd> </dl>

## Return value

If the key does not exist, then the call to the **SetStringValue** method fails.

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

Changing the values of registry entries is a common registry management task. The most challenging aspect of that task is determining which entries you need to change, and to which values they must be changed. After you have this information, you must choose the appropriate Registry Provider methods for making the change.

To change a string value (**REG\_SZ**), you use the **SetStringValue** method; to change a numeric value (**REG\_DWORD**), you use the [**SetDWORDValue**](setdwordvalue-method-in-class-stdregprov.md) method. Each of these methods takes four parameters:

-   A constant that specifies the subtree in which the value being changed is located.
-   The path to the subkey in which the value is located.
-   The name of the entry with the value to be changed.
-   The new value.

These parameters are similar to the parameters used to read registry entries. The only difference is that when registry entries are read, the fourth parameter represents the value read from the registry; when registry entries are configured, the fourth parameter represents the new value being written to the registry.

Be certain to investigate whether other methods of configuration are available before deciding to script direct changes to the registry.

> \[!Caution\]  
> Regardless of where you obtain your information, always back up the registry before modifying it in any way.

 

## Examples

The [Change Computer Name](https://Gallery.TechNet.Microsoft.Com/e43bccc6-e612-4911-9b47-00c3841d983b) VBScript sample changes the local computer name.

The following VBScript code example shows how to call the **SetStringValue** method to write a string value to a key. The script first creates the key.


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strComputer = "."
Set objReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\"&amp;_ 
    strComputer & "\root\default:StdRegProv")

strKeyPath = "SOFTWARE\MyKey\"
KeyPath = "Software\MyKey"
strValueName = "String Value Name"
strValue = "string value"

' Create key to use
Return = objReg.CreateKey(HKEY_LOCAL_MACHINE, KeyPath)
If (Return = 0) And (Err.Number = 0) Then   
    Wscript.Echo "HKEY_LOCAL_MACHINE\Software\MyKey created"

    ' write string value to key    
    Return = objReg.SetStringValue( _
        HKEY_LOCAL_MACHINE,strKeyPath,strValueName,strValue)
    If (Return = 0) And (Err.Number = 0) Then 
        Wscript.Echo "HKEY_LOCAL_MACHINE\Software\MyKey" & _ 
            " contains 'string value'"
    Else
        Wscript.Echo "SetStringValue failed. Error = " & Err.Number
    End If
Else
    Wscript.Echo "CreateKey failed. Error = " & Err.Number
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



## See also

<dl> <dt>

[**StdRegProv**](stdregprov.md)
</dt> <dt>

[Modifying the System Registry](https://msdn.microsoft.com/library/aa392388)
</dt> <dt>

[WMI Tasks: Registry](https://msdn.microsoft.com/library/aa394600)
</dt> </dl>

 

 





