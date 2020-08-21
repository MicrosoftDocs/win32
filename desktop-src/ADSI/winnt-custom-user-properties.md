---
title: WinNT Custom User Properties
description: The WinNT provider makes available the following custom properties for the User class. They may be accessed through the IADs.Get and IADs.Put methods. For more information, see the USER\_INFO\_3 structure.
ms.assetid: 3b122424-ff24-4de7-bdaf-693fb4529b09
ms.tgt_platform: multiple
keywords:
- WinNT Custom User Properties ADSI
- WinNT provider ADSI , user object, custom properties
ms.topic: article
ms.date: 05/31/2018
---

# WinNT Custom User Properties

The WinNT provider makes available the following custom properties for the User class. They may be accessed through the [**IADs.Get**](/windows/desktop/api/Iads/nf-iads-iads-get) and [**IADs.Put**](/windows/desktop/api/Iads/nf-iads-iads-put) methods. For more information, see the [**USER\_INFO\_3**](/windows/desktop/api/lmaccess/ns-lmaccess-user_info_3) structure.



| Property            | Type         | Description                                                                                                                                                                                                                                                                                                                                                   |
|---------------------|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **HomeDirDrive**    | String       | Home Directory Drive of the user. This is a pointer to a Unicode string that specifies the path of the home directory. The string can be **null**. See example in this topic.                                                                                                                                                                                 |
| **ObjectSID**       | Octet String | Object SID of the user. For an example of how to retrieve the Object SID using the WinNT Provider, see [Object SID (WinNT Provider)](object-sid.md)                                                                                                                                                                                                          |
| **Parameters**      | String       | Parameters of the user. Points to a Unicode string that is set aside for use by applications. This string can be a null string, or it can have any number of characters before the terminating null character. Microsoft products use this member to store user configuration data. This property can only be modified by an application during installation. |
| **PasswordAge**     | Time         | Time duration of the password in use. This property indicates the number of seconds that have elapsed since the password was last changed.                                                                                                                                                                                                                    |
| **PasswordExpired** | Integer      | Tells when the password was expired. When you use Get, it will return zero is the password has not expired, or nonzero if it has expired. See example in this topic.                                                                                                                                                                                          |
| **PrimaryGroupID**  | Integer      | User's primary group ID, for example, domain user group ID. See example in this topic.                                                                                                                                                                                                                                                                        |
| **UserFlags**       | Integer      | User Flag defined in [**ADS\_USER\_FLAG\_ENUM**](/windows/win32/api/iads/ne-iads-ads_user_flag_enum). For an example of how to use UserFlags, see [Password Never Expires (WinNT Provider)](winnt-password-never-expires.md)                                                                                                                                                             |



 

This example shows how to set a user's Home Drive Directory.


```VB
Dim usr As Object

Set usr = GetObject("WinNT://Fabrikam/jsmith,user") 
usr.HomeDirectory = "UserHomeDirHere"
usr.HomeDirDrive = "HomeDirDriveHere"
usr.SetInfo
```



This example shows how to use PasswordExpired to force a user to change the password at the next logon.


```VB
Dim usr As Object

Set usr = GetObject("WinNT://Fabrikam/jsmith,user")
usr.Put "PasswordExpired", CLng(1)
usr.SetInfo 

'--- Clear this flag so that the user does not have to change the password at next logon.

usr.Put "PasswordExpired", CLng(0)
usr.SetInfo
```



This example shows how to get the user's primary group.


```VB
Dim usr As Object
Dim grpPrimaryID As Object

Set usr = GetObject("WinNT://Fabrikam/jsmith,user") 
grpPrimaryID = usr.Get("PrimaryGroupID")
```



 

 