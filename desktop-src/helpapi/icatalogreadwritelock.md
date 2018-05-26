---
title: ICatalogReadWriteLock interface
description: Catalog lock state object, holds catalog lock and all info about catalog lock
ms.assetid: ff9ebc61-7385-49b6-a7eb-2c8b27c18ee5
keywords:
- ICatalogReadWriteLock interface HelpAPI
- ICatalogReadWriteLock interface HelpAPI , described
topic_type:
- apiref
api_name:
- ICatalogReadWriteLock
api_location:
- Windows.Help.Runtime.idl
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICatalogReadWriteLock interface

Catalog lock state object, holds catalog lock and all info about catalog lock

## Members

The **ICatalogReadWriteLock** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ICatalogReadWriteLock** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ICatalogReadWriteLock** interface has these methods.



| Method                                                                                         | Description                                                                          |
|:-----------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
| [**EnterReadLock**](icatalogreadwritelock-enterreadlock.md)                                   | method EnterReadLock - creates a read lock<br/>                                |
| [**EnterWriteLock**](icatalogreadwritelock-enterwritelock.md)                                 | method EnterWriteLock - creates a write lock<br/>                              |
| [**ExitNonBlockingWriteOperation**](icatalogreadwritelock-exitnonblockingwriteoperation.md)   | method ExitNonBlockingWriteOperation - exits a non-blocking write lock<br/>    |
| [**ExitReadLock**](icatalogreadwritelock-exitreadlock.md)                                     | method ExitReadLock - exits the read lock<br/>                                 |
| [**ExitWriteLock**](icatalogreadwritelock-exitwritelock.md)                                   | method ExitWriteLock - exits the write lock<br/>                               |
| [**StartNonBlockingWriteOperation**](icatalogreadwritelock-startnonblockingwriteoperation.md) | method StartNonBlockingWriteOperation - creates a non-blocking write lock<br/> |



 

### Properties

The **ICatalogReadWriteLock** interface has these properties.



| Property                                                                                                        | Access type          | Description                                                                             |
|:----------------------------------------------------------------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------------------|
| [**IsCurrentlyNonBlockingWriteLocked**](icatalogreadwritelock-iscurrentlynonblockingwritelocked.md)<br/> | Read-only<br/> | Returns true if a catalog is currently non-blocking write locked, else false<br/> |
| [**IsCurrentlyWriteLocked**](icatalogreadwritelock-iscurrentlywritelocked.md)<br/>                       | Read-only<br/> | Returns true if a catalog is currently write locked, else false<br/>              |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



 

 





