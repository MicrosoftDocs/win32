---
title: IPropertyStorage-Stand-alone Implementation
description: The system-provided, stand-alone implementation of IPropertySetStorage includes an implementation of IPropertyStorage, the interface that reads and writes properties in a property set storage.
ms.assetid: '8de32538-de11-4e4d-9269-145b2accb099'
keywords: ["IPropertyStorage-Stand-alone Implementation", "IPropertyStorage Strctd Stg , implementations, stand-alone"]
---

# IPropertyStorage-Stand-alone Implementation

The system-provided, stand-alone implementation of [**IPropertySetStorage**](ipropertysetstorage.md) includes an implementation of [**IPropertyStorage**](ipropertystorage.md), the interface that reads and writes properties in a property set storage. The **IPropertySetStorage** interface creates and opens property sets in a storage. The [**IEnumSTATPROPSTG**](ienumstatpropstg.md) and [**IEnumSTATPROPSETSTG**](ienumstatpropsetstg.md) interfaces are also provided in the stand-alone implementation.

To get a pointer to the stand-alone implementation of [**IPropertyStorage**](ipropertystorage.md), call the [**StgCreatePropStg**](stgcreatepropstg.md) function to create a new property set or [**StgOpenPropStg**](stgopenpropstg.md) to obtain the interface pointer on an existing property set (or call the [**Create**](ipropertysetstorage-create.md) or [**Open**](ipropertysetstorage-open.md) methods of the [**IPropertySetStorage**](ipropertysetstorage.md) stand-alone implementation).

The stand-alone implementation of [**IPropertyStorage**](ipropertystorage.md) creates property sets on any storage or stream object, not just on compound file storages and streams. The stand-alone implementation does not depend on compound files and can be used with any implementation of structured storages. For more information about the compound file implementation of this interface, see [IPropertyStorage-Compound File Implementation](ipropertystorage-compound-file-implementation.md).

## When to Use

Use [**IPropertyStorage**](ipropertystorage.md) to manage properties within a single property set. Its methods support reading, writing, and deleting both properties and the optional string names that can be associated with property IDs. Other methods support the standard commit and revert storage operations. There is also a method that sets times associated with the property storage, and another that permits the assignment of a CLSID to be used to associate other code, such as user interface code, with the property set. The [**Enum**](ipropertystorage-enum.md) method supplies a pointer to the stand-alone implementation of [**IEnumSTATPROPSTG**](ienumstatpropstg.md), which enumerates the properties in the set.

## Version 0 and Version 1 Property Set Formats

The stand-alone implementation of [**IPropertyStorage**](ipropertystorage.md) supports both the version 0 and the version 1 property set serialization formats. For more information, see [Property Set Serialization](version-0-vs--version-1-property-set-serialization.md). Property sets are created in version 0 format and remain in that format unless new features are requested. At that time, the format is updated to version 1.

For example, if a property set is created with the PROPSETFLAG\_DEFAULT flag, its format is version 0. As long as property types that conform to the version 0 format are written to and read from that property set, the property set remains in version 0 format. If a version 1 property type is written to the property set, the property set is automatically updated to version 1. Subsequently, that property set can no longer be read by implementations that only understand version 0.

## IPropertyStorage and Variant Types

The stand-alone implementation of [**IPropertyStorage**](ipropertystorage.md) does not support the variant types VT\_UNKNOWN or VT\_DISPATCH in the **vt** member of the [**PROPVARIANT**](propvariant.md) structure.

The following variant types are supported within a SafeArray; that is, these values can be combined with VT\_ARRAY in the **vt** member of the [**PROPVARIANT**](propvariant.md) structure.



Variant types supported within SafeArray by compound file implementation of [**IPropertyStorage**](ipropertystorage.md)

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

 



 

When VT\_VARIANT is combined with VT\_ARRAY, the SafeArray itself holds [**PROPVARIANT**](propvariant.md) structures. However, the types of these elements must be taken from the preceding list, cannot be VT\_VARIANT, and cannot include the VT\_VECTOR, VT\_ARRAY, or VT\_BYREF indicators.

## IPropertyStorage Methods

The stand-alone implementation of [**IPropertyStorage**](ipropertystorage.md) supports the following methods:

<dl> <dt>

<span id="IPropertyStorage__ReadMultiple"></span><span id="ipropertystorage__readmultiple"></span><span id="IPROPERTYSTORAGE__READMULTIPLE"></span>[**IPropertyStorage::ReadMultiple**](ipropertystorage-readmultiple.md)
</dt> <dd>

Reads the properties specified in the *rgpspec* array and supplies the values of all valid properties in the *rgvar* array of [**PROPVARIANT**](propvariant.md) elements.

In the system-provided, stand-alone implementation, duplicate property identifiers that refer to stream- or storage-types result in multiple calls to [**IStorage::OpenStream**](istorage-openstream.md) or [**IStorage::OpenStorage**](istorage-openstorage.md) and the success or failure of [**ReadMultiple**](ipropertystorage-readmultiple.md) depends on the underlying storage implementation's ability to share open storages.

In addition, to ensure thread-safe operation if the same stream- or storage-valued property is requested multiple times through the same [**IPropertyStorage**](ipropertystorage.md) pointer, the open will succeed or fail depending on whether or not the property is already open and on whether the underlying file system handles multiple opens of a stream or storage. Thus, the [**ReadMultiple**](ipropertystorage-readmultiple.md) operation on a stream- or storage-valued property always results in a call to [**IStorage::OpenStream**](istorage-openstream.md), or [**IStorage::OpenStorage**](istorage-openstorage.md), passing the access (STGM\_READWRITE, for example) and share values (STGM\_SHARE\_EXCLUSIVE, for example) specified when the property set was originally opened or created.

If the method fails, the values written to *rgvar*\[\] are undefined. If some stream- or storage-valued properties are opened successfully but an error occurs before execution is complete, these properties should be released before the method returns.

</dd> <dt>

<span id="IPropertyStorage__WriteMultiple"></span><span id="ipropertystorage__writemultiple"></span><span id="IPROPERTYSTORAGE__WRITEMULTIPLE"></span>[**IPropertyStorage::WriteMultiple**](ipropertystorage-writemultiple.md)
</dt> <dd>

Writes the properties specified in the *rgpspec*\[\] array, assigning them the [**PROPVARIANT**](propvariant.md) tags and values specified in *rgvar*\[\]. Properties that already exist are assigned the specified **PROPVARIANT** values, and properties that do not currently exist are created.

</dd> <dt>

<span id="IPropertyStorage__DeleteMultiple"></span><span id="ipropertystorage__deletemultiple"></span><span id="IPROPERTYSTORAGE__DELETEMULTIPLE"></span>[**IPropertyStorage::DeleteMultiple**](ipropertystorage-deletemultiple.md)
</dt> <dd>

Deletes the properties specified in the *rgpspec*\[\].

</dd> <dt>

<span id="IPropertyStorage__ReadPropertyNames"></span><span id="ipropertystorage__readpropertynames"></span><span id="IPROPERTYSTORAGE__READPROPERTYNAMES"></span>[**IPropertyStorage::ReadPropertyNames**](ipropertystorage-readpropertynames.md)
</dt> <dd>

Reads existing string names associated with the property IDs specified in the *rgpropid*\[\] array.

</dd> <dt>

<span id="IPropertyStorage__WritePropertyNames"></span><span id="ipropertystorage__writepropertynames"></span><span id="IPROPERTYSTORAGE__WRITEPROPERTYNAMES"></span>[**IPropertyStorage::WritePropertyNames**](ipropertystorage-writepropertynames.md)
</dt> <dd>

Assigns string names specified in the *rglpwstrName* array to property IDs specified in the *rgpropid* array.

</dd> <dt>

<span id="IPropertyStorage__DeletePropertyNames"></span><span id="ipropertystorage__deletepropertynames"></span><span id="IPROPERTYSTORAGE__DELETEPROPERTYNAMES"></span>[**IPropertyStorage::DeletePropertyNames**](ipropertystorage-deletepropertynames.md)
</dt> <dd>

Deletes the string names of the property IDs specified in the *rgpropid* array by writing **NULL** to the property name.

</dd> <dt>

<span id="IPropertyStorage__SetClass"></span><span id="ipropertystorage__setclass"></span><span id="IPROPERTYSTORAGE__SETCLASS"></span>[**IPropertyStorage::SetClass**](ipropertystorage-setclass.md)
</dt> <dd>

Sets the **CLSID** of the property set stream. In the stand-alone implementation, setting the CLSID on a nonsimple property set (one that can contain storage- or stream-valued properties, as described in [**IPropertySetStorage::Create**](ipropertysetstorage-create.md)) also sets the CLSID on the underlying substorage so that it can be obtained through a call to [**IStorage::Stat**](istorage-stat.md).

</dd> <dt>

<span id="IPropertyStorage__Commit"></span><span id="ipropertystorage__commit"></span><span id="IPROPERTYSTORAGE__COMMIT"></span>[**IPropertyStorage::Commit**](ipropertystorage-commit.md)
</dt> <dd>

For both simple and nonsimple property sets, flushes the memory image to the disk subsystem. In addition, for nonsimple transacted-mode property sets, this method calls [**IStorage::Commit**](istorage-commit.md) on the property set.

</dd> <dt>

<span id="IPropertyStorage__Revert"></span><span id="ipropertystorage__revert"></span><span id="IPROPERTYSTORAGE__REVERT"></span>[**IPropertyStorage::Revert**](ipropertystorage-revert.md)
</dt> <dd>

For nonsimple property sets only, calls the [**Revert**](ipropertystorage-revert.md) method of the underlying storage and reopens the 'contents' stream. For simple property sets, only returns E\_OK.

</dd> <dt>

<span id="IPropertyStorage__Enum"></span><span id="ipropertystorage__enum"></span><span id="IPROPERTYSTORAGE__ENUM"></span>[**IPropertyStorage::Enum**](ipropertystorage-enum.md)
</dt> <dd>

Creates an enumerator object that implements [**IEnumSTATPROPSTG**](ienumstatpropstg.md), the methods of which can be called to enumerate the [**STATPROPSTG**](statpropstg.md) structures that provide information about each of the properties in the set.

This implementation creates an array into which the entire property set is read and which can be shared when [**IEnumSTATPROPSTG::Clone**](ienumstatpropstg.md) is called.

</dd> <dt>

<span id="IPropertyStorage__Stat"></span><span id="ipropertystorage__stat"></span><span id="IPROPERTYSTORAGE__STAT"></span>[**IPropertyStorage::Stat**](ipropertystorage-stat.md)
</dt> <dd>

Fills in the members of a [**STATPROPSETSTG**](statpropsetstg.md) structure, which contains information about the property set as a whole. On return, supplies a pointer to the structure.

For nonsimple storage sets, this implementation calls [**IStorage::Stat**](istorage-stat.md) (or [**IStream::Stat**](istream-stat.md)) to get the information from the underlying storage or stream.

</dd> <dt>

<span id="IPropertyStorage__SetTimes"></span><span id="ipropertystorage__settimes"></span><span id="IPROPERTYSTORAGE__SETTIMES"></span>[**IPropertyStorage::SetTimes**](ipropertystorage-settimes.md)
</dt> <dd>

For nonsimple property sets only, sets the times supported by the underlying storage. This implementation of [**SetTimes**](ipropertystorage-settimes.md) calls the [**IStorage::SetElementTimes**](istorage-setelementtimes.md) method of the underlying storage to modify the times. It supports the times supported by the underlying method which can be modification time, access time, or creation time.

</dd> </dl>

## Related topics

<dl> <dt>

[IPropertySetStorage-Stand-alone Implementation](ipropertysetstorage-stand-alone-implementation.md)
</dt> <dt>

[**IPropertyStorage**](ipropertystorage.md)
</dt> <dt>

[**IStorage::SetElementTimes**](istorage-setelementtimes.md)
</dt> <dt>

[**StgOpenPropStg**](stgopenpropstg.md)
</dt> <dt>

[**StgCreatePropStg**](stgcreatepropstg.md)
</dt> <dt>

[**StgCreatePropSetStg**](stgcreatepropsetstg.md)
</dt> </dl>

 

 




