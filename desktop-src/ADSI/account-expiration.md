---
title: Account Expiration (LDAP Provider)
description: To set the account expiration date, set the IADsUser.AccountExpirationDate property to the desired date value.
ms.assetid: d0b90bb3-ad7c-4394-956d-061a915f210d
ms.tgt_platform: multiple
keywords:
- Account Expiration ADSI ,LDAP provider
- LDAP provider ADSI ,user management examples,Account Expiration
ms.topic: article
ms.date: 05/31/2018
---

# Account Expiration (LDAP Provider)

To set the account expiration date, set the [**IADsUser.AccountExpirationDate**](iadsuser-property-methods.md) property to the desired date value. To disable the account expiration date, set the [**accountExpires**](/windows/desktop/ADSchema/a-accountexpires) attribute to zero. The following code examples show how to set the expiration date.


```VB
Public Sub SetUserAccountExpirationDate(User As IADsUser, ExpirationDate As Date)
    If 0 = ExpirationDate Then
        ' Disable the account expiration date.
        User.Put "accountExpires", 0
    Else
        ' Set the new account expiration date.
        User.AccountExpirationDate = ExpirationDate
    End If
    
    User.SetInfo
 
End Sub
```




```C++
/***************************************************************************

    SetUserAccountExpirationDate()

***************************************************************************/

HRESULT SetUserAccountExpirationDate(IADsUser *pUser, DATE date)
{
    if(!pUser) 
    {
        return E_INVALIDARG;
    }

    HRESULT hr;

    if(!date || date < 0) 
    {
        // Account never expires. Set the accountExpires attribute to zero.
        VARIANT var;
        VariantInit(&var);
        V_I4(&var) = 0;
        V_VT(&var) = VT_I4;
        
        hr = pUser->Put(CComBSTR("accountExpires"), var); 

        VariantClear(&var);
    }
    else 
    {
        // Account expires on date.
        hr = pUser->put_AccountExpirationDate(date); 
    }

    if(S_OK == hr)
    {
        hr = pUser->SetInfo();
    }

    return hr;
}
```



> [!Note]  
> The [**accountExpires**](/windows/desktop/ADSchema/a-accountexpires) attribute contains the account expire date. The Active Directory Users and Computers MMC snap-in displays the date that the account will expire at the end of. That is, the Active Directory Users and Computers MMC snap-in will display the account expiration date as one day earlier than the date contained in the **accountExpires** attribute.

 

 

 