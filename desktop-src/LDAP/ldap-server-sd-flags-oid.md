---
title: LDAP\_SERVER\_SD\_FLAGS\_OID control code
description: Used to pass flags to the server to control various security descriptor results.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 195a3e91-32ea-41a6-9227-a7372da7f07b
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_SD_FLAGS_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_SD_FLAGS_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP\_SERVER\_SD\_FLAGS\_OID control code

The LDAP\_SERVER\_SD\_FLAGS\_OID control is used to pass flags to the server to control various security descriptor results.

To use this control, set the members of the [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure as follows.

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_SD_FLAGS_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_SD\_FLAGS\_OID, defined as "1.2.840.113556.1.4.801".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies a BER-encoded sequence of parameters that enables the application to specify various descriptor flags. In the [**berval**](/windows/previous-versions/Winldap/ns-winldap-berval?branch=master) structure, set **bv\_val** to a pointer to the sequence that contains the flag data and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether SD search/modify is critical to the operation.

</dd> </dl>

## Remarks

The Security Descriptor control enables the client to pass flags to specify various security descriptor options. The **ldctl\_value** field is set to the following BER-encoded sequence.

``` syntax
Sequence {
  Flags    INTEGER
}
```

The [**ber\_printf**](/windows/previous-versions/Winber/nf-winber-ber_printf?branch=master) function is used to create the sequence data. The flags portion contains the descriptor options to include. The following example code shows how to format the sequence data.


```C++
LDAPControl *FormatSDFlags(int iFlagValue)
{
  BerElement *pber = NULL;
  PLDAPControl pLControl = NULL;
  PBERVAL pldctrl_value = NULL;
  int success = -1;
  
  // Format and encode the SEQUENCE data in a BerElement.
  pber = ber_alloc_t(LBER_USE_DER);
  if(pber==NULL) return NULL;
  pLControl = new LDAPControl;
  if(pLControl==NULL) { ber_free(pber,1); return NULL; }
  ber_printf(pber,"{i}",iFlagValue);

  // Transfer the encoded data into a BERVAL.
  success = ber_flatten(pber,&amp;pldctrl_value);
  if(success == 0)
      ber_free(pber,1);
  else
  {
      printf("ber_flatten failed");
      // Call error handler here.
  }

  // Copy the BERVAL data to the LDAPControl structure.
  pLControl.ldctl_oid = LDAP_SERVER_SD_FLAGS_OID;
  pLControl.ldctl_iscritical = TRUE;
  pLControl.ldctl_value.bv_val = new char[pldctrl_value->bv_len];
  memcpy(pLControl.ldctl_value.bv_val, 
         pldctrl_value->bv_val, pldctrl_value->bv_len);
  pLControl.ldctl_value.bv_len = pldctrl_value->bv_len;

  // Cleanup temporary berval.
  ber_bvfree(pldctrl_value);

  // Return the formatted LDAPControl data.
  return pLControl;
}
```



The security information flags indicate which security descriptor parts to retrieve during a search. They can be bitwise **OR**ed to get multiple or all parts.



| Security information flag                   | Value                  | Description                                 |
|---------------------------------------------|------------------------|---------------------------------------------|
| **OWNER\_SECURITY\_INFORMATION**<br/> | 0x00000001L<br/> | Owner identifier of the object.<br/>  |
| **GROUP\_SECURITY\_INFORMATION**<br/> | 0x00000002L<br/> | Primary group identifier.<br/>        |
| **DACL\_SECURITY\_INFORMATION**<br/>  | 0x00000004L<br/> | Discretionary ACL of the object.<br/> |
| **SACL\_SECURITY\_INFORMATION**<br/>  | 0x00000008L<br/> | System ACL of the object.<br/>        |



 

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

[**LDAPMessage**](/windows/previous-versions/Winldap/ns-winldap-ldapmsg?branch=master)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





