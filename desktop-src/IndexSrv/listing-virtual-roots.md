---
title: Listing Virtual Roots
description: Listing Virtual Roots
ms.assetid: '9a85c709-7340-4b0a-af9f-f02a203285c7'
---

# Listing Virtual Roots

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Using Indexing Service with IIS, you can specify a list of virtual roots that are indexed for the Web catalog.

To retrieve a list of virtual roots and their indexed state, you need only execute a special query. The results are returned in the same manner as a standard query results page, and can be formatted using standard .htx templates. To retrieve the list of virtual roots, set the [CiScope](variables-in-forms-and-in-idq-files.md#-idxs-ciscope-var) parameter in an .idq file to be the string: VIRTUAL\_ROOTS. The .idq syntax requires that [CiRestriction](variables-in-forms-and-in-idq-files.md#-idxs-cirestriction-var) be set to a non-null value, but a restriction such as \#vpath **\*** can be used to retrieve all roots.

The properties that can be retrieved from this query are all the standard file properties (path, virtual path, and so on) of the directory to which the virtual root maps: metavrootused. This Boolean value is set to TRUE if the root is indexed, FALSE if it is not.

You can determine the type of a virtual root while making the VIRTUAL\_ROOTS query. Look at the value of the special property StorageType—(DBTYPE\_UI4) = b725f130-47ef-101a-a5f1-02608c9eebac 4. The value zero identifies a Web root. The value one identifies a news root.

 

 




