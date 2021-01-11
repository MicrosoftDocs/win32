---
description: Gets or sets the working directory specified in the link.
ms.assetid: c3820deb-9f00-42a9-ab0e-c0f6389e9f29
title: ShellLinkObject.WorkingDirectory property (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellLinkObject.WorkingDirectory
api_type: 
- COM
api_location: 
- Shell32.dll
---

# ShellLinkObject.WorkingDirectory property

Gets or sets the working directory specified in the link.

This property is read/write.

## Syntax


```JScript
strWorkingDirectory = ShellLinkObject.WorkingDirectory
ShellLinkObject.WorkingDirectory(sWorkingDirectory) = strWorkingDirectory
```



## Property value

the fully qualified path of the link's working directory.

## Examples

The following example shows the proper usage of this property in JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellShellLinkObjectWorkingDirectoryJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var objFolder;
        var ssfPROGRAMS = 2;
        
        objFolder = objShell.NameSpace(ssfPROGRAMS);
        if (objFolder != null)
        {
            var objFolderItem;
            
            objFolderItem = objFolder.ParseName("Internet Explorer.lnk");
            if (objFolderItem != null)
            {
                var objShellLink;
                
                objShellLink = objFolderItem.GetLink;
                if (objShellLink != null)
                {
                    var szDirectory;
                    
                    // Get the working directory for the ShellLinkObject.
                    szDirectory = objShellLink.WorkingDirectory;
                    alert(szDirectory);
                    
                    // Set the working directory for the ShellLinkObject.
                    objShellLink.WorkingDirectory = "";
                }
            }
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellLinkObjectWorkingDirectoryVB()
        dim objShell
        dim objFolder
        dim ssfPROGRAMS
        
        ssfPROGRAMS = 2
        set objShell = CreateObject("shell.application")
        set objFolder = objShell.NameSpace(ssfPROGRAMS)
            if (not objFolder is nothing) then
                dim objFolderItem
                
                set objFolderItem = objFolder.ParseName("Internet Explorer.lnk")
                    if (not objFolderItem is nothing) then
                        dim objShellLink
                        
                        set objShellLink = objFolderItem.GetLink
                            if (not objShellLink is nothing) then
                                dim szDirectory
                                
                                'Get the working directory.
                                szDirectory = objShellLink.WorkingDirectory
                                alert(szDirectory)
                                
                                'Set the working directory.
                                objShellLink.WorkingDirectory = ""
                            end if
                        set objShellLink = nothing
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
Private Sub fnShellLinkObjectWorkingDirectoryVB()
    Dim objShell  As Shell
    Dim objFolder As Folder
    
    Set objShell = New Shell
    Set objFolder = objShell.NameSpace(ssfPROGRAMS)
        If (Not objFolder Is Nothing) Then
            Dim objFolderItem As FolderItem
            
            Set objFolderItem = objFolder.ParseName("Internet Explorer.lnk")
                If (Not objFolderItem Is Nothing) Then
                    Dim objShellLink As ShellLinkObject
                    
                    Set objShellLink = objFolderItem.GetLink
                        If (Not objShellLink Is Nothing) Then
                            Dim szDirectory As String
                            
                            'Get the working directory.
                            szDirectory = objShellLink.WorkingDirectory
                            Debug.Print szDirectory
                            
                            'Set the working directory.
                            objShellLink.WorkingDirectory = ""
                        End If
                    Set objShellLink = Nothing
                End If
            Set objFolderItem = Nothing
        End If
    Set objFolder = Nothing
    Set objShell = Nothing
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional with SP3 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 




