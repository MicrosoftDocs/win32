---
description: Gets an object that represents the parent of the item.
ms.assetid: 612e76d8-d8bc-419c-b319-75b1f324840a
title: FolderItem.Parent property (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- FolderItem.Parent
api_type: 
- COM
api_location: 
- Shell32.dll
---

# FolderItem.Parent property

Gets an object that represents the parent of the item.

This property is read-only.

## Syntax


```JScript
objParent = FolderItem.Parent
```



## Property value

A variable of type [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) that receives the parent object.

## Examples

The following example shows the proper use of **Parent** for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnFolderItemParentJ()
    {
        var objShell   = new ActiveXObject("shell.application");
        var objFolder2;
        var ssfWINDOWS = 36;

        objFolder2 = objShell.NameSpace(ssfWINDOWS);
        if (objFolder2 != null)
        {
            var objFolderItem;

            objFolderItem = objFolder2.Self;
            {
                var objParent;

                objParent = objFolderItem.Parent;
                if (objParent != null)
                {
                    alert("Got parent object");
                }
            }
        }
    }
</script>
```



VBScript:


```VB
 <script language="VBScript">
    function fnFolderItemParentVB()
        dim objShell
        dim objFolder2
        dim ssfWINDOWS

        ssfWINDOWS = 36
        set objShell = CreateObject("shell.application")
        set objFolder2 = objShell.NameSpace(ssfWINDOWS)
            if (not objFolder2 is nothing) then
                dim objFolderItem

                set objFolderItem = objFolder2.Self
                    if (not objFolderItem is nothing) then
                        dim objParent

                        set objParent = objFolderItem.Parent
                            if (not objParent is nothing) then
                                alert("Got parent object")
                            end if
                        set objParent = nothing
                    end if
                set objFolderItem = nothing
            end if
        set objFolder2 = nothing
        set objShell = nothing
    end function
 </script>
```



Visual Basic:


```VB
<script language="JScript">
    function fnFolderItemParentJ()
    {
        var objShell   = new ActiveXObject("shell.application");
        var objFolder2;
        var ssfWINDOWS = 36;

        objFolder2 = objShell.NameSpace(ssfWINDOWS);
        if (objFolder2 != null)
        {
            var objFolderItem;

            objFolderItem = objFolder2.Self;
            {
                var objParent;

                objParent = objFolderItem.Parent;
                if (objParent != null)
                {
                    alert("Got parent object");
                }
            }
        }
    }
</script>
```



## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                         |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                           |
| Header<br/>                   | <dl> <dt>Shldisp.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Shldisp.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 4.71 or later)</dt> </dl> |



 

 
