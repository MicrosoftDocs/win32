---
Description: 'The System Registry Provider class StdRegProv for WMI has methods that do the following:'
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: d42248b3-2f96-4771-aee9-a0db139b149e
ms.prod: windows-server-dev
ms.technology: windows-management-instrumentation
ms.tgt_platform: multiple
title: Changing Registry Data
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Changing Registry Data

The [System Registry Provider](https://msdn.microsoft.com/library/aa393886) class [**StdRegProv**](https://msdn.microsoft.com/library/aa393664) for WMI has methods that do the following:

-   Create or delete registry keys.

    Use [**CreateKey**](https://msdn.microsoft.com/library/aa389385) or [**DeleteKey**](https://msdn.microsoft.com/library/aa389869).

-   Create or delete named values, which are called entries when they are under keys.

    Use the name of a new value and [**SetBinaryValue**](https://msdn.microsoft.com/library/aa393286), [**SetDWORDValue**](https://msdn.microsoft.com/library/aa393297), [**SetExpandedStringValue**](https://msdn.microsoft.com/library/aa393299), [**SetMultiStringValue**](https://msdn.microsoft.com/library/aa393465), or [**SetStringValue**](https://msdn.microsoft.com/library/aa393600) to create a named value. Use [**DeleteValue**](https://msdn.microsoft.com/library/aa389872) to delete a named value.

-   Change named values.

    Use the name of a value and the Set methods (identified in the previous bulleted item) to change existing named values under a key. You must know the name of a value to change it. If you do not know the value names under a key, use the [**EnumValues**](https://msdn.microsoft.com/library/aa390388) method to obtain the names.

The following sections are discussed in this topic:

-   [Creating a Registry Key Using VBScript](#creating-a-registry-key-using-vbscript)
-   [Creating a Named Registry Value Using PowerShell and VBScript](#creating-a-named-registry-value-using-powershell-and-vbscript)

## Creating a Registry Key Using VBScript

Because the registry is the central configuration database for the operating system, applications, and services, use caution when you write changes to registry values or delete keys.

> [!Note]  
> You cannot monitor the **HKEY\_CLASSES\_ROOT** subkey of **HKEY\_CURRENT\_USER(HKCU)**. Monitoring **HKEY\_USERS** is not recommended because the subkeys appear and disappear as hives are loaded.

 

The following code examples show how to create a new registry key and a subkey.


```VB
HKEY_LOCAL_MACHINE = &H80000002
strComputer = "."

Set ObjRegistry = GetObject("winmgmts:{impersonationLevel = impersonate}!\\" & strComputer & "\root\default:StdRegProv")

strPath = "SOFTWARE\MyKey\MySubKey"

Return = objRegistry.CreateKey(HKEY_LOCAL_MACHINE, strPath)

If Return <> 0 Then
    WScript.Echo "The operation failed." & Err.Number
    WScript.Quit
Else
    wScript.Echo "New registry key created" & VBCRLF & "HKLM\SOFTWARE\MYKey\"

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
$strComputer = &quot;.&quot;
$strPath = &quot;SOFTWARE\MyKey\MySubKey&quot;

$reg = [wmiclass]&quot;\\$strComputer\root\default:StdRegprov&quot;

[void]$reg.CreateKey($HKEY_LOCAL_MACHINE, $strPath)</code></pre></td>
</tr>
</tbody>
</table>



## Creating a Named Registry Value Using PowerShell and VBScript

The following code example shows how to create a named value called **MultiStringValue** under the **HKEY\_LOCAL\_MACHINE**\\**SOFTWARE**\\**MyKey**\\**MySubKey** key that the previous script creates. The script calls [**StdRegProv.SetMultiStringValue**](https://msdn.microsoft.com/library/aa393465) to write string values to a new named value.


```VB
const HKEY_LOCAL_MACHINE = &H80000002 
strComputer = "."

Set objRegistry = _
    GetObject("winmgmts:{impersonationLevel=impersonate}!\\" _ 
    & strComputer & "\root\default:StdRegProv")

strKeyPath = "SOFTWARE\MyKey\MySubKey"
strValueName = "MultiStringValue"
arrStringValues = Array("one", "two","three", "four")

objRegistry.SetMultiStringValue HKEY_LOCAL_MACHINE, strKeyPath,_
    strValueName, arrStringValues

' Read the values that were just written
objRegistry.GetMultiStringValue HKEY_LOCAL_MACHINE, strKeyPath,_
    strValueName, arrStringValues   

For Each strValue in arrStringValues
    WScript.Echo strValue 
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
$strComputer = &quot;.&quot;
$strPath = &quot;SOFTWARE\MyKey\MySubKey&quot;

$strValueName = &quot;MultiStringValue&quot;
$arrStringValues = @(&quot;one&quot;, &quot;two&quot;,&quot;three&quot;, &quot;four&quot;)

$reg = [wmiclass]&quot;\\$strComputer\root\default:StdRegprov&quot;

[void]$reg.SetMultiStringValue($HKEY_LOCAL_MACHINE, $strKeyPath, $strValueName, $arrStringValues)

$multiValues = $reg.GetMultiStringValue($HKEY_LOCAL_MACHINE, $strKeyPath, $strValueName)
$multiValues.sValue</code></pre></td>
</tr>
</tbody>
</table>



Using WMI, you cannot set access security on a registry key. However, the [**StdRegProv.CheckAccess**](https://msdn.microsoft.com/library/aa384911) method compares the security settings of the current user to the security descriptor on a registry key to determine if the user has a specific permission, such as **KEY\_SET\_VALUE**.

 

 



