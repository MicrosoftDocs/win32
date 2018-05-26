---
title: Router Information Functions
description: Use the following functions to manipulate router information headers and blocks. An information header is composed of private meta-data and information blocks. Information blocks are arrays of information structures of various types.
ms.assetid: e88720aa-080b-4d87-a442-1b436c256ca6
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Router Information Functions

Use the following functions to manipulate router information headers and blocks. An information header is composed of private meta-data and information blocks. Information blocks are arrays of [information structures](router-information-structures.md) of various [types](router-information-enumerations.md).

The following functions manipulate information headers:

-   [**MprInfoCreate**](/windows/win32/Mprapi/nf-mprapi-mprinfocreate?branch=master)
-   [**MprInfoDelete**](/windows/win32/Mprapi/nf-mprapi-mprinfodelete?branch=master)
-   [**MprInfoDuplicate**](/windows/win32/Mprapi/nf-mprapi-mprinfoduplicate?branch=master)
-   [**MprInfoRemoveAll**](/windows/win32/Mprapi/nf-mprapi-mprinforemoveall?branch=master)

The following functions manipulate information blocks within an information header:

-   [**MprInfoBlockAdd**](/windows/win32/Mprapi/nf-mprapi-mprinfoblockadd?branch=master)
-   [**MprInfoBlockFind**](/windows/win32/Mprapi/nf-mprapi-mprinfoblockfind?branch=master)
-   [**MprInfoBlockQuerySize**](/windows/win32/Mprapi/nf-mprapi-mprinfoblockquerysize?branch=master)
-   [**MprInfoBlockRemove**](/windows/win32/Mprapi/nf-mprapi-mprinfoblockremove?branch=master)
-   [**MprInfoBlockSet**](/windows/win32/Mprapi/nf-mprapi-mprinfoblockset?branch=master)

Many of the [router administration and configuration functions](understanding-mprinfo-functions-and-information-headers.md) use information headers.

 

 




