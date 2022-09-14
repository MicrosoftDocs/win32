---
title: Managing Property Sets
description: A persistent property set contains related data as properties.
ms.assetid: 19ff2751-87f3-43d8-9307-ce2dd399f694
keywords:
- Managing Property Sets
ms.topic: article
ms.date: 05/31/2018
---

# Managing Property Sets

A persistent property set contains related data as properties. Each property set is identified with an FMTID, and a globally unique identifier (GUID) that enables applications, accessing the property set, to identify the property set. Through this identification, the application interprets the properties that the set contains.

For example, the character-formatting properties in a word processor or the rendering attributes of an element in a drawing program are property sets.

COM defines the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface to facilitate management of property sets. Through the methods of this interface, you can create a new property set, or open or delete an existing property set. In addition, it provides a method that creates an enumerator and supplies a pointer to its [**IEnumSTATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) interface. You can call the methods of this interface to enumerate [**STATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) structures on your object, which will provide information about all of the property sets on the object.

When you create or open an instance of [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage), it is similar to opening an object that supports [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) or [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream), because you need to specify the storage mode in which you are opening the interface. For **IStorage**, these include the transaction mode, the read/write mode, and the sharing mode.

When you create a property set with a call to [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create), specify whether the property set is to be simple or nonsimple. A simple property set contains types that can be written fully within the property set stream, which is intended to be limited in size, and can be no larger than 256 KB in Windows NT 4.0 and earlier, or 1 MB in Windows 2000, Windows XP, and Windows Server 2003. However, when you need to store a larger amount of information in the property set, you can specify that the property set be nonsimple. This allows you to use one or more of the types that specify only a pointer to a storage or stream object. These types are VT\_STREAM, VT\_STREAMED OBJECT, VT\_STORAGE and VT\_STORED\_OBJECT.

Data stored in these properties is not counted against the 256 KB property-set size limit in Windows NT 4.0 or earlier, or the 1 MB limit in Windows 2000, Windows XP, and Windows Server 2003. However, data about the property, such as its name, does apply. Also, if you need a transacted update, the property set must be nonsimple. There is, of course, a certain performance penalty for opening these types, because it requires opening the stream or storage object to which you have the pointer.

If your application uses compound files, you can use the COM-provided implementation of these interfaces, which are implemented on the COM compound file storage object.

Each property set consists primarily of a logically connected group of properties, as described in [Managing Properties](managing-properties.md).

For more information about property sets in COM, see:

-   [Property Set Implementations in COM](property-set-implementations-in-com.md)
-   [Property Set Considerations](property-set-considerations.md)
-   [IPropertySetStorage Implementation Considerations](ipropertysetstorage-implementation-considerations.md)
-   [Storing Property Sets](storing-property-sets.md)
-   [Performance Characteristics](performance-characteristics.md)
-   [Implementing the Summary Information Property Set](implementing-the-summary-information-property-set.md)

 

 