---
title: Privacy Templates (Wininet.h)
description: The following are privacy levels that equate to rules for accepting, conditionally accepting, or not accepting cookies.
ms.assetid: d8dd9c12-b159-4f95-820e-521aeb1526bf
topic_type:
- apiref
api_name:
- PRIVACY_TEMPLATE_NO_COOKIES
- PRIVACY_TEMPLATE_HIGH
- PRIVACY_TEMPLATE_MEDIUM_HIGH
- PRIVACY_TEMPLATE_MEDIUM
- PRIVACY_TEMPLATE_MEDIUM_LOW
- PRIVACY_TEMPLATE_LOW
- PRIVACY_TEMPLATE_CUSTOM
- PRIVACY_TEMPLATE_ADVANCED
- PRIVACY_TEMPLATE_MAX
api_location:
- Wininet.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Privacy Templates

The following are privacy levels that equate to rules for accepting, conditionally accepting, or not accepting cookies. These levels correspond to the privacy preference levels set on the Privacy tab in Internet Options. See [Privacy in Internet Explorer 6](https://www.bing.com/search?q=Privacy+in+Internet+Explorer+6) for detailed definitions.

<dl> <dt>

<span id="PRIVACY_TEMPLATE_NO_COOKIES"></span><span id="privacy_template_no_cookies"></span>**PRIVACY\_TEMPLATE\_NO\_COOKIES**
</dt> <dd> <dl> <dt>

0
</dt> <dt>



This is the same as **Block All Cookies** on the Privacy Preferences slider bar in **Internet Options**.


</dt> </dl> </dd> <dt>

<span id="PRIVACY_TEMPLATE_HIGH"></span><span id="privacy_template_high"></span>**PRIVACY\_TEMPLATE\_HIGH**
</dt> <dd> <dl> <dt>

1
</dt> <dt>



This is the same as **High** on the Privacy Preferences slider bar in **Internet Options**.


</dt> </dl> </dd> <dt>

<span id="PRIVACY_TEMPLATE_MEDIUM_HIGH"></span><span id="privacy_template_medium_high"></span>**PRIVACY\_TEMPLATE\_MEDIUM\_HIGH**
</dt> <dd> <dl> <dt>

2
</dt> <dt>



This is the same as **Medium\_High** on the Privacy Preferences slider bar in **Internet Options**.


</dt> </dl> </dd> <dt>

<span id="PRIVACY_TEMPLATE_MEDIUM"></span><span id="privacy_template_medium"></span>**PRIVACY\_TEMPLATE\_MEDIUM**
</dt> <dd> <dl> <dt>

3
</dt> <dt>



This is the same as **Medium** on the Privacy Preferences slider bar in **Internet Options**.


</dt> </dl> </dd> <dt>

<span id="PRIVACY_TEMPLATE_MEDIUM_LOW_"></span><span id="privacy_template_medium_low_"></span>**PRIVACY\_TEMPLATE\_MEDIUM\_LOW** 
</dt> <dd> <dl> <dt>

4
</dt> <dt>



This is the same as **Low** on the Privacy Preferences slider bar in **Internet Options**.


</dt> </dl> </dd> <dt>

<span id="PRIVACY_TEMPLATE_LOW"></span><span id="privacy_template_low"></span>**PRIVACY\_TEMPLATE\_LOW**
</dt> <dd> <dl> <dt>

5
</dt> <dt>



This is the same as **Accept All Cookies** on the Privacy Preferences slider bar in **Internet Options**.


</dt> </dl> </dd> <dt>

<span id="PRIVACY_TEMPLATE_CUSTOM"></span><span id="privacy_template_custom"></span>**PRIVACY\_TEMPLATE\_CUSTOM**
</dt> <dd> <dl> <dt>

100
</dt> <dt>



User-defined. See [How to Create a Customized Privacy Import File](https://www.bing.com/search?q=How+to+Create+a+Customized+Privacy+Import+File) to understand how to set custom privacy settings.


</dt> </dl> </dd> <dt>

<span id="PRIVACY_TEMPLATE_ADVANCED"></span><span id="privacy_template_advanced"></span>**PRIVACY\_TEMPLATE\_ADVANCED**
</dt> <dd> <dl> <dt>

101
</dt> <dt>



User-defined. Advanced options are set in the **Advanced Privacy Settings** dialog reachable from the **Privacy** tab in **Internet Options**.


</dt> </dl> </dd> <dt>

<span id="PRIVACY_TEMPLATE_MAX"></span><span id="privacy_template_max"></span>**PRIVACY\_TEMPLATE\_MAX**
</dt> <dd> <dl> <dt>

PRIVACY\_TEMPLATE\_LOW
</dt> <dt>



Same as **PRIVACY\_TEMPLATE\_LOW**.


</dt> </dl> </dd> </dl>

## Remarks

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

 

