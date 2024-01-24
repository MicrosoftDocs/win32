---
description: Shell.ShowBrowserBar method - Displays a browser bar.
ms.assetid: 203636D2-54D3-4163-B9AC-39213D6F4203
title: Shell.ShowBrowserBar method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Shell.ShowBrowserBar
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Shell.ShowBrowserBar method

Displays a browser bar.

## Syntax


```JScript
retVal = Shell.ShowBrowserBar(
  sCLSID,
  vShow
)
```


```VB

Shell.ShowBrowserBar( _
  ByVal sCLSID As BSTR, _
  ByVal vShow As Variant _
) As Variant
```





## Parameters

<dl> <dt>

*sCLSID* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** that contains the string form of the CLSID of the browser bar to be displayed. The object must be registered as an Explorer Bar object with a CATID\_InfoBand component category. For further information, see [Creating Custom Explorer Bars, Tool Bands, and Desk Bands](band-objects.md).

</dd> <dt>

*vShow* \[in\]
</dt> <dd>

Type: **Variant**

Set to **true** to show the browser bar or **false** to hide it.

</dd> </dl>

## Return value

### JScript

Type: **Variant\***

Returns **true** if successful; otherwise, **false**.

### VB

Type: **Variant\***

Returns **true** if successful; otherwise, **false**.

## Remarks

You can display one of the standard Explorer Bars by setting the *sCLSID* parameter to the CLSID of that Explorer Bar. The standard Explorer Bars and their CLSID strings are as follows:



| Explorer Bar | CLSID string                           |
|--------------|----------------------------------------|
| Favorites    | {EFA24E61-B078-11d0-89E4-00C04FC9E26E} |
| Folders      | {EFA24E64-B078-11d0-89E4-00C04FC9E26E} |
| History      | {EFA24E62-B078-11d0-89E4-00C04FC9E26E} |
| Search       | {30D02401-6A81-11d0-8274-00C04FD5AE38} |



 

This method is not currently available in Microsoft Visual Basic.

## Examples

The following examples show the use of **Shell.ShowBrowserBar** to display the **Favorites** browser bar. Usage is shown for JScript and VBScript.

JScript:


```JScript
<script language="JavaScript">
    function fnShowBrowserBarJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var bReturn;
        
        bReturn = objShell.ShowBrowserBar("{EFA24E61-B078-11d0-89E4-00C04FC9E26E}", true);
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShowBrowserBarVB()
        dim objShell
        dim bReturn

        set objShell = CreateObject("shell.application")

        bReturn = objShell.ShowBrowserBar("{EFA24E61-B078-11d0-89E4-00C04FC9E26E}", true)

        set objShell = nothing
    end function
</script>
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 
