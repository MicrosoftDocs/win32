---
title: Account Lockout (WinNT Provider)
description: When the number of failed logon attempts is exceeded, the user account becomes locked out for the number of minutes specified by the lockoutDuration attribute.
ms.assetid: d7c4134a-0712-4809-83ec-cc09e87afae9
ms.tgt_platform: multiple
keywords:
- Account Lockout ADSI ,WinNT provider
- WinNT provider ADSI ,user management examples,Account Lockout
ms.topic: article
ms.date: 05/31/2018
---

# Account Lockout (WinNT Provider)

When the number of failed logon attempts is exceeded, the user account becomes locked out for the number of minutes specified by the [**lockoutDuration**](/windows/desktop/ADSchema/a-lockoutduration) attribute. The [**IADsUser.IsAccountLocked**](iadsuser-property-methods.md) property appears to be the property to use to read and modify the lockout state of a user account, but the WinNT ADSI provider has restrictions that limit the use of the **IsAccountLocked** property.

## Resetting the Account Lockout Status

When using the WinNT provider, the [**IsAccountLocked**](iadsuser-property-methods.md) property can only be set to **FALSE**, which unlocks the account. Attempting to set the **IsAccountLocked** property to **TRUE** will fail. Only the system can lock an account.

The following code example demonstrates how to use Visual Basic with ADSI to unlock a user account.


```VB
Public Sub UnlockAccount(AccountDN As String)
    Dim usr As IADsUser
    
    ' Bind to the user account.
    Set usr = GetObject("WinNT://" + AccountDN)
    
    ' Set the IsAccountLocked property to False
    usr.IsAccountLocked = False
    
    ' Flush the cached attributes to the server.
    usr.SetInfo
End Sub
```



The following code example demonstrates how to use C++ with ADSI to unlock a user account.


```C++
HRESULT UnlockAccount(LPCWSTR pwszUserDN)
{
    if(!pwszUserDN)
    {
        return E_INVALIDARG;
    }

    // Build the ADsPath.
    CComBSTR sbstr = "WinNT://";
    sbstr += pwszUserDN;
    
    HRESULT hr;
    CComPtr<IADsUser> spADsUser;

    // Bind to the object.
    hr = ADsOpenObject(sbstr,
        NULL,
        NULL,
        ADS_SECURE_AUTHENTICATION,
        IID_IADsUser,
        (void**)&spADsUser);
    if(S_OK != hr)
    {
        return hr;
    }
    
    // Set the IsAccountLocked property to FALSE;
    hr = spADsUser->put_IsAccountLocked(VARIANT_FALSE);

    // Commit the changes to the server.
    hr = spADsUser->SetInfo();

    return hr;
}
```



## Reading the Account Lockout Status

With the WinNT provider, the [**IsAccountLocked**](iadsuser-property-methods.md) property can be used to determine if an account is locked out. If an account is locked out, the **IsAccountLocked** property will contain **TRUE**. If an account is not locked out, the **IsAccountLocked** property will contain **FALSE**.

The following code example demonstrates how to use Visual Basic with ADSI to determine if an account is locked out.


```VB
Public Function IsAccountLocked(AccountDN As String) As Boolean
    Dim oUser As IADsUser
    
    ' Bind to the object.
    Set oUser = GetObject("WinNT://" + AccountDN)
    
    ' Get the IsAccountLocked property.
    IsAccountLocked = oUser.IsAccountLocked
End Function
```



The following code example demonstrates how to use C++ with ADSI to determine if an account is locked out.


```C++
HRESULT IsAccountLocked(LPCWSTR pwszUserDN, BOOL *pfLocked)
{
    if(!pwszUserDN || !pfLocked)
    {
        return E_INVALIDARG;
    }

    *pfLocked = FALSE;

    // Build the ADsPath.
    CComBSTR sbstr = "WinNT://";
    sbstr += pwszUserDN;
    
    HRESULT hr;
    CComPtr<IADsUser> spADsUser;

    // Bind to the object.
    hr = ADsOpenObject(sbstr,
        NULL,
        NULL,
        ADS_SECURE_AUTHENTICATION,
        IID_IADsUser,
        (void**)&spADsUser);
    if(S_OK != hr)
    {
        return hr;
    }
    
    VARIANT_BOOL vfLocked;
    hr = spADsUser>get_IsAccountLocked(&vfLocked);
    if(S_OK != hr)
    {
        return hr;
    }

    *pfLocked = (vfLocked != 0);

    return hr;
}
```



 

 