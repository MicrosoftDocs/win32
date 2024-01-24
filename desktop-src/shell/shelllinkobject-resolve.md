---
description: Looks for the target of a Shell link, even if the target has been moved or renamed.
ms.assetid: 60e119be-8e45-4f63-a381-cad048de0765
title: ShellLinkObject.Resolve method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- ShellLinkObject.Resolve
api_type: 
- COM
api_location: 
- Shell32.dll
---

# ShellLinkObject.Resolve method

Looks for the target of a Shell link, even if the target has been moved or renamed.

## Syntax


```JScript
iRetVal = ShellLinkObject.Resolve(
  fFlags
)
```



## Parameters

<dl> <dt>

*fFlags* \[in\]
</dt> <dd>

Type: **Integer**

Flags that specify the action to be taken. This can be a combination of the following values:

<dt>



 (1)


</dt> <dd>

Do not display a dialog box if the link cannot be resolved. When this flag is set, the high-order word of *fFlags* specifies a time-out duration, in milliseconds. The method returns if the link cannot be resolved within the time-out duration. If the high-order word is set to zero, the time-out duration defaults to 3000 milliseconds (3 seconds).

</dd> <dt>



 (4)


</dt> <dd>

If the link has changed, update its path and list of identifiers.

</dd> <dt>



 (8)


</dt> <dd>

Do not update the link information.

</dd> <dt>



 (16)


</dt> <dd>

Do not execute the search heuristics.

</dd> <dt>



 (32)


</dt> <dd>

Do not use distributed link tracking.

</dd> <dt>



 (64)


</dt> <dd>

Disable distributed link tracking. By default, distributed link tracking tracks removable media across multiple devices based on the volume name. It also uses the UNC path to track remote file systems whose drive letter has changed. Setting this flag disables both types of tracking.

</dd> <dt>



 (128)


</dt> <dd>

Call the Windows Installer.

</dd> </dl> </dd> </dl>

## Remarks

This method is essentially identical in functionality to [**Resolve**](/windows/win32/api/shobjidl_core/nf-shobjidl_core-ishelllinka-resolve). For further discussion of link resolution, see the Remarks section of that page.

## Examples

The following example shows the proper usage of this method for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnShellLinkObjectResolveJ()
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
                    objShellLink.Resolve(1);
                }
            }
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnShellLinkObjectResolveVB()
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
                                objShellLink.Resolve(1)
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
Private Sub fnShellLinkObjectResolveVB()
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
                            objShellLink.Resolve (1)
                        End If
                    Set objShellLink = Nothing
                End If
            Set objFolderItem = Nothing
        End If
    Set objFolder = Nothing
    Set objShell = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional with SP3 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



 

 
