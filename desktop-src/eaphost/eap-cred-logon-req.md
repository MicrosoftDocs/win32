---
title: EAP\_CRED\_LOGON\_REQ (Eaptypes.h)
description: Stores EAP security credentials within an EAP\_CONFIG\_INPUT\_FIELD\_ARRAY structure.
ms.assetid: 1F1A2F77-054D-4FD2-83A5-69C3D77418B3
keywords:
- EAP_CRED_LOGON_REQ
ms.topic: reference
ms.date: 05/31/2018
---

# EAP\_CRED\_LOGON\_REQ

The **EAP\_CRED\_LOGON\_REQ** structure stores EAP security credentials within an [**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_array) structure.


```C++
typedef EAP_CONFIG_INPUT_FIELD_ARRAY EAP_CRED_LOGON_REQ;
```



<dl> <dt>

**EAP\_CRED\_LOGON\_REQ**
</dt> <dd>

The **EAP\_CRED\_LOGON\_REQ** structure stores EAP security credentials pointed to by the *pbUiData* parameter of the [**EAP\_INTERACTIVE\_UI\_DATA**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_interactive_ui_data) structure when the *dwDataType* parameter of [**EAP\_INTERACTIVE\_UI\_DATA\_TYPE**](/windows/desktop/api/eaptypes/ne-eaptypes-eap_interactive_ui_data_type) specifies a credential request type. The input fields in this structure are the same as the input fields returned by [**EapHostPeerQueryCredentialInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerquerycredentialinputfields). **EAP\_CRED\_LOGON\_REQ** is used in the initial credential request and [**EAP\_CRED\_REQ**](eap-cred-req.md) is used in the credential retry request during an authentication.

</dd> </dl>

## Remarks

The **EAP\_CRED\_LOGON\_REQ** structure is used to support Single-Sign-On (SSO).

The **EAP\_CRED\_LOGON\_REQ** structure is identical to the [**EAP\_CRED\_LOGON\_RESP**](eap-cred-logon-resp.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Eaptypes.h</dt> </dl> |



## See also

<dl> <dt>

[**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_config_input_field_array)
</dt> <dt>

[**EAP\_CRED\_REQ**](eap-cred-req.md)
</dt> <dt>

[**EAP\_INTERACTIVE\_UI\_DATA**](/windows/desktop/api/eaptypes/ns-eaptypes-eap_interactive_ui_data)
</dt> <dt>

[**EAP\_INTERACTIVE\_UI\_DATA\_TYPE**](/windows/desktop/api/eaptypes/ne-eaptypes-eap_interactive_ui_data_type)
</dt> <dt>

[**EapHostPeerQueryCredentialInputFields**](/previous-versions/windows/desktop/api/eaphostpeerconfigapis/nf-eaphostpeerconfigapis-eaphostpeerquerycredentialinputfields)
</dt> </dl>

 

 





