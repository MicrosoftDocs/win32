---
title: IPropertySetStorage-Stand-alone Implementation
description: The system-provided, stand-alone implementation of IPropertySetStorage includes an implementation of both IPropertyStorage and IPropertySetStorage.
ms.assetid: 0ea5aadf-0b3f-44ac-9bb7-a7e8292f04c2
keywords:
- IPropertySetStorage Strctd Stg , implementations
- IPropertySetStorage Strctd Stg , implementations, stand-alone
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPropertySetStorage-Stand-alone Implementation

The system-provided, stand-alone implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) includes an implementation of both [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) and **IPropertySetStorage**.[**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) is the interface that reads and writes properties in a property set storage. [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) is the interface that creates and opens property sets in a storage. The [**IEnumSTATPROPSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropstg?branch=master) and [**IEnumSTATPROPSETSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropsetstg?branch=master) interfaces are also provided in the stand-alone implementation.

To use the stand-alone implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master), first obtain a pointer to the system-provided, stand-alone implementation and associate the system-provided implementation with your storage object. To get a pointer to the stand-alone implementation of **IPropertySetStorage**, call the [**StgCreatePropSetStg**](/windows/win32/coml2api/nf-coml2api-stgcreatepropsetstg?branch=master) function and provide the *pStorage* parameter specifying the storage object that will contain the property set. This function provides a pointer to the new **IPropertySetStorage** interface for the specified storage object.

The stand-alone implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) creates property sets on any storage object, not just on compound file storages. The stand-alone implementation does not depend on compound files and can be used with any implementation of structured storages. Any restrictions on the caller-provided structured storages apply to this implementation of property sets. For example, if you provide a simple-mode storage to [**StgOpenPropStg**](/windows/win32/coml2api/nf-coml2api-stgopenpropstg?branch=master), the resulting **IPropertySetStorage** will be restricted by the supplied [**IStorage**](/windows/win32/Objidl/nn-objidl-istorage?branch=master).

For more information about the compound file implementation of this interface, see the section [IPropertySetStorage-Compound File Implementation](ipropertysetstorage-compound-file-implementation.md).

## When to Use

Call the methods of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) to create, open, and delete property sets in any structured storage. There is also a method that supplies a pointer to the [**IEnumSTATPROPSETSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropsetstg?branch=master) enumerator that can be used to enumerate the property sets in the storage.

The stand-alone implementation also provides the [**StgCreatePropStg**](/windows/win32/coml2api/nf-coml2api-stgcreatepropstg?branch=master) and [**StgOpenPropStg**](/windows/win32/coml2api/nf-coml2api-stgopenpropstg?branch=master) helper functions, in addition to the [**Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master) and [**Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master) methods, to create and open property sets. These two functions add support for the PROPSETFLAG\_UNBUFFERED value so you can write changes directly to the property set instead of buffering them in a cache. For more information, see [**PROPSETFLAG Constants**](propsetflag-constants.md).

## Methods

The stand-alone implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) supports the following methods.

<dl> <dt>

<span id="IPropertySetStorage__Create"></span><span id="ipropertysetstorage__create"></span><span id="IPROPERTYSETSTORAGE__CREATE"></span>[**IPropertySetStorage::Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master)
</dt> <dd>

Creates a new property set in the storage and returns a pointer to the [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) interface on the property set.

If you plan to use the PROPSETFLAG\_UNBUFFERED value, use the [**StgCreatePropStg**](/windows/win32/coml2api/nf-coml2api-stgcreatepropstg?branch=master) function instead to create and open the new property set and to obtain a pointer to the stand-alone implementation for the [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) interface on the property set.

</dd> <dt>

<span id="IPropertySetStorage__Open"></span><span id="ipropertysetstorage__open"></span><span id="IPROPERTYSETSTORAGE__OPEN"></span>[**IPropertySetStorage::Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master)
</dt> <dd>

Opens an existing property set in the storage and returns a pointer to the [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) interface on the property set.

If you plan to use the PROPSETFLAG\_UNBUFFERED value, use the [**StgOpenPropStg**](/windows/win32/coml2api/nf-coml2api-stgopenpropstg?branch=master) function instead to obtain a pointer to the stand-alone implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) on the specified property set.

</dd> <dt>

<span id="IPropertySetStorage__Delete"></span><span id="ipropertysetstorage__delete"></span><span id="IPROPERTYSETSTORAGE__DELETE"></span>[**IPropertySetStorage::Delete**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-delete?branch=master)
</dt> <dd>

Deletes a property set in this property set storage.

</dd> <dt>

<span id="IPropertySetStorage__Enum"></span><span id="ipropertysetstorage__enum"></span><span id="IPROPERTYSETSTORAGE__ENUM"></span>[**IPropertySetStorage::Enum**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-enum?branch=master)
</dt> <dd>

Creates an object that can be used to enumerate [**STATPROPSETSTG**](/windows/win32/propidlbase/ns-propidl-tagstatpropsetstg?branch=master) structures. Each **STATPROPSETSTG** structure provides data about a single property set.

> [!Note]  
> The DocumentSummaryInformation and UserDefined property set is unique in that it may have two property set sections in a single underlying stream. For more information, see [The DocumentSummaryInformation and UserDefined Property Sets](the-documentsummaryinformation-and-userdefined-property-sets.md) .

 

</dd> </dl>

## Related topics

<dl> <dt>

[IPropertyStorage-Stand-alone Implementation](ipropertystorage-stand-alone-implementation.md)
</dt> <dt>

[**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master)
</dt> <dt>

[**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master)
</dt> <dt>

[**IStorage::EnumElements**](/windows/win32/Objidl/nf-objidl-istorage-enumelements?branch=master)
</dt> <dt>

[**PROPSETFLAG Constants**](propsetflag-constants.md)
</dt> <dt>

[**STATPROPSETSTG**](/windows/win32/propidlbase/ns-propidl-tagstatpropsetstg?branch=master)
</dt> <dt>

[**StgCreatePropSetStg**](/windows/win32/coml2api/nf-coml2api-stgcreatepropsetstg?branch=master)
</dt> <dt>

[**StgCreatePropStg**](/windows/win32/coml2api/nf-coml2api-stgcreatepropstg?branch=master)
</dt> <dt>

[**StgOpenPropStg**](/windows/win32/coml2api/nf-coml2api-stgopenpropstg?branch=master)
</dt> <dt>

[**STGM Constants**](stgm-constants.md)
</dt> </dl>

 

 




