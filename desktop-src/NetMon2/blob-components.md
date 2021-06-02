---
description: BLOB Components
ms.assetid: 757cd311-f834-4017-a0da-ff3f4bc49e7e
title: BLOB Components
ms.topic: article
ms.date: 05/31/2018
---

# BLOB Components

A binary large object (BLOB) includes the following hierarchical components:

-   Owners
-   Categories
-   Tags
-   Values

## Textual Representation

For convenience, BLOBs appear in the Owner:Category:Tag:Value format that they appear in when saved to a file. The internal structure of the BLOB is opaque because it represents pointers and tables. For example, here is an entry from a BLOB that can be used to configure an NPP:

``` syntax
NPP:Configure:BufferSize=32768
```

The Owner is NPP. The Category is Configure, the Tag is BufferSize, and the Value is 32768.

 

 



