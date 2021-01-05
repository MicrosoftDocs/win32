---
description: The DVDAdm.ChangePassword method saves a new application password in the registry.
ms.assetid: 58dac785-e20e-4a41-89cf-56644964da19
title: ChangePassword Method
ms.topic: reference
ms.date: 05/31/2018
---

# ChangePassword Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.ChangePassword` method saves a new application password in the registry.

``` syntax
        DVD.DVDAdm.ChangePassword(sUserName, sOld, sNew)
```

## Parameters

<dl> <dt>

<span id="sUserName"></span><span id="susername"></span><span id="SUSERNAME"></span>*sUserName*
</dt> <dd>

Specifies the current user's logon name as a String. The MSDVDAdm object ignores this parameter. See Remarks.

</dd> <dt>

<span id="sOld"></span><span id="sold"></span><span id="SOLD"></span>*sOld*
</dt> <dd>

Specifies the user's old password as a String.

</dd> <dt>

<span id="sNew"></span><span id="snew"></span><span id="SNEW"></span>*sNew*
</dt> <dd>

Specifies the user's new password as a String. Cannot be an empty string.

</dd> </dl>

## Return Value

No return value.

## Remarks

Currently, the *sUserName* parameter is ignored on this and all related methods. This means that whoever knows the password can set the parental level. There is only one password and one parental level for the application. There is no support for individual user logon names or multiple password management. To enforce parental management levels, parents should set the password and then set the parental level appropriate for younger members of the group of relatives. When parents want to view a disc with adult-rated content, they can change the level, and then change it back when they are done viewing. As long as the children do not know the password, they can only watch content at or below the level set for them.

## See also

<dl> <dt>

[**ConfirmPassword**](confirmpassword-method.md)
</dt> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 



