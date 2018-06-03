---
Description: You can obtain or modify registry data by using the WMI StdRegProv class and its methods.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7cba9dcb-741b-4118-9769-8830c6dc0752
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Obtaining Registry Data
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Registry Data

You can obtain or modify registry data by using the WMI [**StdRegProv**](https://msdn.microsoft.com/library/aa393664) class and its methods. While use the Regedit utility to view and change registry values on the local computer, **StdRegProv** allows you to use a script or application to automate such activities on the local computer and remote computers.

[**StdRegProv**](https://msdn.microsoft.com/library/aa393664) contains methods to do the following:

-   Verify the access permissions for a user
-   Create, enumerate, and delete registry keys
-   Create, enumerate, and delete subkeys or named values
-   Read, write, and delete data values

Registry data is organized by subtrees, keys, and subkeys nested under a top level key. The actual data values are called entries or named values.

The subtrees include the following:

-   **HKEY\_CLASSES\_ROOT** (abbreviated as **HKCR**)
-   **HKEY\_CURRENT\_USER** (**HKCU**)
-   **HKEY\_LOCAL\_MACHINE** (**HKLM**)
-   **HKEY\_USERS**
-   **HKEY\_CURRENT\_CONFIG**

For example, in the registry entry **HKEY**\\**SOFTWARE**\\**Microsoft**\\**DirectX**\\**InstalledVersion**, the HKEY subtree is **SOFTWARE**; the subkeys are **Microsoft** and **DirectX**; and the named value entry is **InstalledVersion**.

A [**RegistryKeyChangeEvent**](https://msdn.microsoft.com/library/aa393040) occurs when a change to a specific key occurs, but the entry does not identify how the values change nor will this event be triggered by changes below the specified key. To identify changes anywhere in a hierarchical key structure, use the [**RegistryTreeChangeEvent**](https://msdn.microsoft.com/library/aa393041), which does not return specific values or key changes that occur. To obtain a specific entry value change, use the [**RegistryValueChangeEvent**](https://msdn.microsoft.com/library/aa393042), and then read the entry to obtain a baseline value.

[**StdRegProv**](https://msdn.microsoft.com/library/aa393664) only has methods that can be called from C++ or script, which is different from the Win32 class structure.

The following code example shows how to use the [**StdRegProv.EnumKey**](https://msdn.microsoft.com/library/aa390387) method to list all of the Microsoft software subkeys under the registry key.

**HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**Microsoft**


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strComputer = "."

Set objReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" & strComputer & "\root\default:StdRegProv")

strKeyPath = "SOFTWARE\Microsoft"
objReg.EnumKey HKEY_LOCAL_MACHINE, strKeyPath, arrSubKeys

For Each subkey In arrSubKeys
Wscript.Echo subkey
    
Next
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
$strKeyPath = &quot;SOFTWARE\Microsoft&quot;

$objReg = [WMIClass]&quot;root\default:StdRegProv&quot;

$arrSubKeys = $objReg.EnumKey($HKEY_LOCAL_MACHINE, $strKeyPath)
foreach ($subKey in ($arrSubKeys.sNames))
{
    $subKey
}</code></pre></td>
</tr>
</tbody>
</table>



[**StdRegProv**](https://msdn.microsoft.com/library/aa393664) has different methods for reading the various registry entry value data types. If the entry has unknown values, then you can call [**StdRegProv.EnumValues**](https://msdn.microsoft.com/library/aa390388) to list them. The following table lists the correspondence between **StdRegProv** methods and the data types.



| Method                                                                                  | Data Type           |
|-----------------------------------------------------------------------------------------|---------------------|
| [**GetBinaryValue**](https://msdn.microsoft.com/library/aa390440)                 | **REG\_BINARY**     |
| [**GetDWORDValue**](https://msdn.microsoft.com/library/aa390445)                   | **REG\_DWORD**      |
| [**GetExpandedStringValue**](https://msdn.microsoft.com/library/aa390455) | **REG\_EXPAND\_SZ** |
| [**GetMultiStringValue**](https://msdn.microsoft.com/library/aa390458)       | **REG\_MULTI\_SZ**  |
| [**GetStringValue**](https://msdn.microsoft.com/library/aa390788)                 | **REG\_SZ**         |



 

The following table lists the corresponding methods for creating new keys or values, or changing existing ones.



| Method                                                                                  | Data Type           |
|-----------------------------------------------------------------------------------------|---------------------|
| [**SetBinaryValue**](https://msdn.microsoft.com/library/aa393286)                 | **REG\_BINARY**     |
| [**SetDWORDValue**](https://msdn.microsoft.com/library/aa393297)                   | **REG\_DWORD**      |
| [**SetExpandedStringValue**](https://msdn.microsoft.com/library/aa393299) | **REG\_EXPAND\_SZ** |
| [**SetMultiStringValue**](https://msdn.microsoft.com/library/aa393465)       | **REG\_MULTI\_SZ**  |
| [**SetStringValue**](https://msdn.microsoft.com/library/aa393600)                 | **REG\_SZ**         |



 

The following example shows how to read the list of sources for the system event log from the registry key.

**HKEY\_LOCAL\_MACHINE**\\**SYSTEM**\\**Current Control Set**\\**Services**\\**Eventlog**\\**System**

Note that the items in the multistring value are treated as a collection or array.


```VB
const HKEY_LOCAL_MACHINE = &amp;H80000002
strComputer = "."

Set objReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\" _ 
    & strComputer & "\root\default:StdRegProv")

strKeyPath = "SOFTWARE\Microsoft"
objReg.EnumKey HKEY_LOCAL_MACHINE, strKeyPath, arrSubKeys

For Each subkey In arrSubKeys
Wscript.Echo subkey
    
Next
```



The registry provider is hosted in LocalService—not the LocalSystem. Therefore, obtaining information remotely from the subtree **HKEY\_CURRENT\_USER** is not possible. However, scripts run on the local computer can still access **HKEY\_CURRENT\_USER**. You can set the hosting model to LocalSystem on a remote machine, but that is a security risk because the registry on the remote machine is vulnerable to hostile access. For more information, see [Provider Hosting and Security](provider-hosting-and-security.md).

## Examples

The [Read a Binary Registry Value](https://Gallery.TechNet.Microsoft.Com/b0724cb2-36ed-4d0d-8b8f-428d0e3d0b82) VBScript code example on TechNet Gallery uses WMI to read a binary registry value.

## Related topics

<dl> <dt>

[WMI Tasks: Registry](wmi-tasks--registry.md)
</dt> </dl>

 

 



