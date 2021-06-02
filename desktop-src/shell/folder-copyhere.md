---
description: Copies an item or items to a folder.
title: Folder.CopyHere method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Folder.CopyHere
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 22bf1b4c-f242-4c52-b094-c5339bb35d02

---

# Folder.CopyHere method

Copies an item or items to a folder.

## Syntax


```JScript
Folder.CopyHere(
  vItem,
  [ vOptions ]
)
```



## Parameters

<dl> <dt>

*vItem* 
</dt> <dd>

Type: **Variant**

The item or items to copy. This can be a string that represents a file name, a [**FolderItem**](folderitem.md) object, or a [**FolderItems**](folderitems.md) object.

</dd> <dt>

*vOptions* \[optional\]
</dt> <dd>

Type: **Variant**

Options for the copy operation. This value can be zero or a combination of the following values. These values are based upon flags defined for use with the **fFlags** member of the C++ [**SHFILEOPSTRUCT**](/windows/desktop/api/Shellapi/ns-shellapi-shfileopstructa) structure. Each Shell namespace must provide its own implementation of these flags, and each namespace can choose to ignore some or even all of these flags. These flags are not defined by name for Visual Basic, VBScript, or JScript, so you must define them yourself or use their numeric equivalents.

> [!Note]  
> In some cases, such as compressed (.zip) files, some option flags may be ignored by design.

 

<dt>



 (4)


</dt> <dd>

Do not display a progress dialog box.

</dd> <dt>



 (8)


</dt> <dd>

Give the file being operated on a new name in a move, copy, or rename operation if a file with the target name already exists.

</dd> <dt>



 (16)


</dt> <dd>

Respond with "Yes to All" for any dialog box that is displayed.

</dd> <dt>



 (64)


</dt> <dd>

Preserve undo information, if possible.

</dd> <dt>



 (128)


</dt> <dd>

Perform the operation on files only if a wildcard file name (\*.\*) is specified.

</dd> <dt>



 (256)


</dt> <dd>

Display a progress dialog box but do not show the file names.

</dd> <dt>



 (512)


</dt> <dd>

Do not confirm the creation of a new directory if the operation requires one to be created.

</dd> <dt>



 (1024)


</dt> <dd>

Do not display a user interface if an error occurs.

</dd> <dt>



 (2048)


</dt> <dd>

[Version 4.71.](versions.md) Do not copy the security attributes of the file.

</dd> <dt>



 (4096)


</dt> <dd>

Only operate in the local directory. Do not operate recursively into subdirectories.

</dd> <dt>



 (8192)


</dt> <dd>

[Version 5.0.](versions.md) Do not copy connected files as a group. Only copy the specified files.

</dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

No notification is given to the calling program to indicate that the copy has completed.

> [!Note]  
> Not all methods are implemented for all folders. For example, the [**ParseName**](folder-parsename.md) method is not implemented for the Control Panel folder (CSIDL\_CONTROLS). If you attempt to call an unimplemented method, a 0x800A01BD (decimal 445) error is raised.

 

## Examples

The following example uses **CopyHere** to copy the Autoexec.bat file from the root directory to the C:\\Windows directory. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnCopyHereJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var objFolder = new Object;
        
        objFolder = objShell.NameSpace("C:\\WINDOWS");
        if (objFolder != null)
        {
            objFolder.CopyHere("C:\\AUTOEXEC.BAT");
        }
    }
 </script>
```



VBScript:


```VB
<script language="VBScript">
    function fnCopyHereVB()
        dim objShell
        dim objFolder
        
        set objShell = CreateObject("shell.application")
        set objFolder = objShell.NameSpace("C:\WINDOWS")
 
        if not objFolder is nothing then
            objFolder.CopyHere("C:\AUTOEXEC.BAT")
        end if
 
        set objShell = nothing
        set objFolder = nothing
    end function
</script>
```



Visual Basic:


```VB
Private Sub btnCopyHere_Click()
    Dim objShell  As Shell
    Dim objFolder As Folder
    
    Set objShell = New Shell
    Set objFolder = objShell.NameSpace("C:\WINDOWS")
 
    If (Not objFolder Is Nothing) Then
        objFolder.CopyHere ("C:\AUTOEXEC.BAT")
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



## See also

<dl> <dt>

[**Folder**](folder.md)
</dt> </dl>

 

 




