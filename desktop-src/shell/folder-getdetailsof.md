---
description: Retrieves details about an item in a folder. For example, its size, type, or the time of its last modification.
ms.assetid: d2fe4550-f171-40d9-8bce-065b61826997
title: Folder.GetDetailsOf method (Shlobj\_core.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Folder.GetDetailsOf
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Folder.GetDetailsOf method

Retrieves details about an item in a folder. For example, its size, type, or the time of its last modification.

## Syntax


```JScript
retVal = Folder.GetDetailsOf(
  vItem,
  iColumn
)
```



## Parameters

<dl> <dt>

*vItem* 
</dt> <dd>

Type: **Variant**

The item for which to retrieve the information. This must be a [**FolderItem**](folderitem.md) object.

</dd> <dt>

*iColumn* 
</dt> <dd>

Type: **Integer**

An **Integer** value that specifies the information to be retrieved. The information available for an item depends on the folder in which it is displayed. This value corresponds to the zero-based column number that is displayed in a Shell view. For an item in the file system, this can be one of the following values:

<dt>



 (0)


</dt> <dd>

Retrieves the name of the item.

</dd> <dt>



 (1)


</dt> <dd>

Retrieves the size of the item.

</dd> <dt>



 (2)


</dt> <dd>

Retrieves the type of the item.

</dd> <dt>



 (3)


</dt> <dd>

Retrieves the date and time that the item was last modified.

</dd> <dt>



 (4)


</dt> <dd>

Retrieves the attributes of the item.

</dd> <dt>



 (-1)


</dt> <dd>

Retrieves the info tip information for the item.

</dd> </dl> </dd> </dl>

## Return value

Type: **[**BSTR**](/previous-versions/windows/desktop/automat/bstr)\***

String containing the retrieved detail.

## Remarks

> [!Note]  
> Not all methods are implemented for all folders. For example, the [**ParseName**](folder-parsename.md) method is not implemented for the Control Panel folder (CSIDL\_CONTROLS). If you attempt to call an unimplemented method, a 0x800A01BD (decimal 445) error is raised.

 

## Examples

The following example uses **GetDetailsOf** to retrieve the type of the file named Clock.avi. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnGetDetailsOfJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var objFolder = new Object;
        
        objFolder = objShell.NameSpace("C:\\WINDOWS");
        if (objFolder != null)
        {
            var objFolderItem = new Object;

            objFolderItem = objFolder.ParseName("clock.avi");
            if (objFolderItem != null)
            {
                var objInfo = new Object;

                objInfo = objFolder.GetDetailsOf(objFolderItem, 2);
            }
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnGetDetailsOfVB()
        dim objShell
        dim objFolder
        
        set objShell = CreateObject("shell.application")
        set objFolder = objShell.NameSpace("C:\WINDOWS")

        if (not objFolder is nothing) then
            dim objFolderItem

            set objFolderItem = objFolder.ParseName("clock.avi")

            if (not objFolderItem Is Nothing) then
                dim objInfo
                        
                objInfo = objFolder.GetDetailsOf(objFolderItem, 2)
            end if
            
            set objFolderItem = nothing
        end if
        
        set objFolder = nothing
        set objShell = nothing
    end function
</script>
```



Visual Basic:


```VB
Private Sub btnGetDetailsOf_Click()
    Dim objShell  As Shell
    Dim objFolder As Folder

    Set objShell = New Shell
    Set objFolder = objShell.NameSpace("C:\WINDOWS")
    
    If (Not objFolder Is Nothing) Then
        Dim objFolderItem As FolderItem
        Set objFolderItem = objFolder.ParseName("clock.avi")
   
        If (Not objFolderItem Is Nothing) Then
            Dim szItem As String
            szItem = objFolder.GetDetailsOf(objFolderItem, 2)
        End If
        
        Set objFolderItem = Nothing
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
| Header<br/>                   | <dl> <dt>Shlobj\_core.h (include Shldisp.h)</dt> </dl>  |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 
