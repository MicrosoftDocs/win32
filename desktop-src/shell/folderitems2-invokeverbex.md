---
description: Executes a verb on a collection of FolderItem objects. This method is an extension of the InvokeVerb method, allowing additional control of the operation through a set of flags.
ms.assetid: 2c02985d-8877-4a02-a232-6aeb1716928c
title: FolderItems2.InvokeVerbEx method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FolderItems2.InvokeVerbEx
api_type: 
- COM
api_location: 
- Shell32.dll
---

# FolderItems2.InvokeVerbEx method

Executes a verb on a collection of [**FolderItem**](folderitem.md) objects. This method is an extension of the [**InvokeVerb**](folderitem-invokeverb.md) method, allowing additional control of the operation through a set of flags.

## Syntax


```JScript
iRetVal = FolderItems2.InvokeVerbEx(
  [ vVerb ],
  [ vArgs ]
)
```



## Parameters

<dl> <dt>

*vVerb* \[in, optional\]
</dt> <dd>

Type: **Variant**

A **Variant** with the verb string that corresponds to the command to be executed. If no verb is specified, the default verb is executed.

</dd> <dt>

*vArgs* \[in, optional\]
</dt> <dd>

Type: **Variant**

A **Variant** that consists of a string with one or more arguments to the command specified by *vVerb*. The format of this string depends on the particular verb.

</dd> </dl>

## Remarks

A verb is a string used to specify a particular action associated with an item or collection of items. Typically, calling a verb launches a related application. For example, calling the **open** verb on a .txt file normally opens the file with a text editor, usually Microsoft Notepad. For further discussion of verbs, see [Launching Applications](launch.md).

## Examples

The following example uses **InvokeVerbEx** to invoke the default verb ("open") on **My Computer**. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnFolderItems2InvokeVerbExJ()
    {
        var objShell  = new ActiveXObject("shell.application");
        var objFolder;
        var ssfDRIVES = 17;
        
        objFolder = objShell.NameSpace(ssfDRIVES);
        if (objFolder != null)
        {
            var objFolderItems2;
            
            objFolderItems2 = objFolder.Items();
            if (objFolderItems2 != null)
            {
                objFolderItems2.InvokeVerbEx();
            }
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnFolderItems2InvokeVerbExVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        if (not objShell is nothing) then
            dim objFolder
            dim ssfDRIVES
                
            ssfWINDOWS = 17
            set objFolder = objShell.NameSpace(ssfWINDOWS)
            if (not objFolder is nothing) then
                dim objFolderItems2
                        
                set objFolderItems2 = objFolder.Items()
                if (not objFolderItems2 is nothing) then
                    objFolderItems2.InvokeVerbEx
                end if
                set objFolderItems2 = nothing
            end if
            set objFolder = nothing
        end if
        set objShell = nothing
    end function
</script>
```



Visual Basic:


```VB
Private Sub fnFolderItems2InvokeVerbExVB()
    Dim objShell      As Shell
    Dim objFolder     As Folder2
    Dim ssfDRIVES     As Long
    
    ssfDRIVES = 17
    Set objShell = New Shell
    Set objFolder = objShell.NameSpace(ssfDRIVES)
        If (Not objFolder Is Nothing) Then
            Dim objFolderItems2 As FolderItems
            
            Set objFolderItems2 = objFolder.Items
                If (Not objFolderItems2 Is Nothing) Then
                    objFolderItems2.InvokeVerbEx
                End If
            Set objFolderItems2 = Nothing
        End If
    Set objFolder = Nothing
    Set objShell = Nothing
End Sub
```



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**FolderItems2**](folderitems2-object.md)
</dt> <dt>

[**InvokeVerb**](folderitem-invokeverb.md)
</dt> </dl>

 

 




