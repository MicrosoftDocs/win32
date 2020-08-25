---
title: Implement a Server-Side UI Automation Provider
description: This topic describes how to implement a server-side Microsoft UI Automation provider for a custom control written in C++.
ms.assetid: c3a919b2-8b8c-4dde-ad71-587f3845a9f5
keywords:
- UI Automation,server-side provider implementation
- UI Automation,provider implementation
- UI Automation,implementing server-side providers
- UI Automation,implementing providers
- server-side providers,implementing
- server-side providers,interfaces
- server-side providers,property values
- server-side providers,events
- server-side providers,assigning a new parent
- events,server-side providers
- interfaces,server-side providers
- providers,implementing
- implementing server-side providers
- implementing providers
ms.topic: article
ms.date: 05/31/2018
---

# Implement a Server-Side UI Automation Provider

This topic describes how to implement a server-side Microsoft UI Automation provider for a custom control written in C++. It contains the following sections:

-   [Provider Interfaces](#provider-interfaces)
-   [Required Functionality for UI Automation Providers](#required-functionality-for-ui-automation-providers)
-   [Property Values](#property-values)
-   [Events from Providers](#events-from-providers)
-   [Provider Navigation](#provider-navigation)
-   [Assigning a New Parent](#assigning-a-new-parent)
-   [Provider Repositioning](#provider-repositioning)
-   [Disconnecting Providers](#disconnecting-providers)
-   [Related topics](#related-topics)

For code examples that show how to implement server-side providers, see [How-To Topics for UI Automation Providers](uiauto-howto-topics-for-uiautomation-providers.md).

## Provider Interfaces

The following Component Object Model (COM) interfaces provide functionality for custom controls. To provide basic functionality, every UI Automation provider must implement at least the [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple) interface. The [**IRawElementProviderFragment**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment) and [**IRawElementProviderFragmentRoot**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragmentroot) interfaces are optional, but should be implemented for elements in a complex control to provide additional functionality.



| Interface                                                                         | Description                                                                                                                                                                   |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple)             | Provides basic functionality for a control hosted in a window, including support for control patterns and properties.                                                         |
| [**IRawElementProviderFragment**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment)         | Adds functionality for an element in a complex control, including navigating in the fragment, setting focus, and returning the bounding rectangle of the element.             |
| [**IRawElementProviderFragmentRoot**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragmentroot) | Adds functionality for the root element in a complex control, including locating a child element at specified coordinates and setting the focus state for the entire control. |



 

> [!Note]  
> In the UI Automation API for managed code, these interfaces form an inheritance hierarchy. This is not the case in C++, where the interfaces are completely separate.

 

The following interfaces provide added functionality but implementation is optional.



| Interface                                                                         | Description                                                                             |
|-----------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| [**IRawElementProviderAdviseEvents**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovideradviseevents) | Enables the provider to track requests for events.                                      |
| [**IRawElementProviderHwndOverride**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderhwndoverride) | Enables repositioning of window-based elements in the UI Automation tree of a fragment. |



 

## Required Functionality for UI Automation Providers

To communicate with UI Automation, your control must implement the main areas of functionality described in the following table.



| Functionality                                              | Implementation                                                                                                                                                                                                                                                                                                |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Expose the provider to UI Automation.                      | In response to a [**WM\_GETOBJECT**](wm-getobject.md) message sent to the control window, return the object that implements [**IRawElementProviderSimple**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovidersimple). For fragments, this must be the provider for the fragment root.                                           |
| Provide property values.                                   | Implement [**IRawElementProviderSimple::GetPropertyValue**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-getpropertyvalue) to provide or override values.                                                                                                                                                             |
| Enable the client to interact with the control.            | Implement interfaces that support each appropriate control pattern, such as [**IInvokeProvider**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iinvokeprovider). Return these control pattern providers in your implementation of [**IRawElementProviderSimple::GetPatternProvider**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-getpatternprovider). |
| Raise events.                                              | [**UiaRaiseAutomationEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseautomationevent), methods of [**IProxyProviderWinEventSink**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-iproxyproviderwineventsink).                                                                                                                                                |
| Enable navigating and focusing in a fragment.              | Implement [**IRawElementProviderFragment**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragment) for each element within the fragment. Not necessary for elements that are not part of a fragment.                                                                                                                         |
| Enable focusing and locating child elements in a fragment. | Implement [**IRawElementProviderFragmentRoot**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderfragmentroot). Not necessary for elements that are not fragment roots.                                                                                                                                                          |



 

## Property Values

UI Automation providers for custom controls must support certain properties that can be used by UI Automation and by client applications. For elements that are hosted in windows, UI Automation can retrieve some properties from the default window provider, but must obtain others from the custom provider.

Typically, providers for window-based controls do not need to provide the following properties that are identified by **PROPERTYID**:

-   [**UIA\_BoundingRectanglePropertyId**](uiauto-automation-element-propids.md)
-   [**UIA\_ClickablePointPropertyId**](uiauto-automation-element-propids.md)
-   [**UIA\_ProcessIdPropertyId**](uiauto-automation-element-propids.md)
-   [**UIA\_ClassNamePropertyId**](uiauto-automation-element-propids.md)
-   [**UIA\_HasKeyboardFocusPropertyId**](uiauto-automation-element-propids.md)
-   [**UIA\_IsEnabledPropertyId**](uiauto-automation-element-propids.md)
-   [**UIA\_IsKeyboardFocusablePropertyId**](uiauto-automation-element-propids.md)
-   [**UIA\_IsPasswordPropertyId**](uiauto-automation-element-propids.md)
-   [**UIA\_NamePropertyId**](uiauto-automation-element-propids.md)
-   [**UIA\_RuntimeIdPropertyId**](uiauto-automation-element-propids.md)

The RuntimeId property of a simple element or fragment root hosted in a window is obtained from the window. However, fragment elements below the root, such as list items in a list box, must provide their own identifiers. For more information, see [**IRawElementProviderFragment::GetRuntimeId**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-getruntimeid).

The IsKeyboardFocusable property should be returned for providers hosted in a Windows Forms control. In this case, the default window provider may be unable to retrieve the correct value.

The Name property is usually supplied by the host provider.

## Events from Providers

UI Automation providers should raise events to notify client applications of changes in the state of the UI. The following functions are used to raise events.



| Function                                                                                   | Description                                                                                                              |
|--------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| [**UiaRaiseAutomationEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseautomationevent)                  | Raises various events, including events triggered by control patterns.                                                   |
| [**UiaRaiseAutomationPropertyChangedEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraiseautomationpropertychangedevent) | Raises an event when a UI Automation property has changed.                                                               |
| [**UiaRaiseStructureChangedEvent**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaraisestructurechangedevent)      | Raises an event when the structure of the UI Automation tree has changed, for example, by removing or adding an element. |



 

The purpose of an event is to notify the client of something taking place in the UI. Providers should raise an event regardless of whether the change was triggered by user input or by a client application using UI Automation. For example, the event identified by [**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md) should be raised whenever the control is invoked, either through direct user input or by the client application calling [**IUIAutomationInvokePattern::Invoke**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationinvokepattern-invoke).

To optimize performance, a provider can selectively raise events, or raise no events at all if no client application is registered to receive them. The following API elements are used for optimization.



| API Element                                                                       | Description                                                                                                                                                       |
|-----------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**UiaClientsAreListening**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaclientsarelistening)           | This function ascertains whether any client applications have subscribed to UI Automation events.                                                                 |
| [**IRawElementProviderAdviseEvents**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementprovideradviseevents) | Implementing this interface on a fragment root enables the provider to be advised when clients register and unregister event handlers for events on the fragment. |



 

> [!Note]  
> Similar to implementing reference counting in COM programming, it is important for UI Automation providers to treat the [**IRawElementProviderAdviseEvents::AdviseEventAdded**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovideradviseevents-adviseeventadded) and [**AdviseEventRemoved**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovideradviseevents-adviseeventremoved) methods like the [**IUnknown::AddRef**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-addref) and [**Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) methods of the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. As long as **AdviseEventAdded** has been called more times than **AdviseEventRemoved** for a specific event or property, the provider should continue to raise corresponding events, because some clients are still listening. Alternatively, UI Automation providers can use the [**UiaClientsAreListening**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiaclientsarelistening) function to determine whether at least one client is listening and, if so, raise all appropriate events.

 

## Provider Navigation

Providers for simple controls, such as a custom button hosted in a window, do not need to support navigation in the UI Automation tree. Navigation to and from the element is handled by the default provider for the host window, which is specified in the implementation of [**IRawElementProviderSimple::HostRawElementProvider**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-get_hostrawelementprovider). When you implement a provider for a complex custom control, however, you must support navigation between the root node of the fragment and its descendants, and between sibling nodes.

> [!Note]  
> Elements of a fragment other than the root must return **NULL** from [**HostRawElementProvider**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-get_hostrawelementprovider), because they are not directly hosted in a window, and no default provider can support navigation to and from them.

 

The structure of the fragment is determined by your implementation of [**IRawElementProviderFragment::Navigate**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-navigate). For each possible direction from each fragment, this method returns the provider object for the element in that direction. If there is no element in that direction, the method returns **NULL**.

The fragment root supports navigation only to child elements. For example, a list box returns the first item in the list when the direction is **NavigateDirection\_FirstChild**, and returns the last item when the direction is **NavigateDirection\_LastChild**. The fragment root does not support navigation to a parent or to siblings; this is handled by the host window provider.

Elements of a fragment that are not the root must support navigation to the parent, and to any siblings and children they have.

## Assigning a New Parent

Pop-up windows are actually top-level windows, and by default, appear in the UI Automation tree as children of the desktop. In many cases, however, pop-up windows are logically children of some other control. For example, the drop-down list of a combo box is logically a child of the combo box. Similarly, a menu pop-up window is logically a child of the menu. UI Automation provides support to assign a new parent to a pop-up window so that it appears to be a child of the associated control.

To assign a new parent to a pop-up window:

1.  Create a provider for the pop-up window. This requires that the class of the pop-up window be known in advance.
2.  Implement all properties and control patterns as usual for that pop-up, as though it were a control in its own right.
3.  Implement the [**IRawElementProviderSimple::HostRawElementProvider**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-get_hostrawelementprovider) property so that it returns the value obtained from [**UiaHostProviderFromHwnd**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahostproviderfromhwnd), where the parameter is the window handle of the pop-up window.
4.  Implement [**IRawElementProviderFragment::Navigate**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderfragment-navigate) for the pop-up window and its parent so that navigation is handled properly from the logical parent to the logical children, and between sibling children.

When UI Automation encounters the pop-up window, it recognizes that navigation is being overridden from the default, and skips over the pop-up window when it is encountered as a child of the desktop. Instead, the node is reachable only through the fragment.

Assigning a new parent is not suitable for cases where a control can host a window of any class. For example, a rebar control can host any type of window in its bands. To handle these cases, UI Automation supports an alternative form of window relocation, as described in the next section.

## Provider Repositioning

UI Automation fragments may contain two or more elements that are each contained in a window. Because each window has its own default provider that considers the window to be a child of a containing window, the UI Automation tree by default, will show the windows in the fragment as children of the parent window. In most cases this is desirable behavior, but sometimes it can lead to confusion because it does not match the logical structure of the UI.

A good example of this is a rebar control. A rebar control contains bands, each of which can in turn contain a window-based control, such as a toolbar, an edit box, or a combo box. The default window provider for the rebar window sees the band control windows as children, and the rebar provider sees the bands as children. Because the window provider and the rebar provider are working in tandem and combining their children, both the bands and the window-based controls appear as children of the rebar control. Logically, however, only the bands should appear as children of the rebar control, and each band provider should be coupled with the default window provider for the control it contains.

To accomplish this, the fragment root provider for the rebar control exposes a set of children representing the bands. Each band has a single provider that may expose properties and control patterns. In its implementation of [**IRawElementProviderSimple::HostRawElementProvider**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementprovidersimple-get_hostrawelementprovider), the band provider returns the default window provider for the control window, which it obtains by calling [**UiaHostProviderFromHwnd**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiahostproviderfromhwnd), passing in the control's window handle (**HWND**). Finally, the fragment root provider for the rebar implements the [**IRawElementProviderHwndOverride**](/windows/desktop/api/UIAutomationCore/nn-uiautomationcore-irawelementproviderhwndoverride) interface, and in its implementation of [**IRawElementProviderHwndOverride::GetOverrideProviderForHwnd**](/windows/desktop/api/UIAutomationCore/nf-uiautomationcore-irawelementproviderhwndoverride-getoverrideproviderforhwnd), it returns the appropriate band provider for the control contained in the specified window.

## Disconnecting Providers

Applications typically create controls as they are needed and destroy them afterward. After destroying a control, the UI Automation provider resources associated with the control should be released by calling the [**UiaDisconnectProvider**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiadisconnectprovider).

Similarly, an application should use the [**UiaDisconnectAllProviders**](/windows/desktop/api/UIAutomationCoreApi/nf-uiautomationcoreapi-uiadisconnectallproviders) function to release all UI Automation resources held by all providers in the application before shutting down.

## Related topics

<dl> <dt>

[UI Automation Provider Programmer's Guide](uiauto-providerportal.md)
</dt> </dl>

 

 