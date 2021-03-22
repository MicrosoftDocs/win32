---
title: External.accountType
description: Note This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported. The accountType property retrieves the account type of the current user.
ms.assetid: 4fb6de90-a32d-4483-bbae-b23cbff93bd5
keywords:
- External.accountType Windows Media Player
topic_type:
- apiref
api_name:
- External.accountType
api_location:
- wmp.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# External.accountType

> [!Note]  
> This topic describes functionality designed for use by online stores. Use of this functionality outside the context of an online store is not supported.

 

The **accountType** property retrieves the account type of the current user.

``` syntax
window.external.accountType
      
```

## Possible Values

This property is a read-only **String** that represents the account type. Strings that represent various account types are defined by the online store.

## Remarks

This property retrieves the account type by calling the [IWMPContentPartner::GetContentPartnerInfo](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getcontentpartnerinfo) method, which is implemented by the online store's plug-in. If the current user is logged in to the online store or the plug-in has cached the user's credentials, the **getContentPartnerInfo** method can determine the user's account type and return it to Windows Media Player. The account type is a string that Windows Media Player does not interpret. Rather, Windows Media Player passes the string from the online store's plug-in to the script on the online store's discovery page.

If the current user is not logged in to the online store and the online store's plug-in does not have cached credentials for the user, this property retrieves whatever string the **getContentPartnerInfo** method returns in that situation.

## Requirements



| Requirement | Value |
|--------------------|------------------------------------------------------------------------------------|
| Version<br/> | Windows Media Player 11.<br/>                                                |
| DLL<br/>     | <dl> <dt>Wmp.dll</dt> </dl> |



## See also

<dl> <dt>

[**External Object for Type 1 Online Stores**](external-object-for-type-1-online-stores.md)
</dt> <dt>

[**External.userLoggedIn**](external-userloggedin.md)
</dt> </dl>

 

 





