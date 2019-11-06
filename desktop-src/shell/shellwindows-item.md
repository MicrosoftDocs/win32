---
Description: Retrieves an InternetExplorer object that represents the Shell window.
ms.assetid: '32390f35-f83a-45d9-a240-282da7cb2b13'
title: ShellWindows.Item method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellWindows.Item
api_type: 
- COM
api_location: 
- Shell32.dll
---

# ShellWindows.Item method

Retrieves an [**InternetExplorer**](https://msdn.microsoft.com/library/Aa752084(v=VS.85).aspx) object that represents the Shell window.

## Syntax


```JScript
retVal = ShellWindows.Item(
  [ iIndex ]
)
```



## Parameters

<dl> <dt>

*iIndex* \[in, optional\]
</dt> <dd>

Type: **Variant**

The zero-based index of the item to retrieve. This value must be less than the value of the [**Count**](shellwindows-count.md) property. If this value is omitted, a default value of 0 is used.

</dd> </dl>

## Return value

Type: **[**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx)\*\***

An object reference to the [**InternetExplorer**](https://msdn.microsoft.com/library/Aa752084(v=VS.85).aspx) object that represents the Shell window.

## Examples

The following example uses [**Item**](folderitemverbs-item.md) to retrieve the [**InternetExplorer**](https://msdn.microsoft.com/library/Aa752084(v=VS.85).aspx) object that represents the first Shell window item. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JavaScript
<script language="JScript">
    function fnShellWindowsItemJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var objShellWindows;
        
        objShellWindows = objshell.Shell_Windows();
        if (objShellWindows != null)
        {
            var objIE;
            objIE = objShellWindows.Item();

            if (objIE != null)
            {
                alert(objIE.path());
            }
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellWindowsItemVB()
        dim objShell
        dim objShellWindows
        
        set objShell = CreateObject("shell.application")
        set objShellWindows = objshell.Shell_Windows

        if (not objShellWindows is nothing) then
            dim objIE
            set objIE = objShellWindows.Item

            if (not objIE is nothing) then
                alert(objIE.path)
            end if

            set objIE = nothing
        end if

        set objShellWindows = nothing
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellWindowsItemVB()
    Dim objShell        As Shell
    Dim objShellWindows As ShellWindows
    
    Set objShell = New Shell
    Set objShellWindows = objshell.Shell_Windows

    If (Not objShellWindows Is Nothing) Then
        Dim objIE As InternetExplorer
        Set objIE = objShellWindows.Item

        If (Not objIE Is Nothing) Then
            Debug.Print objIE.Path
        End If

        Set objIE = Nothing
    End If

    Set objShellWindows = Nothing
    Set objShell = Nothing
End Sub
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Exdisp.h</dt> </dl>                            |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




