---
title: ICatalog interface
description: State object, holds open catalog and all info about catalog
ms.assetid: 6d09032b-3311-434b-b8db-97e3ee2f5f67
keywords:
- ICatalog interface HelpAPI
- ICatalog interface HelpAPI , described
topic_type:
- apiref
api_name:
- ICatalog
api_location:
- adomd.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ICatalog interface

State object, holds open catalog and all info about catalog

## Members

The **ICatalog** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **ICatalog** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **ICatalog** interface has these methods.



| Method                                                                    | Description                                                                                                                                 |
|:--------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**Close**](icatalog-close.md)                                           | method Close - closes a currently open catalog<br/>                                                                                   |
| [**GetReadWriteLock**](icatalog-getreadwritelock.md)                     | Method GetReadWriteLock - Return a reference to the catalog read write lock object for a given location<br/>                          |
| [**IsLanguageSupportAvailable**](icatalog-islanguagesupportavailable.md) | Method IsLanguageSupportAvailable - Check to see if the natural language support is installed on the system for a given language<br/> |
| [**Open**](icatalog-open.md)                                             | method Open - opens a catalog given a valid catalog directory path and list of prioritized languages for fallback<br/>                |
| [**OpenMshx**](icatalog-openmshx.md)                                     | method OpenMshx - opens an MSHX catalog given a valid path to the MSHX file<br/>                                                      |



 

### Properties

The **ICatalog** interface has these properties.



| Property                                               | Access type          | Description                                                                 |
|:-------------------------------------------------------|:---------------------|:----------------------------------------------------------------------------|
| [**ContentPath**](icatalog-contentpath.md)<br/> | Read-only<br/> | property ContentPath - returns the content path for this catalog<br/> |
| [**IsOpen**](icatalog-isopen.md)<br/>           | Read-only<br/> | Returns true if a catalog is currently open, else false<br/>          |



 

## Requirements



|                                     |                                                                                                     |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                                |
| Header<br/>                   | <dl> <dt>Adomd.h</dt> </dl>                  |
| IDL<br/>                      | <dl> <dt>Windows.Help.Runtime.idl</dt> </dl> |



 

 





