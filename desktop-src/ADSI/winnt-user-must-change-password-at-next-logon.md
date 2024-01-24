---
title: User Must Change Password at Next Logon (WinNT Provider)
description: To enable this option, set the PasswordExpired attribute of the user to one (1). Setting this attribute to zero (0) enables the user to log on without changing the password.
ms.assetid: 97dd4232-dcd3-44bd-8a2a-1dcb0f85d53c
ms.tgt_platform: multiple
keywords:
- User Must Change Password at Next Logon (WinNT Provider) ADSI
- User Must Change Password at Next Logon ADSI , WinNT provider
- WinNT provider ADSI , user management examples, User Must Change Password at Next Logon
ms.topic: article
ms.date: 05/31/2018
---

# User Must Change Password at Next Logon (WinNT Provider)

To enable this option, set the **PasswordExpired** attribute of the user to one (1). Setting this attribute to zero (0) enables the user to log on without changing the password.

## Example 1

The following code example shows how to set the change password on next logon option using Visual Basic with ADSI.


```VB
Set usr = GetObject("WinNT://Fabrikam/jeffsmith,user")
usr.Put "PasswordExpired", CLng(1)   ' User must change password.
usr.SetInfo
```



## Example 2

The following code example shows how to set the change password on next logon option using C++ with ADSI.


```C++
IADsUser *pUser = NULL;
HRESULT hr;

hr=ADsGetObject(L"WinNT://Fabrikam/jeffsmith,user",
                IID_IADsUser,
                (void**)&pUser);
VARIANT var;
VariantInit(&var);
V_I4(&var)=1;
V_VT(&var)=VT_I4;
hr = pUser->Put(_bstr_t("PasswordExpired"),var); // User must change password.
hr = pUser->SetInfo();

VariantClear(&var);
pUser->Release();
```



 

 




