---
description: Shell.ExplorerPolicy method - Gets the value for a specified Windows Internet Explorer policy.
ms.assetid: 47E17F6A-ED43-44cd-AF77-A6E49865E1B5
title: Shell.ExplorerPolicy method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.ExplorerPolicy
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.ExplorerPolicy method

Gets the value for a specified Windows Internet Explorer policy.

## Syntax


```JScript
retVal = Shell.ExplorerPolicy(
  bstrPolicyName
)
```


```VB

Shell.ExplorerPolicy( _
  ByVal bstrPolicyName As BSTR _
) As Variant
```





## Parameters

<dl> <dt>

*bstrPolicyName* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

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
        
        vReturn = objShell.ExplorerPolicy("ValueName");
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
            vReturn = objShell.ExplorerPolicy("ValueName")
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
        vReturn = objShell.ExplorerPolicy("ValueName")
        Debug.Print vReturn
    Set objShell = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 6.0 or later)</dt> </dl> |



 

 
