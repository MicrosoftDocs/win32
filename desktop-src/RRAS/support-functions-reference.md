---
title: Support Functions Reference
description: The following functions are provided to routing protocols by the router manager.
ms.assetid: 4e88c9fe-f6ec-4f9c-88b1-8726e10d0f6d
keywords:
- Routing Protocol Interface RRAS ,support functions
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Support Functions Reference

The following functions are provided to routing protocols by the router manager. When the router manager calls the [**StartProtocol**](/windows/desktop/api/Routprot/nc-routprot-pstart_protocol) function (implemented by the routing protocol), the router manager passes the routing protocol a [**SUPPORT\_FUNCTIONS**](/windows/desktop/api/Routprot/ns-routprot-_support_functions_50) structure containing pointers to these functions:

[**DemandDialRequest**](https://www.bing.com/search?q=**DemandDialRequest**)

[**MIBEntryCreate**](https://www.bing.com/search?q=**MIBEntryCreate**)

[**MIBEntryDelete**](https://www.bing.com/search?q=**MIBEntryDelete**)

[**MIBEntryGet**](https://www.bing.com/search?q=**MIBEntryGet**)

[**MIBEntryGetFirst**](https://www.bing.com/search?q=**MIBEntryGetFirst**)

[**MIBEntryGetNext**](https://www.bing.com/search?q=**MIBEntryGetNext**)

[**MIBEntrySet**](https://www.bing.com/search?q=**MIBEntrySet**)

[**SetInterfaceReceiveType**](https://www.bing.com/search?q=**SetInterfaceReceiveType**)

[**ValidateRoute**](https://www.bing.com/search?q=**ValidateRoute**)

 

 




