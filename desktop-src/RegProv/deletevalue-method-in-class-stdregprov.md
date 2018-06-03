---
title: DeleteValue method of the StdRegProv class
description: The DeleteValue method deletes a named value in the specified subkey.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6d0bc82b-4de8-45b3-aaa8-00206070e5b6
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteValue method
- DeleteValue method, StdRegProv class
- StdRegProv class, DeleteValue method
topic_type:
- apiref
api_name:
- StdRegProv.DeleteValue
api_location:
- Stdprov.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteValue method of the StdRegProv class

The **DeleteValue** method deletes a named value in the specified subkey.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 DeleteValue(
  [in] uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in] string sSubKeyName,
  [in] string sValueName
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

A key that contains the named value to be deleted.

</dd> <dt>

*sValueName* \[in\]
</dt> <dd>

The named value to be deleted from the subkey. Specify an empty string to delete the default named value. The default named value is not deleted. The value is set to the following: value not set.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Examples

The following VBScript code example shows how to use the **DeleteValue** method. For purposes of the example, a new key and value are created then the value is deleted.


```VB
Const HKEY_CURRENT_USER As Long = &amp;H80000001
strComputer = "."
Set objReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" &amp;_
                     strComputer & "\root\default:StdRegProv")
strKeyPath = "Software\MyKey\MySubKey"
' Create new key and value
Return = objReg.CreateKey(HKEY_LOCAL_MACHINE, strKeyPath)

If (Return = 0) And (Err.Number = 0) Then    
    Wscript.Echo "HKEY_LOCAL_MACHINE\Software\MyKey\MySubKey created"
Else
    Wscript.Echo "CreateKey failed. Error = " & Err.Number
End If
' Create new value
strValueName = "Example DWORD Value"
objReg.SetDWORDValue HKEY_LOCAL_MACHINE,strKeyPath,strValueName,250
If Err = 0 Then
   objReg.GetDWORDValue HKEY_LOCAL_MACHINE,strKeyPath,strValueName,dwValue
   WScript.Echo "HKEY_LOCAL_MACHINE\SOFTWARE\NewKey\Example DWORD " _
                & "Value contains " & dwValue
Else 
   WScript.Echo "Error in creating key and DWORD value = " & Err.Number
' Delete new value
Return = objReg.DeleteValue_
    (HKEY_LOCAL_MACHINE,strKeyPath,strValueName)

If (Return = 0) And (Err.Number = 0) Then
    WScript.Echo strValueName & "Registry value HKEY_LOCAL_MACHINE," _
                 & strKeyPath & "," & strValueName & "," & dwValue & " deleted"
Else
     WScript.Echo "Registry value not deleted" & VBNewLine _
                  & "Error = " & Err.Number
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

 

 





