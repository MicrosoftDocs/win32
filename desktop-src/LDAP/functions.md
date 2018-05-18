---
title: Functions
description: This section describes the API functions supported in LDAP 2 and 3. The table of contents lists the functions in alphabetical order. The following functions are grouped by task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: '7a0040ea-f8f3-4378-8371-49768714d762'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
keywords: ["LDAP LDAP , Reference, Functions"]
---

# Functions

This section describes the API functions supported in LDAP 2 and 3. The table of contents lists the functions in alphabetical order. The following functions are grouped by task.

## Starting and Stopping an LDAP Session

Use these functions to initialize and open a connection block, authenticate a client to a server, set options for the LDAP session, and close a session.

-   [**cldap\_open**](cldap-open.md)
-   [**ldap\_open**](ldap-open.md)
-   [**ldap\_bind**](ldap-bind.md)
-   [**ldap\_bind\_s**](ldap-bind-s.md)
-   [**ldap\_simple\_bind**](ldap-simple-bind.md)
-   [**ldap\_simple\_bind\_s**](ldap-simple-bind-s.md)
-   [**ldap\_sasl\_bind**](ldap-sasl-bind.md)
-   [**ldap\_sasl\_bind\_s**](ldap-sasl-bind-s.md)
-   [**ldap\_connect**](ldap-connect.md)
-   [**ldap\_init**](ldap-init.md)
-   [**ldap\_sslinit**](ldap-sslinit.md)
-   [**ldap\_get\_option**](ldap-get-option.md)
-   [**ldap\_set\_option**](ldap-set-option.md)
-   [**ldap\_abandon**](ldap-abandon.md)
-   [**ldap\_unbind**](ldap-unbind.md)
-   [**ldap\_unbind\_s**](ldap-unbind-s.md)
-   [**ldap\_cleanup**](ldap-cleanup.md)

## Modifying Directory Entries

Use these functions to perform operations on directory entries.

-   [**ldap\_add**](ldap-add.md)
-   [**ldap\_add\_ext**](ldap-add-ext.md)
-   [**ldap\_add\_s**](ldap-add-s.md)
-   [**ldap\_add\_ext\_s**](ldap-add-ext-s.md)
-   [**ldap\_compare**](ldap-compare.md)
-   [**ldap\_compare\_ext**](ldap-compare-ext.md)
-   [**ldap\_compare\_s**](ldap-compare-s.md)
-   [**ldap\_compare\_ext\_s**](ldap-compare-ext-s.md)
-   [**ldap\_delete**](ldap-delete.md)
-   [**ldap\_delete\_ext**](ldap-delete-ext.md)
-   [**ldap\_delete\_s**](ldap-delete-s.md)
-   [**ldap\_delete\_ext\_s**](ldap-delete-ext-s.md)
-   [**ldap\_extended\_operation\_s**](ldap-extended-operation-s.md)
-   [**ldap\_extended\_operation**](ldap-extended-operation.md)
-   [**ldap\_close\_extended\_op**](ldap-close-extended-op.md)
-   [**ldap\_modify**](ldap-modify.md)
-   [**ldap\_modify\_ext**](ldap-modify-ext.md)
-   [**ldap\_modify\_s**](ldap-modify-s.md)
-   [**ldap\_modify\_ext\_s**](ldap-modify-ext-s.md)

## Searching, Sorting, and Result Handling

Use these functions to search a directory or sort and parse results, with or without controls.

-   [**ldap\_check\_filter**](ldap-check-filter.md)
-   [**ldap\_count\_entries**](ldap-count-entries.md)
-   [**ldap\_count\_references**](ldap-count-references.md)
-   [**ldap\_count\_values**](ldap-count-values.md)
-   [**ldap\_count\_values\_len**](ldap-count-values-len.md)
-   [**ldap\_create\_page\_control**](ldap-create-page-control.md)
-   [**ldap\_create\_sort\_control**](ldap-create-sort-control.md)
-   [**ldap\_create\_vlv\_control**](ldap-create-vlv-control.md)
-   [**ldap\_encode\_sort\_control**](ldap-encode-sort-control.md)
-   [**ldap\_escape\_filter\_element**](ldap-escape-filter-element.md)
-   [**ldap\_first\_attribute**](ldap-first-attribute.md)
-   [**ldap\_next\_attribute**](ldap-next-attribute.md)
-   [**ldap\_first\_entry**](ldap-first-entry.md)
-   [**ldap\_next\_entry**](ldap-next-entry.md)
-   [**ldap\_first\_reference**](ldap-first-reference.md)
-   [**ldap\_next\_reference**](ldap-next-reference.md)
-   [**ldap\_get\_next\_page**](ldap-get-next-page.md)
-   [**ldap\_get\_next\_page\_s**](ldap-get-next-page-s.md)
-   [**ldap\_get\_paged\_count**](ldap-get-paged-count.md)
-   [**ldap\_get\_values**](ldap-get-values.md)
-   [**ldap\_get\_values\_len**](ldap-get-values-len.md)
-   [**ldap\_parse\_extended\_result**](ldap-parse-extended-result.md)
-   [**ldap\_parse\_page\_control**](ldap-parse-page-control.md)
-   [**ldap\_parse\_reference**](ldap-parse-reference.md)
-   [**ldap\_parse\_result**](ldap-parse-result.md)
-   [**ldap\_parse\_sort\_control**](ldap-parse-sort-control.md)
-   [**ldap\_parse\_vlv\_control**](ldap-parse-vlv-control.md)
-   [**ldap\_result**](ldap-result.md)
-   [**ldap\_search**](ldap-search.md)
-   [**ldap\_search\_s**](ldap-search-s.md)
-   [**ldap\_search\_st**](ldap-search-st.md)
-   [**ldap\_search\_ext**](ldap-search-ext.md)
-   [**ldap\_search\_ext\_s**](ldap-search-ext-s.md)
-   [**ldap\_search\_init\_page**](ldap-search-init-page.md)
-   [**ldap\_search\_abandon\_page**](ldap-search-abandon-page.md)

## Error Handling

Use these functions to handle errors.

-   [**ldap\_err2string**](ldap-err2string.md)
-   [**LdapGetLastError**](ldapgetlasterror.md)
-   [**LdapMapErrorToWin32**](ldapmaperrortowin32.md)
-   [**ldap\_result2error**](ldap-result2error.md)

## Memory Management

Use these functions to explicitly free data structures when no longer required.

-   [**ldap\_control\_free**](ldap-control-free.md)
-   [**ldap\_controls\_free**](ldap-controls-free.md)
-   [**ldap\_memfree**](ldap-memfree.md)
-   [**ldap\_msgfree**](ldap-msgfree.md)
-   [**ldap\_value\_free**](ldap-value-free.md)
-   [**ldap\_value\_free\_len**](ldap-value-free-len.md)

## Miscellaneous Functions

Use these functions to convert the forms of distinguished names, modify entry names, convert text strings, and set debugging options.

-   [**ldap\_dn2ufn**](ldap-dn2ufn.md)
-   [**ldap\_ufn2dn**](ldap-ufn2dn.md)
-   [**ldap\_explode\_dn**](ldap-explode-dn.md)
-   [**ldap\_get\_dn**](ldap-get-dn.md)
-   [**ldap\_conn\_from\_msg**](ldap-conn-from-msg.md)
-   [**ldap\_modrdn2**](ldap-modrdn2.md)
-   [**ldap\_modrdn2\_s**](ldap-modrdn2-s.md)
-   [**ldap\_rename\_ext**](ldap-rename-ext.md)
-   [**ldap\_rename\_ext\_s**](ldap-rename-ext-s.md)
-   [**LdapUnicodeToUTF8**](ldapunicodetoutf8.md)
-   [**LdapUTF8ToUnicode**](ldaputf8tounicode.md)
-   [**ber\_init**](ber-init.md)
-   [**ber\_free**](ber-free.md)
-   [**ber\_bvfree**](ber-bvfree.md)
-   [**ber\_bvecfree**](ber-bvecfree.md)
-   [**ber\_bvdup**](ber-bvdup.md)
-   [**ber\_alloc\_t**](ber-alloc-t.md)
-   [**ber\_skip\_tag**](ber-skip-tag.md)
-   [**ber\_peek\_tag**](ber-peek-tag.md)
-   [**ber\_first\_element**](ber-first-element.md)
-   [**ber\_next\_element**](ber-next-element.md)
-   [**ber\_flatten**](ber-flatten.md)
-   [**ber\_printf**](ber-printf.md)
-   [**ber\_scanf**](ber-scanf.md)

 

 




