---
title: IPropertySetStorage-Stand-alone Implementation
description: The system-provided, stand-alone implementation of IPropertySetStorage includes an implementation of both IPropertyStorage and IPropertySetStorage.
ms.assetid: '0ea5aadf-0b3f-44ac-9bb7-a7e8292f04c2'
keywords: ["IPropertySetStorage Strctd Stg , implementations", "IPropertySetStorage Strctd Stg , implementations, stand-alone"]
---

# IPropertySetStorage-Stand-alone Implementation

The system-provided, stand-alone implementation of [**IPropertySetStorage**](ipropertysetstorage.md) includes an implementation of both [**IPropertyStorage**](ipropertystorage.md) and **IPropertySetStorage**.[**IPropertyStorage**](ipropertystorage.md) is the interface that reads and writes properties in a property set storage. [**IPropertySetStorage**](ipropertysetstorage.md) is the interface that creates and opens property sets in a storage. The [**IEnumSTATPROPSTG**](ienumstatpropstg.md) and [**IEnumSTATPROPSETSTG**](ienumstatpropsetstg.md) interfaces are also provided in the stand-alone implementation.

To use the stand-alone implementation of [**IPropertySetStorage**](ipropertysetstorage.md), first obtain a pointer to the system-provided, stand-alone implementation and associate the system-provided implementation with your storage object. To get a pointer to the stand-alone implementation of **IPropertySetStorage**, call the [**StgCreatePropSetStg**](stgcreatepropsetstg.md) function and provide the *pStorage* parameter specifying the storage object that will contain the property set. This function provides a pointer to the new **IPropertySetStorage** interface for the specified storage object.

The stand-alone implementation of [**IPropertySetStorage**](ipropertysetstorage.md) creates property sets on any storage object, not just on compound file storages. The stand-alone implementation does not depend on compound files and can be used with any implementation of structured storages. Any restrictions on the caller-provided structured storages apply to this implementation of property sets. For example, if you provide a simple-mode storage to [**StgOpenPropStg**](stgopenpropstg.md), the resulting **IPropertySetStorage** will be restricted by the supplied [**IStorage**](istorage.md).

For more information about the compound file implementation of this interface, see the section [IPropertySetStorage-Compound File Implementation](ipropertysetstorage-compound-file-implementation.md).

## When to Use

Call the methods of [**IPropertySetStorage**](ipropertysetstorage.md) to create, open, and delete property sets in any structured storage. There is also a method that supplies a pointer to the [**IEnumSTATPROPSETSTG**](ienumstatpropsetstg.md) enumerator that can be used to enumerate the property sets in the storage.

The stand-alone implementation also provides the [**StgCreatePropStg**](stgcreatepropstg.md) and [**StgOpenPropStg**](stgopenpropstg.md) helper functions, in addition to the [**Create**](ipropertysetstorage-create.md) and [**Open**](ipropertysetstorage-open.md) methods, to create and open property sets. These two functions add support for the PROPSETFLAG\_UNBUFFERED value so you can write changes directly to the property set instead of buffering them in a cache. For more information, see [**PROPSETFLAG Constants**](propsetflag-constants.md).

## Methods

The stand-alone implementation of [**IPropertySetStorage**](ipropertysetstorage.md) supports the following methods.

<dl> <dt>

<span id="IPropertySetStorage__Create"></span><span id="ipropertysetstorage__create"></span><span id="IPROPERTYSETSTORAGE__CREATE"></span>[**IPropertySetStorage::Create**](ipropertysetstorage-create.md)
</dt> <dd>

Creates a new property set in the storage and returns a pointer to the [**IPropertyStorage**](ipropertystorage.md) interface on the property set.

If you plan to use the PROPSETFLAG\_UNBUFFERED value, use the [**StgCreatePropStg**](stgcreatepropstg.md) function instead to create and open the new property set and to obtain a pointer to the stand-alone implementation for the [**IPropertyStorage**](ipropertystorage.md) interface on the property set.

</dd> <dt>

<span id="IPropertySetStorage__Open"></span><span id="ipropertysetstorage__open"></span><span id="IPROPERTYSETSTORAGE__OPEN"></span>[**IPropertySetStorage::Open**](ipropertysetstorage-open.md)
</dt> <dd>

Opens an existing property set in the storage and returns a pointer to the [**IPropertyStorage**](ipropertystorage.md) interface on the property set.

If you plan to use the PROPSETFLAG\_UNBUFFERED value, use the [**StgOpenPropStg**](stgopenpropstg.md) function instead to obtain a pointer to the stand-alone implementation of [**IPropertyStorage**](ipropertystorage.md) on the specified property set.

</dd> <dt>

<span id="IPropertySetStorage__Delete"></span><span id="ipropertysetstorage__delete"></span><span id="IPROPERTYSETSTORAGE__DELETE"></span>[**IPropertySetStorage::Delete**](ipropertysetstorage-delete.md)
</dt> <dd>

Deletes a property set in this property set storage.

</dd> <dt>

<span id="IPropertySetStorage__Enum"></span><span id="ipropertysetstorage__enum"></span><span id="IPROPERTYSETSTORAGE__ENUM"></span>[**IPropertySetStorage::Enum**](ipropertysetstorage-enum.md)
</dt> <dd>

Creates an object that can be used to enumerate [**STATPROPSETSTG**](statpropsetstg.md) structures. Each **STATPROPSETSTG** structure provides data about a single property set.

> [!Note]  
> The DocumentSummaryInformation and UserDefined property set is unique in that it may have two property set sections in a single underlying stream. For more information, see [The DocumentSummaryInformation and UserDefined Property Sets](the-documentsummaryinformation-and-userdefined-property-sets.md) .

 

</dd> </dl>

## Related topics

<dl> <dt>

[IPropertyStorage-Stand-alone Implementation](ipropertystorage-stand-alone-implementation.md)
</dt> <dt>

[**IPropertySetStorage**](ipropertysetstorage.md)
</dt> <dt>

[**IPropertyStorage**](ipropertystorage.md)
</dt> <dt>

[**IStorage::EnumElements**](istorage-enumelements.md)
</dt> <dt>

[**PROPSETFLAG Constants**](propsetflag-constants.md)
</dt> <dt>

[**STATPROPSETSTG**](statpropsetstg.md)
</dt> <dt>

[**StgCreatePropSetStg**](stgcreatepropsetstg.md)
</dt> <dt>

[**StgCreatePropStg**](stgcreatepropstg.md)
</dt> <dt>

[**StgOpenPropStg**](stgopenpropstg.md)
</dt> <dt>

[**STGM Constants**](stgm-constants.md)
</dt> </dl>

 

 




