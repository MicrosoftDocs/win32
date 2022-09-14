---
title: What Makes a Fast Query
description: This topic lists preferred programming methods to use while querying a directory.
ms.assetid: d96f330f-3c57-4edc-9fd2-970f908b54c2
ms.tgt_platform: multiple
keywords:
- What Makes a Fast Query ADSI
- queries ADSI , what makes a fast query
ms.topic: article
ms.date: 05/31/2018
---

# What Makes a Fast Query?

Consider the following performance enhancement concepts when executing a query:

-   If possible, filter on indexed attributes only. Use index attributes that you expect will generate the fewest number of hits. For more information and a comprehensive list of indexed attributes for Windows, see [Active Directory Schema](/windows/desktop/ADSchema/active-directory-schema).
-   Search on **objectCategory** instead of **objectClass** because **objectClass** is not an indexed property.
-   Be aware of referrals. Consider searching the global catalog if your attributes are listed as GC replicated.
-   Avoid searching for text in the middle and at the end of a string. For example, "cn=\*hille\*" or "cn=\*larouse".
-   Assume that a subtree search will return a large result set. Use paging when performing subtree searches. The server will then be able to stream a large result set in chunks reducing the server-side memory resources. This effectively flattens out network usage and reduces the need for sending extremely large chunks of data over the network.
-   Properly scope your searches so as to not retrieve more than is necessary.
-   Perform a complex search on multiple attributes, because it is less performance intensive than performing multiple searches. One search for an object that reads two attributes is more efficient than two searches for the same object, each returning one attribute.
-   For reading attribute with a large number of values, use range limits to minimize the search size so that you can read a few thousand members at a time. For more information about specifying attribute range limits, see [Attribute Range Retrieval](attribute-range-retrieval.md).
-   Bind to an object hold the binding handle for the remainder of your session. Do not bind and unbind for each call. If you are using ADO or OLE DB, do not create many connection objects.
-   Read the rootDSE once and remember its contents for the remainder of your session.

 

 