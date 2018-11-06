---
title: Providing Class Information
description: Providing Class Information
ms.assetid: 808d9a39-4511-4aba-a23f-3c929970503b
ms.topic: article
ms.date: 05/31/2018
---

# Providing Class Information

It is often useful for a client of an object to examine the object's type information. Given the object's CLSID, a client can locate the object's type library using registry entries and then can scan the type library for the coclass entry in the library matching the CLSID.

However, not all objects have a CLSID, although they still need to provide type information. In addition, it is convenient for a client to have a way to simply ask an object for its type information instead of going through all the tedium to extract the same information from registry entries. This capability is important when dealing with outgoing interfaces on connectable objects. (See [Using IProvideClassInfo](using-iprovideclassinfo.md) for more information on how connectable objects provide this capability.)

In these cases, a client can query the object for [**IProvideClassInfo**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo) or [**IProvideClassInfo2**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo2). If these interfaces exist, the client calls the [**GetClassInfo**](/windows/desktop/api/OCIdl/nf-ocidl-iprovideclassinfo-getclassinfo) method to get the type information for the interface.

By implementing [**IProvideClassInfo**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo) or [**IProvideClassInfo2**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo2), an object specifies that it can provide type information for its entire class; that is, what it would describe in its coclass section of its type library, if it has one. [**GetClassInfo**](/windows/desktop/api/OCIdl/nf-ocidl-iprovideclassinfo-getclassinfo) returns an **ITypeInfo** pointer corresponding to the object's coclass information. Through this **ITypeInfo** pointer, the client can examine all the object's incoming and outgoing interface definitions.

The object can also provide [**IProvideClassInfo2**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo2). The **IProvideClassInfo2** interface is a simple extension to [**IProvideClassInfo**](/windows/desktop/api/OCIdl/nn-ocidl-iprovideclassinfo) that makes it quick and easy to retrieve an object's outgoing interface identifiers for its default event set. **IProvideClassInfo2** is derived from **IProvideClassInfo**.

## Related topics

<dl> <dt>

[COM Clients and Servers](com-clients-and-servers.md)
</dt> </dl>

 

 




