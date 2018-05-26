---
title: Property Set Implementations in COM
description: Property Set Implementations in COM
ms.assetid: 52d7b534-f81a-4cc9-b5ea-9538bfff056c
keywords:
- Structured Storage Strctd Stg ,using,property set uses in COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Property Set Implementations in COM

While the potential for uses of persistent property sets is not fully tapped, there are currently two primary uses:

-   Storing summary information with an object such as a document
-   Transferring property data between objects

COM property sets were designed to store data that is suited to representation as a moderately sized collection of fine-grained values. Data sets that are too large for this to be feasible should be broken into separate streams, storages, and/or property sets. The COM property set data format was not meant to provide a substitute for a database of many tiny objects.

COM provides implementations of the property set interfaces for various objects, along with three helper functions. The following section describes some performance characteristics of these implementations. For more information on specific interfaces and how to get a pointer to these interfaces, refer to the following in the COM reference section:

-   [IPropertySetStorage–Compound File Implementation](ipropertysetstorage-compound-file-implementation.md)

    The compound file implementation, which provides the [**IStorage**](/windows/win32/Objidl/nn-objidl-istorage?branch=master) and [**IStream**](/windows/win32/Objidl/nn-objidl-istream?branch=master) interfaces, also provides the [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) and [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) interfaces. Given a compound file implementation of **IStorage**, the **IPropertySetStorage** interface can be obtained by calling [**IUnknown::QueryInterface**](_com_iunknown_queryinterface).

-   [IPropertySetStorage–NTFS File System Implementation](ipropertysetstorage-ntfs-file-system-implementation.md)

    The [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) and [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) interfaces can also be obtained for NTFS files that are not compound files. Therefore, it is possible to obtain these interfaces for all files on an NTFS volume.

-   [IPropertySetStorage–Stand-alone Implementation](ipropertysetstorage-stand-alone-implementation.md)

    When this implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) and [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) is instantiated, it is given a pointer to an object that supports the [**IStorage**](/windows/win32/Objidl/nn-objidl-istorage?branch=master) interface. It then manipulates property set storages within that storage object. Thus, it is possible to access and manipulate property sets on any object that supports .

-   [IPropertySetStorage Implementation Considerations](ipropertysetstorage-implementation-considerations.md)

    There are several issues to consider in providing an implementation of the [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) interface. Please refer to these *Implementation Considerations* in the COM Reference section.

In addition, there are four helper functions, designed to aid in dealing with properties that have been read from a property set into memory (into a [**PROPVARIANT**](/windows/win32/propidlbase/ns-propidl-tagpropvariant?branch=master) structure):

-   [**PropVariantInit**](/windows/win32/PropIdl/nf-propidl-propvariantinit?branch=master)
-   [**PropVariantClear**](/windows/win32/Propidl/nf-combaseapi-propvariantclear?branch=master)
-   [**FreePropVariantArray**](/windows/win32/Propidl/nf-combaseapi-freepropvariantarray?branch=master)
-   [**PropVariantCopy**](/windows/win32/Propidl/nf-combaseapi-propvariantcopy?branch=master)

The following sections discuss property set implementations in COM in greater detail:

-   [Managing Property Sets](managing-property-sets.md)
-   [Property Set Considerations](property-set-considerations.md)
-   [Storing Property Sets](storing-property-sets.md)
-   [Performance Characteristics](performance-characteristics.md)
-   [Implementing the Summary Information Property Set](implementing-the-summary-information-property-set.md)
-   [IPropertySetStorage Implementation Considerations](ipropertysetstorage-implementation-considerations.md)

 

 




