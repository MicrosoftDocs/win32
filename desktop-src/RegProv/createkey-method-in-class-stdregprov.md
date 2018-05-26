---
title: CreateKey method of the StdRegProv class
description: Creates a subkey in the specified tree.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 8cbfb9ec-a3ea-445b-9ab3-d75cc112be69
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- CreateKey method
- CreateKey method, StdRegProv class
- StdRegProv class, CreateKey method
topic_type:
- apiref
api_name:
- StdRegProv.CreateKey
api_location:
- Stdprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# CreateKey method of the StdRegProv class

The **CreateKey** method creates a subkey in the specified tree.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 CreateKey(
  [in] uint32 hDefKey = HKEY_LOCAL_MACHINE,
  [in] String sSubKeyName
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

The key to be created. The **CreateKey** method creates all subkeys specified in the path that do not exist. For example, if **MyKey** and **MySubKey** do not exist in the following path, the **CreateKey** method creates both keys: **HKEY\_CURRENT\_USER**\\**SOFTWARE**\\**MyKey**\\**MySubKey**.

</dd> </dl>

## Return value

In C++, the method returns a **uint32** value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that is defined in WinError.h. In C++, use the [**FormatMessage**](https://msdn.microsoft.com/library/windows/desktop/ms679351) function with the **FORMAT\_MESSAGE\_FROM\_SYSTEM** flag to get a generic description of the error. You can also look up return values under the [**WMI Error Constants**](https://msdn.microsoft.com/library/aa394559).

In scripting or Visual Basic, the method returns an integer value that is 0 (zero) if successful. If the function fails, the return value is a nonzero error code that you can look up in [**WbemErrorEnum**](https://msdn.microsoft.com/library/aa393978).

## Remarks

You rarely need to create a registry subkey. However, in some circumstances the solution to a problem - as described in a Knowledge Base article or a security bulletin - requires the addition of a subkey. If you need to create a subkey on a large number of computers, the best solution might very well be a script. After all, a single script can be used to create the subkey on every computer affected by the problem. The Registry Provider's **CreateKey** method enables you to add a new subkey. It takes two parameters: a constant indicating the subtree to which the new subkey will be added and the path of the new subkey.

## Examples

The [Add Sites to an Internet Explorer Security Zone](https://Gallery.TechNet.Microsoft.Com/75588279-de13-44ba-9d8d-be0bfd646ea2) VBScript sample adds the Web site Contoso.com to the Trusted sites zone and BenefitsWeb to the Local intranet zone on a computer running Internet Explorer Enhanced Security Configuration.

The following PowerShell and VBScript code examples show how to use the **CreateKey** method to create the **SOFTWARE\\NewKey** subkeys under **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**.


```VB
Const HKEY_CURRENT_USER As Long = &amp;H80000001
strComputer = "."
Set objReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\default:StdRegProv")
strKeyPath = "Software\MyKey\MySubKey"
' Create new key and value
Return = objReg.CreateKey(HKEY_LOCAL_MACHINE, strKeyPath)

If (Return = 0) And (Err.Number = 0) Then    
    Wscript.Echo "HKEY_LOCAL_MACHINE\Software\MyKey\MySubKey created"
Else
    Wscript.Echo "CreateKey failed. Error = " & Err.Number
End If
```

<span codelanguage="PowerShell"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>PowerShell</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>$HKEY_LOCAL_MACHINE = 2147483650
$strKeyPath = &quot;SOFTWARE\NewKey&quot;

$objReg = [WMIClass]&quot;root\default:StdRegProv&quot;
[void]$objReg.CreateKey($HKEY_LOCAL_MACHINE, $strKeyPath)

&quot;Example created at &quot; + $strKeyPath</code></pre></td>
</tr>
</tbody>
</table>



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

 

 





