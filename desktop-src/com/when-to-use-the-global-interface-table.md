---
title: When to Use the Global Interface Table
description: When to Use the Global Interface Table
ms.assetid: def8f7f8-9d0d-49a4-9d5c-40233903eea5
ms.topic: article
ms.date: 05/31/2018
---

# When to Use the Global Interface Table

If you are unmarshaling an interface pointer multiple times between apartments in a process, you might use the [**IGlobalInterfaceTable**](/windows/desktop/api/ObjIdl/nn-objidl-iglobalinterfacetable) interface. With other techniques, you would have to remarshal each time.

> [!Note]  
> If the interface pointer is unmarshaled only once, you may want to use the [**CoMarshalInterThreadInterfaceInStream**](/windows/desktop/api/combaseapi/nf-combaseapi-comarshalinterthreadinterfaceinstream) function. It can also be used to pass an interface pointer from one thread to another thread in the same process.

 

The [**IGlobalInterfaceTable**](/windows/desktop/api/ObjIdl/nn-objidl-iglobalinterfacetable) interface also makes another previously difficult problem simpler for the programmer. This problem occurs when the following conditions apply:

-   An in-process agile object aggregates the free-threaded marshaler.
-   This same agile object also holds (as member variables) interface pointers to other objects that are not agile and do not aggregate the free-threaded marshaler.

In this situation, if the outer object gets marshaled to another apartment and the application calls on it, and the object tries to call on any of its member variable interface pointers that are not free-threaded or are proxies to objects in other apartments, it might get incorrect results or the error RPC\_E\_WRONG\_THREAD. This error occurs because the inner interface is designed to be callable only from the apartment in which it was first stored in the member variable.

To solve this problem, the outer object aggregating the free-threaded marshaler should call [**IGlobalInterfaceTable::RegisterInterfaceInGlobal**](/windows/win32/api/objidl/nf-objidl-iglobalinterfacetable-registerinterfaceinglobal) on the inner interface and store the resulting cookie in its member variable, instead of storing the actual interface pointer. When the outer object wants to call on an inner object's interface pointer, it should call [**IGlobalInterfaceTable::GetInterfaceFromGlobal**](/windows/win32/api/objidl/nf-objidl-iglobalinterfacetable-getinterfacefromglobal), use the returned interface pointer, and then release it. When the outer object goes away, it should call [**IGlobalInterfaceTable::RevokeInterfaceFromGlobal**](/windows/win32/api/objidl/nf-objidl-iglobalinterfacetable-revokeinterfacefromglobal) to remove the interface from the global interface table.

## Related topics

<dl> <dt>

[Creating the Global Interface Table](creating-the-global-interface-table.md)
</dt> </dl>

 

 