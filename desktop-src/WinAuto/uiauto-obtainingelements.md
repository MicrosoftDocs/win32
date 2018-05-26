---
title: Obtaining UI Automation Elements
description: This topic describes various ways to obtain IUIAutomationElement interfaces for UI elements.
ms.assetid: 8675851a-4a72-4cbe-ab71-ed6fc891be17
keywords:
- clients,obtaining UI Automation elements
- clients,UI Automation elements
- clients,root elements
- clients,search scope
- UI Automation,obtaining elements
- UI Automation,elements
- UI Automation,root elements
- UI Automation,conditions
- UI Automation,search scope
- obtaining UI Automation elements
- root elements
- search scope
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining UI Automation Elements

This topic describes various ways to obtain [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) interfaces for UI elements. It contains the following sections:

-   [Root Element](#root-element)
-   [Conditions](#conditions)
-   [Search Scope](#search-scope)
-   [Finding a Known Element](#finding-a-known-element)
-   [Finding Elements in a Subtree](#finding-elements-in-a-subtree)
-   [Walking a Subtree](#walking-a-subtree)
-   [Other Ways to Retrieve an Element](#other-ways-to-retrieve-an-element)
    -   [From an Event](#from-an-event)
    -   [From a Point](#from-a-point)
    -   [From a Window Handle](#from-a-window-handle)
    -   [From the Focused Control](#from-the-focused-control)
-   [Related topics](#related-topics)

## Root Element

Although elements can be retrieved directly by using methods, such as [**IUIAutomation::GetFocusedElement**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-getfocusedelement?branch=master), some client applications require a view of the hierarchical structure of elements, known as the UI Automation tree. The root element of this hierarchy is the desktop. You can obtain this element by using the [**IUIAutomation::GetRootElement**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-getrootelement?branch=master) method or the [**IUIAutomation::GetRootElementBuildCache**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-getrootelementbuildcache?branch=master) method. Both these methods retrieve an [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) interface pointer. You can search for descendant elements by using methods, such as [**IUIAutomationElement::FindFirst**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findfirst?branch=master) and [**FindAll**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findall?branch=master).

> [!Note]  
> In general, you should try to obtain only direct children of the root element. A search for descendants may iterate through hundreds or thousands of elements. If you are attempting to obtain a specific element at a lower level, you should start your search from the application window or from a container at a lower level.

 

## Conditions

For most techniques you use to retrieve UI Automation elements, you must specify a condition. A condition is a set of criteria that defines the elements that you want to retrieve. A condition is represented by the [**IUIAutomationCondition**](/windows/win32/UIAutomationClient/?branch=master) interface.

The simplest condition is the true condition, which is a predefined object that specifies that all elements in the search scope are to be returned. The false condition is the inverse of the true condition and is less useful, because it would prevent any elements from being found. You can obtain an interface to the true condition by using [**IUIAutomation::CreateTrueCondition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-createtruecondition?branch=master).

Three other predefined conditions, available as properties on the [**IUIAutomation**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation?branch=master) object, can be used alone or in combination with other conditions: [**IUIAutomation::ContentViewCondition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-get_contentviewcondition?branch=master), [**ControlViewCondition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-get_controlviewcondition?branch=master), and [**RawViewCondition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-get_rawviewcondition?branch=master). **RawViewCondition**, used by itself, is equivalent to the true condition, because it does not filter elements by the [**IUIAutomationElement::CurrentIsControlElement**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentiscontrolelement?branch=master) or [**CurrentIsContentElement**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentiscontentelement?branch=master) properties.

Other conditions are built from condition objects, each of which specifies a property value. For example, a property condition might specify that the element is enabled or that it supports a certain control pattern.

Conditions that use Boolean logic can be combined by calling [**IUIAutomation::CreateAndCondition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-createandcondition?branch=master), [**CreateOrCondition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-createorcondition?branch=master), [**CreateNotCondition**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-createnotcondition?branch=master), and related methods.

## Search Scope

Searches that are performed by using [**IUIAutomationElement::FindFirst**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findfirst?branch=master) or [**FindAll**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findall?branch=master) must have a scope and a starting place.

> [!Note]  
> Any commentary about these two methods also applies to [**IUIAutomationElement::FindFirstBuildCache**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findfirstbuildcache?branch=master) and [**FindAllBuildCache**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findallbuildcache?branch=master).

 

The scope defines the space around the starting place that is to be searched. This might include the element itself, its siblings, its parent, its immediate children, and its descendants. Be aware that the **Find** methods do not support searching up the Microsoft UI Automation tree; that is, searching for ancestor elements is not supported.

The scope of a search is defined by a bitwise combination of values from the [**TreeScope**](/windows/win32/UIAutomationClient/ne-uiautomationclient-treescope?branch=master) enumerated type.

## Finding a Known Element

To find a known element that is identified by name, automation ID, or some other property or combination of properties, it is easiest to use the [**IUIAutomationElement::FindFirst**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findfirst?branch=master) method. If the element sought is an application window, the starting point of the search can be the root element.

This way of finding UI Automation elements is most useful in automated testing scenarios.

For a code example that shows how to find a know element, see [Finding an Element by Name](uiauto-howto-find-ui-elements.md#finding-an-element-by-name).

## Finding Elements in a Subtree

To find all elements that meet specific criteria and are related to a known element, you can call [**IUIAutomationElement::FindAll**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findall?branch=master) on the known element. For example, use this method to retrieve list items or menu items from a list or menu, or to identify all controls in a dialog box.

For a code example that shows how to find elements in a subtree, see [Finding Related Elements](uiauto-howto-find-ui-elements.md#finding-related-elements).

## Walking a Subtree

If you have no prior knowledge of the applications that your client may be used with, you can construct a subtree of all elements of interest by using [**IUIAutomationTreeWalker**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtreewalker?branch=master). Your client might do this, for example, in response to a focus-changed event; that is, when an application or control receives input focus, the UI Automation client examines children and perhaps all descendants of the focused element.

Be aware that walking the UI Automation tree is resource-intensive. Walk the tree only when it is not feasible to use the [**IUIAutomationElement::FindFirst**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findfirst?branch=master), [**FindAll**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findall?branch=master), or [**BuildUpdatedCache**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-buildupdatedcache?branch=master) methods.

You can define your own tree walker by passing a custom condition to [**IUIAutomation::CreateTreeWalker**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-createtreewalker?branch=master), or you can use one of the following predefined objects that are defined as properties of the base [**IUIAutomation**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomation?branch=master).



| Object                                                              | Purpose                                                                                                                                                      |
|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ContentViewWalker**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-get_contentviewwalker?branch=master) | Finds only elements whose [**IUIAutomationElement::CurrentIsContentElement**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentiscontentelement?branch=master) property is **TRUE**. |
| [**ControlViewWalker**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-get_controlviewwalker?branch=master) | Finds only elements whose [**IUIAutomationElement::CurrentIsControlElement**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-get_currentiscontrolelement?branch=master) property is **TRUE**. |
| [**RawViewWalker**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-get_rawviewwalker?branch=master)         | Finds all elements.                                                                                                                                          |



 

After you obtain an [**IUIAutomationTreeWalker**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtreewalker?branch=master), call the **IUIAutomationTreeWalker::GetXxx** methods to navigate elements of the subtree, passing in the element from which to start walking.

The [**IUIAutomationTreeWalker::Normalize**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomationtreewalker-normalizeelement?branch=master) method can be used for navigating to an element in the subtree from another element that is not part of the view. For example, suppose you create a view of a subtree by using [**IUIAutomation::ContentViewWalker**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-get_contentviewwalker?branch=master). Your application receives notification that a scroll bar has received the input focus. Because a scroll bar is not a content element, it is not present in your view of the subtree. However, you can pass the [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) that represents the scroll bar to **IUIAutomationTreeWalker::Normalize** and retrieve the nearest ancestor that is in the content view.

For code examples that show how to use the [**IUIAutomationTreeWalker**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationtreewalker?branch=master) interface, see [How to Walk the UI Automation Tree](uiauto-howto-walk-uiautomation-tree.md).

## Other Ways to Retrieve an Element

In addition to searches and navigation, you can retrieve an [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) in the following ways.

### From an Event

When your application receives a UI Automation event, the source object passed to your event handler is represented by an [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master). For example, if you subscribe to focus-changed events, the source passed to your [**IUIAutomationFocusChangedEventHandler**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationfocuschangedeventhandler?branch=master) is the element that received the focus. For more information, see [Subscribing to UI Automation Events](uiauto-eventsforclients.md).

### From a Point

To retrieve an [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) from screen coordinates, for example, a cursor position, use the [**IUIAutomation::ElementFromPoint**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfrompoint?branch=master) method.

### From a Window Handle

To retrieve an [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) from an **HWND**, use the [**IUIAutomation::ElementFromHandle**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-elementfromhandle?branch=master) method.

### From the Focused Control

To retrieve an [**IUIAutomationElement**](/windows/win32/UIAutomationClient/nn-uiautomationclient-iuiautomationelement?branch=master) that represents the focused control, use the [**IUIAutomation::GetFocusedElement**](/windows/win32/UIAutomationClient/nf-uiautomationclient-iuiautomation-getfocusedelement?branch=master) method.

## Related topics

<dl> <dt>


</dt> <dt>

[UI Automation Tree Overview](uiauto-treeoverview.md)
</dt> </dl>

 

 




