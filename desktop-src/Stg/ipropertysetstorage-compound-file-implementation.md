---
title: IPropertySetStorage-Compound File Implementation
description: The COM compound file storage object implementation includes an implementation of both IPropertyStorage, the interface that manages a single persistent property set, and IPropertySetStorage, the interface that manages groups of persistent property sets.
ms.assetid: de2cb778-c6eb-4487-996b-87405674f603
keywords:
- IPropertySetStorage Strctd Stg , implementations, compound file
ms.topic: article
ms.date: 05/31/2018
---

# IPropertySetStorage-Compound File Implementation

The [COM compound file storage object implementation](ipropertystorage-compound-file-implementation.md) includes an implementation of both [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage), the interface that manages a single persistent property set, and [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage), the interface that manages groups of persistent property sets.

To get a pointer to the compound file implementation of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage), specify the header-defined name for the identifier IID\_IStorage as the *riid* parameter, or use the [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex) or [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex) functions. In both cases, specify STGFMT\_STORAGE as the *stgfmt* parameter. (STGFMT\_ANY can alternatively be specified in the case of **StgOpenStorageEx**.) Also, specify the header-defined name for the interface identifier (IID) IID\_IPropertySetStorage as the *riid* parameter. Both functions supply a pointer to the object **IPropertySetStorage** interface.

Another way to get a pointer to the compound file implementation is to specify the header-defined name for the identifier IID\_IStorage as the *riid* parameter, or to use the [**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile) or [**StgOpenStorage**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorage) functions. This will supply a pointer to the object [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface. When you want to deal with persistent property sets, call [**IStorage::QueryInterface**](/windows/win32/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) for the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface.

## When to Use IPropertySetStorage

Call the methods of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) to create, open, or delete property sets in the current compound-file property set storage. There is also a method, [**IPropertySetStorage::Enum**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-enum), that supplies a pointer to an enumerator that can be used to enumerate the property sets in the storage.

## Methods

[**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create)

Creates a new property set in the current compound file storage and, on return, supplies an interface pointer to the [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) compound-file implementation. In this implementation, property sets may be transacted only if PROPSETFLAG\_NONSIMPLE is specified. This method requires that the sharing mode specified in the *grfMode* parameter be STGM\_SHARE\_EXCLUSIVE, and that the access mode be either STGM\_READ or STGM\_READWRITE (STGM\_WRITE mode is not supported).

[**IPropertySetStorage::Open**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-open)

Opens an existing property set in the current property storage. On return, it supplies an interface pointer to the compound file implementation of [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage). This method requires that the sharing mode specified in the *grfMode* parameter be STGM\_SHARE\_EXCLUSIVE, and that the access mode be either STGM\_READ or STGM\_READWRITE (STGM\_WRITE is not supported).

[**IPropertySetStorage::Delete**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-delete)

Deletes a property set in this property storage.

[**IPropertySetStorage::Enum**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-enum)

Creates an object used to enumerate [**STATPROPSETSTG**](/windows/win32/api/propidlbase/nn-propidlbase-ienumstatpropsetstg) structures. Each **STATPROPSETSTG** structure provides data about a single property set.

## Remarks

Starting with Windows 2000, the compound-file implementation of [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) supports simple mode. Simple mode is indicated by specifying the STGM\_SIMPLE flag for the [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex) and [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex) functions. If the compound file is opened in simple mode, the associated **IPropertySetStorage** implementation is limited as follows:

-   Only simple property sets can be created. That is, specifying the PROPSETFLAG\_NONSIMPLE value in the *grfFlags* parameter for the [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) method results in an error.
-   After you create a compound file with [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex) using STGM\_SIMPLE and query for the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface, you can only call [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) once. Then you must release the [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interface before calling the **Create** method again. For more information about simple mode, see [**STGM Constants**](stgm-constants.md).
-   You cannot use the [**IPropertySetStorage::Open**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-open) method to open a property set after using [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex) to create the storage object. Instead you must use [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex) before querying for [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) and calling the **Open** method.
-   After you open a compound file with [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex) using the STGM\_SIMPLE flag and query for the [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) interface, you can open one property set at a time using [**IPropertySetStorage::Open**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-open). Also, it may not be possible for the total size of the property set to be increased while the property set is open.

Simple property sets cannot be transacted. You cannot specify STGM\_TRANSACTED in the *grfmode* parameter of the [**Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) and [**Open**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-open) methods unless you also specify PROPSETFLAG\_NONSIMPLE in the *grfFlags* parameter. Be aware that simple and non-simple property sets are unrelated to the simple-mode property sets described above. For more information about simple and nonsimple property sets, see [Storage and Stream Objects for a Property Set](storage-vs--stream-for-a-property-set.md).

> [!Note]  
> The DocumentSummaryInformation and UserDefined property sets are unique in that they may have two property set sections. For more information, see [The DocumentSummaryInformation and UserDefined Property Sets](the-documentsummaryinformation-and-userdefined-property-sets.md).

 

## Related topics

<dl> <dt>

[IPropertyStorage - Compound File Implementation](ipropertystorage-compound-file-implementation.md)
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
</dt> </dl>

 

 