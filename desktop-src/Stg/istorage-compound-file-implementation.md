---
title: IStorage-Compound File Implementation
description: The compound file implementation of IStorage allows you to create and manage substorages and streams within a storage object residing in a compound file object.
ms.assetid: 2a2253f6-d3d3-403e-a9ba-53a541c7a31e
keywords:
- IStorage Strctd Stg ,compound file implementation
ms.topic: article
ms.date: 05/31/2018
---

# IStorage-Compound File Implementation

The compound file implementation of [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) allows you to create and manage substorages and streams within a storage object residing in a compound file object. To create a compound file object and get an **IStorage** pointer, call the API function [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex). To open an existing compound file object and get its root **IStorage** pointer, call [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex).

Applications that use compound storage should be registered in HKEY\_CLASSES\_ROOT\\SystemFileAssociations and should provide their own property handlers. For more information, see the "Registering Verbs and Other File Association Information" section of [Application Registration](/windows/desktop/shell/app-registration).

## When to Use

Most applications use this implementation to create and manage storages and streams.

## Methods

<dl> <dt>

<span id="IStorage__CreateStream"></span><span id="istorage__createstream"></span><span id="ISTORAGE__CREATESTREAM"></span>[**IStorage::CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream)
</dt> <dd>

Creates and opens a stream object with the specified name contained in this storage object. The name must not exceed 31 characters in length (not including the string terminator). The 000 through 01f characters, serving as the first character of the stream/storage name, are reserved for use by OLE. This is a compound file restriction, not a structured storage restriction. The COM-provided compound file implementation of the [**IStorage::CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream) method does not support the following behaviors:

-   The STGM\_DELETEONRELEASE flag is not supported.
-   Transacted mode (STGM\_TRANSACTED) is not supported for stream objects.
-   Opening the same stream more than once from the same storage is not supported. The STGM\_SHARE\_EXCLUSIVE sharing-mode flag must be specified in the *grfMode* parameter.

</dd> <dt>

<span id="IStorage__OpenStream"></span><span id="istorage__openstream"></span><span id="ISTORAGE__OPENSTREAM"></span>[**IStorage::OpenStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstream)
</dt> <dd>

Opens an existing stream object within this storage object using the access modes specified in the *grfMode* parameter. The 000 through 01f characters, serving as the first character of the stream/storage name, are reserved for use by OLE. This is a compound file restriction, not a structured storage restriction. The COM-provided compound file implementation of the [**IStorage::OpenStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstream) method does not support the following behavior:

-   The STGM\_DELETEONRELEASE flag.
-   Transacted mode (STGM\_TRANSACTED) for stream objects.
-   Opening the same stream more than once from the same storage. The STGM\_SHARE\_EXCLUSIVE flag must be specified.

</dd> <dt>

<span id="IStorage__CreateStorage"></span><span id="istorage__createstorage"></span><span id="ISTORAGE__CREATESTORAGE"></span>[**IStorage::CreateStorage**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstorage)
</dt> <dd>

Creates and opens a new storage object with the specified name in the specified access mode. The name must not exceed 31 characters in length (not including the string terminator). The 000 through 01f characters, serving as the first character of the stream/storage name, are reserved for use by OLE. This is a compound file restriction, not a structured storage restriction. The COM-provided compound file implementation of the [**IStorage::CreateStorage**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstorage) method does not support the following behavior:

-   The STGM\_PRIORITY flag for nonroot storages.
-   Opening the same storage object more than once from the same parent storage. The STGM\_SHARE\_EXCLUSIVE flag must be specified.
-   The STGM\_DELETEONRELEASE flag. If this flag is specified, the function returns STG\_E\_INVALIDFLAG.

</dd> <dt>

<span id="IStorage__OpenStorage"></span><span id="istorage__openstorage"></span><span id="ISTORAGE__OPENSTORAGE"></span>[**IStorage::OpenStorage**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstorage)
</dt> <dd>

Opens an existing storage object with the specified name in the specified access mode. The 000 through 01f characters, serving as the first character of the stream/storage name, are reserved for use by OLE. This is a compound file restriction, not a structured storage restriction. The COM-provided compound file implementation of the [**IStorage::OpenStorage**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstorage) method does not support the following behavior:

-   The STGM\_PRIORITY flag for nonroot storages.
-   Opening the same storage object more than once from the same parent storage. The STGM\_SHARE\_EXCLUSIVE flag must be specified.
-   The STGM\_DELETEONRELEASE flag. If this flag is specified, the function returns STG\_E\_INVALIDFUNCTION.

</dd> <dt>

<span id="IStorage__CopyTo"></span><span id="istorage__copyto"></span><span id="ISTORAGE__COPYTO"></span>[**IStorage::CopyTo**](/windows/desktop/api/Objidl/nf-objidl-istorage-copyto)
</dt> <dd>

Copies only the substorages and streams of this open storage object into another storage object. The *rgiidExclude* parameter can be set to IID\_IStream to copy only substorages, or to IID\_IStorage to copy only streams.

</dd> <dt>

<span id="IStorage__MoveElementTo"></span><span id="istorage__moveelementto"></span><span id="ISTORAGE__MOVEELEMENTTO"></span>[**IStorage::MoveElementTo**](/windows/desktop/api/Objidl/nf-objidl-istorage-moveelementto)
</dt> <dd>

Copies or moves a substorage or stream from this storage object to another storage object.

</dd> <dt>

<span id="IStorage__Commit"></span><span id="istorage__commit"></span><span id="ISTORAGE__COMMIT"></span>[**IStorage::Commit**](/windows/desktop/api/Objidl/nf-objidl-istorage-commit)
</dt> <dd>

Ensures that any changes made to a storage object open in transacted mode are reflected in the parent storage; for a root storage, reflects the changes in the actual device; for example, a file on disk. For a root storage object opened in direct mode, this method has no effect except to flush all memory buffers to the disk. For nonroot storage objects in direct mode, this method has no effect.

The COM-provided compound files implementation uses a two-phase commit process unless STGC\_OVERWRITE is specified in the *grfCommitFlags* parameter. This two-phase process ensures the robustness of data, in case the commit operation fails. First, all new data is written to unused space in the underlying file. If necessary, new space is allocated to the file. After this step has been completed, a table in the file is updated using a single-sector write operation to indicate that the new data is to be used in place of the old. The old data becomes free space to be used at the next commit operation. Thus, the old data is available and can be restored if an error occurs when committing changes. If STGC\_OVERWRITE is specified, a single phase commit operation is used. For more information about transacted mode flags, see [**STGC**](/windows/win32/api/wtypes/ne-wtypes-stgc) enumeration.

</dd> <dt>

<span id="IStorage__Revert"></span><span id="istorage__revert"></span><span id="ISTORAGE__REVERT"></span>[**IStorage::Revert**](/windows/desktop/api/Objidl/nf-objidl-istorage-revert)
</dt> <dd>

Discards all changes that have been made to the storage object since the last commit operation.

</dd> <dt>

<span id="IStorage__EnumElements"></span><span id="istorage__enumelements"></span><span id="ISTORAGE__ENUMELEMENTS"></span>[**IStorage::EnumElements**](/windows/desktop/api/Objidl/nf-objidl-istorage-enumelements)
</dt> <dd>

Creates and retrieves a pointer to an enumerator object that can be used to enumerate the storage and stream objects contained within this storage object. The COM-provided compound file implementation takes a snapshot of that information. Therefore, changes to the streams and storages are not reflected in the enumerator until a new enumerator is obtained.

</dd> <dt>

<span id="IStorage__DestroyElement"></span><span id="istorage__destroyelement"></span><span id="ISTORAGE__DESTROYELEMENT"></span>[**IStorage::DestroyElement**](/windows/desktop/api/Objidl/nf-objidl-istorage-destroyelement)
</dt> <dd>

Removes the specified element (substorage or stream) from this storage object.

</dd> <dt>

<span id="IStorage__RenameElement"></span><span id="istorage__renameelement"></span><span id="ISTORAGE__RENAMEELEMENT"></span>[**IStorage::RenameElement**](/windows/desktop/api/Objidl/nf-objidl-istorage-renameelement)
</dt> <dd>

Renames the specified substorage or stream in this storage object. The 000 through 01f characters, serving as the first character of the stream/storage name, are reserved for use by OLE. This is a compound file restriction, not a structured storage restriction.

</dd> <dt>

<span id="IStorage__SetElementTimes"></span><span id="istorage__setelementtimes"></span><span id="ISTORAGE__SETELEMENTTIMES"></span>[**IStorage::SetElementTimes**](/windows/desktop/api/Objidl/nf-objidl-istorage-setelementtimes)
</dt> <dd>

Sets the modification, access, and creation times of the specified storage element. The COM-provided compound-file implementation maintains modification and change times for internal storage objects. Root storage objects support whatever is supported by the underlying file system (or by [**ILockBytes**](/windows/desktop/api/Objidl/nn-objidl-ilockbytes)). The compound file implementation does not maintain any time stamps for internal streams. Unsupported time stamps are reported as zero, which allows the caller to test for support.

</dd> <dt>

<span id="IStorage__SetClass"></span><span id="istorage__setclass"></span><span id="ISTORAGE__SETCLASS"></span>[**IStorage::SetClass**](/windows/desktop/api/Objidl/nf-objidl-istorage-setclass)
</dt> <dd>

Assigns the specified CLSID to this storage object.

</dd> <dt>

<span id="IStorage__SetStateBits"></span><span id="istorage__setstatebits"></span><span id="ISTORAGE__SETSTATEBITS"></span>[**IStorage::SetStateBits**](/windows/desktop/api/Objidl/nf-objidl-istorage-setstatebits)
</dt> <dd>

Stores up to 32 bits of state information in this storage object. The state set by this method is for external use only. The COM-provided compound file implementation does not perform any action based on the state.

</dd> <dt>

<span id="IStorage__Stat"></span><span id="istorage__stat"></span><span id="ISTORAGE__STAT"></span>[**IStorage::Stat**](/windows/desktop/api/Objidl/nf-objidl-istorage-stat)
</dt> <dd>

Retrieves the [**STATSTG**](/windows/win32/api/objidl/ns-objidl-statstg) structure for this open storage object.

</dd> </dl>

## Remarks

If the storage object is opened in simple mode, use of the above methods is restricted. A storage is in simple mode if it is opened with the STGM\_SIMPLE element specified in the *grfMode* parameter of the [**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex) or [**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex) function. For more information about simple-mode storages, see [**STGM Constants**](stgm-constants.md). If the simple-mode storage object was obtained from the **StgCreateStorageEx** function, then the [**CreateStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-createstream) method can be called but the [**OpenStream**](/windows/desktop/api/Objidl/nf-objidl-istorage-openstream) method cannot. If the simple mode storage object was obtained from the **StgOpenStorageEx** function, then the **OpenStream** method can be called but the **CreateStream** method cannot.

When a simple-mode storage object is used to create a stream, the minimum size of that stream typically is 4096 bytes. If less data is written to the stream, the size is rounded up to 4096 bytes.

## Related topics

<dl> <dt>

[Compound File Implementation Limits](structured-storage-interfaces.md)
</dt> <dt>

[**IFillLockBytes**](/windows/desktop/api/Objidl/nn-objidl-ifilllockbytes)
</dt> <dt>

[**ILockBytes**](/windows/desktop/api/Objidl/nn-objidl-ilockbytes)
</dt> <dt>

[**IRootStorage**](/windows/desktop/api/Objidl/nn-objidl-irootstorage)
</dt> <dt>

[**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage)
</dt> <dt>

[**IStream**](/windows/desktop/api/Objidl/nn-objidl-istream)
</dt> <dt>

[**StgCreateDocfile**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatedocfile)
</dt> <dt>

[**StgCreateStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgcreatestorageex)
</dt> <dt>

[**StgOpenStorage**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorage)
</dt> <dt>

[**StgOpenStorageEx**](/windows/desktop/api/coml2api/nf-coml2api-stgopenstorageex)
</dt> </dl>

 

 