---
description: Translates a logon name to the corresponding user security ID in string format.
title: DiskQuotaControl.TranslateLogonNameToSID method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.TranslateLogonNameToSID
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: 3b6b0d03-e9ef-4575-bb67-f7b7b39d2a16
api_name: 
 - DiskQuotaControl.TranslateLogonNameToSID
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# DiskQuotaControl.TranslateLogonNameToSID method

Translates a logon name to the corresponding user security ID in string format.

## Syntax


```JScript
DiskQuotaControl.TranslateLogonNameToSID(
  logonname
)
```



## Parameters

<dl> <dt>

*logonname* 
</dt> <dd>

Type: **String**

A string value that specifies the user's logon name.

</dd> </dl>

## Return value

Returns the user security ID (SID) in string format corresponding to the provided logon name. The returned string includes the standard enclosing braces. For example:

"{S-1-5-21-2127521184-1604012920-1887927527-19009}"

## Remarks

The returned SID string can be passed to the [**FindUser**](diskquotacontrol-finduser.md) method in place of a logon name.

When a call to the [**FindUser**](diskquotacontrol-finduser.md)( *logonname*) method fails, it could be due to a mismatch between the form (for example, Security Account Manager \[SAM\] compatible and User Principal Name \[UPN\]) of the logon name provided and the form stored in the SID-name cache. In such cases, the logon name can be converted to a SID and the call to **FindUser** repeated. **FindUser** recognizes a SID string and will bypass the SID-name cache lookup. The following Microsoft Visual Basic Scripting Edition (VBScript) code illustrates this technique.


```
Function Find(dqc, name)
    On Error Resume Next
    SET Find = dqc.FindUser(name)

    If Err.Number <> 0 Then
        Err.Clear
        SET Find = dqc.FindUser(dqc.TranslateLogonNameToSID(name))
    End If    

End Function
```



Name-to-SID translation can be a slow process when compared to lookups in the SID-name cache. Therefore, it is recommended that [**FindUser**](diskquotacontrol-finduser.md) first be called with a logon name. The example above uses this technique.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DiskQuotaControl Object**](diskquotacontrol-object.md)
</dt> </dl>

 

 




