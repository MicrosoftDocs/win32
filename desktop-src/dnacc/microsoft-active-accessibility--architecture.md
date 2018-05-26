---
Description: Rob Sinclair
ms.assetid: 41938c9b-4b98-4b0e-abf3-3ddcb05817e7
title: Microsoft Active Accessibility Architecture
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Microsoft Active Accessibility: Architecture

Rob Sinclair

Microsoft Corporation

May 2000

**Summary:** This is the first of two articles that describe using Microsoft Active Accessibility programming interfaces to write accessible controls, modules, or applications in a COM programming context. This first article presents the basic Active Accessibility architecture and spells out Active Accessibility Server Requirements. (10 printed pages)

For detailed information about Microsoft Active Accessibility, see [Microsoft Active Accessibility](https://msdn.microsoft.com/library/windows/desktop/dd373592).

-   [Introduction](#introduction)
-   [Definitions](#definitions)
-   [Using Active Accessibility Clients](#using-active-accessibility-clients)
-   [Active Accessibility Objects](#active-accessibility-objects)
-   [Types of IAccessible Support](#types-of-iaccessible-support)
    -   [Native Active Accessibility Implementation](#native-active-accessibility-implementation)
    -   [IAccessible Proxies](#iaccessible-proxies)
-   [Creating a Proxy](#creating-a-proxy)
-   [What Information Is Exposed](#what-information-is-exposed)
-   [Generic Proxy Objects](#generic-proxy-objects)
    -   [WinEvents](#users-role-in-winevents)
    -   [USER's role in WinEvents](#users-role-in-winevents)
    -   [Receiving event notifications](#receiving-event-notifications)
    -   [In process](#in-process)
    -   [Out of process](#out-of-process)
    -   [Sending events](#sending-events)
-   [Client-Server Communication](#client-server-communication)
    -   [Event-Driven Communication](#event-driven-communication)
    -   [Retrieving an IAccessible Object](#retrieving-an-iaccessible-object)
-   [Active Accessibility Server Requirements](#active-accessibility-server-requirements)
    -   [Expose Relevant Properties](#expose-relevant-properties)
-   [Support Navigation](#support-navigation)
    -   [Spatial Navigation](#spatial-navigation)
    -   [Logical Navigation](#logical-navigation)
-   [Support Hit Testing](#support-hit-testing)
-   [Generate Appropriate WinEvents](#generate-appropriate-winevents)

## Introduction

Microsoft Active Accessibility is a COM-based technology that provides a standard, consistent mechanism for applications and Active Accessibility clients to exchange information. This technology was integrated into the Microsoft Windows operating system beginning with Windows 98 and continues to be updated with each new release.

> [!Note]  
> Active Accessibility is available as an add-on for Windows 95 and is built into Windows NT 4.0 (Service Pack 6 and later) and Windows 2000.

 

## Definitions

[**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) is the Active Accessibility COM interface.

A dynamic-link library (DLL), OLEACC, provides the Active Accessibility runtime and manages requests from Active Accessibility clients.

An Active Accessibility *client* is any program that uses Active Accessibility to access, identify, or manipulate the user interface (UI) elements of an application. Clients include accessibility aids, automated testing tools, and some computer-based training applications. (*Accessibility aids* are specialized programs that help people with disabilities use computers more effectively.)

Any control, module, or application that uses Active Accessibility to expose information about its user interface is considered an Active Accessibility *server*. Servers communicate with clients by sending event notifications (such as calling [**NotifyWinEvent**](https://msdn.microsoft.com/library/windows/desktop/dd373603)) and responding to client requests for access to UI elements (such as handling [**WM\_GETOBJECT**](https://msdn.microsoft.com/library/windows/desktop/dd373892) messages sent from OLEACC). Servers expose information through the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface.

## Using Active Accessibility Clients

Clients need to know when the server's UI changes so they can convey that information to the user. They learn about changes in the server UI by registering to receive notifications of specific changes through a mechanism called Window Events, or *WinEvents*. For more information, see [WinEvents](#winevents).

To learn about and manipulate a particular UI element, clients use the Active Accessibility COM interface, [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466).

A client can retrieve an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object for a UI element in any of four ways:

-   Call [**AccessibleObjectFromWindow**](https://msdn.microsoft.com/library/windows/desktop/dd317978) and pass the UI element's window handle.
-   Call [**AccessibleObjectFromPoint**](https://msdn.microsoft.com/library/windows/desktop/dd317977) and pass a screen location that lies within the UI element's bounding rectangle.
-   Set a WinEvent hook, receive a notification, and call [**AccessibleObjectFromEvent**](https://msdn.microsoft.com/library/windows/desktop/dd317976) to retrieve an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object for the UI element that generated the event.
-   Call an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) method such as [**accNavigate**](https://msdn.microsoft.com/library/windows/desktop/dd318473) or [**get\_accParent**](https://msdn.microsoft.com/library/windows/desktop/dd318484) to move to a different **IAccessible** object.

## Active Accessibility Objects

In Active Accessibility terminology, there are *accessible objects* and *simple elements*. Although most applications contain both, accessible objects are more common than simple elements.

An *accessible object* is any UI element that implements the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface. To interact with the accessible object, an Active Accessibility client needs only this **IAccessible** object.

A *simple element* is a UI element that shares an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object with other elements and relies on that **IAccessible** object to expose its properties. To differentiate between the elements sharing an **IAccessible** object, the server assigns a unique, positive child identifier to each simple element. This assignment is done on a per-instance-of-interface basis, so the IDs must be unique within that context. Many implementations assign these IDs sequentially, beginning with 1. This scheme does not allow simple elements to have children of their own.

To be completely described, a simple element requires an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object and child ID. Therefore, when communicating with an **IAccessible** object, the clients must supply the appropriate child ID. A special identifier, CHILDID\_SELF, can be used to refer to the accessible object itself, instead of one of its children.

The [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object shared among simple elements often corresponds to a common parent object in the user interface. For example, system list boxes expose an accessible object for the overall list box and simple elements for each list box item. In this case, the **IAccessible** object for the list box is also called the *parent* or *container* of the list items.

## Types of IAccessible Support

There are two types of [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) support found in Active Accessibility servers: native and proxied. The UI elements used in an application determine which type of support is appropriate. Many servers being written today take full advantage of **IAccessible** proxies and only implement **IAccessible** for those controls that are not proxied by OLEACC.

### Native Active Accessibility Implementation

UI elements that implement the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface are said to provide a *native implementation*. Although the development cost for implementing **IAccessible** (or any other COM interface) can be high, the benefit is complete control over the information exposed to clients. By providing native support, an application is free to innovate in its UI while remaining 100 percent accessible.

If your application uses custom controls or other controls that cannot be proxied by OLEACC, you will need to provide a native implementation.

### IAccessible Proxies

[**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) proxies provide default accessibility information for standard UI elements: USER controls, USER menus, and common controls from COMCTL. This default support is exposed through **IAccessible** objects created by OLEACC and delivers Active Accessibility support without additional server development work. However, the server has little control over the information that is exposed.

## Creating a Proxy

To determine whether a UI element natively supports the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) interface, OLEACC sends it a [**WM\_GETOBJECT**](https://msdn.microsoft.com/library/windows/desktop/dd373892) message. A nonzero return value means the element natively supports Active Accessibility and provides its own **IAccessible** support. However, if the return value is zero, OLEACC provides a proxy object for the UI element and attempts to return meaningful information on its behalf.

## What Information Is Exposed

OLEACC uses the *windows* classname for each element to determine what information should be exposed for each of its [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) properties and how to collect that information. For example, OLEACC calls the [**GetWindowText**](https://msdn.microsoft.com/library/windows/desktop/ms633520) function to retrieve the **Name** property for a standard pushbutton, but calls this same function to retrieve the **Value** property for a standard edit control. OLEACC is, in effect, mapping each **IAccessible** method to an appropriate Microsoft Win32 or control-specific message or function call. By using this classname-based special casing, it can return meaningful information through **IAccessible** proxies without any Active Accessibility support in the server.

Applications that use only standard UI elements typically get full Active Accessibility support without additional development work. The exceptions to this rule are controls that have been subclassed, that do not store their own strings (absence of the HASSTRINGS style), or that are owner-drawn. In these cases, OLEACC cannot gather the information it needs because the information is stored outside the control. However, in many of these scenarios there are established workarounds that allow the server to cooperate with the proxies provided by OLEACC.

## Generic Proxy Objects

If OLEACC does not recognize the classname of the UI element, it creates a generic proxy that exposes as much information as possible. At most, this includes the object's bounding rectangle, parent object, name (from [**WM\_GETTEXT**](https://msdn.microsoft.com/library/windows/desktop/ms632627)), and any children in the window hierarchy.

### WinEvents

Window Events (WinEvents) are used by Active Accessibility to notify clients of changes in an application's user interface, such as creating and destroying objects or changing the name, state, or value of a UI element.

### USER's role in WinEvents

WinEvent support is provided by USER, a fundamental part of the Windows operating system. USER provides:

-   A simple way for clients to register for event notifications.
-   A mechanism for injecting client code into servers.
-   Routing of events from servers to interested clients.
-   Automatic event generation for most HWND-based controls.

Event generation for HWND-based controls is especially important for server developers. As discussed earlier, OLEACC provides [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) proxies for standard UI elements. Similarly, USER provides automatic WinEvent support for these same UI elements. Because USER is involved in creating, destroying, moving, resizing, and other actions on standard HWND-based controls, it is the natural candidate to generate the appropriate WinEvents.

USER's automatic event generation completes the "default" Active Accessibility support that is provided for standard controls. Server requirements for generating WinEvents are discussed in the section [Active Accessibility Server Requirements](#active-accessibility-server-requirements).

### Receiving event notifications

Clients register one or more callback functions (with USER) to receive event notifications. To do this, the client calls [**SetWinEventHook**](https://msdn.microsoft.com/library/windows/desktop/dd373640) and specifies which events to receive and how to receive them. The client may choose to:

-   Receive all events or a specific set of events.
-   Receive events from all threads or from a specific thread.
-   Receive events from all processes or from a specific process.
-   Handle events in process or out of process (discussed below).

When an event is generated that matches the specified criteria, USER calls the client's callback function (or "hook procedure").

### In process

An in-process event hook executes in the context of the target process. It typically offers better performance than an out-of-process hook. Also, because the procedure is in the target process, it executes synchronously; therefore, care must be taken to avoid lengthy processing time or other negative impacts on the target process.

To execute in process, the hook procedure must be located in a DLL so it can be injected into the target process. It must be registered with USER by calling [**SetWinEventHook**](https://msdn.microsoft.com/library/windows/desktop/dd373640) with the WINEVENT\_INCONTEXT flag. USER then injects the hook procedure as needed. When the process fires its first event after the client has registered its hook, USER checks to see if the hook procedure has already been injected into the target process. If not, it is injected and the callback is made.

Although an event hook is registered as in process, it will receive some events out of process. This is because kernel processes (and other secure processes) send events but will not allow a client's DLL to be loaded into their process.

### Out of process

Out-of-process event handling is similar to calling a [**PostMessage**](https://msdn.microsoft.com/library/windows/desktop/ms644944) because the notifications are received asynchronously. The event hook is not injected into the target process; thus, it can live in a DLL or in the client's executable. Clients must be prepared to handle possible reentrancy when handling events out of process.

### Sending events

To broadcast an event notification to all interested clients, servers call [**NotifyWinEvent**](https://msdn.microsoft.com/library/windows/desktop/dd373603) and pass information that identifies the type of event and the UI element to which the event applies. Clients can use this information to retrieve an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object for the UI element and collect more information.

For example, to notify clients that a control's name has changed, a server calls [**NotifyWinEvent**](https://msdn.microsoft.com/library/windows/desktop/dd373603) and passes EVENT\_OBJECT\_NAMECHANGE in the *event* parameter.

As just discussed, when a server calls [**NotifyWinEvent**](https://msdn.microsoft.com/library/windows/desktop/dd373603), USER determines which clients are interested in that particular event and calls their registered callback function. If no clients have registered for that event, the server's call to **NotifyWinEvent** is comparable to a NO-OP and the performance impact is negligible.

For more guidelines and information on WinEvents, see [Microsoft Active Accessibility](https://msdn.microsoft.com/library/windows/desktop/dd373592).

## Client-Server Communication

The WinEvent mechanism provides a way for servers to easily communicate with Active Accessibility clients. Clients often collect information by reacting to WinEvents (for example, following focus), but they are free to request information from a server at any time.

### Event-Driven Communication

As discussed earlier, clients must register a WinEvent hook before they can receive WinEvent notifications. To avoid unnecessary callbacks and improve performance, clients are advised to register only for the events they need to receive.

Inside the hook procedure, the client can call [**AccessibleObjectFromEvent**](https://msdn.microsoft.com/library/windows/desktop/dd317976) to retrieve an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object for the element to which the event applies. With this object, the client can begin calling **IAccessible** methods to retrieve information or interact with the UI element.

### Retrieving an IAccessible Object

To collect specific information about a UI element, clients must first retrieve an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) for the element. To retrieve an element's **IAccessible**object, clients can use one of the **AccessibleObjectFrom***X* functions:

-   [**AccessibleObjectFromPoint**](https://msdn.microsoft.com/library/windows/desktop/dd317977)
-   [**AccessibleObjectFromWindow**](https://msdn.microsoft.com/library/windows/desktop/dd317978)
-   [**AccessibleObjectFromEvent**](https://msdn.microsoft.com/library/windows/desktop/dd317976)

Here is an example of this type of request:

Client calls **AccessibleObjectFrom***X*.

1.  OLEACC sends a [**WM\_GETOBJECT**](https://msdn.microsoft.com/library/windows/desktop/dd373892) message to server.
2.  The server determines which UI element corresponds to the request.
3.  The server either:

    Returns zero to request an OLEACC proxy.

    -or-

    Returns an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object (native implementation). To do this, it:

    -   Constructs an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object for the element.
    -   Calls [**LresultFromObject**](https://msdn.microsoft.com/library/windows/desktop/dd318557) to marshal the object's pointer.
    -   Returns the LRESULT to OLEACC.

4.  OLEACC examines the return value from [**WM\_GETOBJECT**](https://msdn.microsoft.com/library/windows/desktop/dd373892).

    If it is zero, OLEACC constructs a proxy object and returns it to the client.

    -or-

    If it is nonzero, OLEACC calls [**ObjectFromLresult**](https://msdn.microsoft.com/library/windows/desktop/dd373605) to unmarshal the native [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object pointer and returns it to the client.

## Active Accessibility Server Requirements

An application is considered an Active Accessibility server if it:

-   Adheres to Windows Guidelines for Accessible Software Design.
-   Exposes relevant properties.
-   Supports proper navigation.
-   Supports proper hit testing.
-   Generates appropriate WinEvents.

Depending on the application's design and implementation, some of these requirements may be satisfied by Active Accessibility's default support.

### Expose Relevant Properties

Not all [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) properties and methods are relevant for all UI elements. The properties supported by an object vary depending on the type of UI element the object represents. If an object does not support a particular **IAccessible** property or method, it should return the standard COM error "Member Not Found" (DISP\_E\_MEMBERNOTFOUND). If the method will be supported but has not yet been implemented, it should return "Not Implemented" (E\_NOTIMPL).

Servers must support the following properties and methods for every object:

-   Name
-   Role
-   State
-   Location (and [**IAccessible::accHitTest**](https://msdn.microsoft.com/library/windows/desktop/dd318471))
-   Parent (and [**IAccessible::accNavigate**](https://msdn.microsoft.com/library/windows/desktop/dd318473))
-   Child Count

The following properties must be supported if they are applicable to the object:

-   Keyboard Shortcut
-   Default Action (and [**IAccessible::accDoDefaultAction**](https://msdn.microsoft.com/library/windows/desktop/dd318477))
-   Value

The following properties must be supported if the object has children:

-   Child
-   Focus
-   Selection (and[**IAccessible::accSelect**](https://msdn.microsoft.com/library/windows/desktop/dd318474))

The following properties are optional, but they provide useful information about the object. In particular, the **Description** property should be supported to describe bitmaps and other visual elements:

-   Description
-   Help or Help Topic

For more specific information regarding these properties and which are relevant for a particular type of UI element, refer to the Active Accessibility SDK.

## Support Navigation

By using [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) navigation, a client can move through the Active Accessibility object hierarchy and dynamically discover what UI elements and objects are available. Therefore, all UI elements must support the [**accNavigate**](https://msdn.microsoft.com/library/windows/desktop/dd318473) method.

The two [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) navigation modes are *spatial navigation* (up, down, left, right) and *logical navigation* (next, previous, parent, first child, last child).

### Spatial Navigation

A client uses spatial navigation to move from one UI element to another based on their on-screen position. However, an accessible object must support spatial navigation only to its siblings. Spatial navigation is relevant only within the context of a single container.

Practically speaking, this form of navigation is rarely meaningful to an end user unless the UI elements are arranged in a grid where it is meaningful to navigate left, right, up, and down.

Consider a list-view control in large icon view. Because all icons are children of the parent list-view control (that is, they are siblings to each other) and they are arranged in a near-grid pattern, spatial navigation is a natural means for moving between UI elements and should be supported.

### Logical Navigation

Clients can use logical navigation to explore the Active Accessibility object hierarchy and discover what controls and elements exist. To do this, clients rely on proper support for navigation from an [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) object to its parent, children, and siblings. This form of navigation also provides the foundation on which Active Accessibility clients can develop more powerful capabilities, such as hands-free navigation of UI elements.

For the list-view control just described in [Spatial Navigation](#spatial-navigation), logical navigation provides a simple mechanism for visiting each list-view icon exactly one time. To do this, the client could begin with the list-view control's [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466)object, navigate to its first child, and then repeatedly navigate *next* until [**accNavigate**](https://msdn.microsoft.com/library/windows/desktop/dd318473) fails. Beginning with the list-view control's last child and repeatedly navigating *previous* achieves the same result.

Because logical navigation is widely used by Active Accessibility clients, all servers must ensure full support for this form of navigation.

For more information, see [Microsoft Active Accessibility](https://msdn.microsoft.com/library/windows/desktop/dd373592).

## Support Hit Testing

Active Accessibility uses hit testing to drill down through the [**IAccessible**](https://msdn.microsoft.com/library/windows/desktop/dd318466) hierarchy to retrieve an **IAccessible** object for the UI element at a specified screen location. OLEACC's [**AccessibleObjectFromPoint**](https://msdn.microsoft.com/library/windows/desktop/dd317977) function relies on proper support for [**IAccessible::accHitTest**](https://msdn.microsoft.com/library/windows/desktop/dd318471) to find the appropriate UI element. Therefore, all visual UI elements must support hit testing through the **accHitTest** method.

## Generate Appropriate WinEvents

Server developers need to ensure that appropriate WinEvents are generated for all UI elements, including window-based UI elements, windowless UI elements, and UI elements with highly customized behavior.

USER provides default WinEvent support for standard, HWND-based UI elements. Because USER generates these events automatically, servers need to generate events only for custom controls, windowless elements, or controls whose events are not already generated by USER.

To send an event, servers call [**NotifyWinEvent**](https://msdn.microsoft.com/library/windows/desktop/dd373603) and pass the event constant, an identifier (object ID) for the object, and the HWND for a window that can respond to client requests for more information. The events that need to be fired vary according to the type of UI element.

To learn which events are expected for a particular type of UI element, run the [Accessible Event Watcher](https://msdn.microsoft.com/library/windows/desktop/dd317979) tool, AccEvent (available in the [Microsoft Windows Software Development Kit](http://go.microsoft.com/fwlink/p/?linkid=154879)), to see which events are already being sent by USER.

 

 



