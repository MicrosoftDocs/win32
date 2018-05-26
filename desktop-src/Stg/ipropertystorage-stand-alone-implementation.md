---
title: IPropertyStorage-Stand-alone Implementation
description: The system-provided, stand-alone implementation of IPropertySetStorage includes an implementation of IPropertyStorage, the interface that reads and writes properties in a property set storage.
ms.assetid: 8de32538-de11-4e4d-9269-145b2accb099
keywords:
- IPropertyStorage-Stand-alone Implementation
- IPropertyStorage Strctd Stg , implementations, stand-alone
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPropertyStorage-Stand-alone Implementation

The system-provided, stand-alone implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) includes an implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master), the interface that reads and writes properties in a property set storage. The **IPropertySetStorage** interface creates and opens property sets in a storage. The [**IEnumSTATPROPSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropstg?branch=master) and [**IEnumSTATPROPSETSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropsetstg?branch=master) interfaces are also provided in the stand-alone implementation.

To get a pointer to the stand-alone implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master), call the [**StgCreatePropStg**](/windows/win32/coml2api/nf-coml2api-stgcreatepropstg?branch=master) function to create a new property set or [**StgOpenPropStg**](/windows/win32/coml2api/nf-coml2api-stgopenpropstg?branch=master) to obtain the interface pointer on an existing property set (or call the [**Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master) or [**Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master) methods of the [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) stand-alone implementation).

The stand-alone implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) creates property sets on any storage or stream object, not just on compound file storages and streams. The stand-alone implementation does not depend on compound files and can be used with any implementation of structured storages. For more information about the compound file implementation of this interface, see [IPropertyStorage-Compound File Implementation](ipropertystorage-compound-file-implementation.md).

## When to Use

Use [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) to manage properties within a single property set. Its methods support reading, writing, and deleting both properties and the optional string names that can be associated with property IDs. Other methods support the standard commit and revert storage operations. There is also a method that sets times associated with the property storage, and another that permits the assignment of a CLSID to be used to associate other code, such as user interface code, with the property set. The [**Enum**](/windows/win32/Propidl/nf-propidl-ipropertystorage-enum?branch=master) method supplies a pointer to the stand-alone implementation of [**IEnumSTATPROPSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropstg?branch=master), which enumerates the properties in the set.

## Version 0 and Version 1 Property Set Formats

The stand-alone implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) supports both the version 0 and the version 1 property set serialization formats. For more information, see [Property Set Serialization](version-0-vs--version-1-property-set-serialization.md). Property sets are created in version 0 format and remain in that format unless new features are requested. At that time, the format is updated to version 1.

For example, if a property set is created with the PROPSETFLAG\_DEFAULT flag, its format is version 0. As long as property types that conform to the version 0 format are written to and read from that property set, the property set remains in version 0 format. If a version 1 property type is written to the property set, the property set is automatically updated to version 1. Subsequently, that property set can no longer be read by implementations that only understand version 0.

## IPropertyStorage and Variant Types

The stand-alone implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) does not support the variant types VT\_UNKNOWN or VT\_DISPATCH in the **vt** member of the [**PROPVARIANT**](/windows/win32/propidlbase/ns-propidl-tagpropvariant?branch=master) structure.

The following variant types are supported within a SafeArray; that is, these values can be combined with VT\_ARRAY in the **vt** member of the [**PROPVARIANT**](/windows/win32/propidlbase/ns-propidl-tagpropvariant?branch=master) structure.



Variant types supported within SafeArray by compound file implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master)

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

The stand-alone implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) supports the following methods:

<dl> <dt>

<span id="IPropertyStorage__ReadMultiple"></span><span id="ipropertystorage__readmultiple"></span><span id="IPROPERTYSTORAGE__READMULTIPLE"></span>[**IPropertyStorage::ReadMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-readmultiple?branch=master)
</dt> <dd>

Reads the properties specified in the *rgpspec* array and supplies the values of all valid properties in the *rgvar* array of [**PROPVARIANT**](/windows/win32/propidlbase/ns-propidl-tagpropvariant?branch=master) elements.

In the system-provided, stand-alone implementation, duplicate property identifiers that refer to stream- or storage-types result in multiple calls to [**IStorage::OpenStream**](/windows/win32/Objidl/nf-objidl-istorage-openstream?branch=master) or [**IStorage::OpenStorage**](/windows/win32/Objidl/nf-objidl-istorage-openstorage?branch=master) and the success or failure of [**ReadMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-readmultiple?branch=master) depends on the underlying storage implementation's ability to share open storages.

In addition, to ensure thread-safe operation if the same stream- or storage-valued property is requested multiple times through the same [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) pointer, the open will succeed or fail depending on whether or not the property is already open and on whether the underlying file system handles multiple opens of a stream or storage. Thus, the [**ReadMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-readmultiple?branch=master) operation on a stream- or storage-valued property always results in a call to [**IStorage::OpenStream**](/windows/win32/Objidl/nf-objidl-istorage-openstream?branch=master), or [**IStorage::OpenStorage**](/windows/win32/Objidl/nf-objidl-istorage-openstorage?branch=master), passing the access (STGM\_READWRITE, for example) and share values (STGM\_SHARE\_EXCLUSIVE, for example) specified when the property set was originally opened or created.

If the method fails, the values written to *rgvar*\[\] are undefined. If some stream- or storage-valued properties are opened successfully but an error occurs before execution is complete, these properties should be released before the method returns.

</dd> <dt>

<span id="IPropertyStorage__WriteMultiple"></span><span id="ipropertystorage__writemultiple"></span><span id="IPROPERTYSTORAGE__WRITEMULTIPLE"></span>[**IPropertyStorage::WriteMultiple**](/windows/win32/Propidl/nf-propidl-ipropertystorage-writemultiple?branch=master)
</dt> <dd>

Writes the properties specified in the *rgpspec*\[\] array, assigning them the [**PROPVARIANT**](/windows/win32/propidlbase/ns-propidl-tagpropvariant?branch=master) tags and values specified in *rgvar*\[\]. Properties that already exist are assigned the specified **PROPVARIANT** values, and properties that do not currently exist are created.

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

Deletes the string names of the property IDs specified in the *rgpropid* array by writing **NULL** to the property name.

</dd> <dt>

<span id="IPropertyStorage__SetClass"></span><span id="ipropertystorage__setclass"></span><span id="IPROPERTYSTORAGE__SETCLASS"></span>[**IPropertyStorage::SetClass**](/windows/win32/Propidl/nf-propidl-ipropertystorage-setclass?branch=master)
</dt> <dd>

Sets the **CLSID** of the property set stream. In the stand-alone implementation, setting the CLSID on a nonsimple property set (one that can contain storage- or stream-valued properties, as described in [**IPropertySetStorage::Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master)) also sets the CLSID on the underlying substorage so that it can be obtained through a call to [**IStorage::Stat**](/windows/win32/Objidl/nf-objidl-istorage-stat?branch=master).

</dd> <dt>

<span id="IPropertyStorage__Commit"></span><span id="ipropertystorage__commit"></span><span id="IPROPERTYSTORAGE__COMMIT"></span>[**IPropertyStorage::Commit**](/windows/win32/Propidl/nf-propidl-ipropertystorage-commit?branch=master)
</dt> <dd>

For both simple and nonsimple property sets, flushes the memory image to the disk subsystem. In addition, for nonsimple transacted-mode property sets, this method calls [**IStorage::Commit**](/windows/win32/Objidl/nf-objidl-istorage-commit?branch=master) on the property set.

</dd> <dt>

<span id="IPropertyStorage__Revert"></span><span id="ipropertystorage__revert"></span><span id="IPROPERTYSTORAGE__REVERT"></span>[**IPropertyStorage::Revert**](/windows/win32/Propidl/nf-propidl-ipropertystorage-revert?branch=master)
</dt> <dd>

For nonsimple property sets only, calls the [**Revert**](/windows/win32/Propidl/nf-propidl-ipropertystorage-revert?branch=master) method of the underlying storage and reopens the 'contents' stream. For simple property sets, only returns E\_OK.

</dd> <dt>

<span id="IPropertyStorage__Enum"></span><span id="ipropertystorage__enum"></span><span id="IPROPERTYSTORAGE__ENUM"></span>[**IPropertyStorage::Enum**](/windows/win32/Propidl/nf-propidl-ipropertystorage-enum?branch=master)
</dt> <dd>

Creates an enumerator object that implements [**IEnumSTATPROPSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropstg?branch=master), the methods of which can be called to enumerate the [**STATPROPSTG**](/windows/win32/propidlbase/ns-propidl-tagstatpropstg?branch=master) structures that provide information about each of the properties in the set.

This implementation creates an array into which the entire property set is read and which can be shared when [**IEnumSTATPROPSTG::Clone**](/windows/win32/propidlbase/nn-propidl-ienumstatpropstg?branch=master) is called.

</dd> <dt>

<span id="IPropertyStorage__Stat"></span><span id="ipropertystorage__stat"></span><span id="IPROPERTYSTORAGE__STAT"></span>[**IPropertyStorage::Stat**](/windows/win32/Propidl/nf-propidl-ipropertystorage-stat?branch=master)
</dt> <dd>

Fills in the members of a [**STATPROPSETSTG**](/windows/win32/propidlbase/ns-propidl-tagstatpropsetstg?branch=master) structure, which contains information about the property set as a whole. On return, supplies a pointer to the structure.

For nonsimple storage sets, this implementation calls [**IStorage::Stat**](/windows/win32/Objidl/nf-objidl-istorage-stat?branch=master) (or [**IStream::Stat**](/windows/win32/Objidl/nf-objidl-istream-stat?branch=master)) to get the information from the underlying storage or stream.

</dd> <dt>

<span id="IPropertyStorage__SetTimes"></span><span id="ipropertystorage__settimes"></span><span id="IPROPERTYSTORAGE__SETTIMES"></span>[**IPropertyStorage::SetTimes**](/windows/win32/Propidl/nf-propidl-ipropertystorage-settimes?branch=master)
</dt> <dd>

For nonsimple property sets only, sets the times supported by the underlying storage. This implementation of [**SetTimes**](/windows/win32/Propidl/nf-propidl-ipropertystorage-settimes?branch=master) calls the [**IStorage::SetElementTimes**](/windows/win32/Objidl/nf-objidl-istorage-setelementtimes?branch=master) method of the underlying storage to modify the times. It supports the times supported by the underlying method which can be modification time, access time, or creation time.

</dd> </dl>

## Related topics

<dl> <dt>

[IPropertySetStorage-Stand-alone Implementation](ipropertysetstorage-stand-alone-implementation.md)
</dt> <dt>

[**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master)
</dt> <dt>

[**IStorage::SetElementTimes**](/windows/win32/Objidl/nf-objidl-istorage-setelementtimes?branch=master)
</dt> <dt>

[**StgOpenPropStg**](/windows/win32/coml2api/nf-coml2api-stgopenpropstg?branch=master)
</dt> <dt>

[**StgCreatePropStg**](/windows/win32/coml2api/nf-coml2api-stgcreatepropstg?branch=master)
</dt> <dt>

[**StgCreatePropSetStg**](/windows/win32/coml2api/nf-coml2api-stgcreatepropsetstg?branch=master)
</dt> </dl>

 

 




