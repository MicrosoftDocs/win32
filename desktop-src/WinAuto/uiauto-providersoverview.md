---
title: UI Automation Providers Overview
description: This topic provides an overview of how control developers implement UI Automation providers.
ms.assetid: 8928c889-0e0a-439f-87e8-a9d121fcf73f
keywords:
- UI Automation,providers overview
- UI Automation,provider types
- UI Automation,provider concepts
- providers,about
- providers,types
- providers,concepts
- providers,elements
- providers,navigation
- providers,views
- providers,frameworks
- providers,fragments
- providers,hosts
ms.topic: article
ms.date: 05/31/2018
---

# UI Automation Providers Overview

A Microsoft UI Automation provider is a software object that exposes an element of an application's UI so that accessibility client applications can retrieve information about the element and invoke its functionality. In general, each control or other distinct element in a UI has a provider.

Microsoft includes a provider for each of the standard controls that are supplied with Microsoft Win32, Windows Forms, and Windows Presentation Foundation (WPF). This means that the standard controls are automatically exposed to UI Automation clients; you do not need to implement any accessibility interfaces for the standard controls.

If your application includes any custom controls, you need to implement UI Automation providers for those controls to make them accessible to accessibility client applications. You also need to implement providers for any third party controls that do not include a provider. You implement a provider by implementing UI Automation provider interfaces and control pattern interfaces.

This topic provides an overview of how control developers implement UI Automation providers. It includes the following sections.

-   [Types of Providers](#types-of-providers)
-   [UI Automation Provider Concepts](#ui-automation-provider-concepts)
    -   [Elements](#elements)
    -   [Frameworks](#frameworks)
    -   [Fragments](#fragments)
    -   [Hosts](#hosts)
-   [Related topics](#related-topics)

## Types of Providers

UI Automation providers fall into two categories: server-side providers, and client-side (or *proxy*) providers.

A server-side provider is an object, such as a custom control, that contains its own native implementation of the relevant UI Automation provider interfaces. A server-side provider communicates with client applications across the process boundary by exposing its implementation of the provider interfaces to the UI Automation core, which services requests from clients. For more information about server-side providers, see [Implementing a Server-Side UI Automation Provider](uiauto-serversideprovider.md).

A client-side provider, or proxy, is an object that implements UI Automation provider interfaces on behalf of a control does not include a full provider implementation of its own. Without a proxy, such a control is largely opaque to UI Automation, which can supply only basic information available from the window handle (**HWND**), such as the control location. Typically, proxy providers communicate with the application across the process boundary by sending and receiving Windows messages. For more information, see [Implementing a Client-Side (Proxy) UI Automation Provider](uiauto-clientsideprovider.md).

## UI Automation Provider Concepts

This section provides brief explanations of some of the key concepts you need to understand in order to implement UI Automation providers.

### Elements

UI Automation elements are pieces of the UI—typically windows or controls—that are visible to UI Automation clients. Examples include application windows, panes, buttons, tooltips, list boxes, and list items.

UI Automation elements are exposed to clients as a tree. UI Automation constructs the tree by navigating from one element to another. Navigation is enabled by the provider for each element. Each element can point to its own parent element, its sibling elements, and its first and last child elements.

A client can see the UI Automation tree in three principal views, as described in the following table:



| View         | Description                                                    |
|--------------|----------------------------------------------------------------|
| Raw view     | Includes all elements.                                         |
| Control view | Includes elements that are controls.                           |
| Content view | Includes control elements that convey information to the user. |



 

It is the responsibility of the provider implementation to define an element as a content element or a control element. Control elements may or may not also be content elements, but all content elements are control elements.

For more information on the client view of the tree, see [UI Automation Tree Overview](uiauto-treeoverview.md).

### Frameworks

A framework is a component that manages child controls, hit-testing, and rendering in an area of the screen. For example, a Win32 window, often referred to as an **HWND**, can serve as a framework that contains multiple UI Automation elements, such as a menu bar, a status bar, and buttons.

Win32 container controls such as list boxes and tree-view controls are considered to be frameworks because they contain their own code for rendering child items and performing hit-testing on them. By contrast, a WPF list box is not a framework, because the rendering and hit-testing is being handled by the containing window.

The UI in an application can be made up of different frameworks. For example, an **HWND** in an application might contain Dynamic HTML (DHTML) which in turn can contain a component such as a combo box in an **HWND**.

### Fragments

A complete subtree of elements from a particular framework is called a fragment. The element at the root node of the subtree is called a fragment root. A fragment root does not have a parent, but is hosted within some other framework, usually a Win32 window (**HWND**).

### Hosts

The root node of every fragment must be hosted in an element, usually a Win32 window (**HWND**). The exception is the desktop, which is not hosted in any other element. The host of a custom control is the **HWND** of the control itself, not the application window or any other window that might contain groups of top-level controls.

The host of a fragment plays an important role in providing UI Automation services. It enables navigation to the fragment root, and supplies some default properties so that the custom provider does not have to implement them.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Implementing a Client-Side UI Automation Provider](uiauto-clientsideprovider.md)
</dt> <dt>

[Implementing a Server-Side UI Automation Provider](uiauto-serversideprovider.md)
</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




