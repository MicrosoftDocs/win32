---
title: EnumValues method of the StdRegProv class
description: Enumerates the values of the given subkey.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c673911e-1b72-4ad5-a79d-ee32a1e4e90c
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- EnumValues method
- EnumValues method, StdRegProv class
- StdRegProv class, EnumValues method
topic_type:
- apiref
api_name:
- StdRegProv.EnumValues
api_location:
- Stdprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# EnumValues method of the StdRegProv class

The **EnumValues** method enumerates the values of the given subkey. If it has not been changed, the default value of the registry key is always returned. The method returns an empty string ("") if the data is empty. For more information about accessing the registry with WMI, see [Obtaining Registry Data](https://msdn.microsoft.com/library/aa392722).

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 EnumValues(
  [in]  uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in]  string sSubKeyName,
  [out] string sNames[],
  [out] sint32 Types[]
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

A path that contains the named values to be enumerated.

</dd> <dt>

*sNames* \[out\]
</dt> <dd>

An array of named value strings. The elements of this array correspond directly to the elements of the *Types* parameter. Returns null if only the default value is available.

</dd> <dt>

*Types* \[out\]
</dt> <dd>

An array of data value types (integers). You can use these types to determine which of the several **Get** methods to call. For example, if the data value type is **REG\_SZ**, you call the [**GetStringValue**](getstringvalue-method-in-class-stdregprov.md) method to retrieve the named value's data value. The elements of this array correspond directly with the elements of the *sNames* parameter.

The following data value types are defined in WinNT.h:

-   **REG\_SZ** (1)
-   **REG\_EXPAND\_SZ** (2)
-   **REG\_BINARY** (3)
-   **REG\_DWORD** (4)
-   **REG\_MULTI\_SZ** (7)
-   **REG\_QWORD** (11)

Returns null if only the default value is available.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

Registry subkeys group entries with related information, and it is often useful to display that related information. Unfortunately, this is not necessarily a straightforward procedure; after all, you cannot read a registry value unless you use the appropriate method. But how can you call the appropriate method if you do not know the data type of the value being read?

Fortunately, you can accomplish this task by using the Registry Provider EnumValues method to retrieve an array containing the entry names and an array containing the data type of each entry. After you know the entry name and its data type, you can select the appropriate method to retrieve and display the value of each entry.

This method returns a null value for the array when the default value is the only one present. When writing scripts, be sure to check for the null value (using IsNull); this is a good practice before accessing any VBScript variant.

## Examples

The [List All Installed Software](https://Gallery.TechNet.Microsoft.Com/8035d5a9-dc92-436d-a60c-67d381da15a3) VBScript sample returns a list of all software installed on a computer, whether or not by Windows Installer, by reading installed applications from the registry.

The [Gather Remote Firewall Status And Rules With Powershell](https://Gallery.TechNet.Microsoft.Com/Gather-Remote-Firewall-1d8721e4) sample gathers the firewall status and rules from multiple systems

The following VBScript code example shows how to enumerate the values under:

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**Current Control Set**\\**Control**\\**Lsa**

You can save the script as a file with a .vbs extension and send the output to a file by executing the command line in the folder that contains the script:

**cscript** *Filename.vbs* **&gt;** *output.txt*


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
const REG_SZ = 1
const REG_EXPAND_SZ = 2
const REG_BINARY = 3
const REG_DWORD = 4
const REG_MULTI_SZ = 7
strComputer = "."
Set oReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" &amp;_ 
   strComputer & "\root\default:StdRegProv")
strKeyPath = "SYSTEM\CurrentControlSet\Control\Lsa"
oReg.EnumValues HKEY_LOCAL_MACHINE, strKeyPath,_
   arrValueNames, arrValueTypes
For I=0 To UBound(arrValueNames)
    WScript.Echo "Value Name: " & arrValueNames(I) 
    Select Case arrValueTypes(I)
        Case REG_SZ
            WScript.Echo "Data Type: String"
        Case REG_EXPAND_SZ
            WScript.Echo "Data Type: Expanded String"
        Case REG_BINARY
            WScript.Echo "Data Type: Binary"
        Case REG_DWORD
            WScript.Echo "Data Type: DWORD"
        Case REG_MULTI_SZ
            WScript.Echo "Data Type: Multi String"
    End Select 
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

 

 





