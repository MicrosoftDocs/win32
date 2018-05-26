---
title: User Must Change Password at Next Logon (WinNT Provider)
description: To enable this option, set the PasswordExpired attribute of the user to one (1). Setting this attribute to zero (0) enables the user to log on without changing the password.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 97dd4232-dcd3-44bd-8a2a-1dcb0f85d53c
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- User Must Change Password at Next Logon (WinNT Provider) ADSI
- User Must Change Password at Next Logon ADSI , WinNT provider
- WinNT provider ADSI , user management examples, User Must Change Password at Next Logon
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# User Must Change Password at Next Logon (WinNT Provider)

To enable this option, set the **PasswordExpired** attribute of the user to one (1). Setting this attribute to zero (0) enables the user to log on without changing the password.

## Example Code

The following code example shows how to set the change password on next logon option using Visual Basic with ADSI.


```VB
Set usr = GetObject("WinNT://Fabrikam/jeffsmith,user")
usr.Put "PasswordExpired", CLng(1)   ' User must change password.
usr.SetInfo
```



## Example Code

The following code example shows how to set the change password on next logon option using C++ with ADSI.


```C++
IADsUser *pUser = NULL;
HRESULT hr;

hr=ADsGetObject(L"WinNT://Fabrikam/jeffsmith,user",
                IID_IADsUser,
                (void**)&amp;pUser);
VARIANT var;
VariantInit(&amp;var);
V_I4(&amp;var)=1;
V_VT(&amp;var)=VT_I4;
hr = pUser->Put(_bstr_t("PasswordExpired"),var); // User must change password.
hr = pUser->SetInfo();

VariantClear(&amp;var);
pUser->Release();
```



 

 




