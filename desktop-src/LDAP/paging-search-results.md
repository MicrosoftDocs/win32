---
title: Paging Search Results
description: When an LDAP client is accessing a server across a slow connection, or if the client suspects that the result set from a given query may be very large, the client should be able to retrieve a result set in small pieces.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\mbaldwin
ms.assetid: 'bf19f427-c7b0-43d6-9bd8-44010c297804'
ms.prod: 'windows-server-dev'
ms.technology: 'active-directory-lightweight-directory-services'
ms.tgt_platform: multiple
---

# Paging Search Results

When an LDAP client is accessing a server across a slow connection, or if the client suspects that the result set from a given query may be very large, the client should be able to retrieve a result set in small pieces. The Simple Paged Result extended control allows this type of retrieval by allowing a one-way walk through a result set. Options on this control allow the client to set the initial page size and reset the page size with each subsequent request to the server.

The Simple Paged Result control is also used to access all of a large results set when there is a server-side administrative limit to the number of items returned from a query. For example, Active Directory servers have a default server-side limit of 1000 entries as the maximum number of results that are returned in a single request. If the results of a query exceed this limit, the Paged Results control is used with a page size equal to or less than the server-side limit in order to retrieve all of the results of the query.

The interaction between client and server is as follows.

The client sends the server a search request with the Simple Paged Results control with an empty previous Enumeration Key, also known as a cookie, and the initial page size. The server then returns the number of entries specified by the page size and also returns a cookie used on the next client request to get the next page of results. The client then issues a search with the cookie included (optionally resetting the page size) and the server then responds with up to that number of entries.

Paged results are indicated as a control on the [**ldap\_search\_ext**](ldap-search-ext.md) function call. Use [**ldap\_create\_page\_control**](ldap-create-page-control.md) to construct this control, and then call **ldap\_search\_ext** to add the control. This control structure must then be added to the list of server controls in the **ldap\_search\_ext** call. When the server returns the first page of results, it includes the resume cookie in the controls field of the SearchResultDone message. The client must then extract the cookie from the search result by retrieving the server controls by using [**ldap\_parse\_result**](ldap-parse-result.md) and parsing the control with [**ldap\_parse\_page\_control**](ldap-parse-page-control.md). The client then uses the cookie in the next call to **LDAP\_create\_page\_control** to retrieve the next page of results.

 

 




