---
title: Searching with the LDAP VLV Control
description: Active Directory supports the LDAP virtual list view (VLV) control.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: b2b03021-7e6a-413b-8e0a-df037d9a71de
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
keywords:
- Searching with the LDAP VLV Control
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Searching with the LDAP VLV Control

Active Directory supports the LDAP virtual list view (VLV) control. This enables a client to specify that the server return, for a given LDAP search, a contiguous subset of a large search result set. The advantage of using the VLV control is that it allows the client to retrieve results more quickly and prevents the client from needing to store too many search results at a time. To the user who views the virtual list in an application, even though he may see only ten entries at a time, it appears that the entire result set has been retrieved, because the entries in the result set are updated to reflect user interaction such as scrolling through the list, entering a word or letter to scroll to, or using arrow keys.

An example of an application that might require a virtual list would be an email address book application that displays a list of all the names of people with email accounts at a large university. The list is sorted alphabetically. While there may be tens of thousands of entries in this list, the address book list window displays only 20 accounts at any one time.

The LDAP VLV control extends a regular LDAP search operation to provide this functionality.

A VLV search must include a server-side sorting control. When the sort control is used with the VLV control, the server does not return the complete set of sorted search results, but instead, it returns a contiguous subset of those entries specified in the VLV control, using a target entry as a reference point for results.

The sort control may contain any sort specification valid for the server. You will choose the attributes that will be used for the search in the **sk\_attrtype** member of the [**LDAPSortKey**](/windows/previous-versions/Winldap/ns-winldap-ldapsortkeya?branch=master) structure. For example, in the address book scenario, you would set **sk\_attrtype** to "name".

The desired target entry, and the number of entries to be returned both before and after the target entry are determined by the client's [LDAP\_CONTROL\_VLVREQUEST](ldap-control-vlvrequest.md) control.

When the server returns the set of entries to the client, it attaches a [LDAP\_CONTROL\_VLVRESPONSE](ldap-control-vlvresponse.md) control to the **SearchResultDone** message that it returns to the client after it has received the last entry that it has calculated to belong to the requested subset. The server returns the following data in the LDAP\_CONTROL\_VLVRESPONSE control: the current server estimate for the list content count, a numeric value for the list position of the target entry (for example, the hundredth entry would be 100), and any LDAP server-side error codes. The server also returns a cookie to the client, which can in turn use the cookie in subsequent VLV search requests to improve efficiency.

 

 




