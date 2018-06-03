---
title: Sorting Search Results
description: When an LDAP client needs search results sorted and is not able or is unwilling to perform the sort itself, the client can request that the server do it.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: d5ac4ee8-0b90-46c3-b7aa-3bb710abd5e9
ms.prod: windows-server-dev
ms.technology: active-directory-lightweight-directory-services
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sorting Search Results

When an LDAP client needs search results sorted and is not able or is unwilling to perform the sort itself, the client can request that the server do it. The Sort control allows the client to give the server the information required to sort the result set.

The interaction between client and server is as follows.

The client sends the server a search request with the Sort control, which specifies the sort keys. Each sort key consists of an AttributeType, an Ordering Rule, and a flag that indicates whether entries are sorted in forward or reverse order. The server then tells the client whether the sorting operation is successful and returns entries.

Sort is indicated as a control on the [**ldap\_search\_ext**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_search_ext) function call. To construct this control, the API provides [**ldap\_create\_sort\_control**](/previous-versions/windows/desktop/api/Winldap/nf-winldap-ldap_create_sort_control). The control must then be added to the list of server controls in the **ldap\_search\_ext** call. When the server returns the results, it returns a control in the SearchResultDone message to reflect the success or failure of the search. The API provides **ldap\_parse\_search\_control** as a method of parsing the sort control as returned by the server in the SearchResultDone message.

Using sort and paged results together, The Paged Results draft \[3\] explicitly states that the search command that is used to get subsequent pages of the result set must have everything the same with the exception of the cookie on the control and the possible exception of the page size. Therefore, when sort and paged results are used together, the sort control must be set to the same value for every retrieval of a page of a given result set.

 

 




