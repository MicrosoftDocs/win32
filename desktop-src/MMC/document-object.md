---
title: Document Object object
description: The Document object is used to manage the application document.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 77bf197d-f9c4-407d-9f55-0b1e66f8559c
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Document Object object MMC
- Document Object object MMC , described
topic_type:
- apiref
api_name:
- Document Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# Document Object object

The **Document** object is used to manage the application document.

## Members

The **Document Object** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Document Object** object has these methods.



| Method                                                | Description                                            |
|:------------------------------------------------------|:-------------------------------------------------------|
| [**Close**](document-close.md)                       | Closes the document.<br/>                        |
| [**CreateProperties**](document-createproperties.md) | Creates a new (empty) Properties object.<br/>    |
| [**Save**](document-save.md)                         | Saves the MMC document.<br/>                     |
| [**SaveAs**](document-saveas.md)                     | Saves the MMC document to a specified file.<br/> |



 

### Properties

The **Document Object** object has these properties.



| Property                                                     | Description                                                                                                                                 |
|:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActiveView**](document-activeview.md)<br/>         | Returns the active [**View object**](view-object.md).<br/>                                                                           |
| [**Application**](document-application.md)<br/>       | Returns the Application object that is the parent of the document.<br/>                                                               |
| [**IsSaved**](document-issaved.md)<br/>               | Returns whether the file has been saved; if not saved, the file has had changes and should be saved prior to closing or exiting.<br/> |
| [**Location**](document-location.md)<br/>             | Retrieves the location of the current document.<br/>                                                                                  |
| [**Mode**](document-mode.md)<br/>                     | The mode of the current document.<br/>                                                                                                |
| [**Name**](document-name.md)<br/>                     | The name of the current console file.<br/>                                                                                            |
| [**RootNode**](document-rootnode.md)<br/>             | Retrieves the root Node object.<br/>                                                                                                  |
| [**ScopeNamespace**](document-scopenamespace.md)<br/> | Retrieves the ScopeNamespace object.<br/>                                                                                             |
| [**SnapIns**](document-snapins.md)<br/>               | Retrieves the SnapIns object, which represents the collection of snap-ins that are loaded for this document.<br/>                     |
| [**Views**](document-views.md)<br/>                   | Retrieves the Views object, which represents the collection of View objects in effect for this document.<br/>                         |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Document<br/>                                                                |



 

 





