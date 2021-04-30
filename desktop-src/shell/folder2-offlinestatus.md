---
description: Contains the offline status of the folder.
ms.assetid: b50b130d-0675-49b5-b730-f67ea1c71d8c
title: Folder2.OfflineStatus property (Shldisp.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Folder2.OfflineStatus
api_type: 
- COM
api_location: 
- Shell32.dll
---

# Folder2.OfflineStatus property

Contains the offline status of the folder.

This property is read-only.

## Syntax


```JScript
iOfflineStatus = Folder2.OfflineStatus
```



## Property value

An **Integer** that is set to one of the following values.

<dt>



 (OFS\_DIRTYCACHE)


</dt> <dd>

Server is online with unsynchronized changes.

</dd> <dt>



 (OFS\_INACTIVE)


</dt> <dd>

Offline caching is not enabled for this folder.

</dd> <dt>



 (OFS\_OFFLINE)


</dt> <dd>

Server is offline.

</dd> <dt>



 (OFS\_ONLINE)


</dt> <dd>

Server is online.

</dd> <dt>



 (OFS\_SERVERBACK)


</dt> <dd>

Server is offline but can be reached.

</dd> </dl>

## Remarks

> [!Note]  
> Offline Files must be enabled through Folder Options for **OfflineStatus** to work correctly. If the Offline Files option is not enabled, the property returns **OFS\_INACTIVE**.

 

## Examples

The following example shows the proper use of **OfflineStatus** for JScript, VBScript, and Visual Basic.

JScript:


```JScript
<script language="JScript">
    function fnOfflineStatusJ()
    {
        var objShell   = new ActiveXObject("shell.application");
        var objFolder2 = new Object;
        
        objFolder2 = objShell.NameSpace("\\\\server\\share\\folder");
        if (objFolder2 != null)
        {
            var nReturn;

            nReturn = objFolder2.OfflineStatus;
        }
    }
</script>
```



VBScript:


```VB
<script language="VBScript">
    function fnOfflineStatusVB()
        dim objShell
        dim objFolder2
       
        set objShell = CreateObject("shell.application")
        set objFolder2 = objShell.NameSpace("\\server\share\folder")

        if (not objFolder2 is nothing) then
            dim nReturn

            nReturn = objFolder2.OfflineStatus
        end if

        set objFolder = nothing
        set objShell = nothing
    end function
</script>
```



Visual Basic:


```VB
Private Sub fnOfflineStatusVB()
    Dim objShell   As Shell
    Dim objFolder2 As Folder2
    
    Set objShell = New Shell
    Set objFolder2 = objShell.NameSpace("\\server\share\folder")

    If (Not objFolder2 Is Nothing) Then
        Dim nReturn As Integer
        
        nReturn = objFolder2.OfflineStatus()
    End If

    Set objFolder2 = Nothing
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

[**Folder2**](folder2-object.md)
</dt> <dt>

[**Folder**](folder.md)
</dt> </dl>

 

 




