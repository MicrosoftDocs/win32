---
Description: Retrieves system information.
ms.assetid: 94C10DD6-FE49-4dd4-AEED-69B73A75EDEF
title: Shell.GetSystemInformation method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Shell.GetSystemInformation method

Retrieves system information.

## Syntax


```JScript
retVal = Shell.GetSystemInformation(
  sName
)
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>Shell.GetSystemInformation( _
  ByVal sName As BSTR _
) As Variant</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*sName* \[in\]
</dt> <dd>

Type: **[**BSTR**](https://msdn.microsoft.com/windows/desktop/1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

A **String** that specifies the system information that is being requested.

</dd> </dl>

## Return value

### JScript

Type: **Variant**

Returns the value of the requested system information. The return type depends on which system information is requested. See the Remarks section for details.

### VB

Type: **Variant**

Returns the value of the requested system information. The return type depends on which system information is requested. See the Remarks section for details.

## Remarks

This method can be used to request many system information values. The following table gives the *sName* value that is used to request the information and the associated type of the returned value.



*sName*

Return type

Description

DirectoryServiceAvailable

**Boolean**

Set to **true** if the directory service is available; otherwise, **false**.

DoubleClickTime

**Integer**

The double-click time, in milliseconds.

ProcessorLevel

**Integer**

**Windows Vista and later**. The processor level. Returns 3, 4, or 5, for x386, x486, and Pentium-level processors, respectively.

ProcessorSpeed

**Integer**

The processor speed, in megahertz (MHz).

ProcessorArchitecture

**Integer**

The processor architecture. For details, see the discussion of the **wProcessorArchitecture** member of the [**SYSTEM\_INFO**](https://msdn.microsoft.com/windows/desktop/971293b8-0af0-4bdf-a7d7-6b1bb80a469c) structure.

PhysicalMemoryInstalled

**Integer**

The amount of physical memory installed, in bytes.

The following are valid only on Windows XP.

IsOS\_Professional

**Boolean**

Set to **true** if the operating system is Windows XP Professional Edition; otherwise, **false**.

IsOS\_Personal

**Boolean**

Set to **true** if the operating system is Windows XP Home Edition; otherwise, **false**.

The following is valid only on Windows XP and later.

IsOS\_DomainMember

**Boolean**

Set to **true** if the computer is a member of a domain; otherwise, **false**.



 

This method is not currently available in Microsoft Visual Basic.

## Examples

The following examples show the use of **GetSystemInformation** for JScript and VBScript.

JScript:


```JScript
<script language="JavaScript">
    function fnGetSystemInformationJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var vReturn;

        vReturn = objShell.GetSystemInformation("ProcessorLevel");
        document.write(vReturn);
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnGetSystemInformationVB()
        dim objShell
        dim vReturn

        set objShell = CreateObject("shell.application")

        vReturn = objShell.GetSystemInformation("ProcessorLevel")
        document.write(vReturn)

        set objShell = nothing
    end function
</script>
```



## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 




