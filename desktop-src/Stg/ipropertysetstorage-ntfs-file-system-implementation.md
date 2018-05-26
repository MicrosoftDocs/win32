---
title: IPropertySetStorage-NTFS File System Implementation
description: NTFS version 5.0 provides an implementation of IPropertySetStorage for files on an NTFS volume when the files themselves are not compound files.
ms.assetid: cd7290bb-bb4e-4dea-9bf6-2e1fdd0ebae8
keywords:
- IPropertySetStorage Strctd Stg , implementations, NTFS file system
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IPropertySetStorage-NTFS File System Implementation

NTFS version 5.0 provides an implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) for files on an NTFS volume when the files themselves are not compound files. The NTFS implementation is equivalent to the [compound file implementation](ipropertysetstorage-compound-file-implementation.md). For more information about exceptions, see Remarks.

**To get a pointer to the NTFS implementation of IPropertySetStorage**

1.  Call [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master) and specify **STGFMT\_FILE** in the *grfFlags* parameter to create a new file.
2.  Call [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) and specify either the **STGFMT\_FILE** or **STGFMT\_ANY** enumeration value in the *grfFlags* parameter to open an existing file.

However, you cannot obtain the NTFS implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) for a compound file. When opening a compound file with [**StgOpenStorage**](/windows/win32/coml2api/nf-coml2api-stgopenstorage?branch=master), specifying the **STGFMT\_FILE** enumeration value results in an error.

Also, simple property sets cannot be transacted. That is, you cannot specify **STGM\_TRANSACTED** in the *grfmode* parameter of the [**Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master) and [**Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master) methods unless you also specify **PROPSETFLAG\_NONSIMPLE** in the *grfFlags* parameter. The property set storage object itself does not support transaction processing.

## When to Use

Call the [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) methods to create, open, or delete property sets in the current NTFS property set storage. There is also a method, [**IPropertySetStorage::Enum**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-enum?branch=master), that supplies a pointer to an enumerator that can be used to enumerate the property sets in the storage.

## Compatibility

The NTFS implementations of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) and [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) are available starting with Windows 2000. Earlier versions cannot access these property sets.

The NTFS implementation stores property sets in alternate streams of an NTFS file. The alternate streams must be copied when the main file is copied.

> \[!Caution\]  
> Not all file systems support such streams. If an NTFS file with property sets is copied to a FAT volume, only the data in the file is copied; the property set is lost. The [**CopyFile**](https://msdn.microsoft.com/library/windows/desktop/aa363851) function does not return an error in this case.

 

> \[!Caution\]  
> If the computer performing the file copy is not a computer running on Windows 2000 or later, the property sets may be lost. For example, if a computer running on Windows 95 operating system copies an NTFS file, the property set is lost even if the destination file is also on an NTFS volume.

 

## Methods

The NTFS file system implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) supports the following methods.

<dl> <dt>

<span id="IPropertySetStorage__Create"></span><span id="ipropertysetstorage__create"></span><span id="IPROPERTYSETSTORAGE__CREATE"></span>[**IPropertySetStorage::Create**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-create?branch=master)
</dt> <dd>

Creates a new property set in the current NTFS file storage and, on return, supplies an interface pointer to the [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) NTFS file implementation. The sharing mode specified in the *grfmode* parameter must be **STGM\_SHARE\_EXCLUSIVE**.

</dd> <dt>

<span id="IPropertySetStorage__Open"></span><span id="ipropertysetstorage__open"></span><span id="IPROPERTYSETSTORAGE__OPEN"></span>[**IPropertySetStorage::Open**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-open?branch=master)
</dt> <dd>

Opens an existing property set in the current property storage. On return, it supplies an interface pointer to the NTFS file implementation of [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master). The sharing mode specified in the *grfmode* parameter must be **STGM\_SHARE\_EXCLUSIVE**.

</dd> <dt>

<span id="IPropertySetStorage__Delete"></span><span id="ipropertysetstorage__delete"></span><span id="IPROPERTYSETSTORAGE__DELETE"></span>[**IPropertySetStorage::Delete**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-delete?branch=master)
</dt> <dd>

Deletes a property set in the current property storage.

</dd> <dt>

<span id="IPropertySetStorage__Enum"></span><span id="ipropertysetstorage__enum"></span><span id="IPROPERTYSETSTORAGE__ENUM"></span>[**IPropertySetStorage::Enum**](/windows/win32/Propidl/nf-propidl-ipropertysetstorage-enum?branch=master)
</dt> <dd>

Creates an object used to enumerate [**STATPROPSETSTG**](/windows/win32/propidlbase/ns-propidl-tagstatpropsetstg?branch=master) structures. Each **STATPROPSETSTG** structure provides data about a single property set.

</dd> </dl>

## Remarks

The NTFS implementations of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) and [**IPropertyStorage**](/windows/win32/Propidl/nn-propidl-ipropertystorage?branch=master) store property sets in a file without affecting the contents of that file. For example, if you create a property set in an HTML file named Default.htm, that file still displays properly in a Web browser. That is, changes to a file using these two interfaces are undetectable when accessing a file with the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.

The NTFS implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) provides a safe implementation when used to write property sets to a file on an NTFS version 5.0 volume. Such property sets cannot be corrupted by the implementation even in the event of a system failure. For example, if the power to a system fails during a call to [**IPropertyStorage::Commit**](/windows/win32/Propidl/nf-propidl-ipropertystorage-commit?branch=master) while the property set is flushed to the disk, the property set is never left in an intermediate state. Either the previous version of the property set remains or all of the updates are saved.

The NTFS implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) differs from the compound file implementation in the following ways:

-   A [**STATPROPSETSTG**](/windows/win32/propidlbase/ns-propidl-tagstatpropsetstg?branch=master) structure obtained from the [**IEnumSTATPROPSETSTG**](/windows/win32/propidlbase/nn-propidl-ienumstatpropsetstg?branch=master) interface contains a **clsid** member whose value is always zero (**CLSID\_NULL**). With the compound file implementation, the correct **clsid** member is returned for non-simple (see [Storage and Stream Objects for a Property Set](storage-vs--stream-for-a-property-set.md)) property sets.
-   When obtaining an NTFS implementation of [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) interface pointer using the [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master) or [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) function, the *grfmode* parameter must follow the same rules as for the compound file implementation.

    In addition, the following flags may not be used:

    **STGM\_SIMPLE**, **STGM\_TRANSACTED**, **STGM\_CONVERT**, **STGM\_PRIORITY**, and **STGM\_DELETEONRELEASE**.

-   When an NTFS [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) interface is obtained by the [**StgCreateStorageEx**](/windows/win32/coml2api/nf-coml2api-stgcreatestorageex?branch=master) or [**StgOpenStorageEx**](/windows/win32/coml2api/nf-coml2api-stgopenstorageex?branch=master) functions, the sharing modes primarily apply to other instances of that interface, and not to instances of opening the file itself. For example, if an NTFS **IPropertySetStorage** interface is opened by calling the **StgOpenStorageEx** function, with the *grfmode* parameter set to **STGM\_READWRITE\|STGM\_SHARE\_EXCLUSIVE**, it is possible to open the file with the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function.

    Such simultaneous instances of opening this interface are subject to the following constraints: the *dwShareMode* parameter in the [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858) function must specify the **FILE\_SHARE\_READ** flag, and the *dwAccess* parameter must not specify the **DELETE** flag. Also, the [**DeleteFile**](https://msdn.microsoft.com/library/windows/desktop/aa363915) and [**MoveFile**](https://msdn.microsoft.com/library/windows/desktop/aa365239) functions must not be called on a file for which these property set interfaces are open, as these functions require **DELETE** access to the file.

-   If an NTFS [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) method is opened as read-only, and the file currently has no property sets, the object returned will not actually hold open the file. Consequently, other openings of that file will succeed, even if the sharing mode of the original open operation would otherwise reject it.

    Example; if an NTFS [**IPropertySetStorage**](/windows/win32/Propidl/nn-propidl-ipropertysetstorage?branch=master) is opened in the mode **STGM\_READ\|STGM\_SHARE\_EXCLUSIVE**, and the file has no property sets, it will be possible to simultaneously open the file **STGM\_READWRITE\|STGM\_SHARE\_EXCLUSIVE**.

## Related topics

<dl> <dt>

[IPropertyStorage-NTFS File System Implementation](ipropertystorage-ntfs-file-system-implementation.md)
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

 

 




