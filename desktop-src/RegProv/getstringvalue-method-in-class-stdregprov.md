---
title: GetStringValue method of the StdRegProv class
description: Returns the data value for a named value whose data type is REG\_SZ.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9cd8d255-23d0-47a4-b207-08a6818ddfbe
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetStringValue method
- GetStringValue method, StdRegProv class
- StdRegProv class, GetStringValue method
topic_type:
- apiref
api_name:
- StdRegProv.GetStringValue
api_location:
- Stdprov.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetStringValue method of the StdRegProv class

The **GetStringValue** method returns the data value for a named value whose data type is **REG\_SZ**.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 GetStringValue(
  [in]  uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in]  string sSubKeyName,
  [in]  string sValueName,
  [out] string sValue
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

\[in\] A path that contains the named values.

</dd> <dt>

*sValueName* \[in\]
</dt> <dd>

\[in\] A named value whose data value you are retrieving. Specify an empty string to get the default named value.

</dd> <dt>

*sValue* \[out\]
</dt> <dd>

\[out\] A data value for the named value.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

The majority of registry values that hold useful information for a system administrator are made up of either alphanumeric characters (**REG\_SZ**) or numbers (**REG\_DWORD**). String values in the registry are often clearly interpretable words, such as the name of a component manufacturer. Registry values of other types, like binary values, cannot be interpreted quite so readily.

You can read **REG\_SZ** and **REG\_DWORD** values by using the **GetStringValue** and the [**GetDWORDValue**](getdwordvalue-method-in-class-stdregprov.md) methods, respectively.

## Examples

The [List Installed Applications on 32- or 64-Bit Computers](https://Gallery.TechNet.Microsoft.Com/37e834bc-3c64-4c23-b448-3659d3ac2dcf) VBScript code sample queries the registry for installed applications on either 32-bit or 64-bit systems.

The following VBScript sample returns a list of startup scripts displayed on a per-Group Policy Object (GPO) basis.


```VB
Const HKEY_LOCAL_MACHINE = &amp;H80000002 
 
strComputer = "." 
  
Set oReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & _  
    strComputer & "\root\default:StdRegProv") 
  
strKeyPath = "Software\Policies\Microsoft\Windows\System\Scripts\Startup" 
oReg.EnumKey HKEY_LOCAL_MACHINE, strKeyPath, arrSubKeys 
  
For Each subkey In arrSubKeys 
    strValueName  = "DisplayName" 
    strGUIDVName  = "GPOName" 
    strFullKeyPath = strKeyPath & "\" & subkey 
    oReg.GetStringValue HKEY_LOCAL_MACHINE, strFullKeyPath, strValueName, szValue  
    oReg.GetStringValue HKEY_LOCAL_MACHINE, strFullKeyPath, strGUIDVName, szGPOName  
    wScript.Echo "Name and GUID of GPO deploying Startup Script = " & szValue & _ 
        "    " & szGPOName 
 
    oReg.EnumKey HKEY_LOCAL_MACHINE, strFullKeyPath, arrGPOSubKeys 
    For Each Scriptsubkey in arrGPOSubkeys 
        ' Script and parameters under subkeys 
        strScript = "Script" 
        strParam  = "Parameters" 
        strScriptKeyPath = strFullKeyPath & "\" & Scriptsubkey 
        oReg.GetStringValue HKEY_LOCAL_MACHINE, strScriptKeyPath, strScript, szScript  
        oReg.GetStringValue HKEY_LOCAL_MACHINE, strScriptKeyPath, strParam,  szParam  
        wScript.Echo "   Shutdown script = " & szScript 
        wScript.Echo "   Script Parameters = " & szParam 
        wScript.Echo "    " 
    Next 
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

 

 





