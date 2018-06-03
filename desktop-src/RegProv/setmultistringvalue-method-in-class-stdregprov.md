---
title: SetMultiStringValue method of the StdRegProv class
description: The SetMultiStringValue method sets the data value for a named value whose data type is REG\_MULTI\_SZ.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c8a63b4b-dc86-40e7-9362-9709d6859353
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetMultiStringValue method
- SetMultiStringValue method, StdRegProv class
- StdRegProv class, SetMultiStringValue method
topic_type:
- apiref
api_name:
- StdRegProv.SetMultiStringValue
api_location:
- Stdprov.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetMultiStringValue method of the StdRegProv class

The **SetMultiStringValue** method sets the data value for a named value whose data type is **REG\_MULTI\_SZ**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetMultiStringValue(
  [in] uint32  hDefKey = HKEY_LOCAL_MACHINE,
  [in] string  sSubKeyName,
  [in] string  sValueName,
  [in] Variant sValue[] = 
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

An array of string data values.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

Multistring-valued registry entries are relatively rare in the registry. The Registry Provider does, however, provide the **SetMultiStringValue** method to enable you to create these entries as needed. Because a multistring can store a list of strings, the **SetMultiStringValue** method accepts an array of strings as the parameter that determines the values of the entry.

Note that if you use the **SetMultiStringValue** method to append to an existing multistring-valued entry rather than create a new one, you have to first use the [**GetMultiStringValue**](getmultistringvalue-method-in-class-stdregprov.md) method to retrieve the existing list of strings. This is because **SetMultiStringValue** overwrites any existing value.

## Examples

The [Configure Desktop Module](https://Gallery.TechNet.Microsoft.Com/cc98b735-c943-4158-8b66-9c8aa78eafbd) PowerShell sample configures Windows Explorer settings, Internet Explorer download and Internet Explorer home pages.

The following VBScript code example shows how to write an array of new values to the **REG\_MULTI\_SZ** value that is located in **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**NewKey**\\**MultiValueName**.


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strKeyPath = "SOFTWARE\NewKey"
MultValueName = "Example Multistring Value"
strComputer = "."
iValues = Array("string1", "string2")
Set oReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\default:StdRegProv")
oReg.CreateKey HKEY_LOCAL_MACHINE,strKeyPath
oReg.SetMultiStringValue HKEY_LOCAL_MACHINE,strKeyPath,MultValueName,iValues
WScript.Echo "Set registry value HKLM\SOFTWARE\NewKey\Example MultiString Value to string1 string 2"

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

 

 





