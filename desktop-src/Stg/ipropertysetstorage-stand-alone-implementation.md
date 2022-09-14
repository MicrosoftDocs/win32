---
title: IPropertySetStorage-Stand-alone Implementation
description: The system-provided, stand-alone implementation of IPropertySetStorage includes an implementation of both IPropertyStorage and IPropertySetStorage.
ms.assetid: 0ea5aadf-0b3f-44ac-9bb7-a7e8292f04c2
keywords:
- IPropertySetStorage Strctd Stg , implementations
- IPropertySetStorage Strctd Stg , implementations, stand-alone
ms.topic: article
ms.date: 05/31/2018
---

# IPropertySetStorage-Stand-alone Implementation

The system-provided, stand-alone implementation of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) includes an implementation of both [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) and **IPropertySetStorage**.[**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) is the interface that reads and writes properties in a property set storage. [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) is the interface that creates and opens property sets in a storage. The [**IEnumSTATPROPSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropstg) and [**IEnumSTATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) interfaces are also provided in the stand-alone implementation.

To use the stand-alone implementation of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage), first obtain a pointer to the system-provided, stand-alone implementation and associate the system-provided implementation with your storage object. To get a pointer to the stand-alone implementation of **IPropertySetStorage**, call the [**StgCreatePropSetStg**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatepropsetstg) function and provide the *pStorage* parameter specifying the storage object that will contain the property set. This function provides a pointer to the new **IPropertySetStorage** interface for the specified storage object.

The stand-alone implementation of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) creates property sets on any storage object, not just on compound file storages. The stand-alone implementation does not depend on compound files and can be used with any implementation of structured storages. Any restrictions on the caller-provided structured storages apply to this implementation of property sets. For example, if you provide a simple-mode storage to [**StgOpenPropStg**](/windows/desktop/api/coml2api/nf-coml2api-stgopenpropstg), the resulting **IPropertySetStorage** will be restricted by the supplied [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage).

For more information about the compound file implementation of this interface, see the section [IPropertySetStorage-Compound File Implementation](ipropertysetstorage-compound-file-implementation.md).

## When to Use

Call the methods of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) to create, open, and delete property sets in any structured storage. There is also a method that supplies a pointer to the [**IEnumSTATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) enumerator that can be used to enumerate the property sets in the storage.

The stand-alone implementation also provides the [**StgCreatePropStg**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatepropstg) and [**StgOpenPropStg**](/windows/desktop/api/coml2api/nf-coml2api-stgopenpropstg) helper functions, in addition to the [**Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) and [**Open**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-open) methods, to create and open property sets. These two functions add support for the PROPSETFLAG\_UNBUFFERED value so you can write changes directly to the property set instead of buffering them in a cache. For more information, see [**PROPSETFLAG Constants**](propsetflag-constants.md).

## Methods

The stand-alone implementation of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) supports the following methods.

<dl> <dt>

<span id="IPropertySetStorage__Create"></span><span id="ipropertysetstorage__create"></span><span id="IPROPERTYSETSTORAGE__CREATE"></span>[**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create)
</dt> <dd>

Creates a new property set in the storage and returns a pointer to the [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interface on the property set.

If you plan to use the PROPSETFLAG\_UNBUFFERED value, use the [**StgCreatePropStg**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatepropstg) function instead to create and open the new property set and to obtain a pointer to the stand-alone implementation for the [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interface on the property set.

</dd> <dt>

<span id="IPropertySetStorage__Open"></span><span id="ipropertysetstorage__open"></span><span id="IPROPERTYSETSTORAGE__OPEN"></span>[**IPropertySetStorage::Open**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-open)
</dt> <dd>

Opens an existing property set in the storage and returns a pointer to the [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interface on the property set.

If you plan to use the PROPSETFLAG\_UNBUFFERED value, use the [**StgOpenPropStg**](/windows/desktop/api/coml2api/nf-coml2api-stgopenpropstg) function instead to obtain a pointer to the stand-alone implementation of [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) on the specified property set.

</dd> <dt>

<span id="IPropertySetStorage__Delete"></span><span id="ipropertysetstorage__delete"></span><span id="IPROPERTYSETSTORAGE__DELETE"></span>[**IPropertySetStorage::Delete**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-delete)
</dt> <dd>

Deletes a property set in this property set storage.

</dd> <dt>

<span id="IPropertySetStorage__Enum"></span><span id="ipropertysetstorage__enum"></span><span id="IPROPERTYSETSTORAGE__ENUM"></span>[**IPropertySetStorage::Enum**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-enum)
</dt> <dd>

Creates an object that can be used to enumerate [**STATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) structures. Each **STATPROPSETSTG** structure provides data about a single property set.

> [!Note]  
> The DocumentSummaryInformation and UserDefined property set is unique in that it may have two property set sections in a single underlying stream. For more information, see [The DocumentSummaryInformation and UserDefined Property Sets](the-documentsummaryinformation-and-userdefined-property-sets.md) .

 

</dd> </dl>

## Related topics

<dl> <dt>

[IPropertyStorage-Stand-alone Implementation](ipropertystorage-stand-alone-implementation.md)
</dt> <dt>

[**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage)
</dt> <dt>

[**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage)
</dt> <dt>

[**IStorage::EnumElements**](/windows/desktop/api/Objidl/nf-objidl-istorage-enumelements)
</dt> <dt>

[**PROPSETFLAG Constants**](propsetflag-constants.md)
</dt> <dt>

[**STATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg)
</dt> <dt>

[**StgCreatePropSetStg**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatepropsetstg)
</dt> <dt>

[**StgCreatePropStg**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatepropstg)
</dt> <dt>

[**StgOpenPropStg**](/windows/desktop/api/coml2api/nf-coml2api-stgopenpropstg)
</dt> <dt>

[**STGM Constants**](stgm-constants.md)
</dt> </dl>

 

 