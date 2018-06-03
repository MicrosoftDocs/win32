---
title: Functions
description: This section describes the API functions supported in LDAP 2 and 3. The table of contents lists the functions in alphabetical order. The following functions are grouped by task.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 7a0040ea-f8f3-4378-8371-49768714d762
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- LDAP LDAP , Reference, Functions
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Functions

This section describes the API functions supported in LDAP 2 and 3. The table of contents lists the functions in alphabetical order. The following functions are grouped by task.

## Starting and Stopping an LDAP Session

Use these functions to initialize and open a connection block, authenticate a client to a server, set options for the LDAP session, and close a session.

-   [**cldap\_open**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-cldap_open)
-   [**ldap\_open**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_open)
-   [**ldap\_bind**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_bind)
-   [**ldap\_bind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_bind_s)
-   [**ldap\_simple\_bind**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_simple_bind)
-   [**ldap\_simple\_bind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_simple_bind_s)
-   [**ldap\_sasl\_bind**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_sasl_binda)
-   [**ldap\_sasl\_bind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_sasl_bind_sa)
-   [**ldap\_connect**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_connect)
-   [**ldap\_init**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_init)
-   [**ldap\_sslinit**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_sslinit)
-   [**ldap\_get\_option**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_option)
-   [**ldap\_set\_option**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_set_option)
-   [**ldap\_abandon**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_abandon)
-   [**ldap\_unbind**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_unbind)
-   [**ldap\_unbind\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_unbind_s)
-   [**ldap\_cleanup**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_cleanup)

## Modifying Directory Entries

Use these functions to perform operations on directory entries.

-   [**ldap\_add**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_add)
-   [**ldap\_add\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_add_ext)
-   [**ldap\_add\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_add_s)
-   [**ldap\_add\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_add_ext_s)
-   [**ldap\_compare**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_compare)
-   [**ldap\_compare\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_compare_ext)
-   [**ldap\_compare\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_compare_s)
-   [**ldap\_compare\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_compare_ext_s)
-   [**ldap\_delete**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_delete)
-   [**ldap\_delete\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_delete_ext)
-   [**ldap\_delete\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_delete_s)
-   [**ldap\_delete\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_delete_ext_s)
-   [**ldap\_extended\_operation\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_extended_operation_sa)
-   [**ldap\_extended\_operation**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_extended_operation)
-   [**ldap\_close\_extended\_op**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_close_extended_op)
-   [**ldap\_modify**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_modify)
-   [**ldap\_modify\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_modify_ext)
-   [**ldap\_modify\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_modify_s)
-   [**ldap\_modify\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_modify_ext_s)

## Searching, Sorting, and Result Handling

Use these functions to search a directory or sort and parse results, with or without controls.

-   [**ldap\_check\_filter**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_check_filtera)
-   [**ldap\_count\_entries**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_count_entries)
-   [**ldap\_count\_references**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_count_references)
-   [**ldap\_count\_values**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_count_values)
-   [**ldap\_count\_values\_len**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_count_values_len)
-   [**ldap\_create\_page\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_create_page_control)
-   [**ldap\_create\_sort\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_create_sort_control)
-   [**ldap\_create\_vlv\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_create_vlv_controla)
-   [**ldap\_encode\_sort\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_encode_sort_control)
-   [**ldap\_escape\_filter\_element**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_escape_filter_element)
-   [**ldap\_first\_attribute**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_first_attribute)
-   [**ldap\_next\_attribute**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_next_attribute)
-   [**ldap\_first\_entry**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_first_entry)
-   [**ldap\_next\_entry**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_next_entry)
-   [**ldap\_first\_reference**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_first_reference)
-   [**ldap\_next\_reference**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_next_reference)
-   [**ldap\_get\_next\_page**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_next_page)
-   [**ldap\_get\_next\_page\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_next_page_s)
-   [**ldap\_get\_paged\_count**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_paged_count)
-   [**ldap\_get\_values**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_values)
-   [**ldap\_get\_values\_len**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_values_len)
-   [**ldap\_parse\_extended\_result**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_extended_resulta)
-   [**ldap\_parse\_page\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_page_control)
-   [**ldap\_parse\_reference**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_reference)
-   [**ldap\_parse\_result**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_result)
-   [**ldap\_parse\_sort\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_sort_control)
-   [**ldap\_parse\_vlv\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_parse_vlv_controla)
-   [**ldap\_result**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_result)
-   [**ldap\_search**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search)
-   [**ldap\_search\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_s)
-   [**ldap\_search\_st**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_st)
-   [**ldap\_search\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext)
-   [**ldap\_search\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext_s)
-   [**ldap\_search\_init\_page**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_init_page)
-   [**ldap\_search\_abandon\_page**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_abandon_page)

## Error Handling

Use these functions to handle errors.

-   [**ldap\_err2string**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_err2string)
-   [**LdapGetLastError**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldapgetlasterror)
-   [**LdapMapErrorToWin32**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldapmaperrortowin32)
-   [**ldap\_result2error**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_result2error)

## Memory Management

Use these functions to explicitly free data structures when no longer required.

-   [**ldap\_control\_free**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_control_free)
-   [**ldap\_controls\_free**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_controls_free)
-   [**ldap\_memfree**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_memfree)
-   [**ldap\_msgfree**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_msgfree)
-   [**ldap\_value\_free**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_value_free)
-   [**ldap\_value\_free\_len**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_value_free_len)

## Miscellaneous Functions

Use these functions to convert the forms of distinguished names, modify entry names, convert text strings, and set debugging options.

-   [**ldap\_dn2ufn**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_dn2ufn)
-   [**ldap\_ufn2dn**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_ufn2dn)
-   [**ldap\_explode\_dn**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_explode_dn)
-   [**ldap\_get\_dn**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_get_dn)
-   [**ldap\_conn\_from\_msg**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_conn_from_msg)
-   [**ldap\_modrdn2**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_modrdn2)
-   [**ldap\_modrdn2\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_modrdn2_s)
-   [**ldap\_rename\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_rename_ext)
-   [**ldap\_rename\_ext\_s**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_rename_ext_s)
-   [**LdapUnicodeToUTF8**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldapunicodetoutf8)
-   [**LdapUTF8ToUnicode**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldaputf8tounicode)
-   [**ber\_init**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_init)
-   [**ber\_free**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_free)
-   [**ber\_bvfree**](/previous-versions/windows/desktop/api/winldap/nf-winber-ber_bvfree)
-   [**ber\_bvecfree**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_bvecfree)
-   [**ber\_bvdup**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_bvdup)
-   [**ber\_alloc\_t**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_alloc_t)
-   [**ber\_skip\_tag**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_skip_tag)
-   [**ber\_peek\_tag**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_peek_tag)
-   [**ber\_first\_element**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_first_element)
-   [**ber\_next\_element**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_next_element)
-   [**ber\_flatten**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_flatten)
-   [**ber\_printf**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_printf)
-   [**ber\_scanf**](/previous-versions/windows/desktop/api/Winber/nf-winber-ber_scanf)

 

 




