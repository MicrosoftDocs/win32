---
title: IPropertyStorage-Compound File Implementation
description: The COM implementation of the Structured Storage architecture is called compound files.
ms.assetid: c4b4f313-de58-44f2-8ce1-a07cc187d8ca
keywords:
- IPropertyStorage Strctd Stg , implementations, compound file
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPropertyStorage-Compound File Implementation

The COM implementation of the Structured Storage architecture is called [compound files](istorage-compound-file-implementation.md). Storage objects as implemented in compound files include an implementation of both [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master), the interface that manages a single persistent property set, and [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master), the interface that manages groups of persistent property sets. For more information about the **IPropertyStorage** interface, see **IPropertyStorage** and [Property Storage Considerations](property-storage-considerations.md).

To get a pointer to the compound file implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master), call [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master) to create a new compound file object or [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) to open a previously created compound file object. In the case of **StgCreateStorageEx**, the *stgfmt* parameter should be set to STGFMT\_STORAGE. In the case of **StgOpenStorageEx**, the *stgfmt* parameter should be set to STGFMT\_STORAGE or STGFMT\_ANY. In both cases, the *riid* parameter should be set to IID\_IPropertySetStorage. Both functions supply a pointer to the object [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) interface. By calling either the [**Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master) or [**Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master) method of that interface, you will get a pointer to the **IPropertyStorage** interface, which you can use to call any of its methods.

An alternative way to get a pointer to the compound file implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) is to call the older [**StgCreateDocfile**](/windows/win32/coml2api/nf-coml2api-stgcreatedocfile?branch=master) and [**StgOpenStorage**](/windows/win32/coml2api/nf-coml2api-stgopenstorage?branch=master) functions, or to specify an *riid* parameter of IID\_IStorage to the [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master) or [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) function. In either case, a pointer to the object's [**IStorage**](/windows/win32/Objidl/nn-objidl-istorage?branch=master) interface is returned. With persistent property sets, call [**QueryInterface**](_com_iunknown_queryinterface) for the **IPropertySetStorage** interface, specifying the header-defined name for the interface identifier (IID) IID\_IPropertySetStorage.

## When to Use

Use [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) to manage properties within a single property set. Its methods support reading, writing, and deleting both properties and the optional string names that can be associated with property identifiers. Other methods support the standard commit and revert storage operations. There is also a method that enables you to set times associated with the property storage, and another that permits the assignment of a CLSID that can be used to associate other code, such as user interface code, with the property set. Calling the [**Enum**](/windows/win32/Propidl/nf-propidl-ipropertystorage-enum?branch=master) method supplies a pointer to the compound file implementation of [**IEnumSTATPROPSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropstg?branch=master), which allows you to enumerate the properties in the set.

> [!Note]  
> If you obtain a pointer to [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) by calling [**StgCreateDocfile**](/windows/win32/coml2api/nf-coml2api-stgcreatedocfile?branch=master), [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master), [**StgOpenStorage**](/windows/win32/coml2api/nf-coml2api-stgopenstorage?branch=master) or [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) on a simple-mode property set storage, the **IPropertyStorage** methods adhere to the rules of simple-mode streams. The property set storage is simple mode if it was obtained for a file that was created or opened with the STGM\_SIMPLE flag. In this case, it is not always possible to make the underlying stream larger and it is not possible to replace existing properties with larger properties. For more information, see [IPropertySetStorage-Compound File Implementation](ipropertysetstorage-compound-file-implementation.md).

 

## IPropertyStorage and Caching

The compound file implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) caches open property sets in memory in order to improve performance. As a result, changes to a property set are not written to the compound file until the [**Commit**](/windows/win32/Propidl/nf-propidl-ipropertystorage-commit?branch=master) or **Release** (last reference) methods are called.

## Simple Mode Property Sets

A property storage object is in simple mode if it is created from a simple mode property set storage object. For example, a property set storage object would be in simple mode if it were obtained from the [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) function, with the STGM\_SIMPLE flag set in the *grfMode* parameter. Note that "simple mode" is unrelated to "simple property sets". A property set is simple if it is created by calling [**IPropertySetStorage::Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master) with the PROPSETFLAG\_NONSIMPLE flag set in the *grfFlags* parameter. For more information about simple and nonsimple property sets, see [Storage and Stream Objects for a Property Set](storage-vs--stream-for-a-property-set.md).

When a simple mode property storage object is created, there are no restrictions on its use. When an existing simple-mode property storage object is opened, the underlying stream object that stores the property set cannot be grown. Consequently, it is not always possible to modify such a property storage object if the change requires a larger stream.

## Property Set Formats

The compound file implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) supports both the version 0 and the version 1 property set serialization formats. The version 1 format is supported on computers running on Windows 2000. For more information, see [Property Set Serialization](version-0-vs--version-1-property-set-serialization.md). Property sets are created in version 0 format and remain in that format unless new features are requested. When that occurs, the format is updated to version 1.

For example, if a property set is created with the PROPSETFLAG\_DEFAULT flag, its format is version 0. As long as property types that conform to the version 0 format are written to and read from that property set, the property set remains in version 0 format. If a version 1 property type is written to the property set, the property set is automatically updated to version 1. Subsequently, that property set can no longer be read by implementations that recognize only version 0.

## IPropertyStorage and Variant Types

The compound file implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) does not support the variant types VT\_UNKNOWN or VT\_DISPATCH in the **vt** member of the [**PROPVARIANT**](/windows/win32/propidlbase/ns-propidl-tagpropvariant?branch=master) structure.

The following table lists variant types that are supported within a SafeArray; that is, these values can be combined with VT\_ARRAY in the **vt** member of the [**PROPVARIANT**](/windows/win32/propidlbase/ns-propidl-tagpropvariant?branch=master) structure.



Variant types supported within SafeArray by compound file implementation of IPropertyStorage

VT\_I1

VT\_UI1

VT\_I2

VT\_UI2

VT\_I4

VT\_UI4

VT\_INT

VT\_UINT

VT\_R4

VT\_R8

VT\_CY

VT\_DATE

VT\_BSTR

VT\_BOOL

VT\_DECIMAL

VT\_ERROR

VT\_VARIANT

 



 

When VT\_VARIANT is combined with VT\_ARRAY, the SafeArray itself holds [**PROPVARIANT**](/windows/win32/propidlbase/ns-propidl-tagpropvariant?branch=master) structures. However, the types of these elements must be taken from the preceding list, cannot be VT\_VARIANT, and cannot include the VT\_VECTOR, VT\_ARRAY, or VT\_BYREF indicators.

## IPropertyStorage Methods

The compound file implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) supports the following methods:

<dl> <dt>

<span id="IPropertyStorage__ReadMultiple"></span><span id="ipropertystorage__readmultiple"></span><span id="IPROPERTYSTORAGE__READMULTIPLE"></span>[**IPropertyStorage::ReadMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-readmultiple?branch=master)
</dt> <dd>

Reads the properties specified in the *rgpspec* array and supplies the values of all valid properties in the *rgvar* array of PROPVARIANTs. In the COM compound file implementation, duplicate property identifiers that refer to stream or storage types result in multiple calls to [**IStorage::OpenStream**](/windows/win32/Objidl/nf-objidl-istorage-openstream?branch=master) or [**IStorage::OpenStorage**](/windows/win32/Objidl/nf-objidl-istorage-openstorage?branch=master) and the success or failure of **ReadMultiple** depends on the underlying storage implementation's ability to share opening operations. Because in a compound file STGM\_SHARE\_EXCLUSIVE is forced, multiple open attempts will fail. Opening the same storage object more than once from the same parent storage is not supported. The STGM\_SHARE\_EXCLUSIVE flag must be specified.

In addition, to ensure thread-safe operation if the same stream- or storage-valued property is requested several times through the same [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) pointer in the COM compound file implementation, the open operation will succeed or fail depending on whether the property is already open and whether the underlying file system handles multiple openings of a stream or storage. Thus, the **ReadMultiple** operation on a stream- or storage-valued property always results in a call to [**IStorage::OpenStream**](/windows/win32/Objidl/nf-objidl-istorage-openstream?branch=master), or [**IStorage::OpenStorage**](/windows/win32/Objidl/nf-objidl-istorage-openstorage?branch=master), which passes the access (STGM\_READWRITE, and so forth) and share flags (STGM\_SHARE\_EXCLUSIVE, and so on) specified when the original property set was opened or created.

If the method fails, the values written to *rgvar*\[\] are undefined. If some stream- or storage-valued properties are opened successfully but an error occurs before execution is complete, these should be released before the method returns.

</dd> <dt>

<span id="IPropertyStorage__WriteMultiple"></span><span id="ipropertystorage__writemultiple"></span><span id="IPROPERTYSTORAGE__WRITEMULTIPLE"></span>[**IPropertyStorage::WriteMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-writemultiple?branch=master)
</dt> <dd>

Writes the properties specified in the *rgpspec*\[\] array, assigning them the [**PROPVARIANT**](/windows/win32/propidlbase/ns-propidl-tagpropvariant?branch=master) tags and values specified in *rgvar*\[\]. Properties that already exist are assigned the specified **PROPVARIANT** values. Properties that do not currently exist are created.

</dd> <dt>

<span id="IPropertyStorage__DeleteMultiple"></span><span id="ipropertystorage__deletemultiple"></span><span id="IPROPERTYSTORAGE__DELETEMULTIPLE"></span>[**IPropertyStorage::DeleteMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-deletemultiple?branch=master)
</dt> <dd>

Deletes the properties specified in the *rgpspec*\[\].

</dd> <dt>

<span id="IPropertyStorage__ReadPropertyNames"></span><span id="ipropertystorage__readpropertynames"></span><span id="IPROPERTYSTORAGE__READPROPERTYNAMES"></span>[**IPropertyStorage::ReadPropertyNames**](/windows/win32/Propidl/nf-propidl-ipropertystorage-readpropertynames?branch=master)
</dt> <dd>

Reads existing string names associated with the property IDs specified in the *rgpropid*\[\] array.

</dd> <dt>

<span id="IPropertyStorage__WritePropertyNames"></span><span id="ipropertystorage__writepropertynames"></span><span id="IPROPERTYSTORAGE__WRITEPROPERTYNAMES"></span>[**IPropertyStorage::WritePropertyNames**](/windows/win32/Propidl/nf-propidl-ipropertystorage-writepropertynames?branch=master)
</dt> <dd>

Assigns string names specified in the *rglpwstrName* array to property IDs specified in the *rgpropid* array.

</dd> <dt>

<span id="IPropertyStorage__DeletePropertyNames"></span><span id="ipropertystorage__deletepropertynames"></span><span id="IPROPERTYSTORAGE__DELETEPROPERTYNAMES"></span>[**IPropertyStorage::DeletePropertyNames**](/windows/win32/Propidl/nf-propidl-ipropertystorage-deletepropertynames?branch=master)
</dt> <dd>

Deletes property names for the properties specified in the *rgpropid*\[\] array.

</dd> <dt>

<span id="IPropertyStorage__SetClass"></span><span id="ipropertystorage__setclass"></span><span id="IPROPERTYSTORAGE__SETCLASS"></span>[**IPropertyStorage::SetClass**](/windows/win32/Propidl/nf-propidl-ipropertystorage-setclass?branch=master)
</dt> <dd>

Sets the **CLSID** of the property set stream. In the compound file implementation, setting the CLSID on a nonsimple property set (one that can legally contain storage- or stream-valued properties, as described in [**IPropertySetStorage::Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master)) also sets the CLSID on the underlying substorage so that it can be obtained through a call to [**IStorage::Stat**](/windows/win32/Objidl/nf-objidl-istorage-stat?branch=master).

</dd> <dt>

<span id="IPropertyStorage__Commit"></span><span id="ipropertystorage__commit"></span><span id="IPROPERTYSTORAGE__COMMIT"></span>[**IPropertyStorage::Commit**](/windows/win32/Propidl/nf-propidl-ipropertystorage-commit?branch=master)
</dt> <dd>

For both simple and nonsimple property sets, flushes the property set memory image to the underlying storage. In addition, for nonsimple transacted-mode property sets, this method performs a commit (as in [**IStorage::Commit**](/windows/win32/Objidl/nf-objidl-istorage-commit?branch=master)) on the storage which contains the property set.

</dd> <dt>

<span id="IPropertyStorage__Revert"></span><span id="ipropertystorage__revert"></span><span id="IPROPERTYSTORAGE__REVERT"></span>[**IPropertyStorage::Revert**](/windows/win32/Propidl/nf-propidl-ipropertystorage-revert?branch=master)
</dt> <dd>

For nonsimple property sets only, calls the [**Revert**](/windows/win32/Propidl/nf-propidl-ipropertystorage-revert?branch=master) method of the underlying storage and reopens the 'contents' stream. For simple property sets, this interface always returns S\_OK. Nonsimple property sets are those which were created using the PROPSETFLAG\_NONSIMPLE flag in the [**IPropertySetStorage::Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master) method. For more information, see [Storage and Stream Objects for a Property Set](storage-vs--stream-for-a-property-set.md) .

</dd> <dt>

<span id="IPropertyStorage__Enum"></span><span id="ipropertystorage__enum"></span><span id="IPROPERTYSTORAGE__ENUM"></span>[**IPropertyStorage::Enum**](/windows/win32/Propidl/nf-propidl-ipropertystorage-enum?branch=master)
</dt> <dd>

Constructs an instance of [**IEnumSTATPROPSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropstg?branch=master), the methods of which can be called to enumerate the [**STATPROPSTG**](/windows/win32/propidlbase/ns-propidl-tagstatpropstg?branch=master) structures that provide information about each of the properties in the set. This implementation creates an array into which the entire property set is read and which can be shared when **IEnumSTATPROPSTG::Clone** is called. Changes to the property set are not reflected in an open **IEnumSTATPROPSTG** instance. To see such changes, a new instance of this enumerator must be constructed.

</dd> <dt>

<span id="IPropertyStorage__Stat"></span><span id="ipropertystorage__stat"></span><span id="IPROPERTYSTORAGE__STAT"></span>[**IPropertyStorage::Stat**](/windows/win32/Propidl/nf-propidl-ipropertystorage-stat?branch=master)
</dt> <dd>

Fills in the members of a [**STATPROPSETSTG**](/windows/win32/propidlbase/ns-propidl-tagstatpropsetstg?branch=master) structure, which contains data about the property set as a whole. On return, supplies a pointer to the structure. For nonsimple storage sets, this implementation calls [**IStorage::Stat**](/windows/win32/Objidl/nf-objidl-istorage-stat?branch=master) (or [**IStream::Stat**](/windows/win32/Objidl/nf-objidl-istream-stat?branch=master)) to get the times from the underlying storage or stream. For simple storage sets, no times are maintained.

</dd> <dt>

<span id="IPropertyStorage__SetTimes"></span><span id="ipropertystorage__settimes"></span><span id="IPROPERTYSTORAGE__SETTIMES"></span>[**IPropertyStorage::SetTimes**](/windows/win32/Propidl/nf-propidl-ipropertystorage-settimes?branch=master)
</dt> <dd>

For nonsimple property sets only, sets the times supported by the underlying storage. The compound file storage implementation supports all three: modification, access, and creation. This implementation of [**SetTimes**](/windows/win32/Propidl/nf-propidl-ipropertystorage-settimes?branch=master) calls the [**IStorage::SetElementTimes**](/windows/win32/Objidl/nf-objidl-istorage-setelementtimes?branch=master) method of the underlying storage to retrieve these times.

</dd> </dl>

## Related topics

<dl> <dt>

[**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master)
</dt> <dt>

[**IStorage::SetElementTimes**](/windows/win32/Objidl/nf-objidl-istorage-setelementtimes?branch=master)
</dt> </dl>

 

 




