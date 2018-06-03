---
title: GetBinaryValue method of the StdRegProv class
description: The GetBinaryValue method returns the data value for a named value whose data type is REG\_BINARY.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: b6f81c83-809f-4045-92d6-347ee3dc788e
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetBinaryValue method
- GetBinaryValue method, StdRegProv class
- StdRegProv class, GetBinaryValue method
topic_type:
- apiref
api_name:
- StdRegProv.GetBinaryValue
api_location:
- Stdprov.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetBinaryValue method of the StdRegProv class

The **GetBinaryValue** method returns the data value for a named value whose data type is **REG\_BINARY**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetBinaryValue(
  [in]  uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in]  string sSubKeyName,
  [in]  string sValueName,
  [out] uint8  uValue[]
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

A path that contains the named values.

</dd> <dt>

*sValueName* \[in\]
</dt> <dd>

A named value whose data value you are retrieving. Specify an empty string to get the default named value.

</dd> <dt>

*uValue* \[out\]
</dt> <dd>

An array of binary bytes.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

Binary registry values are very cryptic, and difficult for humans to make sense of. However, there is useful information in the registry that is stored in binary format. As an advanced system administrator, you might find yourself interested in understanding, and possibly even editing, certain binary entries. For example, services are organized in groups. The **GroupOrderList** subkey stores information about the order in which groups of services are loaded when Windows boots. This information looks similar to the following:

`17 0 0 0 14 0 0 0 1 0 0 0 2 0 0 0 3 0 0 0 4 0 0 0 5 0 0 0 6 0 0 0 7 0 0 0 8 0 0 0 9 0 0 0  10 0 0 0 11 0 0 0 12 0 0 0 13 0 0 0 15 0 0 0 16 0 0 0 17 0 0 0`

Although this type of information is rarely useful to a system administrator, it can be important to support personnel troubleshooting computer problems. If support personnel need to know the value of a binary registry entry, you can use scripts to retrieve this information.

The caution about manipulating registry entries directly is even more relevant with binary entry values. For one thing, they are cryptic, with no obvious meaning. Along the same lines, they are difficult to remember in case you need to restore their original values. Although there is no harm in reading one of these values, be very careful about modifying the value in any way.

The Registry Provider includes the **GetBinaryValue** method to enable you to work with binary entry values. The method takes, as one of its parameters, a variable that is used to store the retrieved value. The value is returned as an array of bytes. Therefore, to extract the value, you need to loop through the array, extracting a single byte with each pass.

## Examples

For an example of how to use **GetBinaryValue**, see the example in the [**GetDWORDValue**](getdwordvalue-method-in-class-stdregprov.md) topic.

The [Multithreaded Remote Registry Gathering](https://Gallery.TechNet.Microsoft.Com/Multithreaded-Remote-ca714e12) with Powershell sample gathers specific subkey values or an entire registry key s subkey values with PowerShell and multithreading.

The following code sample uses WMI to read a binary registry value.


```VB
Const HKEY_LOCAL_MACHINE = &amp;H80000002

strComputer = "."
Set StdOut = WScript.StdOut
 
Set oReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & _ 
    strComputer & "\root\default:StdRegProv")
 
strKeyPath = "SOFTWARE\Microsoft\Windows NT\CurrentVersion"
strValueName = "LicenseInfo"
oReg.GetBinaryValue HKEY_LOCAL_MACHINE,strKeyPath, _
    strValueName,strValue
 
 
For i = lBound(strValue) to uBound(strValue)
    StdOut.WriteLine  strValue(i)
Next
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

 

 





