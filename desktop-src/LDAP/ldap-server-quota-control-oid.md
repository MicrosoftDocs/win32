---
title: LDAP\_SERVER\_QUOTA\_CONTROL\_OID control code
description: Used to pass the SID of a security principal, whose quota is being queried, to the server in a LDAP search operation.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 1840a9c9-5f62-4104-ac41-64451421e7c0
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_QUOTA_CONTROL_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_QUOTA_CONTROL_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP\_SERVER\_QUOTA\_CONTROL\_OID control code

The LDAP\_SERVER\_QUOTA\_CONTROL\_OID control is used to pass the SID of a security principal, whose quota is being queried, to the server in a LDAP search operation. The LDAP search operation queries the constructed attributes [**ms-DS-Quota-Effective**](https://msdn.microsoft.com/library/ms677473) and [**ms-DS-Quota-Used**](https://msdn.microsoft.com/library/ms677475) specified below. The SID is passed as the "value" of the control as a binary value. The absence of this control in a search means that the SID of the user performing the search operation is to be used; that is, self-quota is queried.

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_QUOTA_CONTROL_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_QUOTA\_CONTROL\_OID, which is defined as "1.2.840.113556.1.4.1852".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies a **querySID** OCTET string whose value is a BER-encoded sequence of parameters that specify the SID of the security principal whose quota is to be queried. In the [**berval**](/windows/previous-versions/Winldap/ns-winldap-berval?branch=master) structure, set **bv\_val** to a pointer to the sequence that contains the SID of a security principal, and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the SID results is critical to the application.

</dd> </dl>

## Remarks

If the value of the *ldctl\_value* sequence argument is required to be created manually, the sequence data is formatted as follows:

``` syntax
Sequence {
  querySID     OCTET STRING
}
```

The following table lists the sequence fields.



| Sequence data           | Description                                                                                               |
|-------------------------|-----------------------------------------------------------------------------------------------------------|
| **querySID**<br/> | An Octet String that specifies the SID of the security principal whose quota is to be queried.<br/> |



 

The following code example shows how to manually format the sequence data for the first call to an extended LDAP search function.


```C++
LDAPControl lControl;
BerElement *pber = NULL;
PBERVAL pldctrl_value = NULL;
int success = -1;

// Format and encode the SEQUENCE data in a BerElement.
pber = ber_alloc_t(LBER_USE_DER);
if(pber==NULL) return BER_ALLOC_FAILURE_CODE;
ber_printf(pber,"{o}",NULL,0);

// Transfer the encoded data into a BERVAL.
success = ber_flatten(pber,&amp;pldctrl_value);
if(success == 0)
    ber_free(pber,1);
else
{
    printf("ber_flatten failed");
    // Call an error routine.
}

// Copy the BERVAL data to the LDAPControl structure.
lControl.ldctl_oid = LDAP_SERVER_QUOTA_CONTROL_OID;
lControl.ldctl_iscritical = TRUE;
lControl.ldctl_value.bv_val = new char[pldctrl_value->bv_len];
memcpy(lControl.ldctl_value.bv_val, 
       pldctrl_value->bv_val, pldctrl_value->bv_len);
lControl.ldctl_value.bv_len = pldctrl_value->bv_len;

// Cleanup temporary berval.
ber_bvfree(pldctrl_value);

// The LDAPControl data is ready for use in ldap_search_ext()
// or another call.
```



## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



## See also

<dl> <dt>

[Data Structures](data-structures.md)
</dt> <dt>

[**LDAPSearch**](/windows/previous-versions/Winldap/?branch=master)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





