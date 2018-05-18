---
title: IPropertySetStorage-Compound File Implementation
description: The COM compound file storage object implementation includes an implementation of both IPropertyStorage, the interface that manages a single persistent property set, and IPropertySetStorage, the interface that manages groups of persistent property sets.
ms.assetid: 'de2cb778-c6eb-4487-996b-87405674f603'
keywords: ["IPropertySetStorage Strctd Stg , implementations, compound file"]
---

# IPropertySetStorage-Compound File Implementation

The [COM compound file storage object implementation](ipropertystorage-compound-file-implementation.md) includes an implementation of both [**IPropertyStorage**](ipropertystorage.md), the interface that manages a single persistent property set, and [**IPropertySetStorage**](ipropertysetstorage.md), the interface that manages groups of persistent property sets.

To get a pointer to the compound file implementation of [**IPropertySetStorage**](ipropertysetstorage.md), specify the header-defined name for the identifier IID\_IStorage as the *riid* parameter, or use the [**StgCreateStorageEx**](stgcreatestorageex.md) or [**StgOpenStorageEx**](stgopenstorageex.md) functions. In both cases, specify STGFMT\_STORAGE as the *stgfmt* parameter. (STGFMT\_ANY can alternatively be specified in the case of **StgOpenStorageEx**.) Also, specify the header-defined name for the interface identifier (IID) IID\_IPropertySetStorage as the *riid* parameter. Both functions supply a pointer to the object **IPropertySetStorage** interface.

Another way to get a pointer to the compound file implementation is to specify the header-defined name for the identifier IID\_IStorage as the *riid* parameter, or to use the [**StgCreateDocfile**](stgcreatedocfile.md) or [**StgOpenStorage**](stgopenstorage.md) functions. This will supply a pointer to the object [**IStorage**](istorage.md) interface. When you want to deal with persistent property sets, call [**IStorage::QueryInterface**](_com_iunknown_queryinterface) for the [**IPropertySetStorage**](ipropertysetstorage.md) interface.

## When to Use IPropertySetStorage

Call the methods of [**IPropertySetStorage**](ipropertysetstorage.md) to create, open, or delete property sets in the current compound-file property set storage. There is also a method, [**IPropertySetStorage::Enum**](ipropertysetstorage-enum.md), that supplies a pointer to an enumerator that can be used to enumerate the property sets in the storage.

## Methods

[**IPropertySetStorage::Create**](ipropertysetstorage-create.md)

Creates a new property set in the current compound file storage and, on return, supplies an interface pointer to the [**IPropertyStorage**](ipropertystorage.md) compound-file implementation. In this implementation, property sets may be transacted only if PROPSETFLAG\_NONSIMPLE is specified. This method requires that the sharing mode specified in the *grfMode* parameter be STGM\_SHARE\_EXCLUSIVE, and that the access mode be either STGM\_READ or STGM\_READWRITE (STGM\_WRITE mode is not supported).

[**IPropertySetStorage::Open**](ipropertysetstorage-open.md)

Opens an existing property set in the current property storage. On return, it supplies an interface pointer to the compound file implementation of [**IPropertyStorage**](ipropertystorage.md). This method requires that the sharing mode specified in the *grfMode* parameter be STGM\_SHARE\_EXCLUSIVE, and that the access mode be either STGM\_READ or STGM\_READWRITE (STGM\_WRITE is not supported).

[**IPropertySetStorage::Delete**](ipropertysetstorage-delete.md)

Deletes a property set in this property storage.

[**IPropertySetStorage::Enum**](ipropertysetstorage-enum.md)

Creates an object used to enumerate [**STATPROPSETSTG**](statpropsetstg.md) structures. Each **STATPROPSETSTG** structure provides data about a single property set.

## Remarks

Starting with Windows 2000, the compound-file implementation of [**IPropertySetStorage**](ipropertysetstorage.md) supports simple mode. Simple mode is indicated by specifying the STGM\_SIMPLE flag for the [**StgCreateStorageEx**](stgcreatestorageex.md) and [**StgOpenStorageEx**](stgopenstorageex.md) functions. If the compound file is opened in simple mode, the associated **IPropertySetStorage** implementation is limited as follows:

-   Only simple property sets can be created. That is, specifying the PROPSETFLAG\_NONSIMPLE value in the *grfFlags* parameter for the [**IPropertySetStorage::Create**](ipropertysetstorage-create.md) method results in an error.
-   After you create a compound file with [**StgCreateStorageEx**](stgcreatestorageex.md) using STGM\_SIMPLE and query for the [**IPropertySetStorage**](ipropertysetstorage.md) interface, you can only call [**IPropertySetStorage::Create**](ipropertysetstorage-create.md) once. Then you must release the [**IPropertyStorage**](ipropertystorage.md) interface before calling the **Create** method again. For more information about simple mode, see [**STGM Constants**](stgm-constants.md).
-   You cannot use the [**IPropertySetStorage::Open**](ipropertysetstorage-open.md) method to open a property set after using [**StgCreateStorageEx**](stgcreatestorageex.md) to create the storage object. Instead you must use [**StgOpenStorageEx**](stgopenstorageex.md) before querying for [**IPropertySetStorage**](ipropertysetstorage.md) and calling the **Open** method.
-   After you open a compound file with [**StgOpenStorageEx**](stgopenstorageex.md) using the STGM\_SIMPLE flag and query for the [**IPropertySetStorage**](ipropertysetstorage.md) interface, you can open one property set at a time using [**IPropertySetStorage::Open**](ipropertysetstorage-open.md). Also, it may not be possible for the total size of the property set to be increased while the property set is open.

Simple property sets cannot be transacted. You cannot specify STGM\_TRANSACTED in the *grfmode* parameter of the [**Create**](ipropertysetstorage-create.md) and [**Open**](ipropertysetstorage-open.md) methods unless you also specify PROPSETFLAG\_NONSIMPLE in the *grfFlags* parameter. Be aware that simple and non-simple property sets are unrelated to the simple-mode property sets described above. For more information about simple and nonsimple property sets, see [Storage and Stream Objects for a Property Set](storage-vs--stream-for-a-property-set.md).

> [!Note]  
> The DocumentSummaryInformation and UserDefined property sets are unique in that they may have two property set sections. For more information, see [The DocumentSummaryInformation and UserDefined Property Sets](the-documentsummaryinformation-and-userdefined-property-sets.md).

 

## Related topics

<dl> <dt>

[IPropertyStorage - Compound File Implementation](ipropertystorage-compound-file-implementation.md)
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
</dt> </dl>

 

 




