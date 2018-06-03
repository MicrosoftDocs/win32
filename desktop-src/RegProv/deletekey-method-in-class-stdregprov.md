---
title: DeleteKey method of the StdRegProv class
description: Deletes a subkey in the specified tree.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: e26398a1-e8a8-4437-bc37-c65cbcd36d05
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DeleteKey method
- DeleteKey method, StdRegProv class
- StdRegProv class, DeleteKey method
topic_type:
- apiref
api_name:
- StdRegProv.DeleteKey
api_location:
- Stdprov.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DeleteKey method of the StdRegProv class

The **DeleteKey** method deletes a subkey in the specified tree.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 DeleteKey(
  [in] uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in] string sSubKeyName
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

The key to be deleted.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Examples

The [Delete a Registry Key](https://Gallery.TechNet.Microsoft.Com/a0bd42f4-f2e8-400e-8b8a-dd3746f77672) VBScript code sample deletes a registry key.

The following VBScript code example shows how to use the **DeleteKey** method to delete the **MySubKey** subkey created in the [**CreateKey**](createkey-method-in-class-stdregprov.md) example.


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strComputer = "."
Set objReg=GetObject("winmgmts:"_
    & "{impersonationLevel=impersonate}!\\" &amp;_ 
    strComputer & "\root\default:StdRegProv")

KeyPath = "Software\MyKey\MySubKey"
' Create new key
Return = objReg.CreateKey(HKEY_LOCAL_MACHINE, KeyPath)

If (Return = 0) And (Err.Number = 0) Then    
    Wscript.Echo "HKEY_LOCAL_MACHINE\Software\MyKey\MySubKey created"
Else
    Wscript.Echo "CreateKey failed. Error = " & Err.Number
End If

'Delete new key
Return = objReg.DeleteKey(HKEY_LOCAL_MACHINE, KeyPath)
If (Return = 0) And (Err.Number = 0) Then    
    Wscript.Echo _
        "HKEY_LOCAL_MACHINE\Software\MyKey\MySubKey" & _
        " successfully deleted"
Else
    Wscript.Echo "DeleteKey failed. Error = " & Err.Number
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

 

 





