---
title: BcdStore class
description: Represents a BCD store that contains a collection of BCD objects.
ms.assetid: e5020c65-48e6-4e3c-8323-893bfb686fec
keywords:
- BcdStore class Boot Config
- BcdStore class Boot Config , described
topic_type:
- apiref
api_name:
- BcdStore
- BcdStore.FilePath
api_location:
- Root\WMI
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# BcdStore class

Represents a BCD store that contains a collection of BCD objects.

## Syntax

``` syntax
class BcdStore
{
  string FilePath;
};
```

## Members

The **BcdStore** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **BcdStore** class has these methods.



| Method                                                        | Description                                                                                                                                                                           |
|:--------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CopyObject**](copyobject-bcdstore.md)                     | Copies the specified object from another store.<br/>                                                                                                                            |
| [**CopyObjects**](copyobjects-bcdstore.md)                   | Copies the objects of the specified type from another store.<br/>                                                                                                               |
| [**CreateObject**](createobject-bcdstore.md)                 | Creates the specified object.<br/>                                                                                                                                              |
| [**CreateStore**](createstore-bcdstore.md)                   | Creates a new store.<br/>                                                                                                                                                       |
| [**DeleteObject**](deleteobject-bcdstore.md)                 | Deletes the specified object.<br/>                                                                                                                                              |
| [**DeleteSystemStore**](deletesystemstore-bcdstore.md)       | Deletes the system store.<br/>                                                                                                                                                  |
| [**EnumerateObjects**](enumerateobjects-bcdstore.md)         | Enumerates the objects of the specified type.<br/>                                                                                                                              |
| [**ExportStore**](exportstore-bcdstore.md)                   | Saves the system store to the specified file.<br/>                                                                                                                              |
| [**GetSystemDisk**](getsystemdisk-bcdstore.md)               | Retrieves the system disk.<br/>                                                                                                                                                 |
| [**GetSystemPartition**](getsystempartition-bcdstore.md)     | Retrieves the system partition.<br/>                                                                                                                                            |
| [**ImportStore**](importstore-bcdstore.md)                   | Marks the specified store as the system store.<br/>                                                                                                                             |
| [**ImportStoreWithFlags**](importstorewithflags-bcdstore.md) | Marks the specified store as the system store and optionally reinitializes boot entries in NVRAM on a computer with Unified Extensible Firmware Interface (UEFI) firmware.<br/> |
| [**OpenObject**](openobject-bcdstore.md)                     | Opens the specified object.<br/>                                                                                                                                                |
| [**OpenStore**](openstore-bcdstore.md)                       | Opens a store.<br/>                                                                                                                                                             |



 

### Properties

The **BcdStore** class has these properties.

<dl> <dt>

**FilePath**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

A file path that uniquely identifies the store. The system store is denoted by an empty string ("").

</dd> </dl>

## Remarks

Each store is contained in a file. One store is marked as the system store, which is the store currently in use on the system. When the system is booted, it uses the settings in the system store.

The [**CreateStore**](createstore-bcdstore.md), [**OpenStore**](openstore-bcdstore.md), and [**ImportStore**](importstore-bcdstore.md) methods are static methods; they can be called without an instance of the class. To do so, open a WMI object that represents the **BcdStore** class and call these methods.

## Requirements



|                                     |                                                                                    |
|-------------------------------------|------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                               |
| Namespace<br/>                | Root\\WMI<br/>                                                               |
| MOF<br/>                      | <dl> <dt>Bcd.mof</dt> </dl> |



 

 





