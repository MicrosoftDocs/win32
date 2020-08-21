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

[**DemandDialRequest**](/previous-versions/windows/desktop/legacy/aa373924(v=vs.85))

[**MIBEntryCreate**](/previous-versions/windows/desktop/legacy/aa374538(v=vs.85))

[**MIBEntryDelete**](/previous-versions/windows/desktop/legacy/aa374539(v=vs.85))

[**MIBEntryGet**](/previous-versions/windows/desktop/legacy/aa374540(v=vs.85))

[**MIBEntryGetFirst**](/previous-versions/windows/desktop/legacy/aa374541(v=vs.85))

[**MIBEntryGetNext**](/previous-versions/windows/desktop/legacy/aa374542(v=vs.85))

[**MIBEntrySet**](/previous-versions/windows/desktop/legacy/aa374543(v=vs.85))

[**SetInterfaceReceiveType**](/previous-versions/windows/desktop/legacy/aa382181(v=vs.85))

[**ValidateRoute**](/previous-versions/windows/desktop/legacy/aa382342(v=vs.85))

 

 