---
title: IPropertySetStorage-Compound File Implementation
description: The COM compound file storage object implementation includes an implementation of both IPropertyStorage, the interface that manages a single persistent property set, and IPropertySetStorage, the interface that manages groups of persistent property sets.
ms.assetid: de2cb778-c6eb-4487-996b-87405674f603
keywords:
- IPropertySetStorage Strctd Stg , implementations, compound file
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPropertySetStorage-Compound File Implementation

The [COM compound file storage object implementation](ipropertystorage-compound-file-implementation.md) includes an implementation of both [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master), the interface that manages a single persistent property set, and [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master), the interface that manages groups of persistent property sets.

To get a pointer to the compound file implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master), specify the header-defined name for the identifier IID\_IStorage as the *riid* parameter, or use the [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master) or [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) functions. In both cases, specify STGFMT\_STORAGE as the *stgfmt* parameter. (STGFMT\_ANY can alternatively be specified in the case of **StgOpenStorageEx**.) Also, specify the header-defined name for the interface identifier (IID) IID\_IPropertySetStorage as the *riid* parameter. Both functions supply a pointer to the object **IPropertySetStorage** interface.

Another way to get a pointer to the compound file implementation is to specify the header-defined name for the identifier IID\_IStorage as the *riid* parameter, or to use the [**StgCreateDocfile**](/windows/win32/coml2api/nf-coml2api-stgcreatedocfile?branch=master) or [**StgOpenStorage**](/windows/win32/coml2api/nf-coml2api-stgopenstorage?branch=master) functions. This will supply a pointer to the object [**IStorage**](/windows/win32/Objidl/nn-objidl-istorage?branch=master) interface. When you want to deal with persistent property sets, call [**IStorage::QueryInterface**](_com_iunknown_queryinterface) for the [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) interface.

## When to Use IPropertySetStorage

Call the methods of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) to create, open, or delete property sets in the current compound-file property set storage. There is also a method, [**IPropertySetStorage::Enum**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-enum?branch=master), that supplies a pointer to an enumerator that can be used to enumerate the property sets in the storage.

## Methods

[**IPropertySetStorage::Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master)

Creates a new property set in the current compound file storage and, on return, supplies an interface pointer to the [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) compound-file implementation. In this implementation, property sets may be transacted only if PROPSETFLAG\_NONSIMPLE is specified. This method requires that the sharing mode specified in the *grfMode* parameter be STGM\_SHARE\_EXCLUSIVE, and that the access mode be either STGM\_READ or STGM\_READWRITE (STGM\_WRITE mode is not supported).

[**IPropertySetStorage::Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master)

Opens an existing property set in the current property storage. On return, it supplies an interface pointer to the compound file implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master). This method requires that the sharing mode specified in the *grfMode* parameter be STGM\_SHARE\_EXCLUSIVE, and that the access mode be either STGM\_READ or STGM\_READWRITE (STGM\_WRITE is not supported).

[**IPropertySetStorage::Delete**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-delete?branch=master)

Deletes a property set in this property storage.

[**IPropertySetStorage::Enum**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-enum?branch=master)

Creates an object used to enumerate [**STATPROPSETSTG**](/windows/win32/propidlbase/ns-propidl-tagstatpropsetstg?branch=master) structures. Each **STATPROPSETSTG** structure provides data about a single property set.

## Remarks

Starting with Windows 2000, the compound-file implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) supports simple mode. Simple mode is indicated by specifying the STGM\_SIMPLE flag for the [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master) and [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) functions. If the compound file is opened in simple mode, the associated **IPropertySetStorage** implementation is limited as follows:

-   Only simple property sets can be created. That is, specifying the PROPSETFLAG\_NONSIMPLE value in the *grfFlags* parameter for the [**IPropertySetStorage::Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master) method results in an error.
-   After you create a compound file with [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master) using STGM\_SIMPLE and query for the [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) interface, you can only call [**IPropertySetStorage::Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master) once. Then you must release the [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) interface before calling the **Create** method again. For more information about simple mode, see [**STGM Constants**](stgm-constants.md).
-   You cannot use the [**IPropertySetStorage::Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master) method to open a property set after using [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master) to create the storage object. Instead you must use [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) before querying for [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) and calling the **Open** method.
-   After you open a compound file with [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) using the STGM\_SIMPLE flag and query for the [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) interface, you can open one property set at a time using [**IPropertySetStorage::Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master). Also, it may not be possible for the total size of the property set to be increased while the property set is open.

Simple property sets cannot be transacted. You cannot specify STGM\_TRANSACTED in the *grfmode* parameter of the [**Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master) and [**Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master) methods unless you also specify PROPSETFLAG\_NONSIMPLE in the *grfFlags* parameter. Be aware that simple and non-simple property sets are unrelated to the simple-mode property sets described above. For more information about simple and nonsimple property sets, see [Storage and Stream Objects for a Property Set](storage-vs--stream-for-a-property-set.md).

> [!Note]  
> The DocumentSummaryInformation and UserDefined property sets are unique in that they may have two property set sections. For more information, see [The DocumentSummaryInformation and UserDefined Property Sets](the-documentsummaryinformation-and-userdefined-property-sets.md).

 

## Related topics

<dl> <dt>

[IPropertyStorage - Compound File Implementation](ipropertystorage-compound-file-implementation.md)
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
</dt> </dl>

 

 




