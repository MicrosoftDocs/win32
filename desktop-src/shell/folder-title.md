---
description: Contains the title of the folder.
ms.assetid: 95c064ff-4504-4e9c-80ac-47beca443ad4
title: Folder.Title property (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Folder.Title
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Folder.Title property

Contains the title of the folder.

This property is read-only.

## Syntax


```JScript
strTitle = Folder.Title
```



## Property value

A string containing the object's title.

## Remarks

> [!Note]  
> Not all methods are implemented for all folders. For example, the [**ParseName**](folder-parsename.md) method is not implemented for the Control Panel folder (CSIDL\_CONTROLS). If you attempt to call an unimplemented method, a 0x800A01BD (decimal 445) error is raised.

 

## Examples

The following example uses **Title** to retrieve the title of the folder holding the user's program groups (usually "Programs"). Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnFolderTitleJ()
    {
        var objShell    = new ActiveXObject("shell.application");
        var objFolder;
        var ssfPROGRAMS = 2;
        
        objFolder = objShell.NameSpace(ssfPROGRAMS);
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
    function fnFolderTitleVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        if (not objShell is nothing) then
            dim objFolder
            dim ssfPROGRAMS
            
            ssfPROGRAMS = 2
            set objFolder = objShell.NameSpace(ssfPROGRAMS)
            if (not objFolder is nothing) then
                alert(objFolder.Title)
            end if
            set objFolder = nothing
        end if
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnFolderTitleVB()
    Dim objShell    As Shell
    Dim objFolder   As Folder
    Dim ssfPROGRAMS As Long
            
    ssfPROGRAMS = 2
    Set objShell = New Shell
    Set objFolder = objShell.NameSpace(ssfPROGRAMS)
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



 

 




