---
description: IShellDispatch.Windows method - Creates and returns a ShellWindows object. This object represents a collection of all of the open windows that belong to the Shell.
ms.assetid: 788E2106-3534-4e22-801F-677FD02BDFE0
title: IShellDispatch.Windows method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch.Windows
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch.Windows method

Creates and returns a [**ShellWindows**](shellwindows.md) object. This object represents a collection of all of the open windows that belong to the Shell.

## Syntax


```JScript
retVal = IShellDispatch.Windows()
```


```VB

IShellDispatch.Windows() As IDispatch
```





## Parameters

This method has no parameters.

## Return value

### JScript

Type: **[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)\*\***

An object reference to the [**ShellWindows**](shellwindows.md) object.

### VB

Type: **[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)\*\***

An object reference to the [**ShellWindows**](shellwindows.md) object.

## Remarks

This method is implemented and accessed through the [**Shell.Windows**](shell-windows.md) method.

## Examples

The following examples use **Windows** to retrieve the [**ShellWindows**](shellwindows.md) object and display a count of the number of items that it contains. Usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellWindowsJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var objShellWindows;
        
        objShellWindows = objshell.Windows();

        if (objShellWindows != null)
        {
            alert(objShellWindows.Count);
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellWindowsVB()
        dim objShell
        dim objShellWindows
        
        set objShell = CreateObject("shell.application")
        set objShellWindows = objshell.Windows

        if (not objShellWindows is nothing) then
            alert(objShellWindows.Count)
        end if

        set objShellWindows = nothing
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellWindowsVB()
    Dim objShell        As Shell
    Dim objShellWindows As ShellWindows
    
    Set objShell = New Shell
    Set objShellWindows = objshell.Windows

    If (Not objShellWindows Is Nothing) Then
        Debug.Print objShellWindows.Count
    End If

    Set objShellWindows = Nothing
    Set objShell = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 
