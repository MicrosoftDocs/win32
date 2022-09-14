---
description: IShellDispatch.BrowseForFolder method - Creates a dialog box that enables the user to select a folder and then returns the selected folder's Folder object.
ms.assetid: 578C51C1-F59B-4604-A09B-62BA61225ABB
title: IShellDispatch.BrowseForFolder method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- IShellDispatch.BrowseForFolder
api_type: 
- COM
api_location: 
- Shell32.dll
---

# IShellDispatch.BrowseForFolder method

Creates a dialog box that enables the user to select a folder and then returns the selected folder's [**Folder**](folder.md) object.

## Syntax


```JScript
retVal = IShellDispatch.BrowseForFolder(
  Hwnd,
  sTitle,
  iOptions,
  [ vRootFolder ]
)
```


```VB

IShellDispatch.BrowseForFolder( _
  ByVal Hwnd As Integer, _
  ByVal sTitle As BSTR, _
  ByVal iOptions As Integer, _
  [ ByVal vRootFolder As Variant ] _
) As FOLDER
```





## Parameters

<dl> <dt>

*Hwnd* \[in\]
</dt> <dd>

Type: **Integer**

The handle to the parent window of the dialog box. This value can be zero.

</dd> <dt>

*sTitle* \[in\]
</dt> <dd>

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)**

A **String** value that represents the title displayed inside the **Browse** dialog box.

</dd> <dt>

*iOptions* \[in\]
</dt> <dd>

Type: **Integer**

An **Integer** value that contains the options for the method. This can be zero or a combination of the values listed under the **ulFlags** member of the [**BROWSEINFO**](/windows/desktop/api/shlobj_core/ns-shlobj_core-browseinfoa) structure.

</dd> <dt>

*vRootFolder* \[in, optional\]
</dt> <dd>

Type: **Variant**

The root folder to use in the dialog box. The user cannot browse higher in the tree than this folder. If this value is not specified, the root folder used in the dialog box is the desktop. This value can be a string that specifies the path of the folder or one of the [**ShellSpecialFolderConstants**](/windows/desktop/api/Shldisp/ne-shldisp-shellspecialfolderconstants) values. Note that the constant names found in **ShellSpecialFolderConstants** are available in Visual Basic, but not in VBScript or JScript. In those cases, the numeric values must be used in their place.

</dd> </dl>

## Return value

### JScript

Type: **FOLDER\*\***

An object reference to the selected folder's [**Folder**](folder.md) object.

### VB

Type: **FOLDER\*\***

An object reference to the selected folder's [**Folder**](folder.md) object.

## Remarks

This method is implemented and accessed through the [**Shell.BrowseForFolder**](shell-browseforfolder.md) method.

## Examples

The following examples use **BrowseForFolder** to display a browse window titled "Example" rooted at the Windows folder. Usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellBrowseForFolderJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var ssfWINDOWS = 36;
        var objFolder;
        
        objFolder = objshell.BrowseForFolder(0, "Example", 0, ssfWINDOWS);
        if (objFolder != null)
        {
            // Add code here.
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellBrowseForFolderVB()
        dim objShell
        dim ssfWINDOWS
        dim objFolder
        
        ssfWINDOWS = 36
        set objShell = CreateObject("shell.application")
            set objFolder = objshell.BrowseForFolder(0, "Example", 0, ssfWINDOWS)
                if (not objFolder is nothing) then
                    'Add code here.
                end if
            set objFolder = nothing
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
Private Sub fnShellBrowseForFolderVB()
    Dim objShell   As Shell
    Dim ssfWINDOWS As Long
    Dim objFolder  As Folder
    
    ssfWINDOWS = 36
    Set objShell = New Shell
        Set objFolder = objshell.BrowseForFolder(0, "Example", 0, ssfWINDOWS)
            If (Not objFolder Is Nothing) Then
                'Add code here
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



 

 
