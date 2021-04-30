---
description: Finds a user's entry, by name, in the volume's quota file.
title: DiskQuotaControl.FindUser method
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- DiskQuotaControl.FindUser
api_type: 
- COM
api_location: 
- Shell32.dll
ms.assetid: e5767d28-4c0a-49bc-a1d3-ba809411456d
api_name: 
 - DiskQuotaControl.FindUser
api_type: 
 - COM
api_location: 
 - Shell32.dll
topic_type: 
 - APIRef
 - kbSyntax

---

# DiskQuotaControl.FindUser method

Finds a user's entry, by name, in the volume's quota file.

## Syntax


```JScript
DiskQuotaControl.FindUser(
  sLogonName
)
```



## Parameters

<dl> <dt>

*sLogonName* 
</dt> <dd>

Type: **String**

A string value that contains the user's logon name.

</dd> </dl>

## Return value

Returns an object expression that evaluates to the user's [**DIDiskQuotaUser**](didiskquotauser-object.md) object.

## Remarks

This method returns a [**DIDiskQuotaUser**](didiskquotauser-object.md) object even if there is no entry for the user in the quota file. The returned user object has warning threshold and hard quota limits set to the volume's default values.

The string returned from [**TranslateLogonNameToSID**](diskquotacontrol-translatelogonnametosid.md) may be passed in place of the *sLogonName* parameter. When **FindUser** receives a SID string it uses the corresponding SID for direct lookup of the user's quota record on the volume. This bypasses the SID-name cache. In cases where **FindUser** fails due to a mismatch in format (for example, SAM-compatible and UPN) of the logon name provided and the logon name cached, the logon name can be translated to a SID string using **TranslateLogonNameToSID** then passed again to **FindUser**. The following VBScript code illustrates this technique.


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



## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                    |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                          |
| DLL<br/>                      | <dl> <dt>Shell32.dll (version 5.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**DiskQuotaControl Object**](diskquotacontrol-object.md)
</dt> </dl>

 

 




