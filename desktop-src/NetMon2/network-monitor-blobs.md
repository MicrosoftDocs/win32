---
description: The Network Monitor binary large object (BLOB) is a generic data structure that contains configuration and location information of network interface cards (NICs).
ms.assetid: 910bf929-aa89-434d-83c3-07c80c627405
title: Network Monitor BLOBs
ms.topic: article
ms.date: 05/31/2018
---

# Network Monitor BLOBs

The Network Monitor binary large object (BLOB) is a generic data structure that contains configuration and location information of network interface cards (NICs). Use BLOBs to represent NICs and to filter entries in a list of NICs. BLOBS can also contain application-specific data without affecting the other data that they hold. BLOB implementation is opaque to all levels that must access BLOBs with BLOB APIs.

## BLOB Structure

A BLOB can be considered as a hierarchical tree used to designate strings. This tree has three layers: Owner, Category, and Tag. Owner is a string that indicates, in general, who reads an entry. The Category is also a string, which designates a general functional grouping of tags under the owner. The Tag is the actual name of the entry.

The structural characteristics of BLOBs include:

-   BLOB helpers within one process are protected from one another by a mutex built into each BLOB.
-   Each BLOB has an internal version number so that the helpers can handle both present and future BLOB forms. Version conflicts may occur if you send a BLOB to another computer via a remote procedure call.
-   The BLOB itself is a pointer to a void. Be aware that applications should allocate BLOBs with the **const** modifier to avoid altering the contents.
-   Each of the designators, as well as their values, are strings. Be aware that the strings returned by **GetString** functions are actually pointers into the BLOB and should not be changed. For this reason, these strings must be specified as **const char***\*pX* to keep applications from accidentally changing them.

In general, all parameters with the **const** designator encourage the caller to refrain from changing the values rather than prohibit the helper functions from changing them. In fact, the helper functions will usually change those values.

 

 



