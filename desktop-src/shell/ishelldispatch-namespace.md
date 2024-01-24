---
description: IShellDispatch.NameSpace method - Creates and returns a Folder object for the specified folder.
ms.assetid: CEA73705-1C27-4138-86C4-1715016E2ED8
title: IShellDispatch.NameSpace method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch.NameSpace
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch.NameSpace method

Creates and returns a [**Folder**](folder.md) object for the specified folder.

## Syntax


```JScript
retVal = IShellDispatch.NameSpace(
  vDir
)
```


```VB

IShellDispatch.NameSpace( _
  ByVal vDir As Variant _
) As Folder
```





## Parameters

<dl> <dt>

*vDir* \[in\]
</dt> <dd>

Type: **Variant**

The folder for which to create the [**Folder**](folder.md) object. This can be a string that specifies the path of the folder or one of the [**ShellSpecialFolderConstants**](/windows/desktop/api/Shldisp/ne-shldisp-shellspecialfolderconstants) values. Note that the constant names found in **ShellSpecialFolderConstants** are available in Visual Basic, but not in VBScript or JScript. In those cases, the numeric values must be used in their place.

</dd> </dl>

## Return value

### JScript

Type: **[**Folder**](folder.md)\*\***

Object reference to the [**Folder**](folder.md) object for the specified folder. If the folder is not successfully created, this value returns **null**.

### VB

Type: **[**Folder**](folder.md)\*\***

Object reference to the [**Folder**](folder.md) object for the specified folder. If the folder is not successfully created, this value returns **null**.

## Remarks

This method is implemented and accessed through the [**Shell.NameSpace**](shell-namespace.md) method.

## Examples

The following examples show the use of [**NameSpace**](shell-namespace.md) in JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellNameSpaceJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var objFolder;
        var ssfWINDOWS = 36
        
        objFolder = objShell.NameSpace(ssfWINDOWS);
        if (objFolder != null)
        {
            alert(objFolder.Title);
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellNameSpaceVB()
        dim objShell
        dim objFolder
        
        set objShell = CreateObject("shell.application")
        set objFolder = objShell.NameSpace("C:\")

        if (not objFolder is nothing) then
            alert(objFolder.Title)
        end if

        set objFolder = nothing
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellNameSpaceVB()
    Dim objShell  As Shell
    Dim objFolder As Folder

    Set objShell = New Shell
    Set objFolder = objShell.NameSpace(ssfPERSONAL)

    If (Not objFolder Is Nothing) Then
        Debug.Print objFolder.Title
    End If

    Set objFolder = Nothing
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



 

 




