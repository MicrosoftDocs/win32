---
title: Support Functions Reference
description: The following functions are provided to routing protocols by the router manager.
ms.assetid: 4e88c9fe-f6ec-4f9c-88b1-8726e10d0f6d
keywords:
- Routing Protocol Interface RRAS ,support functions
ms.topic: article
ms.date: 05/31/2018
---

# Support Functions Reference

The following functions are provided to routing protocols by the router manager. When the router manager calls the [**StartProtocol**](/windows/desktop/api/Routprot/nc-routprot-pstart_protocol) function (implemented by the routing protocol), the router manager passes the routing protocol a [**SUPPORT\_FUNCTIONS**](/windows/desktop/api/Routprot/ns-routprot-support_functions_50) structure containing pointers to these functions:

[**DemandDialRequest**](https://msdn.microsoft.com/en-us/library/Aa373924(v=VS.85).aspx)

[**MIBEntryCreate**](https://msdn.microsoft.com/en-us/library/Aa374538(v=VS.85).aspx)

[**MIBEntryDelete**](https://msdn.microsoft.com/en-us/library/Aa374539(v=VS.85).aspx)

[**MIBEntryGet**](https://msdn.microsoft.com/en-us/library/Aa374540(v=VS.85).aspx)

[**MIBEntryGetFirst**](https://msdn.microsoft.com/en-us/library/Aa374541(v=VS.85).aspx)

[**MIBEntryGetNext**](https://msdn.microsoft.com/en-us/library/Aa374542(v=VS.85).aspx)

[**MIBEntrySet**](https://msdn.microsoft.com/en-us/library/Aa374543(v=VS.85).aspx)

[**SetInterfaceReceiveType**](https://msdn.microsoft.com/en-us/library/Aa382181(v=VS.85).aspx)

[**ValidateRoute**](https://msdn.microsoft.com/en-us/library/Aa382342(v=VS.85).aspx)

 

 




