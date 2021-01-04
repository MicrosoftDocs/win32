---
title: Privacy Type (Wininet.h)
description: Specifies that privacy settings are for either first-party or third-party cookies.
ms.assetid: 7d0846d4-fd81-4af9-b7e6-05c4c1438770
topic_type:
- apiref
api_name:
- PRIVACY_TYPE_FIRST_PARTY
- PRIVACY_TYPE_THIRD_PARTY
api_location:
- Wininet.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Privacy Type

Specifies that privacy settings are for either first-party or third-party cookies.

<dl> <dt>

<span id="PRIVACY_TYPE_FIRST_PARTY"></span><span id="privacy_type_first_party"></span>**PRIVACY\_TYPE\_FIRST\_PARTY**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



Refers to privacy settings for first party cookies.


</dt> </dl> </dd> <dt>

<span id="PRIVACY_TYPE_THIRD_PARTY"></span><span id="privacy_type_third_party"></span>**PRIVACY\_TYPE\_THIRD\_PARTY**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



Refers to privacy settings for third party cookies.


</dt> </dl> </dd> </dl>

## Remarks

Cookies are categorized as first-party and third-party. A first-party cookie is one that originates from the host domain. If "https://www.blueyonderairlines.com" is found in the Microsoft Internet Explorer address bar, "www.blueyonderairlines.com" is the host domain. While visiting this page, if a cookie is set from a domain other than "www.blueyonderairlines.com", such as "www.fourthcoffee.com", this cookie is considered a third-party cookie.

> [!Note]  
> WinINet does not support server implementations. In addition, it should not be used from a service. For server implementations or services use [Microsoft Windows HTTP Services (WinHTTP)](/windows/desktop/WinHttp/winhttp-start-page).

 

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>Wininet.h</dt> </dl> |



## See also

<dl> <dt>

[**PrivacyGetZonePreferenceW**](/windows/win32/api/winineti/nf-winineti-privacygetzonepreferencew)
</dt> <dt>

[**PrivacySetZonePreferenceW**](/windows/win32/api/winineti/nf-winineti-privacysetzonepreferencew)
</dt> </dl>

 

