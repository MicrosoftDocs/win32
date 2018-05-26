---
title: DSML Services for Windows and LDAP
description: DSML Services for Windows expresses LDAP requests and responses as XML document fragments.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: e234bcb0-eefb-4f51-8bfd-7a92fe78ce46
ms.prod: windows-server-dev
ms.technology: active-directory-domain-services
ms.tgt_platform: multiple
keywords:
- DSML Services for Windows and LDAP DSML
- operations grouping
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DSML Services for Windows and LDAP

DSML Services for Windows expresses LDAP requests and responses as XML document fragments. When DSML Services for Windows receives a DSML V2 request from a client, it translates it into an LDAP 3 query that is sent to Active Directory. When the subsequent LDAP 3 response from Active Directory is received, it gets translated back into a DSML V2 response that is returned to the originating client.

When a DSML V2 element name matches an identifier in the LDAP ASN.1 grammar, as defined by RFC 2251, the named element means the same thing both in DSML V2 and in LDAP. Except where noted otherwise, the DSML V2 grammar follows the same rules as the LDAP grammar, even if those rules are not explicitly expressed in the schema. For example, a DSML V2 **AttributeDescription** element can contain only those characters allowed by LDAP.

There are, however, a few areas where DSML V2 deviates from LDAP behavior:

-   Operations Grouping

    LDAP does not include a method for grouping operations in a single request, but DSML V2 does. A single DSML request document can contain multiple requests. A positional relationship is maintained between individual operations in a DSML request document and the corresponding responses in a response document.

-   Search Responses

    In LDAP, a search request usually generates multiple responses. In DSML V2, all the related LDAP responses for a given search request are wrapped into a single **searchResponse** element and returned in a DSML document.

DSML V2 also eliminates an extra level of nested elements that occurs in LDAP and is caused by the translation of the LDAPMessage structure and the way in which LDAP uses defaulting.

For more information about the differences between LDAP and DSML V2, see the DSML V2 specification in the *Directory Services* section of [http://www.oasis-open.org](http://go.microsoft.com/fwlink/p/?linkid=84150). (This resource may not be available in some languages and countries or regions.)

 

 




