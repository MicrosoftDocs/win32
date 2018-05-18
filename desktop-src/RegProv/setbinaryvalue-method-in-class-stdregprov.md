---
title: SetBinaryValue method of the StdRegProv class
description: The SetBinaryValue method sets the data value for a named value whose data type is REG\_BINARY.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '47e46838-7ad5-41c1-b46e-3af199f29f71'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetBinaryValue method", "SetBinaryValue method, StdRegProv class", "StdRegProv class, SetBinaryValue method"]
topic_type:
- apiref
api_name:
- StdRegProv.SetBinaryValue
api_location:
- Stdprov.dll
api_type:
- COM
---

# SetBinaryValue method of the StdRegProv class

The **SetBinaryValue** method sets the data value for a named value whose data type is **REG\_BINARY**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetBinaryValue(
  [in] uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in] string sSubKeyName,
  [in] string sValueName,
  [in] uint8  uValue[]
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

An array of binary data values. The default value is \[1,2\].

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Examples

The [Send a file to the Recycle Bin](https://Gallery.TechNet.Microsoft.Com/191eb207-3a7e-4dbc-884d-5f4498440574) VBScript code sample sends a file to the Recycle Bin instead of permanently deleting that file.

The following VBScript code example shows how to write a new value to the **REG\_BINARY** value that is located in **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**MyKey**\\**MyBinaryNamedValue**.


```VB
Const HKEY_CURRENT_USER = &amp;H80000001
Set objRegistry = _
   GetObject("Winmgmts:root\default:StdRegProv")

strPath = "Software\MyKey"
uBinary = Array(1,2,3,4,5,6,7,8)
Return = objRegistry.SetBinaryValue(HKEY_CURRENT_USER, _
   strPath, _
   "MyBinaryNamedValue", _
   uBinary)

If (Return = 0) And (Err.Number = 0) Then
    Wscript.Echo "Binary value added successfully"
Else
    ' An error occurred
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

 

 





