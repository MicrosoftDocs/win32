---
title: MSFT\_StorageTier class
description: Represents a storage tier.
ms.assetid: 0E049D07-DD37-4F64-8483-3ECF32211567
keywords:
- MSFT_StorageTier class Windows Storage Management API
- MSFT_StorageTier class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageTier
- MSFT_StorageTier.FriendlyName
- MSFT_StorageTier.MediaType
- MSFT_StorageTier.Size
- MSFT_StorageTier.Description
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_StorageTier class

Represents a storage tier.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageTier : MSFT_StorageObject
{
  String FriendlyName;
  UInt16 MediaType;
  UInt64 Size;
  String Description;
};
```

## Members

The **MSFT\_StorageTier** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_StorageTier** class has these methods.



| Method                                                        | Description                                                        |
|:--------------------------------------------------------------|:-------------------------------------------------------------------|
| [**DeleteObject**](msft-storagetier-deleteobject.md)         | Deletes the storage tier.<br/>                               |
| [**GetSupportedSize**](msft-storagetier-getsupportedsize.md) | Returns the supported sizes for a new storage tier.<br/>     |
| [**Resize**](msft-storagetier-resize.md)                     | Resizes the storage tier on the virtual disk.<br/>           |
| [**SetAttributes**](msft-storagetier-setattributes.md)       | Updates or sets various attributes on the storage tier.<br/> |
| [**SetDescription**](msft-storagetier-setdescription.md)     | Updates the description of the storage tier. <br/>           |
| [**SetFriendlyName**](msft-storagetier-setfriendlyname.md)   | Renames the storage tier. <br/>                              |



 

### Properties

The **MSFT\_StorageTier** class has these properties.

<dl> <dt>

**Description**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A description of the storage tier, provided by the user.

</dd> <dt>

**FriendlyName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The friendly name of the storage tier, defined by the user.

</dd> <dt>

**MediaType**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The media type of the storage tier.



| Value                                                                                                | Meaning                |
|------------------------------------------------------------------------------------------------------|------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Unspecified<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | HDD<br/>         |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | SSD<br/>         |



 

</dd> <dt>

**Size**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The size of the tier on the virtual disk. This property is available only when the storage tier is part of a virtual disk. The property is unspecified for pool-level storage tiers.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageObject**](msft-storageobject.md)
</dt> </dl>

 

 





