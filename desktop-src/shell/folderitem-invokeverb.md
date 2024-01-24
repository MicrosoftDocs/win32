---
description: Executes a verb on the item.
ms.assetid: 569bdc88-15ef-4d08-923c-4f41e5ae5a38
title: FolderItem.InvokeVerb method (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FolderItem.InvokeVerb
api_type: 
- COM
api_location: 
- Shell32.dll
---

# FolderItem.InvokeVerb method

Executes a verb on the item.

## Syntax


```JScript
FolderItem.InvokeVerb(
  [ vVerb ]
)
```



## Parameters

<dl> <dt>

*vVerb* \[in, optional\]
</dt> <dd>

Type: **Variant**

A string that specifies the verb to be executed. It must be one of the values returned by the item's [**FolderItemVerb.Name**](folderitemverb-name.md) property. If no verb is specified, the default verb will be invoked.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

A verb is a string used to specify a particular action that an item supports. Invoking a verb is equivalent to selecting a command from an item's shortcut menu. Typically, invoking a verb launches a related application. For example, invoking the "open" verb on a .txt file opens the file with a text editor, usually Microsoft Notepad. See [Launching Applications](launch.md) for further discussion of verbs.

The [**FolderItemVerbs**](folderitemverbs.md) object represents the collection of verbs associated with the item. The default verb may vary for different items, but it is typically "open".

## Examples

The following example uses **InvokeVerb** to invoke the default verb ("open" in this case) on the Windows folder. Proper usage is shown for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnFolderItemInvokeVerbJ()
    {
        var objShell = new ActiveXObject("shell.application");
        var objFolder2;
        var ssfWINDOWS = 36;
        
        objFolder2 = objShell.NameSpace(ssfWINDOWS);
        if (objFolder2 != null)
        {
            var objFolderItem;
            
            objFolderItem = objFolder2.Self;
            if (objFolderItem != null)
            {
                var szReturn;
                
                objFolderItem.InvokeVerb();
            }
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnFolderItemInvokeVerbVB()
        dim objShell
        
        set objShell = CreateObject("shell.application")
        if (not objShell is nothing) then
            dim objFolder2
            dim ssfWINDOWS
                
            ssfWINDOWS = 36
            set objFolder2 = objShell.NameSpace(ssfWINDOWS)
            if (not objFolder2 is nothing) then
                dim objFolderItem
                        
                set objFolderItem = objFolder2.Self
                if (not objFolderItem is nothing) then
                    dim szReturn
                                
                    objFolderItem.InvokeVerb()
                end if
                set objFolderItem = nothing
            end if
            set objFolder2 = nothing
        end if
        set objShell = nothing
    end function
</script>
```



Visual Basic:


```VB
Private Sub fnFolderItemInvokeVerbVB()
    Dim objShell   As Shell
    Dim objFolder2 As Folder2
    Dim ssfWINDOWS As Long
    
    ssfWINDOWS = 36
    Set objShell = New Shell
    Set objFolder2 = objShell.NameSpace(ssfWINDOWS)
        If (Not objFolder2 Is Nothing) Then
            Dim objFolderItem As FolderItem
            
            Set objFolderItem = objFolder2.Self
                If (Not objFolderItem Is Nothing) Then
                    Dim szReturn As String
                    
                    objFolderItem.InvokeVerb
                Else
                    'FolderItem object returned nothing.
                End If
            Set objFolderItem = Nothing
        Else
            'Folder object returned nothing.
        End If
    Set objFolder2 = Nothing
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

[**FolderItem**](folderitem.md)
</dt> <dt>

[**Verbs**](folderitem-verbs.md)
</dt> <dt>

[**DoIt**](folderitemverb-doit.md)
</dt> </dl>

 

 




