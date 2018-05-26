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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Functions

This section describes the API functions supported in LDAP 2 and 3. The table of contents lists the functions in alphabetical order. The following functions are grouped by task.

## Starting and Stopping an LDAP Session

Use these functions to initialize and open a connection block, authenticate a client to a server, set options for the LDAP session, and close a session.

-   [**cldap\_open**](/windows/previous-versions/Winldap/nf-winldap-cldap_open?branch=master)
-   [**ldap\_open**](/windows/previous-versions/Winldap/nf-winldap-ldap_open?branch=master)
-   [**ldap\_bind**](/windows/previous-versions/Winldap/nf-winldap-ldap_bind?branch=master)
-   [**ldap\_bind\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_bind_s?branch=master)
-   [**ldap\_simple\_bind**](/windows/previous-versions/Winldap/nf-winldap-ldap_simple_bind?branch=master)
-   [**ldap\_simple\_bind\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_simple_bind_s?branch=master)
-   [**ldap\_sasl\_bind**](/windows/previous-versions/Winldap/nf-winldap-ldap_sasl_binda?branch=master)
-   [**ldap\_sasl\_bind\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_sasl_bind_sa?branch=master)
-   [**ldap\_connect**](/windows/previous-versions/Winldap/nf-winldap-ldap_connect?branch=master)
-   [**ldap\_init**](/windows/previous-versions/Winldap/nf-winldap-ldap_init?branch=master)
-   [**ldap\_sslinit**](/windows/previous-versions/Winldap/nf-winldap-ldap_sslinit?branch=master)
-   [**ldap\_get\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_option?branch=master)
-   [**ldap\_set\_option**](/windows/previous-versions/Winldap/nf-winldap-ldap_set_option?branch=master)
-   [**ldap\_abandon**](/windows/previous-versions/Winldap/nf-winldap-ldap_abandon?branch=master)
-   [**ldap\_unbind**](/windows/previous-versions/Winldap/nf-winldap-ldap_unbind?branch=master)
-   [**ldap\_unbind\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_unbind_s?branch=master)
-   [**ldap\_cleanup**](/windows/previous-versions/Winldap/nf-winldap-ldap_cleanup?branch=master)

## Modifying Directory Entries

Use these functions to perform operations on directory entries.

-   [**ldap\_add**](/windows/previous-versions/Winldap/nf-winldap-ldap_add?branch=master)
-   [**ldap\_add\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_add_ext?branch=master)
-   [**ldap\_add\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_add_s?branch=master)
-   [**ldap\_add\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_add_ext_s?branch=master)
-   [**ldap\_compare**](/windows/previous-versions/Winldap/nf-winldap-ldap_compare?branch=master)
-   [**ldap\_compare\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_compare_ext?branch=master)
-   [**ldap\_compare\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_compare_s?branch=master)
-   [**ldap\_compare\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_compare_ext_s?branch=master)
-   [**ldap\_delete**](/windows/previous-versions/Winldap/nf-winldap-ldap_delete?branch=master)
-   [**ldap\_delete\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_delete_ext?branch=master)
-   [**ldap\_delete\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_delete_s?branch=master)
-   [**ldap\_delete\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_delete_ext_s?branch=master)
-   [**ldap\_extended\_operation\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_extended_operation_sa?branch=master)
-   [**ldap\_extended\_operation**](/windows/previous-versions/Winldap/nf-winldap-ldap_extended_operation?branch=master)
-   [**ldap\_close\_extended\_op**](/windows/previous-versions/Winldap/nf-winldap-ldap_close_extended_op?branch=master)
-   [**ldap\_modify**](/windows/previous-versions/Winldap/nf-winldap-ldap_modify?branch=master)
-   [**ldap\_modify\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_modify_ext?branch=master)
-   [**ldap\_modify\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_modify_s?branch=master)
-   [**ldap\_modify\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_modify_ext_s?branch=master)

## Searching, Sorting, and Result Handling

Use these functions to search a directory or sort and parse results, with or without controls.

-   [**ldap\_check\_filter**](/windows/previous-versions/Winldap/nf-winldap-ldap_check_filtera?branch=master)
-   [**ldap\_count\_entries**](/windows/previous-versions/Winldap/nf-winldap-ldap_count_entries?branch=master)
-   [**ldap\_count\_references**](/windows/previous-versions/Winldap/nf-winldap-ldap_count_references?branch=master)
-   [**ldap\_count\_values**](/windows/previous-versions/Winldap/nf-winldap-ldap_count_values?branch=master)
-   [**ldap\_count\_values\_len**](/windows/previous-versions/Winldap/nf-winldap-ldap_count_values_len?branch=master)
-   [**ldap\_create\_page\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_create_page_control?branch=master)
-   [**ldap\_create\_sort\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_create_sort_control?branch=master)
-   [**ldap\_create\_vlv\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_create_vlv_controla?branch=master)
-   [**ldap\_encode\_sort\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_encode_sort_control?branch=master)
-   [**ldap\_escape\_filter\_element**](/windows/previous-versions/Winldap/nf-winldap-ldap_escape_filter_element?branch=master)
-   [**ldap\_first\_attribute**](/windows/previous-versions/Winldap/nf-winldap-ldap_first_attribute?branch=master)
-   [**ldap\_next\_attribute**](/windows/previous-versions/Winldap/nf-winldap-ldap_next_attribute?branch=master)
-   [**ldap\_first\_entry**](/windows/previous-versions/Winldap/nf-winldap-ldap_first_entry?branch=master)
-   [**ldap\_next\_entry**](/windows/previous-versions/Winldap/nf-winldap-ldap_next_entry?branch=master)
-   [**ldap\_first\_reference**](/windows/previous-versions/Winldap/nf-winldap-ldap_first_reference?branch=master)
-   [**ldap\_next\_reference**](/windows/previous-versions/Winldap/nf-winldap-ldap_next_reference?branch=master)
-   [**ldap\_get\_next\_page**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_next_page?branch=master)
-   [**ldap\_get\_next\_page\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_next_page_s?branch=master)
-   [**ldap\_get\_paged\_count**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_paged_count?branch=master)
-   [**ldap\_get\_values**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_values?branch=master)
-   [**ldap\_get\_values\_len**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_values_len?branch=master)
-   [**ldap\_parse\_extended\_result**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_extended_resulta?branch=master)
-   [**ldap\_parse\_page\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_page_control?branch=master)
-   [**ldap\_parse\_reference**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_reference?branch=master)
-   [**ldap\_parse\_result**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_result?branch=master)
-   [**ldap\_parse\_sort\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_sort_control?branch=master)
-   [**ldap\_parse\_vlv\_control**](/windows/previous-versions/Winldap/nf-winldap-ldap_parse_vlv_controla?branch=master)
-   [**ldap\_result**](/windows/previous-versions/Winldap/nf-winldap-ldap_result?branch=master)
-   [**ldap\_search**](/windows/previous-versions/Winldap/nf-winldap-ldap_search?branch=master)
-   [**ldap\_search\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_s?branch=master)
-   [**ldap\_search\_st**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_st?branch=master)
-   [**ldap\_search\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext?branch=master)
-   [**ldap\_search\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_ext_s?branch=master)
-   [**ldap\_search\_init\_page**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_init_page?branch=master)
-   [**ldap\_search\_abandon\_page**](/windows/previous-versions/Winldap/nf-winldap-ldap_search_abandon_page?branch=master)

## Error Handling

Use these functions to handle errors.

-   [**ldap\_err2string**](/windows/previous-versions/Winldap/nf-winldap-ldap_err2string?branch=master)
-   [**LdapGetLastError**](/windows/previous-versions/Winldap/nf-winldap-ldapgetlasterror?branch=master)
-   [**LdapMapErrorToWin32**](/windows/previous-versions/Winldap/nf-winldap-ldapmaperrortowin32?branch=master)
-   [**ldap\_result2error**](/windows/previous-versions/Winldap/nf-winldap-ldap_result2error?branch=master)

## Memory Management

Use these functions to explicitly free data structures when no longer required.

-   [**ldap\_control\_free**](/windows/previous-versions/Winldap/nf-winldap-ldap_control_free?branch=master)
-   [**ldap\_controls\_free**](/windows/previous-versions/Winldap/nf-winldap-ldap_controls_free?branch=master)
-   [**ldap\_memfree**](/windows/previous-versions/Winldap/nf-winldap-ldap_memfree?branch=master)
-   [**ldap\_msgfree**](/windows/previous-versions/Winldap/nf-winldap-ldap_msgfree?branch=master)
-   [**ldap\_value\_free**](/windows/previous-versions/Winldap/nf-winldap-ldap_value_free?branch=master)
-   [**ldap\_value\_free\_len**](/windows/previous-versions/Winldap/nf-winldap-ldap_value_free_len?branch=master)

## Miscellaneous Functions

Use these functions to convert the forms of distinguished names, modify entry names, convert text strings, and set debugging options.

-   [**ldap\_dn2ufn**](/windows/previous-versions/Winldap/nf-winldap-ldap_dn2ufn?branch=master)
-   [**ldap\_ufn2dn**](/windows/previous-versions/Winldap/nf-winldap-ldap_ufn2dn?branch=master)
-   [**ldap\_explode\_dn**](/windows/previous-versions/Winldap/nf-winldap-ldap_explode_dn?branch=master)
-   [**ldap\_get\_dn**](/windows/previous-versions/Winldap/nf-winldap-ldap_get_dn?branch=master)
-   [**ldap\_conn\_from\_msg**](/windows/previous-versions/Winldap/nf-winldap-ldap_conn_from_msg?branch=master)
-   [**ldap\_modrdn2**](/windows/previous-versions/Winldap/nf-winldap-ldap_modrdn2?branch=master)
-   [**ldap\_modrdn2\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_modrdn2_s?branch=master)
-   [**ldap\_rename\_ext**](/windows/previous-versions/Winldap/nf-winldap-ldap_rename_ext?branch=master)
-   [**ldap\_rename\_ext\_s**](/windows/previous-versions/Winldap/nf-winldap-ldap_rename_ext_s?branch=master)
-   [**LdapUnicodeToUTF8**](/windows/previous-versions/Winldap/nf-winldap-ldapunicodetoutf8?branch=master)
-   [**LdapUTF8ToUnicode**](/windows/previous-versions/Winldap/nf-winldap-ldaputf8tounicode?branch=master)
-   [**ber\_init**](/windows/previous-versions/Winber/nf-winber-ber_init?branch=master)
-   [**ber\_free**](/windows/previous-versions/Winber/nf-winber-ber_free?branch=master)
-   [**ber\_bvfree**](/windows/previous-versions/winldap/nf-winber-ber_bvfree?branch=master)
-   [**ber\_bvecfree**](/windows/previous-versions/Winber/nf-winber-ber_bvecfree?branch=master)
-   [**ber\_bvdup**](/windows/previous-versions/Winber/nf-winber-ber_bvdup?branch=master)
-   [**ber\_alloc\_t**](/windows/previous-versions/Winber/nf-winber-ber_alloc_t?branch=master)
-   [**ber\_skip\_tag**](/windows/previous-versions/Winber/nf-winber-ber_skip_tag?branch=master)
-   [**ber\_peek\_tag**](/windows/previous-versions/Winber/nf-winber-ber_peek_tag?branch=master)
-   [**ber\_first\_element**](/windows/previous-versions/Winber/nf-winber-ber_first_element?branch=master)
-   [**ber\_next\_element**](/windows/previous-versions/Winber/nf-winber-ber_next_element?branch=master)
-   [**ber\_flatten**](/windows/previous-versions/Winber/nf-winber-ber_flatten?branch=master)
-   [**ber\_printf**](/windows/previous-versions/Winber/nf-winber-ber_printf?branch=master)
-   [**ber\_scanf**](/windows/previous-versions/Winber/nf-winber-ber_scanf?branch=master)

 

 




