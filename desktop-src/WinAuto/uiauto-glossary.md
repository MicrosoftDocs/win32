---
title: Glossary (Windows Accessibility features)
description: Glossary page
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: c45583f2-a6e8-4a01-9577-9b604b5bbc62
ms.topic: article
ms.date: 05/31/2018
---

# Glossary (Windows Accessibility features)

## A

<dl> <dt>

**access key**
</dt> <dd>

An underlined character in the text of a control's label.

</dd> <dt>

**accessibility aid**
</dt> <dd>

Also called assistive technology; specialized programs that work with a computer's operating system to accommodate specific impairments, such as a limited range of motion or blindness. Products include larger keyboards, eye-gaze-operated keyboards, voice input utilities, onscreen keyboards, and products that can convert text to speech or to a dynamic Braille display. For more information, see [Assistive Technology Products](https://www.microsoft.com/enable/at/default.aspx).

</dd> <dt>

**accessible object**
</dt> <dd>

Any user interface element that implements the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface and has properties that describe the object's name, screen locations, and other information needed by accessibility aids. For more information, see [Accessible Objects](accessible-objects.md).

</dd> </dl>

## C

<dl> <dt>

**child element**
</dt> <dd>

See [*simple element*](uiauto-glossary.md).

</dd> <dt>

**client**
</dt> <dd>

Any program that uses UI Automation or Microsoft Active Accessibility to access, identify, or manipulate the user interface elements of an applications; clients include accessibility aids, automated testing tools, and some computer-based training applications. For more information, see [How Active Accessibility Works](how-active-accessibility-works.md).

</dd> <dt>

**client-side provider**
</dt> <dd>

A software component that is implemented by a UI Automation client to retrieve information about the UI of an application that does not support, or does not fully support, UI Automation. Typically, client-side providers (proxies) communicate with the application across the process boundary by sending and receiving Windows messages.

</dd> <dt>

**container**
</dt> <dd>

Also called a parent; an accessible object that corresponds to one or more simple elements; for example, an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object for a list box is the parent of the list items.

</dd> <dt>

**control pattern**
</dt> <dd>

In UI Automation, a design implementation that describes a discrete piece of functionality for a control. This functionality can include the visual appearance of a control and the actions it can perform.

</dd> <dt>

**control pattern object**
</dt> <dd>

A run-time instance of a COM object that exposes one or more control pattern interfaces.

</dd> <dt>

**control pattern provider**
</dt> <dd>

A software component that implements one or more control pattern interfaces.

</dd> <dt>

**custom control**
</dt> <dd>

A control authored by a user or third-party software vendor, or a system-defined control that was modified by a user or third-party software vendor.

</dd> </dl>

## D

<dl> <dt>

**degenerate text range (empty range)**
</dt> <dd>

An object that represents an empty (zero-character) span of text. A degenerate text range has adjacent endpoints and specifies a point between two characters.

</dd> <dt>

**disjoint text range**
</dt> <dd>

An object that represents multiple spans of text that are not physically adjacent to each other.

</dd> <dt>

**docking container**
</dt> <dd>

A control that allows the arrangement of child elements, both horizontally and vertically, relative to the boundaries of the docking container and other elements within the container.

</dd> </dl>

## E

<dl> <dt>

**event listener**
</dt> <dd>

A client application that has registered to receive notifications from UI Automation or Microsoft Active Accessibility whenever specific UI changes occur.

</dd> <dt>

**event notification**
</dt> <dd>

A call from a UI Automation provider to a client, in which the provider notifies the client of an event that might affect the state or appearance of a UI item.

</dd> </dl>

## F

<dl> <dt>

**filter\[ing\]**
</dt> <dd>

To define the types of UI Automation elements to be included in a view of the UI Automation tree. See also: raw view, control view, and content view.

</dd> <dt>

**fragment root**
</dt> <dd>

The UI Automation element at the root node of a subtree of the UI Automation tree. A fragment root does not have a parent but is hosted within some other framework, usually a Win32 window handle (**HWND**).

</dd> </dl>

## H

<dl> <dt>

**host**
</dt> <dd>

A UI element, such as a window or control, that contains other UI elements. A host performs UI Automation services on behalf of the hosted elements.

</dd> </dl>

## I

<dl> <dt>

**IAccessible**
</dt> <dd>

The COM interface that contains all the methods and properties for Microsoft Active Accessibility.

</dd> <dt>

**IAccessible proxy**
</dt> <dd>

A type of [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) support that provides default accessibility information for standard UI elements: USER controls, USER menus, and common controls from COMCTL and COMCTL32. For more information, see [IAccessible Proxies](iaccessible-proxies.md).

</dd> </dl>

## L

<dl> <dt>

**logical navigation**
</dt> <dd>

One of two [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) navigation modes in which a client explores the Microsoft Active Accessibility object hierarchy (next, previous, parent, first child, last child).

</dd> </dl>

## M

<dl> <dt>

**marshaling**
</dt> <dd>

Packaging and sending interface parameters across process boundaries.

</dd> </dl>

## N

<dl> <dt>

**native implementation**
</dt> <dd>

The type of support provided by user interface elements that implement the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface.

</dd> </dl>

## O

<dl> <dt>

**off-screen model**
</dt> <dd>

This model is a database of objects on the screen and includes their properties and their spatial relationships.

</dd> <dt>

**OLEACC**
</dt> <dd>

The dynamic-link library that provides the Microsoft Active Accessibility run time and manages requests from Microsoft Active Accessibility clients.

</dd> </dl>

## P

<dl> <dt>

**parent**
</dt> <dd>

Also called a container; an accessible object that corresponds to one or more simple elements; for example, an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object for a list box is the parent of the list items

</dd> <dt>

**placeholder automation element**
</dt> <dd>

A UI Automation element that represents a virtualized item in the UI Automation tree. Typically, a placeholder does not have loaded data for all UI Automation properties, and it is required to implement only the [VirtualizedItem](uiauto-implementingvirtualizeditem.md) control pattern.

</dd> <dt>

**property-changed event**
</dt> <dd>

An event that is triggered when the value of a property has changed. Clients register to receive specific property-changed events, and UI Automation notifies the registered clients when those events occur.

</dd> <dt>

**provider interface**
</dt> <dd>

A collection of public methods implemented by a UI Automation provider.

</dd> <dt>

**proxy**
</dt> <dd>

See [*IAccessible proxy*](uiauto-glossary.md).

</dd> </dl>

## R

<dl> <dt>

**raw view**
</dt> <dd>

The full tree of [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) objects in the UI Automation tree for which the desktop is the root. The raw view closely follows the native programmatic structure of an application and, therefore, is the most accurate view of the UI structure. It is also the base on which the other views of the tree are built.

</dd> <dt>

**realized item**
</dt> <dd>

A UI item for which full information has been loaded into memory, enabling UI Automation to create an automation element for the item.

</dd> <dt>

**run-time identifier**
</dt> <dd>

An array of integers that identifies the running instance of a UI Automation element. The identifier is unique within the UI of the desktop on which it was generated.

</dd> </dl>

## S

<dl> <dt>

**safe array**
</dt> <dd>

A self-describing data type for declaring arrays used in creating COM components. Along with the data, a safe array contains information about the number and bounds of its dimensions.

</dd> <dt>

**scoping**
</dt> <dd>

Defining the extent of the view, starting from a base element.

</dd> <dt>

**server**
</dt> <dd>

Any control, module, or applications that uses Microsoft Active Accessibility to expose information about its user interface

</dd> <dt>

**server-side provider**
</dt> <dd>

A software component that exposes information about a UI element that is based on a UI framework that does not support UI Automation natively. Server-side providers (native providers) communicate with client applications across the process boundary by exposing COM interfaces to the UI Automation core system, which services requests from clients.

</dd> <dt>

**simple element**
</dt> <dd>

Also known as a Child Element; any user interface element that shares an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object with other elements and relies on that **IAccessible** object to expose its properties. For more information, see [Simple Elements](simple-elements.md).

</dd> <dt>

**spatial navigation**
</dt> <dd>

One of two [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) navigation modes in which a client moves from one user interface element to another based on their on-screen positions (up, down, left, right).

</dd> </dl>

## T

<dl> <dt>

**Text Services Framework**
</dt> <dd>

A scalable system framework that enables natural language services and advanced text input on the desktop and within applications.

</dd> <dt>

**text unit**
</dt> <dd>

A predefined unit of text (character, word, line, or paragraph) used for navigating through logical segments of a text range.

</dd> </dl>

## U

<dl> <dt>

**UI Automation client**
</dt> <dd>

An assistive technology application, such as a screen reader, that uses UI Automation to obtain programmatic access to the UI elements in an application user interface. The client presents information about UI elements to the end user. Automated test scripts are also considered to be UI Automation clients.

</dd> <dt>

**UI Automation core**
</dt> <dd>

A run-time component that implements the UI Automation framework.

</dd> <dt>

**UI Automation element**
</dt> <dd>

A UI item that is represented by a COM object that implements a UI Automation provider interface and that exposes the [**IUIAutomationElement**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationelement) interface to UI Automation clients.

</dd> <dt>

**UI Automation framework**
</dt> <dd>

An integral Windows component that supports programmatic access to most UI elements on the desktop. It enables assistive technology products such as screen readers to provide information about the UI to end users, and to manipulate the UI by means other than standard input. UI Automation also allows automated test scripts to interact with the UI.

</dd> <dt>

**UI Automation node**
</dt> <dd>

Deprecated. See UI Automation element.

</dd> <dt>

**UI Automation provider**
</dt> <dd>

An implementation of UI Automation interfaces that exposes programmatic information about a UI element. The provider supplies this information to the UI Automation framework in response to UI Automation client requests.

</dd> <dt>

**UI Automation tree**
</dt> <dd>

A hierarchical representation of all UI Automation elements on the Windows desktop. The tree consists of a root element that represents the current desktop, and whose child elements represent application Windows. Each of these child elements can contain elements that represent pieces of the UI, such as menus, buttons, toolbars, and list boxes. These elements can contain elements such as list items.

</dd> <dt>

**UI framework**
</dt> <dd>

A component that manages child controls, hit-testing, and rendering in an area of the screen.

</dd> </dl>

## V

<dl> <dt>

**view identifier**
</dt> <dd>

A value that identifies a view that is available for a UI Automation element that implements a control pattern. This type of element provides and is able to switch between multiple representations of the same set of information or child controls.

</dd> <dt>

**virtualized item**
</dt> <dd>

A UI element that is loaded into memory only when it is needed, typically when the element becomes visible on the screen. A virtualized item is represented by a placeholder automation element in the UI Automation tree.

</dd> </dl>

## W

<dl> <dt>

**Window Events (WinEvents)**
</dt> <dd>

The type of event used to notify clients that an accessible object has changed in some manner.

</dd> <dt>

**window-based element**
</dt> <dd>

A UI Automation element that represents a UI item that has its own Win32 window handle (**HWND**).

</dd> </dl>

 

 




