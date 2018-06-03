---
title: System.Gadget.Flyout object
description: Defines the properties, methods, and events that provide gadget Flyout functionality.
ms.assetid: 0373aad5-cf64-4065-918b-974efc3b2313
keywords:
- System.Gadget.Flyout object Windows Sidebar
- System.Gadget.Flyout object Windows Sidebar , described
topic_type:
- apiref
api_name:
- System.Gadget.Flyout
api_location:
- Sidebar.Exe
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# System.Gadget.Flyout object

\[The Windows Gadget Platform/Sidebar is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. \]

Defines the properties, methods, and events that provide gadget **Flyout** functionality.

## Members

The **System.Gadget.Flyout** object has these types of members:

-   [Events](#events)
-   [Properties](#properties)

### Events

The **System.Gadget.Flyout** object has these events.



| Event                                         | Description                                                   |
|:----------------------------------------------|:--------------------------------------------------------------|
| [**onHide**](system-gadget-flyout-onhide.md) | Event fired when the gadget **Flyout** is hidden. <br/> |
| [**onShow**](system-gadget-flyout-onshow.md) | Event fired when the gadget **Flyout** is shown. <br/>  |



 

### Properties

The **System.Gadget.Flyout** object has these properties.



| Property                                                     | Access type           | Description                                                                            |
|:-------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------|
| [**document**](system-gadget-flyout-document.md)<br/> | Read-only<br/>  | Gets an object that represents the DOM of the gadget **Flyout** HTML file. <br/> |
| [**file**](system-gadget-flyout-file.md)<br/>         | Read/write<br/> | Gets or sets the HTML filename for the gadget **Flyout** UI. <br/>               |
| [**show**](system-gadget-flyout-show.md)<br/>         | Read/write<br/> | Gets or sets whether a gadget **Flyout** is visible. <br/>                       |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                           |
| End of client support<br/>    | Windows 7<br/>                                                                                           |
| End of server support<br/>    | Windows Server 2008<br/>                                                                                 |
| IDL<br/>                      | <dl> <dt>Sidebar.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Sidebar.Exe (version 1.00 or later)</dt> </dl> |



 

 





