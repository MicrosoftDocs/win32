---
description: The DVDAdm.ConfirmPassword method tests whether the specified password matches the previously saved password.
ms.assetid: 4dddc28d-edf7-45a2-ae1f-1c37b5df2eea
title: ConfirmPassword Method (Segment.h)
ms.topic: reference
ms.date: 05/31/2018
---

# ConfirmPassword Method

> [!Note]  
> This component is available for use in the Microsoft Windows 2000, Windows XP, and Windows Server 2003 operating systems. It may be altered or unavailable in subsequent versions.

 

The `DVDAdm.ConfirmPassword` method tests whether the specified password matches the previously saved password.

``` syntax
[ bIsConfirmed = ] DVD.DVDAdm.ConfirmPassword(sUserName, sPassword)
```

## Parameters

<dl> <dt>

<span id="sUserName"></span><span id="susername"></span><span id="SUSERNAME"></span>*sUserName*
</dt> <dd>

Specifies the user's name as a String.

</dd> <dt>

<span id="sPassword"></span><span id="spassword"></span><span id="SPASSWORD"></span>*sPassword*
</dt> <dd>

Specifies the new password as a String.

</dd> </dl>

## Return Value

Returns true if the specified password matches the existing password, false otherwise.

## Remarks

Currently, the *sUserName* parameter is ignored on this and all related methods.

## Requirements



| Requirement | Value |
|-------------------|--------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Segment.h</dt> </dl> |



## See also

<dl> <dt>

[**ChangePassword**](changepassword-method.md)
</dt> <dt>

[MSDVDAdm Object](msdvdadm-object.md)
</dt> </dl>

 

 




