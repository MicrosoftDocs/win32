---
title: GetMultiStringValue method of the StdRegProv class
description: The GetMultiStringValue method returns the data value for a named value whose data type is REG\_MULTI\_SZ.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 97b57a9a-6640-4ea9-8398-e5031425c3c3
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetMultiStringValue method
- GetMultiStringValue method, StdRegProv class
- StdRegProv class, GetMultiStringValue method
topic_type:
- apiref
api_name:
- StdRegProv.GetMultiStringValue
api_location:
- Stdprov.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetMultiStringValue method of the StdRegProv class

The **GetMultiStringValue** method returns the data value for a named value whose data type is **REG\_MULTI\_SZ**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetMultiStringValue(
  [in]  uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in]  string sSubKeyName,
  [in]  string sValueName,
  [out] string sValue[]
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

A named value whose data value you are retrieving.

</dd> <dt>

*sValue* \[out\]
</dt> <dd>

An array of string data values for the named value.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

A multistring value stores a list of strings. A typical use of a multistring value is demonstrated by the Autorecover MOFs entry in the **HKEY\_LOCAL\_MACHINE\\SOFTWARE\\Microsoft\\WBEM\\CIMOM** subkey. This entry holds a list of .mof files that are used to autorecover the CIM repository. The list could have been held in a series of string-valued entries, all stored under a single Autorecover MOFs subkey. However, using a multistring value is more compact and makes programmatic retrieval of the values more convenient. With a multistring entry, there is only one registry entry to read, which makes it more likely that you will retrieve every value. By contrast, storing each value in a separate registry entry requires you to individually read each of those entries. In turn, that increases the likelihood of you missing a value.

You use the **GetMultiStringValue** method to retrieve a multistring value. The method takes as one of its parameters a variable that holds the set of strings retrieved. The strings are returned in an array, so you must use a For Each loop in your script to enumerate each of the individual strings in the array.

## Examples

The [Show NIC Binding Order](https://Gallery.TechNet.Microsoft.Com/Show-NIC-Binding-Order-cbf8dae3) VBScript sample shows the NIC binding order.

The [Get or Set the Internet Explorer Start Pages](https://Gallery.TechNet.Microsoft.Com/e25bf8ea-e294-4680-af17-b984bed47e97) PowerShell sample retrieves the IE start page or pages, and will also allow you to set the IE start pages.

The following VBScript code example shows how to read the value of type **REG\_MULTI\_SZ** located in the registry key **HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**CurrentControlSet**\\**Services**\\**Eventlog**\\**System**\\**Sources** and print the list to the screen. You can save the script as a file with a .vbs extension and send the output to a file by executing the command line in the folder that contains the script:

**cscript Filename.vbs &gt;** *output.txt*


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strComputer = "."
Set objReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\"&amp;_ 
    strComputer & "\root\default:StdRegProv")
strKeyPath = "SYSTEM\CurrentControlSet\Services\Eventlog\System"
strValueName = "Sources"
Return = objReg.GetMultiStringValue(HKEY_LOCAL_MACHINE,strKeyPath,_
    strValueName,arrValues)
If (Return = 0) And (Err.Number = 0) Then   
' Treat the multistring value as a collection of strings 
'    separated by spaces and output
    For Each strValue In arrValues
    WScript.Echo  strValue
Next
Else
    Wscript.Echo "GetMultiStringValue failed. Error = " & Err.Number
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

 

 





