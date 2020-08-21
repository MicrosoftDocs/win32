---
title: Property Storage Considerations
description: IPropertyStorage ReadMultiple reads as many of the properties specified in the rgpspec array as are found in the property set.
ms.assetid: 7540966f-a3b2-46c9-9e04-b15133a517eb
ms.topic: article
ms.date: 05/31/2018
---

# Property Storage Considerations

[**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple) reads as many of the properties specified in the *rgpspec* array as are found in the property set. As long as any of the properties requested is read, a request to retrieve a property that does not exist is not an error. Instead, this must cause VT\_EMPTY to be written for that property to the *rgvar*\[\] array on return. When none of the requested properties exist, the method should return S\_FALSE, and set VT\_EMPTY in each [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant). If any other error is returned, no property values are retrieved, and the caller need not worry about releasing them.

The *rgpspec* parameter is an array of [**PROPSPEC**](/windows/win32/api/propidlbase/ns-propidlbase-propspec) structures, which specify for each property either its property identifier or, if one is assigned, a string identifier. You can map a string to a property identifier by calling [**IPropertyStorage::WritePropertyNames**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writepropertynames). The use of property identifiers is, however, likely to be significantly more efficient than the use of strings.

Properties that are requested by string name (PRSPEC\_LPWSTR) are mapped case-insensitively to property identifiers (IDs) as they are specified in the current property set (and according to the current system locale).

When the property type is VT\_LPSTR and the property is read from an ANSI property set, that is, the code page for the property set is set to something other than Unicode, the value of the property uses the same code page as the property set. When a VT\_LPSTR property is read from a Unicode property set, the value of the property uses the system's current default ANSI code page, that is, the code page returned from the **GetACP** function.

A [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant), except for those that are pointers to streams and storages, is called a simple **PROPVARIANT**. These simple **PROPVARIANT**s receive data by value, so a call to [**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple) supplies a copy of the data that the caller then owns. To create or update these properties, call [**IPropertyStorage::WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple).

In contrast, the variant types VT\_STREAM, VT\_STREAMED\_OBJECT, VT\_STORAGE, and VT\_STORED\_OBJECT are non-simple properties, because rather than supplying a value, the method retrieves a pointer to the indicated interface, from which the data can then be read. These types permit the storage of large amounts of information through a single property. There are several issues that arise in using nonsimple properties.

To create these properties, as for the other properties, call [**IPropertyStorage::WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple). Rather than calling the same method to update, however, it is more efficient to first call [**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple) to get the interface pointer to the stream or storage, then write data using the [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) or [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) methods. A stream or storage opened through a property is always opened in direct mode, so an additional level of nested transaction is not introduced. There may, however, still be a transaction on the property set as a whole, depending on how it was opened or created through [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage). Further, the access and share mode tags specified when the property set is opened or created, are passed to property-based streams or storages.

The lifetimes of property-based stream or storage pointers, although theoretically independent of their associated [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) and [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) pointers, in fact, effectively depend on them. The data visible through the stream or storage is related to the transaction on the property storage object from which it is retrieved, just as for a storage object (supporting [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage)) with contained stream and storage sub-objects. If the transaction on the parent object is aborted, existing [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) and **IStorage** pointers subordinate to that object are no longer accessible. Because **IPropertyStorage** is the only interface on the property storage object, the useful lifetime of the contained **IStream** and **IStorage** pointers is bounded by the lifetime of the **IPropertyStorage** interface.

The implementation must also deal with the situation where the same stream- or storage-valued property is requested multiple times through the same [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) interface instance. For example, in the COM compound file implementation, the open will succeed or fail depending on whether or not the property is already open.

Another issue is multiple opens in transacted mode. The result depends on the isolation level that was specified through a call to [**IPropertySetStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertysetstorage) methods, (either the [**Open**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-open) or [**Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create) method, through the STGM flags) at the time that the property storage was opened.

If the call to open the property set specifies read-write access, [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) and [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream)-valued properties are always opened with read-write access. Data can then be written through these interfaces, changing the value of the property, which is the most efficient way to update these properties. The property value itself does not have an additional level of transaction nesting, so changes are scoped under the transaction (if any) on the property storage object.

## Storage and Stream Properties

To write a stream or storage object to a property set, the property set must have been created as nonsimple. For more information on simple and nonsimple property sets, see the section titled [Storage and Stream Objects for a Property Set](storage-vs--stream-for-a-property-set.md). The following property types, as specified in the *vt* field of the *rgvar* array elements, are stream or storage types: VT\_STREAM, VT\_STORAGE, VT\_STREAMED\_OBJECT, VT\_STORED\_OBJECT.

To write a stream or storage object as a property in a non-simple property set, call [**IPropertyStorage::WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple). While you would also call this method to update simple properties, it is not an efficient way to update stream and storage objects in a property set. This is because updating one of these properties through a call to **WriteMultiple** creates in the property storage object a copy of the passed-in data, and the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) or [**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream) pointers are not retained beyond the duration of this call. It is usually more efficient to update stream or storage objects directly by first calling [**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple) to get the interface pointer to the stream or storage, then writing data through the **IStream** or **IStorage** methods.

For example, you can call [**IPropertyStorage::WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple) to write a **NULL** stream or storage object. The implementation will then create an empty object in the property set. You can then get access to this object by calling [**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple). When you finish updating this object you need not write it to the property set, as your updates were going directly into the property set.

A stream or storage opened through a property is always opened in direct mode, so an additional level of nested transaction is not introduced. There still may be a transaction on the property set as a whole. (For example, if the [**IPropertyStorage**](/windows/desktop/api/Propidl/nn-propidl-ipropertystorage) was obtained by calling [**IPropertySetStorage::Open**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-open) with the STGM\_TRANSACTED flag set in the *grfmode* parameter.) Further, a property-based stream or storage is opened in read-write mode, if possible, given the mode on the property set; otherwise, read mode is used.

As mentioned earlier, when a stream or storage object is written to a property set with the [**WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple) method, a copy of the object is made. When such a copy is made on a stream object, the copy operation starts at the current seek position of the source. The seek position is undefined on failure, but on success it is at the end of the stream; the seek pointer is not restored to its original position.

If a stream or storage property has been read from a property set with [**ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple), is still held open, and a subsequent call to [**WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple) for the same property is made, the **WriteMultiple** operation will succeed. The previously opened stream or storage property is placed in the reverted state (all calls to it will return STG\_E\_REVERTED error).

If the [**WriteMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-writemultiple) method returns an error when writing an array of properties, or even individual non-simple properties, the amount of data actually written is undefined.

## Reference Properties

If a specified [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure includes the VT\_BYREF flag in its **vt** member, the associated property is a reference property. A reference property is automatically dereferenced before writing the value to the property set. For example, if the **vt** member of the **PROPVARIANT** structure specifies a value of type VT\_BYREF \| VT\_I4, the actual value written is a VT\_I4 type. A subsequent call to the [**IPropertyStorage::ReadMultiple**](/windows/desktop/api/Propidl/nf-propidl-ipropertystorage-readmultiple) method returns a value as VT\_I4. Using reference properties is similar to calling the [VariantCopyInd](/windows/win32/api/oleauto/nf-oleauto-variantcopyind) function. [VariantCopyInd](/windows/win32/api/oleauto/nf-oleauto-variantcopyind) frees the destination variant and makes a copy of the source VARIANTARG, performing the necessary indirection if the source is specified to be VT\_BYREF. This function is useful when a copy of a variant is needed, and to guarantee that it is not VT\_BYREF, for example when handling arguments in an implementation of [**IDispatch::Invoke**](/windows/win32/api/oaidl/nf-oaidl-idispatch-invoke).

## Notes to Callers

It is recommended that property sets be created as Unicode, by not setting the PROPSETFLAG\_ANSI flag in the *grfFlags* parameter of [**IPropertySetStorage::Create**](/windows/desktop/api/Propidl/nf-propidl-ipropertysetstorage-create). It is also recommended that you avoid using VT\_LPSTR values, and use VT\_LPWSTR values instead. When the property set code page is Unicode, VT\_LPSTR string values are converted to Unicode when stored, and back to multibyte string values when retrieved. When the code page of the property set is not Unicode, property names, VT\_BSTR strings, and non-simple property values are converted to multibyte strings when stored, and converted back to Unicode when retrieved, all using the current system ANSI code page.

## Notes to Implementers

When allocating a property identifier, the implementation can choose any value not currently in use in the property set for a property identifier, as long as it is not 0 or 1 or greater than 0x80000000, all of which are reserved values. The *propidNameFirst* parameter establishes a minimum value for property identifiers within the set, and must be greater than 1 and less than 0x80000000. See Remarks section above.

## Related topics

<dl> <dt>

[IPropertyStorage-Compound File Implementation](ipropertystorage-compound-file-implementation.md)
</dt> <dt>

[IPropertyStorage-NTFS File System Implementation](ipropertystorage-ntfs-file-system-implementation.md)
</dt> <dt>

[IPropertyStorage-Stand-alone Implementation](ipropertystorage-stand-alone-implementation.md)
</dt> </dl>

 

 