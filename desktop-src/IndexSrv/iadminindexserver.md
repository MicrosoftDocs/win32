---
title: IAdminIndexServer interface
description: Manages the indexing service itself, including the collection of catalogs that identify the documents to be indexed. This object also provides methods to detect whether the indexing service is currently running and to start and stop it programmatically.
ms.assetid: 6e537b83-00d6-4bcd-85c3-7a882c53024c
keywords:
- IAdminIndexServer interface Indexing Service
- IAdminIndexServer interface Indexing Service , described
topic_type:
- apiref
api_name:
- IAdminIndexServer
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# IAdminIndexServer interface

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Manages the indexing service itself, including the collection of catalogs that identify the documents to be indexed. This object also provides methods to detect whether the indexing service is currently running and to start and stop it programmatically.

## Members

The **IAdminIndexServer** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IAdminIndexServer** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IAdminIndexServer** interface has these methods.



| Method                                                         | Description                                                                                                                           |
|:---------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| [**AddCatalog**](iadminindexserver-addcatalog.md)             | Creates a new catalog.<br/>                                                                                                     |
| [**Continue**](iadminindexserver-continue.md)                 | Continues Indexing Service.<br/>                                                                                                |
| [**EnableCI**](iadminindexserver-enableci.md)                 | Enables Indexing Service to start automatically.<br/>                                                                           |
| [**FindFirstCatalog**](iadminindexserver-findfirstcatalog.md) | Initializes a catalog enumeration.<br/>                                                                                         |
| [**FindNextCatalog**](iadminindexserver-findnextcatalog.md)   | Enumerates the next catalog.<br/>                                                                                               |
| [**GetCatalog**](iadminindexserver-getcatalog.md)             | Retrieves the current catalog during an enumeration.<br/>                                                                       |
| [**GetCatalogByName**](iadminindexserver-getcatalogbyname.md) | Retrieves a catalog object by name.<br/>                                                                                        |
| [**GetLongProperty**](iadminindexserver-getlongproperty.md)   | Retrieves a content index registry value of type **REG\_DWORD**, as described in [Registry Entries](registry-entries.md).<br/> |
| [**GetSZProperty**](iadminindexserver-getszproperty.md)       | Retrieves a content index registry value of type **REG\_SZ**, as described in [Registry Entries](registry-entries.md).<br/>    |
| [**IsPaused**](iadminindexserver-ispaused.md)                 | Determines whether Indexing Service is paused.<br/>                                                                             |
| [**IsRunning**](iadminindexserver-isrunning.md)               | Determines whether Indexing Service is running.<br/>                                                                            |
| [**Pause**](iadminindexserver-pause.md)                       | Pauses Indexing Service.<br/>                                                                                                   |
| [**RemoveCatalog**](iadminindexserver-removecatalog.md)       | Removes an existing catalog.<br/>                                                                                               |
| [**SetLongProperty**](iadminindexserver-setlongproperty.md)   | Sets a content index registry value of type **REG\_DWORD**, as described in [Registry Entries](registry-entries.md).<br/>      |
| [**SetSZProperty**](iadminindexserver-setszproperty.md)       | Sets a content index registry value of type **REG\_SZ**, as described in [Registry Entries](registry-entries.md).<br/>         |
| [**Start**](iadminindexserver-start.md)                       | Starts Indexing Service.<br/>                                                                                                   |
| [**Stop**](iadminindexserver-stop.md)                         | Stops Indexing Service.<br/>                                                                                                    |



 

### Properties

The **IAdminIndexServer** interface has these properties.



| Property                                                        | Access type           | Description                                       |
|:----------------------------------------------------------------|:----------------------|:--------------------------------------------------|
| [**MachineName**](iadminindexserver-machinename.md)<br/> | Read/write<br/> | The name of Indexing Service computer.<br/> |



 

## Remarks

Although you can manage many aspects of Indexing Service while it is running, you must stop the service to create catalogs with the [**AddCatalog**](iadminindexserver-addcatalog.md) method or delete catalogs with [**RemoveCatalog**](iadminindexserver-removecatalog.md). To determine whether Indexing Service is running, use [**IsRunning**](iadminindexserver-isrunning.md). To stop the service, use the [**Stop**](iadminindexserver-stop.md) method, make any additions or deletions necessary, and begin the service again using the **Start** method. Additional information about configuring catalogs can be found through the **Help** command on the **Start** menu.

If multiple instances of the AdminIndexServer object are created, changes made to one instance do not propagate to the other running instances. For example, if you have two instances of the AdminIndexServer object running and invoke the [**AddCatalog**](iadminindexserver-addcatalog.md) method of one object, the other AdminIndexServer object doesn't know about the newly added catalog. New instances of this object are created with the most current information.

The programmatic identifier (ProgID) in the registry under **HKEY\_LOCAL\_MACHINE/Software/Classes** for the administration object in Ciodm.dll is Microsoft.ISAdm.1. The version-independent ProgID is Microsoft.ISAdm. The Indexing Service administration object implementation is enabled for apartment and free threading.

This object supports **IErrorInfo** to report errors.

Registry entries currently in use by Indexing Service can be found under **HKEY\_LOCAL\_MACHINE/System/CurrentControlSet/Control/ContentIndex**.

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |
| End of client support<br/>    | Windows 7<br/>                                       |
| End of server support<br/>    | Windows Server 2008 R2<br/>                          |



 

 





