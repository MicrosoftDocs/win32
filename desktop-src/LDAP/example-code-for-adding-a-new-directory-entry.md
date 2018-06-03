---
title: Example Code for Adding a New Directory Entry
description: The following code example creates LDAPMod structures for a new entry with six initial attributes, and then constructs an array of these structures to pass to ldap\_add (the asynchronous add function).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 6cc64c44-5472-43b4-b524-5e18dd55a163
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Example Code for Adding a New Directory Entry LDAP
- Adding a New Directory Entry LDAP
- Adding a Directory Entry LDAP
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Example Code for Adding a New Directory Entry

The following code example creates [**LDAPMod**](/previous-versions/windows/desktop/api/Winldap/ns-winldap-ldapmoda) structures for a new entry with six initial attributes, and then constructs an array of these structures to pass to [**ldap\_add**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_add) (the asynchronous add function).


```C++
#include <winldap.h>
ULONG CallValue;

// Attributes include Name, Class, First name, Last name, Title, and Telephone number
LDAPMod Name, OClass, FName, LName, Title, Phone;
LDAP *ld = ldap_init(NULL,LDAP_PORT);

CallValue = ldap_connect(ld,NULL);

if(CallValue!=LDAP_SUCCESS)
{
    return 0;
}


// Specify the distinguished name for the entry.
char *entry_dn = "cn=Jeff Smith,CN=Users";

char *cn_values[] = { "Jeff Smith", NULL };
Name.mod_op = LDAP_MOD_ADD;
Name.mod_type = "cn";
Name.mod_values = cn_values;. 

char *oc_values[] = { "user", NULL };
OClass.mod_op = LDAP_MOD_ADD;
OClass.mod_type = "objectClass";
OClass.mod_values = oc_values;. 

char *gn_values[] = { "Jeff", NULL };
FName.mod_op = LDAP_MOD_ADD;
FName.mod_type = "givenName";
FName.mod_values = gn_values;. 

char *sn_values[] = { "Smith", NULL };
LName.mod_op = LDAP_MOD_ADD;
LName.mod_type = "sn";
LName.mod_values = sn_values;. 

char *ti_values[] = { "Developer", NULL };
Title.mod_op = LDAP_MOD_ADD;
Title.mod_type = "title";
Title.mod_values = ti_values;. 

char *pn_values[] = { "425) 555-0174", NULL };
Phone.mod_op = LDAP_MOD_ADD;
Phone.mod_type = "telephoneNumber";
Phone.mod_values = pn_values;. 

// Build the array of attributes. 
LDAPMod *NewEntry[7];

NewEntry[0] = &amp;Name;
NewEntry[1] = &amp;OClass
NewEntry[2] = &amp;FName;
NewEntry[3] = &amp;LName;
NewEntry[4] = &amp;Title;
NewEntry[5] = &amp;Phone;
NewEntry[6] = NULL;

// Add the entry.
CallValue = ldap_add( ld, entry_dn, NewEntry);

// Pass CallValue to ldap_result to verify the 
// status of the asynchronous operation.

CallValue = ldap_unbind(ld);
```



 

 




