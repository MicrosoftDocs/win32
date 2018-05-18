---
title: Application Object object
description: The Application object is used to initiate and control a Microsoft Management Console (MMC) session. You must create an Application object before using any other MMC 2.0 automation objects.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '11785084-2eda-4d7b-8b7f-d1944e8bf555'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["Application Object object MMC", "Application Object object MMC , described"]
topic_type:
- apiref
api_name:
- Application Object
api_location:
- mmcobj.h
api_type:
- COM
---

# Application Object object

The **Application** object is used to initiate and control a Microsoft Management Console (MMC) session. You must create an **Application** object before using any other MMC 2.0 automation objects.

## Members

The **Application Object** object has these types of members:

-   [Events](#events)
-   [Methods](#methods)
-   [Properties](#properties)

### Events

The **Application Object** object has these events.



| Event                                                                | Description                                                             |
|:---------------------------------------------------------------------|:------------------------------------------------------------------------|
| [**OnContextMenuExecuted**](application-oncontextmenuexecuted.md)   | Occurs when a context menu is executed.<br/>                      |
| [**OnDocumentClose**](application-ondocumentclose.md)               | Occurs when a document is closed.<br/>                            |
| [**OnDocumentOpen**](application-ondocumentopen.md)                 | Occurs when an MMC document is opened.<br/>                       |
| [**OnListUpdated**](application-onlistupdated.md)                   | Occurs when one or more list items are updated.<br/>              |
| [**OnNewView**](application-onnewview.md)                           | Occurs when a view is added.<br/>                                 |
| [**OnQuit**](application-onquit.md)                                 | Occurs when the MMC application is ended.<br/>                    |
| [**OnSelectionChange**](application-onselectionchange.md)           | Occurs when the result item selection for a view is changed.<br/> |
| [**OnSnapInAdded**](application-onsnapinadded.md)                   | Occurs when a snap-in has been added.<br/>                        |
| [**OnSnapInRemoved**](application-onsnapinremoved.md)               | Occurs when a snap-in has been removed.<br/>                      |
| [**OnToolbarButtonClicked**](application-ontoolbarbuttonclicked.md) | Occurs when a toolbar button is clicked.<br/>                     |
| [**OnViewChange**](application-onviewchange.md)                     | Occurs when the view is changed.<br/>                             |
| [**OnViewClose**](application-onviewclose.md)                       | Occurs when the view is closed.<br/>                              |



 

### Methods

The **Application Object** object has these methods.



| Method                           | Description                                        |
|:---------------------------------|:---------------------------------------------------|
| [**Help**](application-help.md) | Displays online Help for the console.<br/>   |
| [**Hide**](application-hide.md) | Hides the application.<br/>                  |
| [**Load**](application-load.md) | Loads a document from a specified file.<br/> |
| [**Quit**](application-quit.md) | Quits the MMC application.<br/>              |
| [**Show**](application-show.md) | Shows the application.<br/>                  |



 

### Properties

The **Application Object** object has these properties.



| Property                                                    | Access type           | Description                                                                                                                                        |
|:------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Document**](application-document.md)<br/>         | Read-only<br/>  | Document object associated with the application.<br/>                                                                                        |
| [**Frame**](application-frame.md)<br/>               | Read-only<br/>  | [**Frame object**](frame-object.md) for the application.<br/>                                                                               |
| [**UserControl**](application-usercontrol.md)<br/>   | Read/write<br/> | UserControl setting for the application; determines whether the application is controlled by the user.<br/>                                  |
| [**VersionMajor**](application-versionmajor.md)<br/> | Read-only<br/>  | Major version number of MMC.<br/>                                                                                                            |
| [**VersionMinor**](application-versionminor.md)<br/> | Read-only<br/>  | Minor version number of MMC.<br/>                                                                                                            |
| [**Visible**](application-visible.md)<br/>           | Read-only<br/>  | Determines whether the application is visible (set by the [**Show**](application-show.md) or [**Hide**](application-hide.md) method).<br/> |



 

## Remarks

When your application starts MMC using the MMC 2.0 automation object model, a document and view are automatically created. [**OnDocumentOpen**](application-ondocumentopen.md) and [**OnNewView**](application-onnewview.md) events will not be sent for the initial document and view, as MMC does not begin sending events until after the first view has been created. The **OnDocumentOpen** and **OnNewView** events aren't required during application startup, as the application can easily open a document (by calling the [**Application.Load**](application-load.md) method) or make a new view (by calling the [**Views.Add**](views-add.md) method). MMC sends your application the [**OnDocumentClose**](application-ondocumentclose.md) and [**OnViewClose**](application-onviewclose.md) events when the initial document and view are closed.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                        |
| Header<br/>                   | <dl> <dt>Mmcobj.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mmcobj.idl</dt> </dl> |
| CLSID<br/>                    | CLSID\_Application is defined as 49B2791A-B1AE-4C90-9B8E-E860BA07F889<br/>      |



## See also

<dl> <dt>

[Controlling the Lifetime of an MMC Instance](controlling-the-lifetime-of-an-mmc-instance.md)
</dt> </dl>

 

 





