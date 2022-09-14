---
title: EAP\_CERT Error Constants (Eaphosterror.h)
description: Define certificate-related errors common to all EAPHost API technologies.
ms.assetid: 12f626e1-520a-4aba-954b-769c3062a38c
topic_type:
- apiref
api_name:
- _EAP_CERT_FIRST
- _EAP_CERT_LAST
- _EAP_CERT_NOT_FOUND
- _EAP_CERT_INVALID
- _EAP_CERT_EXPIRED
- _EAP_CERT_REVOKED
- _EAP_CERT_OTHER_ERROR
- _EAP_CERT_REJECTED
- _EAP_CERT_NAME_REQUIRED
- _EAP_GENERAL_FIRST
- _EAP_GENERAL_LAST
api_location:
- eaphosterror.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# EAP\_CERT Error Constants

These constants define certificate-related errors common to all EAPHost API technologies.

<dl> <dt>

<span id="_EAP_CERT_FIRST"></span><span id="_eap_cert_first"></span>**\_EAP\_CERT\_FIRST**
</dt> <dd> <dl> <dt>

0x0
</dt> <dt>



Defines the boundary of error reports; any certificate error will occur between **\_EAP\_CERT\_FIRST** and **\_EAP\_CERT\_LAST**.


</dt> </dl> </dd> <dt>

<span id="_EAP_CERT_LAST"></span><span id="_eap_cert_last"></span>**\_EAP\_CERT\_LAST**
</dt> <dd> <dl> <dt>

0xF
</dt> <dt>



Defines the boundary of error reports; any certificate error will occur between **\_EAP\_CERT\_FIRST** and **\_EAP\_CERT\_LAST**.


</dt> </dl> </dd> <dt>

<span id="_EAP_CERT_NOT_FOUND"></span><span id="_eap_cert_not_found"></span>**\_EAP\_CERT\_NOT\_FOUND**
</dt> <dd> <dl> <dt>

0x1
</dt> <dt>



No user certificate was found.


</dt> </dl> </dd> <dt>

<span id="_EAP_CERT_INVALID"></span><span id="_eap_cert_invalid"></span>**\_EAP\_CERT\_INVALID**
</dt> <dd> <dl> <dt>

0x2
</dt> <dt>



The user certificate is invalid.


</dt> </dl> </dd> <dt>

<span id="_EAP_CERT_EXPIRED"></span><span id="_eap_cert_expired"></span>**\_EAP\_CERT\_EXPIRED**
</dt> <dd> <dl> <dt>

0x3
</dt> <dt>



The user certificate has expired.


</dt> </dl> </dd> <dt>

<span id="_EAP_CERT_REVOKED"></span><span id="_eap_cert_revoked"></span>**\_EAP\_CERT\_REVOKED**
</dt> <dd> <dl> <dt>

0x4
</dt> <dt>



The user certificate was revoked.


</dt> </dl> </dd> <dt>

<span id="_EAP_CERT_OTHER_ERROR"></span><span id="_eap_cert_other_error"></span>**\_EAP\_CERT\_OTHER\_ERROR**
</dt> <dd> <dl> <dt>

0x5
</dt> <dt>



There is an unknown certificate related error.


</dt> </dl> </dd> <dt>

<span id="_EAP_CERT_REJECTED"></span><span id="_eap_cert_rejected"></span>**\_EAP\_CERT\_REJECTED**
</dt> <dd> <dl> <dt>

0x6
</dt> <dt>



The user certificate was rejected.


</dt> </dl> </dd> <dt>

<span id="_EAP_CERT_NAME_REQUIRED"></span><span id="_eap_cert_name_required"></span>**\_EAP\_CERT\_NAME\_REQUIRED**
</dt> <dd> <dl> <dt>

0x7
</dt> <dt>



The user certificate requires a name.


</dt> </dl> </dd> <dt>

<span id="_EAP_GENERAL_FIRST"></span><span id="_eap_general_first"></span>**\_EAP\_GENERAL\_FIRST**
</dt> <dd> <dl> <dt>

0x10
</dt> <dt>



Defines the boundary of error reports; any general EAP error will occur between **\_EAP\_GENERAL\_FIRST** and **\_EAP\_GENERAL\_LAST**.


</dt> </dl> </dd> <dt>

<span id="_EAP_GENERAL_LAST"></span><span id="_eap_general_last"></span>**\_EAP\_GENERAL\_LAST**
</dt> <dd> <dl> <dt>

0x3F
</dt> <dt>



Defines the boundary of error reports; any general EAP error will occur between **\_EAP\_GENERAL\_FIRST** and **\_EAP\_GENERAL\_LAST**.


</dt> </dl> </dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                      |
| Header<br/>                   | <dl> <dt>Eaphosterror.h</dt> </dl> |



## See also

<dl> <dt>

[Common EAPHost Constants](common-eap-host-error-constants.md)
</dt> </dl>

 

 





