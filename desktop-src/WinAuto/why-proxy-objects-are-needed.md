---
title: Why Proxy Objects Are Needed
description: With accessible objects, when a client sets an in-context hook function, the DLL in which the client's hook function is implemented is loaded into the server's address space.
ms.assetid: e8e93271-1da6-42cd-9200-23a3e08b490b
ms.topic: article
ms.date: 05/31/2018
---

# Why Proxy Objects Are Needed

With accessible objects, when a client sets an [in-context hook function](in-context-and-out-of-context-hook-functions.md), the DLL in which the client's hook function is implemented is loaded into the server's address space. In this case, when the client calls [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent) from within the hook function, the interface pointer that is returned points directly to code in the server's address space. When the client calls an interface property using this pointer, the Component Object Model (COM) library is not involved with marshaling or unmarshaling and cannot detect if an object is destroyed. Therefore, the server must detect this situation and return an error code to the client.

 

 




