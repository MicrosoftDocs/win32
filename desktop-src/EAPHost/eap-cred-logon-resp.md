---
title: EAP\_CRED\_LOGON\_RESP
description: Stores EAP security credentials within a EAP\_CONFIG\_INPUT\_FIELD\_ARRAY structure.
ms.assetid: '1244A40F-6999-4053-97C4-1C4FB107B2F5'
keywords: ["EAP_CRED_LOGON_RESP"]
---

# EAP\_CRED\_LOGON\_RESP

The **EAP\_CRED\_LOGON\_RESP** structure stores EAP security credentials within a [**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](eap-config-input-field-array.md) structure.


```C++
typedef EAP_CONFIG_INPUT_FIELD_ARRAY EAP_CRED_LOGON_RESP;
```



<dl> <dt>

**EAP\_CRED\_LOGON\_RESP**
</dt> <dd>

The **EAP\_CRED\_LOGON\_RESP** structure stores EAP security credentials pointed to by the *pbUiData* parameter of the [**EAP\_INTERACTIVE\_UI\_DATA**](eap-interactive-ui-data.md) structure when the *dwDataType* parameter of [**EAP\_INTERACTIVE\_UI\_DATA\_TYPE**](eap-interactive-ui-data-type.md) specifies a credential request type. The input fields in this structure will be same as the input fields returned by [**EapHostPeerQueryCredentialInputFields**](eaphostpeerquerycredentialinputfields.md). **EAP\_CRED\_LOGON\_RESP** is used in the initial credential request and [**EAP\_CRED\_RESP**](eap-cred-resp.md) is used in the credential retry request during an authentication.

</dd> </dl>

## Remarks

The **EAP\_CRED\_LOGON\_RESP** structure is used to support Single-Sign-On (SSO).

The **EAP\_CRED\_LOGON\_RESP** structure is identical to the [**EAP\_CRED\_LOGON\_REQ**](eap-cred-logon-req.md) structure.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                               |
| Header<br/>                   | <dl> <dt>Eaptypes.h</dt> </dl> |



## See also

<dl> <dt>

[**EapHostPeerQueryCredentialInputFields**](eaphostpeerquerycredentialinputfields.md)
</dt> <dt>

[**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](eap-config-input-field-array.md)
</dt> <dt>

[**EAP\_CRED\_LOGON\_REQ**](eap-cred-logon-req.md)
</dt> <dt>

[**EAP\_INTERACTIVE\_UI\_DATA**](eap-interactive-ui-data.md)
</dt> <dt>

[**EAP\_INTERACTIVE\_UI\_DATA\_TYPE**](eap-interactive-ui-data-type.md)
</dt> </dl>

 

 





