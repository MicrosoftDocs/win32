---
title: UI Automation Element Interfaces for Clients
description: This section describes the interfaces used by Microsoft UI Automation client to locate, access, and query UI Automation elements.
ms.assetid: 'dd7cdcf1-3511-424f-b729-b71a7e11cdd8'
---

# UI Automation Element Interfaces for Clients

This section describes the interfaces used by Microsoft UI Automation client to locate, access, and query UI Automation elements.

## In this section



| Interface                                                                        | Description                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IUIAutomation**](uiauto-iuiautomation.md)<br/>                         | Exposes methods that enable UI Automation client applications to discover, access, and filter UI Automation elements. UI Automation exposes every element of the UI Automation as an object represented by the [**IUIAutomation**](uiauto-iuiautomation.md) interface. The members of this interface are not specific to a particular element.<br/> |
| [**IUIAutomation2**](uiauto-iuiautomation2.md)<br/>                       | Extends the [**IUIAutomation**](uiauto-iuiautomation.md) interface to expose additional methods for controlling UI Automation functionality.<br/>                                                                                                                                                                                                   |
| [**IUIAutomation3**](uiauto-iuiautomation3.md)<br/>                       | Extends the [**IUIAutomation2**](uiauto-iuiautomation2.md) interface to expose additional methods for controlling UI Automation functionality.<br/>                                                                                                                                                                                                 |
| [**IUIAutomation4**](uiauto-iuiautomation4.md)<br/>                       | Extends the [**IUIAutomation3**](uiauto-iuiautomation3.md) interface to expose additional methods for controlling UI Automation functionality.<br/>                                                                                                                                                                                                 |
| [**IUIAutomation5**](uiauto-iuiautomation5.md)<br/>                       | Extends the [**IUIAutomation4**](uiauto-iuiautomation4.md) interface to expose additional methods for controlling UI Automation functionality.<br/>                                                                                                                                                                                                 |
| [**IUIAutomationCacheRequest**](uiauto-iuiautomationcacherequest.md)<br/> | Exposes properties and methods of a cache request. Client applications use this interface to specify the properties and control patterns to be cached when a UI Automation element is obtained.<br/>                                                                                                                                                 |
| [**IUIAutomationElement**](uiauto-iuiautomationelement.md)<br/>           | Exposes methods and properties for a UI Automation element, which represents a UI item. <br/>                                                                                                                                                                                                                                                        |
| [**IUIAutomationElement2**](uiauto-iuiautomationelement2.md)<br/>         | Extends the [**IUIAutomationElement**](uiauto-iuiautomationelement.md) interface. <br/>                                                                                                                                                                                                                                                             |
| [**IUIAutomationElement3**](uiauto-iuiautomationelement3.md)<br/>         | Extends the [**IUIAutomationElement2**](uiauto-iuiautomationelement2.md) interface. <br/>                                                                                                                                                                                                                                                           |
| [**IUIAutomationElement4**](uiauto-iuiautomationelement4.md)<br/>         | Extends the [**IUIAutomationElement3**](uiauto-iuiautomationelement3.md) interface. <br/>                                                                                                                                                                                                                                                           |
| [**IUIAutomationElement5**](uiauto-iuiautomationelement5.md)<br/>         | Extends the [**IUIAutomationElement4**](uiauto-iuiautomationelement4.md) interface to provide access to current and cached landmark data.<br/>                                                                                                                                                                                                      |
| [**IUIAutomationElement6**](uiauto-iuiautomationelement6.md)<br/>         | Extends the [**IUIAutomationElement5**](uiauto-iuiautomationelement5.md) interface to provide access to current and cached full descriptions.<br/>                                                                                                                                                                                                  |
| [**IUIAutomationElement7**](uiauto-iuiautomationelement7.md)<br/>         | Extends the [**IUIAutomationElement6**](uiauto-iuiautomationelement6.md) interface.<br/>                                                                                                                                                                                                                                                            |
| [**IUIAutomationElement8**](uiauto-iuiautomationelement8.md)<br/>         | Extends the [**IUIAutomationElement7**](uiauto-iuiautomationelement7.md) interface.<br/>                                                                                                                                                                                                                                                            |
| [**IUIAutomationElementArray**](uiauto-iuiautomationelementarray.md)<br/> | Represents a collection of UI Automation elements.<br/>                                                                                                                                                                                                                                                                                              |
| [**IUIAutomationRegistrar**](uiauto-iuiautomationregistrar.md)<br/>       | Exposes methods for registering new control patterns, properties, and events.<br/>                                                                                                                                                                                                                                                                   |
| [**IUIAutomationTreeWalker**](uiauto-iuiautomationtreewalker.md)<br/>     | Exposes properties and methods that UI Automation client applications use to view and navigate the UI Automation elements on the desktop. <br/>                                                                                                                                                                                                      |



 

## Related topics

<dl> <dt>

[UI Automation Clients](uiauto-entry-uiautoclientsforwin32apps.md)
</dt> </dl>

 

 





