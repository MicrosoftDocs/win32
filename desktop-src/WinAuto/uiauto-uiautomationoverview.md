---
title: UI Automation Overview
description: Microsoft UI Automation is an accessibility framework for Windows.
ms.assetid: 99610542-761c-432d-a4ac-4cd3812577a8
keywords:
- UI Automation,about
- UI Automation,accessibility
- UI Automation,components
- UI Automation,Provider API
- UI Automation,Client API
- UI Automation,header files
- UI Automation,model
- components
- accessibility
- Provider API
- Client API
- header files
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation Overview

Microsoft UI Automation is an accessibility framework for Windows. It provides programmatic access to most UI elements on the desktop. It enables assistive technology products, such as screen readers, to provide information about the UI to end users and to manipulate the UI by means other than standard input. UI Automation also allows automated test scripts to interact with the UI.

UI Automation was first available in Windows XP as part of the Microsoft .NET Framework. Although an unmanaged C++ API was also published at that time, the usefulness of client functions was limited because of interoperability issues. For Windows 7, the API has been rewritten in the Component Object Model (COM).

> [!Note]  
> Although the library functions introduced in the earlier version of UI Automation are still documented, they should not be used in new applications.

 

UI Automation client applications can be written with the assurance that they will work on multiple Microsoft Windows control frameworks. The UI Automation core masks any differences in the frameworks that underlie various pieces of the UI. For example, the **Content** property of a Windows Presentation Foundation (WPF) button, the **Caption** property of a Microsoft Win32 button, and the **ALT** property of an HTML image are all mapped to a single property, **Name**, in the UI Automation view.

UI Automation provides full functionality in Windows XP, Windows Server 2003, and later operating systems.

UI Automation providers are components that implement UI Automation support on controls and offer some support for Microsoft Active Accessibility client applications, through a built-in bridging service.

> [!Note]  
> UI Automation does not enable communication between processes that are started by different users through the **Run as** command.

 

This topic contains the following sections.

-   [UI Automation Components](#ui-automation-components)
-   [UI Automation Header Files](#ui-automation-header-files)
-   [UI Automation Model](#ui-automation-model)
-   [Related topics](#related-topics)

## UI Automation Components

UI Automation has four main components, as shown in the following table.




| Component | Description | 
|-----------|-------------|
| Provider API | A set of COM interfaces that are implemented by UI Automation providers. UI Automation providers are objects that provide information about UI elements and respond to programmatic input. | 
| Client API | A set of COM interfaces that enable client applications to obtain information about the UI and to send input to controls.<blockquote>[!Note]<br />The functions described in <a href="uiauto-entry-cpfunctions.md">Deprecated Control Pattern Functions</a> and <a href="uiauto-entry-uianodefunctions.md">Deprecated Node Functions</a> are deprecated. Instead, client applications should use the UI Automation COM interfaces described in <a href="uiauto-entry-uiautoclientinterfaces.md">UI Automation Element Interfaces for Clients</a>.</blockquote><br /> | 
| UIAutomationCore.dll | The run-time library, sometimes called the UI Automation core, that handles communication between providers and clients. | 
| Oleacc.dll | The run-time library for Microsoft Active Accessibility and the proxy objects. The library also provides proxy objects used by the Microsoft Microsoft Active Accessibility to UI Automation Proxy to support Win32 controls. | 




 

There are two ways of using UI Automation: to create support for custom controls by using the provider API, and to create client applications that use the UI Automation core to communicate with, and retrieve information about, UI elements. Depending on your focus, you should refer to different parts of the documentation. If you need to create support for custom controls, see [UI Automation Provider Programmer's Guide](uiauto-providerportal.md). If you need to communicate with or retrieve information about UI elements, see [UI Automation Client Programmer's Guide](uiauto-clientportal.md).

## UI Automation Header Files

The UI Automation API is defined in several different C/C++ header files that are included with the Windows Software Development Kit (SDK). The UI Automation header files are described in the following table:



| Header file           | Description                                                                                                                                                                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UIAutomationClient.h  | Defines the interfaces and related programming elements used by UI Automation clients.                                                                                                                                                                                           |
| UIAutomationCore.h    | Defines the interfaces and related programming elements used by UI Automation providers.                                                                                                                                                                                         |
| UIAutomationCoreApi.h | Defines general constants, GUIDs, data types, and structures used by UI Automation clients and providers. It also contains definitions for the deprecated node and control pattern functions.                                                                                    |
| UIAutomation.h        | Includes all of the other UI Automation header files. Because most UI Automation applications require elements from all UI Automation header files, it is best to include UIAutomation.h in your UI Automation application projects instead of including each file individually. |



 

If you are developing an application that uses the UI Automation API, you should include UIAutomation.h in your project. If your application supports Microsoft Active Accessibility, include the Oleacc.h header file. UI Automation applications that use GUIDs also require the Initguid.h header file. If needed, Initguid.h should be included before UIAutomation.h.

## UI Automation Model

UI Automation exposes every element of the UI to client applications as an object represented by the [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface. Elements are contained in a tree structure, with the desktop as the root element. Clients can filter the raw view of the tree as a control view or a content view. These standard views of the structure can easily be seen by using the [Inspect](inspect-objects.md) application that is included with the Windows SDK. Applications can also create custom views.

A UI Automation element exposes properties of the control or UI element that it represents. One of these properties is the control type, which defines the basic appearance and functionality of the control or UI element as a single recognizable entity, for example, a button or check box. For more information about control types, see [UI Automation Control Types Overview](uiauto-controltypesoverview.md).

In addition, a UI Automation element exposes one or more control patterns. A control pattern provides a set of properties that are specific to a particular control type. A control pattern also exposes methods that enable client applications to get more information about the element and to provide input to the element. For more information about control patterns, see [UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md).

> [!Note]  
> There is no one-to-one correspondence between control types and control patterns. A control pattern may be supported by multiple control types, and a control may support multiple control patterns, each of which exposes different aspects of its behavior. For example, a combo box has at least two control patterns: one that represents its ability to expand and collapse, and another that represents the selection mechanism. However, a control can exhibit only a single control type.

 

UI Automation provides information to client applications through events. Unlike WinEvents, UI Automation events are not based on a broadcast mechanism. UI Automation clients register for specific event notifications and can request that specific properties and control pattern information be passed to their event handlers. In addition, a UI Automation event contains a reference to the element that raised it. Providers can improve performance by raising events selectively, depending on whether any clients are listening. For more information about events, see [UI Automation Events Overview](uiauto-eventsoverview.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Control Types Overview](uiauto-controltypesoverview.md)
</dt> <dt>

[UI Automation Control Patterns Overview](uiauto-controlpatternsoverview.md)
</dt> <dt>

[UI Automation Events Overview](uiauto-eventsoverview.md)
</dt> </dl>

 

 





