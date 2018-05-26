---
title: EAP\_CRED\_RESP
description: Stores EAP security credentials within a EAP\_CONFIG\_INPUT\_FIELD\_ARRAY structure.
ms.assetid: 714c75d8-71c7-4c3f-802a-a5e4f6ca65c2
keywords:
- EAP_CRED_RESP
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# EAP\_CRED\_RESP

The **EAP\_CRED\_RESP** structure stores EAP security credentials within a [**EAP\_CONFIG\_INPUT\_FIELD\_ARRAY**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_config_input_field_array?branch=master) structure.


```C++
typedef EAP_CONFIG_INPUT_FIELD_ARRAY EAP_CRED_RESP;
```



<dl> <dt>

**EAP\_CRED\_RESP**
</dt> <dd>

The **EAP\_CRED\_RESP** structure stores both the old and new EAP security credentials pointed to by the *pbUiData* parameter of the [**EAP\_INTERACTIVE\_UI\_DATA**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_interactive_ui_data?branch=master) structure when the *dwDataType* parameter of [**EAP\_INTERACTIVE\_UI\_DATA\_TYPE**](/windows/previous-versions/eaptypes/ne-eaptypes-_eap_interactive_ui_data_type?branch=master) specifies a credential response type.

</dd> </dl>

## Remarks

The **EAP\_CRED\_RESP** structure is used to support Single-Sign-On (SSO).

The **EAP\_CRED\_RESP** structure is identical to the [**EAP\_CRED\_REQ**](eap-cred-req.md) structure.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Eaptypes.h</dt> </dl> |



## See also

<dl> <dt>

[EAPHost Supplicant Structures](eap-host-supplicant-structures.md)
</dt> <dt>

[**EAP\_CRED\_REQ**](eap-cred-req.md)
</dt> <dt>

[**EAP\_CRED\_EXPIRY\_REQ**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_cred_expiry_req?branch=master)
</dt> <dt>

[**EAP\_CRED\_EXPIRY\_RESP**](https://msdn.microsoft.com/library/windows/desktop/bb530539)
</dt> <dt>

[**EAP\_INTERACTIVE\_UI\_DATA**](/windows/previous-versions/eaptypes/ns-eaptypes-_eap_interactive_ui_data?branch=master)
</dt> <dt>

[SSO and PLAP](understanding-sso-and-plap.md)
</dt> </dl>

 

 





