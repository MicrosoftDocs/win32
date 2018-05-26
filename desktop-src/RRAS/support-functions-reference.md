---
title: Support Functions Reference
description: The following functions are provided to routing protocols by the router manager.
ms.assetid: 4e88c9fe-f6ec-4f9c-88b1-8726e10d0f6d
keywords:
- Routing Protocol Interface RRAS ,support functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Support Functions Reference

The following functions are provided to routing protocols by the router manager. When the router manager calls the [**StartProtocol**](/windows/win32/Routprot/nc-routprot-pstart_protocol?branch=master) function (implemented by the routing protocol), the router manager passes the routing protocol a [**SUPPORT\_FUNCTIONS**](/windows/win32/Routprot/ns-routprot-_support_functions_50?branch=master) structure containing pointers to these functions:

[**DemandDialRequest**](demanddialrequest.md)

[**MIBEntryCreate**](mibentrycreate.md)

[**MIBEntryDelete**](mibentrydelete.md)

[**MIBEntryGet**](mibentryget.md)

[**MIBEntryGetFirst**](mibentrygetfirst.md)

[**MIBEntryGetNext**](mibentrygetnext.md)

[**MIBEntrySet**](mibentryset.md)

[**SetInterfaceReceiveType**](setinterfacereceivetype.md)

[**ValidateRoute**](validateroute.md)

 

 




