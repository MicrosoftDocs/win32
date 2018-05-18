---
title: IPropertyStorage-NTFS File System Implementation
description: The NTFS version 5.0 provides an implementation of the IPropertyStorage interface for files on an NTFS volume when the files are not compound files.
ms.assetid: 'd0ffd975-5bc2-4de3-b0c1-c9188541f46a'
keywords: ["IPropertyStorage Strctd Stg , implementations, NTFS file system"]
---

# IPropertyStorage-NTFS File System Implementation

The NTFS version 5.0 provides an implementation of the [**IPropertyStorage**](ipropertystorage.md) interface for files on an NTFS volume when the files are not compound files.

**To get a pointer to the NTFS file system implementation of IPropertySetStorage**

1.  Call [**IPropertySetStorage::Create**](ipropertysetstorage-create.md) using the NTFS implementation of [**IPropertySetStorage**](ipropertysetstorage.md).
2.  Call [**IPropertySetStorage::Open**](ipropertysetstorage-open.md) using the NTFS implementation of [**IPropertySetStorage**](ipropertysetstorage.md).

## When to Use

Use [**IPropertyStorage**](ipropertystorage.md) to manage properties within a single property set. Its methods support reading, writing, and deleting properties and the optional string names that can be associated with property identifiers. Another method enables you to set times associated with the property storage, and another permits the assignment of a CLSID, used to associate other code, such as user interface (UI) code, with the property set. Calling the [**Enum**](ipropertystorage-enum.md) method supplies a pointer to the NTFS implementation of [**IEnumSTATPROPSTG**](ienumstatpropstg.md), which enables you to enumerate the properties in the set.

## Remarks

The NTFS implementation provides essentially the same features as the compound file implementation. For more information, see [IPropertyStorage-Compound File Implementation](ipropertystorage-compound-file-implementation.md).

Because NTFS is a robust file system, an NTFS property set will never be left in an incorrect state. When the content of an NTFS [**IPropertyStorage**](ipropertystorage.md) is flushed to the underlying NTFS file, either all or none of the state is written to the file as an atomic operation, even if there is a failure during the operation such as an abnormal process termination. To achieve similar behavior with the compound file implementation, the parent [**IPropertySetStorage**](ipropertysetstorage.md) interface must be opened in transacted mode.

This level of robustness is only possible when accessing an NTFS property set on an NTFS 5.0 volume. It is possible to access NTFS property sets on earlier versions of NTFS (for example, a computer running on Windows NT or Windows 2000 that accesses the property sets on a file server computer running on Windows NT 4.0), but they are not guaranteed to be in a correct state in the event of an unexpected failure.

Although the NTFS implementation of [**IPropertySetStorage**](ipropertysetstorage.md) does not support transactioning, the NTFS implementation of [**IPropertyStorage**](ipropertystorage.md) supports it. That is, **STGM\_TRANSACTED** may be specified in the *grfMode* parameter to the [**Create**](ipropertysetstorage-create.md) and [**Open**](ipropertysetstorage-open.md) methods of **IPropertySetStorage**. As in the compound file implementation, transacted mode is possible only for nonsimple property storages (specifying **PROPSETFLAG\_NONSIMPLE** in the *grfFlags* parameter).

## Related topics

<dl> <dt>

[**IPropertyStorage**](ipropertystorage.md)
</dt> <dt>

[IPropertySetStorage-NTFS File System Implementation](ipropertysetstorage-ntfs-file-system-implementation.md)
</dt> </dl>

 

 




