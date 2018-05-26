---
title: LDAP\_SERVER\_CROSSDOM\_MOVE\_TARGET\_OID control code
description: Used with an extended LDAP rename function to move an LDAP object from one domain to another.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e6d6d59b-741e-4fa9-b392-f1ae68ef58e6
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# LDAP\_SERVER\_CROSSDOM\_MOVE\_TARGET\_OID control code

The LDAP\_SERVER\_CROSSDOM\_MOVE\_TARGET\_OID control is used with an extended LDAP rename function to move an LDAP object from one domain to another. The control specifies the DNS hostname of the domain controller in the destination domain.

To use this control, set the members of the [**LDAPControl**](/windows/previous-versions/Winldap/ns-winldap-ldapcontrola?branch=master) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

Pointer to a wide, null-terminated string, LDAP\_SERVER\_CROSSDOM\_MOVE\_TARGET\_OID, defined as "1.2.840.113556.1.4.521".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies the DNS name of the destination DC. In the [**berval**](/windows/previous-versions/Winldap/ns-winldap-berval?branch=master) structure, set **bv\_val** to a pointer to an UTF-8 string that contains the DNS name, and set **bv\_len** to the length of the string.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the results of the move is critical to your application.

</dd> </dl>

## Remarks

The following code example shows how to use the cross-domain control with the [**ldap\_rename\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_rename_ext_s?branch=master) function.


```C++
ULONG LDAPCrossDom (
    LDAP *ldapConnection,
    PWCHAR  pszOldDN,       // source object DN in Unicode
    PWCHAR  pszNewRDN,      // destination object DN in Unicode
    PWCHAR  pszNewParent,   // destination object parent DN in Unicode
    PWCHAR  pszDestDomain)  // destination domain DNS name in Unicode
{
ULONG ulErr;
LDAPControl CrossDomControl;
PLDAPControl controlArray[] = { &amp;CrossDomControl, NULL };
LPSTR pszDestDomainUTF8 = NULL;
int iDDSrclen = 0;
int iDDlen;
berval bvValue;

// Verify input parameters.
if (pszOldDN == NULL || pszNewRDN == NULL 
                     || pszNewParent == NULL
                     || pszDestDomain == NULL )
    return LDAP_PARAM_ERROR;

// Get required length of UTF-8 string buffer.
iDDSrclen = wcslen(pszDestDomain);
iDDlen = LdapUnicodeToUTF8(pszDestDomain,iDDSrclen,NULL,0);

// Check for zero length string
if (0 == iDDlen)
    return LDAP_PARAM_ERROR;

// Allocate buffer for UTF-8 string.
pszDestDomainUTF8 = (LPSTR) malloc(iDDlen+1);
if (pszDestDomainUTF8 == NULL)
    return LDAP_NO_MEMORY;

// Convert Unicode to UTF-8.
LdapUnicodeToUTF8(pszDestDomain,iDDSrclen,pszDestDomainUTF8,iDDlen+1);
pszDestDomainUTF8[iDDlen] = '\0';

// Setup control data.
bvValue.bv_val = (PCHAR) pszDestDomainUTF8;
bvValue.bv_len = iDDlen;
    
// Setup control.
CrossDomControl.ldctl_oid = LDAP_SERVER_CROSSDOM_MOVE_TARGET_OID_W;
CrossDomControl.ldctl_value = bvValue;
CrossDomControl.ldctl_iscritical = TRUE;
    
controlArray[0] = &amp;CrossDomControl;
controlArray[1] = NULL;
    
// Rename object across domains.
ulErr = ldap_rename_ext_s(ldapConnection, 
                           pszOldDN,  
                           pszNewRDN,
                           pszNewParent,
                           TRUE,
                           controlArray, 
                           NULL);
if (LDAP_SUCCESS == ulErr)
    wprintf(L"Successful move\n");
if (NULL != pszDestDomainUTF8)
    free(pszDestDomainUTF8);

return ulErr;
}
```



> [!Note]  
> The user application must have the proper directory service access rights to successfully use this control. The user application must have permission to delete objects in the source domain and create objects in the destination domain.

 

## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



## See also

<dl> <dt>

[**ldap\_rename\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_rename_ext_s?branch=master)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





