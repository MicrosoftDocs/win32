---
title: LDAP\_SERVER\_EXTENDED\_DN\_OID control code
description: Used with an extended LDAP search function to request an extended form of an Active Directory object distinguished name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b375a6a1-c72a-4479-9c1a-9168f2fbe891
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP_SERVER_EXTENDED_DN_OID control code LDAP
topic_type:
- apiref
api_name:
- LDAP_SERVER_EXTENDED_DN_OID
api_location:
- Ntldap.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# LDAP\_SERVER\_EXTENDED\_DN\_OID control code

The LDAP\_SERVER\_EXTENDED\_DN\_OID control is used with an extended LDAP search function to request an extended form of an Active Directory object distinguished name. The extended form includes a string representation of the object **objectGUID** property. For security principal objects such as users, groups, and computers, the extended form also includes a string representation of the object **objectSID** property.

To use this control, set the members of the [**LDAPControl**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapcontrola) structure as follows:

``` syntax
PWCHAR ldctl_oid = LDAP_SERVER_EXTENDED_DN_OID;
struct berval ldctl_value;
BOOLEAN ldctl_iscritical;
```

## Members

<dl> <dt>

**ldctl\_oid**
</dt> <dd>

LDAP\_SERVER\_EXTENDED\_DN\_OID, which is defined as "1.2.840.113556.1.4.529".

</dd> <dt>

**ldctl\_value**
</dt> <dd>

Specifies the BER-encoded sequence of parameters that enables the application to specify the string format of the returned GUID and SID. In the [**berval**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-berval) structure, set **bv\_val** to a pointer to the sequence that contains the flag data and set **bv\_len** to the length of the sequence. For more information, see the Remarks section.

</dd> <dt>

**ldctl\_iscritical**
</dt> <dd>

Can be **TRUE** or **FALSE** depending on whether the search is critical to your application.

</dd> </dl>

## Remarks

The Extended DN Control enables the client to request that the results returned by an LDAP search that uses this control return the GUID and SID data of an object along with the object *distinguishedName*, which is returned as follows.

``` syntax
<GUID=xxxxxxxx>;<SID=yyyyyyyyy>;distinguishedName
```

Where *xxxxxxxx* is a string that contains the GUID, *yyyyyyyy* is a string that contains the SID, and *distinguishedName* is the DN, as in "cn=users,dc=fabrikam,dc=com". The GUID and DN are always present; the SID is present only for security principals.

The flag value passed in the **ldctl\_value** field specifies the string format of the returned GUID and SID values, and is set to the following Ber-encoded sequence:

``` syntax
Sequence {
  Flag    INTEGER
}
```

A flag value **0** specifies that the GUID and SID values be returned in hexadecimal string format such as "&lt;GUID=3BC72D2DEC5A704BBDC21F4EF97B7870&gt;" and "&lt;SID=0105000000000005150000005951B81766725D2564633B0B9B602C00&gt;".

A flag value of **1** will return the GUID and SID values in standard string format such as "&lt;GUID=098f2470-bae0-11cd-b579-08002b30bfeb&gt;" and "&lt;SID=S-1-5-21-397955417-626881126-188441444-2908315&gt;".

The following C++ example code shows how to manually format the sequence data. The [**ber\_printf**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_printf) function is used to create the sequence data. The flags portion contains the GUID/SID string format specifier.


```C++
LDAPControl *FormatExtDNFlags(int iFlagValue)
{
  BerElement *pber = NULL;
  PLDAPControl pLControl = NULL;
  PBERVAL pldctrl_value = NULL;
  int success = -1;

  // Ensure that iFlagValue is either 0 or 1. Convert TRUE (-1) to a legal value.
  if(iFlagValue != 0) iFlagValue = 1;
    
  // Format and encode the SEQUENCE data in a BerElement.
  pber = ber_alloc_t(LBER_USE_DER);
  if(pber==NULL) return NULL;
  pLControl = new LDAPControl;
  if(pLControl==NULL) { ber_free(pber,1); return NULL; }
  ber_printf(pber,"{i}",iFlagValue);

  // Transfer encoded data into a BERVAL.
  success = ber_flatten(pber,&amp;pldctrl_value);
  ber_free(pber,1);
  if(success != 0) {return NULL;}

  // Copy the BERVAL data to the LDAPControl structure.
  pLControl.ldctl_oid = LDAP_SERVER_EXTENDED_DN_OID;
  pLControl.ldctl_iscritical = TRUE;
  pLControl.ldctl_value.bv_val = new char[pldctrl_value->bv_len];
  memcpy(pLControl.ldctl_value.bv_val, 
         pldctrl_value->bv_val, pldctrl_value->bv_len);
  pLControl.ldctl_value.bv_len = pldctrl_value->bv_len;

  // Cleanup temporary berval.
  ber_bvfree(pldctrl_value);

  // Return formatted LDAPControl data.
  return pLControl;
}
```



The following C++ example code shows how to use the extended DN control with the [**ldap\_search\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext_s) function.


```C++
INT err;
LDAP *ldapConnection = NULL;
PLDAPControl pExtDNcontrol;
PLDAPControl controlArray[2];
LDAPMessage *results = NULL;
LDAPMessage *message = NULL;
PWCHAR dn = NULL;

// Connect to the default LDAP server.
ldapConnection = ldap_open( NULL, 0 );
if ( ldapConnection == NULL ) goto FatalExit0;
 
// Bind to the server using default credentials.
err = ldap_bind_s( ldapConnection, NULL, NULL, LDAP_AUTH_NEGOTIATE );
if (LDAP_SUCCESS != err) goto FatalExit0;

// Setup the extended DN control, requesting 'standard string' format.
pExtDNControl = FormatExtDNFlags(1);
if (pExtDNControl == NULL) goto FatalExit0;
controlArray[0] = pExtDNcontrol;
controlArray[1] = NULL;

// Perform a synchronous search.
err   = ldap_search_ext_s( ldapConnection,
                     L"cn=users,dc=Fabrikam,dc=com",
                     LDAP_SCOPE_SUBTREE,
                     L"objectClass=*",
                     NULL,          // Retrieve all attributes.
                     0,             // Retrieve attributes and values.
                     (PLDAPControl *) &amp;controlArray,
                     NULL,          // Client controls.
                     0,             // Timeout.
                     0,             // Sizelimit.
                     &amp;results       // Receives identifier for results.
                     );
if (LDAP_SUCCESS != err) goto FatalExit0;

// Process the search results.
message = ldap_first_entry( ldapConnection, results );
while (message != NULL) 
{
    // Print the distinguished name of the object.
    dn = ldap_get_dn( ldapConnection, message );
    if (!dn) goto FatalExit0;
    wprintf( L"  Distinguished Name is : %s\n", dn );
    ldap_memfree(dn);
    message = ldap_next_entry( ldapConnection, message );
}
 
FatalExit0:
if (ldapConnection)
    ldap_unbind( ldapConnection );
if (results)
    ldap_msgfree( results );
```



## Requirements



|                                     |                                                                                     |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                      |
| Header<br/>                   | <dl> <dt>Ntldap.h</dt> </dl> |



## See also

<dl> <dt>

[**ldap\_search\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext_s)
</dt> <dt>

[Using Controls](using-controls.md)
</dt> </dl>

 

 





