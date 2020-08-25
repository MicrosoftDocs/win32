---
title: UI Automation Clients Overview
description: This topic describes the main tasks involved in implementing a Microsoft UI Automation client application.
ms.assetid: 536ccf03-2f52-49e5-a95f-ea56cf821779
keywords:
- UI Automation,clients overview
- clients,about
- clients,elements
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation Clients Overview

This topic describes the main tasks involved in implementing a Microsoft UI Automation client application.

A UI Automation client is any application that uses the UI Automation API to access information about UI elements, or to control applications through programmatic manipulation of their UI elements. UI Automation clients include assistive technology applications such as screen readers, which retrieve information about UI elements and present the information in a way that is usable for people with disabilities. They also include applications such as speech recognition programs and software testing tools, which use UI Automation instead of the mouse and keyboard to "drive" other applications.

From a UI Automation perspective, the main tasks that a UI Automation client application must accomplish include the following:

1.  **Obtain an instance of the CUIAutomation object.**

    Information about UI elements, and access to UI element functionality, is exposed to clients by UI Automation providers. However, client applications do not work directly with providers. Instead, a core service lies between the client and the provider. When a client calls the UI Automation API, it is actually calling the UI Automation core service which, in turn, makes calls to the interfaces implemented by the provider.

    To gain access to the core UI Automation service, a client must create an instance of the [**CUIAutomation**](/previous-versions/windows/desktop/legacy/ff384838(v=vs.85)) object and retrieve an [**IUIAutomation**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomation) interface pointer on the object. The **IUIAutomation** pointer is the client's key to accessing all of the UI Automation functionality that is available to the client. For more information, see [Creating the CUIAutomation Object](uiauto-creatingcuiautomation.md).

2.  **Retrieve IUIAutomationElement interfaces for UI elements from the UI Automation tree.**

    UI Automation exposes individual UI elements as objects that implement the [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface. Information about an element is available to clients through properties exposed by the element's **IUIAutomationElement** interface, along with access to the element's control patterns. Properties and methods exposed by the control pattern interfaces provide access to control-specific information and functionality.

    The UI Automation element objects are provided to clients in a hierarchical tree structure called the UI Automation tree. Clients use methods exposed by the [**IUIAutomation**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomation) interface to retrieve [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interfaces for UI elements in the tree, and to retrieve other interfaces used to search the tree for elements that match a particular set of criteria. For more information, see [Obtaining UI Automation Elements](uiauto-obtainingelements.md).

    When retrieving UI elements, clients can improve system performance by using the caching capabilities of UI Automation. Caching enables a client to specify a set of properties and control patterns to retrieve along with the element. In a single interprocess call, UI Automation retrieves the element and the specified properties and control patterns, and then stores them in the cache. Without caching, a separate interprocess call is required to retrieve each property or control pattern. For more information, see [Caching UI Automation Properties and Control Patterns](uiauto-cachingforclients.md).

3.  **Retrieve UI element properties and invoke UI element functionality.**

    Clients use the [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface to retrieve an element's properties and control patterns. The interface includes two versions of each property retrieval method—one version retrieves the property from the cache, the other retrieves the property from the provider. For more information, see [Retrieving Properties from UI Automation Elements](uiauto-propertiesforclients.md).

4.  **Respond to UI Automation events.**

    UI Automation providers notify clients of changes or important occurrences in the UI by raising events. Clients must determine which events they need, and then implement and register event handling interfaces to receive and process those events. For more information, see [Subscribing to UI Automation Events](uiauto-eventsforclients.md).

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> <dt>

[UI Automation Properties Overview](uiauto-propertiesoverview.md)
</dt> <dt>

[UI Automation Events Overview](uiauto-eventsoverview.md)
</dt> </dl>

 

 