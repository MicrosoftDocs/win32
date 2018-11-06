---
Description: Retrieves an object that represents the parent of the current object.
ms.assetid: 2FDEF8D3-3F5B-43ae-9812-83B4249D9CBB
title: IShellDispatch.Parent property
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch.Parent
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch.Parent property

Retrieves an object that represents the parent of the current object.

This property is read-only.

## Syntax


```JScript
objParent = IShellDispatch.Parent
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
<td><pre><code>Property Parent As Object</code></pre></td>
</tr>
</tbody>
</table>



## Property value

A variable of type [**IDispatch**](https://msdn.microsoft.com/en-us/library/ms221608(v=VS.71).aspx) that receives the parent object.

## Remarks

This property is implemented and accessed through the [**Shell.Parent**](shell-parent.md) property.

## Examples

The following examples show the use of **Parent** in JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellParentJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var objParent;

        objParent = objshell.Shell_Parent;
        if (objParent != null)
        {
            alert("Got parent property");
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellParentVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
            if (not objShell is nothing) then
                dim objParent

                set objParent = objshell.Parent
                    if (not objParent is nothing) then
                        alert("Got parent property")
                    end if
                set objParent = nothing
            end if
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellParentVB()
    Dim objShell As Shell
    
    Set objShell = New Shell
        If (Not objShell Is Nothing) Then
            Dim objParent As Object
            
            Set objParent = objshell.Parent
                If (Not objParent Is Nothing) Then
                    Debug.Print "Got parent object"
                End If
            Set objParent = Nothing
        End If
    Set objShell = Nothing
End Sub
```



## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 




