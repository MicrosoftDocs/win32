---
title: MSFT\_FileStorageTier class
description: This class provides methods to manually pin a file onto a storage tier and to unpin it.
ms.assetid: 002FE1D2-A54F-45DB-B511-F7776A39FAD4
keywords:
- MSFT_FileStorageTier class Windows Storage Management API
- MSFT_FileStorageTier class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_FileStorageTier
- MSFT_FileStorageTier.FilePath
- MSFT_FileStorageTier.State
- MSFT_FileStorageTier.PlacementStatus
- MSFT_FileStorageTier.DesiredStorageTierName
- MSFT_FileStorageTier.FileSizeOnDesiredStorageTier
- MSFT_FileStorageTier.FileSize
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

# MSFT\_FileStorageTier class

This class provides methods to manually pin a file onto a storage tier and to unpin it.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_FileStorageTier
{
  String FilePath;
  UInt16 State;
  UInt16 PlacementStatus;
  String DesiredStorageTierName;
  UInt64 FileSizeOnDesiredStorageTier;
  UInt64 FileSize;
};
```

## Members

The **MSFT\_FileStorageTier** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MSFT\_FileStorageTier** class has these methods.



| Method                                      | Description                                        |
|:--------------------------------------------|:---------------------------------------------------|
| [**Clear**](msft-filestoragetier-clear.md) | Unpins a file from a storage tier.<br/>      |
| [**Get**](msft-filestoragetier-get.md)     | Gets tier information for pinned files.<br/> |
| [**Set**](msft-filestoragetier-set.md)     | Pins a file to a storage tier.<br/>          |



 

### Properties

The **MSFT\_FileStorageTier** class has these properties.

<dl> <dt>

**DesiredStorageTierName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The desired name of the storage tier.

</dd> <dt>

**FilePath**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: Key
</dt> </dl>

The path of the file.

</dd> <dt>

**FileSize**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file size.

</dd> <dt>

**FileSizeOnDesiredStorageTier**
</dt> <dd> <dl> <dt>

Data type: **UInt64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The file size on the desired storage tier.

</dd> <dt>

**PlacementStatus**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The placement status of the file.



| Value                                                                                                | Meaning                       |
|------------------------------------------------------------------------------------------------------|-------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Unknown<br/>            |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | Completely on tier<br/> |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Partially on tier<br/>  |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | Not on tier<br/>        |



 

</dd> <dt>

**State**
</dt> <dd> <dl> <dt>

Data type: **UInt16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The state of the attempt to pin the file.



| Value                                                                                                | Meaning                          |
|------------------------------------------------------------------------------------------------------|----------------------------------|
| <span id="0"></span><dl> <dt>**0**</dt> </dl> | Unknown<br/>               |
| <span id="1"></span><dl> <dt>**1**</dt> </dl> | OK<br/>                    |
| <span id="2"></span><dl> <dt>**2**</dt> </dl> | Insufficient Capacity<br/> |
| <span id="3"></span><dl> <dt>**3**</dt> </dl> | In Process<br/>            |
| <span id="4"></span><dl> <dt>**4**</dt> </dl> | Pending<br/>               |



 

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





