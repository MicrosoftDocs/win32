---
description: IShellDispatch2.FindPrinter method - Displays the Find Printer dialog box.
ms.assetid: a3d1e810-f0cf-48ec-93da-5cc01117c5d4
title: IShellDispatch2.FindPrinter method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch2.FindPrinter
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch2.FindPrinter method

Displays the **Find Printer** dialog box.

## Syntax


```JScript
iRetVal = IShellDispatch2.FindPrinter(
  [ sName ],
  [ sLocation ],
  [ sModel ]
)
```


```VB

IShellDispatch2.FindPrinter( _
  [ ByVal sName As BSTR ], _
  [ ByVal sLocation As BSTR ], _
  [ ByVal sModel As BSTR ] _
) As Integer
```





## Parameters

<dl> <dt>

*sName* \[in, optional\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** that contains the printer name.

</dd> <dt>

*sLocation* \[in, optional\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** that contains the printer location.

</dd> <dt>

*sModel* \[in, optional\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** that contains the printer model.

</dd> </dl>

## Remarks

This method is implemented and accessed through the [**Shell.FindPrinter**](./shell-findprinter.md) method.

If you assign strings to one or more of the optional parameters, they are displayed as default values in the associated edit control when the **Find Printer** dialog box is displayed. The user can either accept or override these values. If no value is assigned to a parameter, the associated edit box is empty and the user must enter a value.

This method is not currently available in Microsoft Visual Basic.

## Examples

The following examples show the use of **FindPrinter** to display the **Find Printer** dialog box for a particular application. Usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnFindPrinterJ()
    {
        var objShell = new ActiveXObject("shell.application");
        
        objShell.FindPrinter();
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnFindPrinterVB()
        dim objShell
        dim bReturn

        set objShell = CreateObject("shell.application")
        objShell.FindPrinter()

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



 

 
