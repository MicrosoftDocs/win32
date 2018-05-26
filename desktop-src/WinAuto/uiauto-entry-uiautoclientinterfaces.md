---
title: UI Automation Element Interfaces for Clients
description: This section describes the interfaces used by Microsoft UI Automation client to locate, access, and query UI Automation elements.
ms.assetid: dd7cdcf1-3511-424f-b729-b71a7e11cdd8
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# UI Automation Element Interfaces for Clients

This section describes the interfaces used by Microsoft UI Automation client to locate, access, and query UI Automation elements.

## In this section



| Interface                                                                        | Description                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUIAutomation**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation?branch=master)<br/>                         | Exposes methods that enable UI Automation client applications to discover, access, and filter UI Automation elements. UI Automation exposes every element of the UI Automation as an object represented by the [**IUIAutomation**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation?branch=master) interface. The members of this interface are not specific to a particular element.<br/> |
| [**IUIAutomation2**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation2?branch=master)<br/>                       | Extends the [**IUIAutomation**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation?branch=master) interface to expose additional methods for controlling UI Automation functionality.<br/>                                                                                                                                                                                                   |
| [**IUIAutomation3**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation3?branch=master)<br/>                       | Extends the [**IUIAutomation2**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation2?branch=master) interface to expose additional methods for controlling UI Automation functionality.<br/>                                                                                                                                                                                                 |
| [**IUIAutomation4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation4?branch=master)<br/>                       | Extends the [**IUIAutomation3**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation3?branch=master) interface to expose additional methods for controlling UI Automation functionality.<br/>                                                                                                                                                                                                 |
| [**IUIAutomation5**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation5?branch=master)<br/>                       | Extends the [**IUIAutomation4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation4?branch=master) interface to expose additional methods for controlling UI Automation functionality.<br/>                                                                                                                                                                                                 |
| [**IUIAutomationCacheRequest**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationcacherequest?branch=master)<br/> | Exposes properties and methods of a cache request. Client applications use this interface to specify the properties and control patterns to be cached when a UI Automation element is obtained.<br/>                                                                                                                                                 |
| [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master)<br/>           | Exposes methods and properties for a UI Automation element, which represents a UI item. <br/>                                                                                                                                                                                                                                                        |
| [**IUIAutomationElement2**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement2?branch=master)<br/>         | Extends the [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) interface. <br/>                                                                                                                                                                                                                                                             |
| [**IUIAutomationElement3**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement3?branch=master)<br/>         | Extends the [**IUIAutomationElement2**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement2?branch=master) interface. <br/>                                                                                                                                                                                                                                                           |
| [**IUIAutomationElement4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement4?branch=master)<br/>         | Extends the [**IUIAutomationElement3**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement3?branch=master) interface. <br/>                                                                                                                                                                                                                                                           |
| [**IUIAutomationElement5**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement5?branch=master)<br/>         | Extends the [**IUIAutomationElement4**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement4?branch=master) interface to provide access to current and cached landmark data.<br/>                                                                                                                                                                                                      |
| [**IUIAutomationElement6**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement6?branch=master)<br/>         | Extends the [**IUIAutomationElement5**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement5?branch=master) interface to provide access to current and cached full descriptions.<br/>                                                                                                                                                                                                  |
| [**IUIAutomationElement7**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement7?branch=master)<br/>         | Extends the [**IUIAutomationElement6**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement6?branch=master) interface.<br/>                                                                                                                                                                                                                                                            |
| [**IUIAutomationElement8**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement8?branch=master)<br/>         | Extends the [**IUIAutomationElement7**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement7?branch=master) interface.<br/>                                                                                                                                                                                                                                                            |
| [**IUIAutomationElementArray**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelementarray?branch=master)<br/> | Represents a collection of UI Automation elements.<br/>                                                                                                                                                                                                                                                                                              |
| [**IUIAutomationRegistrar**](/windows/win32/UIAutomationCore/nn-uiautomationcore-iuiautomationregistrar?branch=master)<br/>       | Exposes methods for registering new control patterns, properties, and events.<br/>                                                                                                                                                                                                                                                                   |
| [**IUIAutomationTreeWalker**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtreewalker?branch=master)<br/>     | Exposes properties and methods that UI Automation client applications use to view and navigate the UI Automation elements on the desktop. <br/>                                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[UI Automation Clients](uiauto-entry-uiautoclientsforwin32apps.md)
</dt> </dl>

 

 





