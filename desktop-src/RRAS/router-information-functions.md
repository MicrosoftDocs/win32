---
title: Router Information Functions
description: Use the following functions to manipulate router information headers and blocks. An information header is composed of private meta-data and information blocks. Information blocks are arrays of information structures of various types.
ms.assetid: e88720aa-080b-4d87-a442-1b436c256ca6
ms.topic: article
ms.date: 05/31/2018
---

# Router Information Functions

Use the following functions to manipulate router information headers and blocks. An information header is composed of private meta-data and information blocks. Information blocks are arrays of [information structures](router-information-structures.md) of various [types](router-information-enumerations.md).

The following functions manipulate information headers:

-   [**MprInfoCreate**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfocreate)
-   [**MprInfoDelete**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfodelete)
-   [**MprInfoDuplicate**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoduplicate)
-   [**MprInfoRemoveAll**](/windows/desktop/api/Mprapi/nf-mprapi-mprinforemoveall)

The following functions manipulate information blocks within an information header:

-   [**MprInfoBlockAdd**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockadd)
-   [**MprInfoBlockFind**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockfind)
-   [**MprInfoBlockQuerySize**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockquerysize)
-   [**MprInfoBlockRemove**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockremove)
-   [**MprInfoBlockSet**](/windows/desktop/api/Mprapi/nf-mprapi-mprinfoblockset)

Many of the [router administration and configuration functions](understanding-mprinfo-functions-and-information-headers.md) use information headers.

 

 




