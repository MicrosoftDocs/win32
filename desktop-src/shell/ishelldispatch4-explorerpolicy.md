---
Description: Gets the value for a specified Windows Internet Explorer policy.
ms.assetid: 490c3e18-b606-456a-9016-dc4f7bad2bc3
title: IShellDispatch4.ExplorerPolicy method
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IShellDispatch4.ExplorerPolicy method

Gets the value for a specified Windows Internet Explorer policy.

## Syntax


```JScript
retVal = IShellDispatch4.ExplorerPolicy(
  bstrPolicyName
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
<td><pre><code>IShellDispatch4.ExplorerPolicy( _
  ByVal bstrPolicyName As BSTR _
) As Variant</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>

*bstrPolicyName* \[in\]
</dt> <dd>

Type: **[**BSTR**](1b2d7d2c-47af-4389-a6b6-b01b7e915228)**

A **String** that specifies the name of the policy.

</dd> </dl>

## Return value

### JScript

Type: **Variant\***

The value associated with the specified policy name.

### VB

Type: **Variant\***

The value associated with the specified policy name.

## Remarks

Network Administrators can control and manage the computing environment of their users by setting policies.

The specified value name must be within the **HKEY\_CURRENT\_USER**\\**Software**\\**Microsoft**\\**Windows**\\**CurrentVersion**\\**Policies**\\**Explorer** subkey. If the value name does not exist then the method returns **null**.

## Examples

The following examples show the proper use of **ExplorerPolicy** for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnIShellDispatch4ExplorerPolicyJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var vReturn;
        
        vReturn = objshell.ExplorerPolicy("ValueName");
        alert(vReturn);
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
     function fnIShellDispatch4ExplorerPolicyVB()
        dim objShell
        dim vReturn
        
        set objShell = CreateObject("shell.application")
            vReturn = objshell.ExplorerPolicy("ValueName")
            alert(vReturn)
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnIShellDispatch4ExplorerPolicyVB()
    Dim objShell As Shell
    Dim vReturn  As Variant
    
    Set objShell = New Shell
        vReturn = objshell.ExplorerPolicy("ValueName")
        Debug.Print vReturn
    Set objShell = Nothing
End Sub
```



## Requirements



|                                     |                                                                                                               |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 6.0 or later)</dt> </dl> |



 

 




