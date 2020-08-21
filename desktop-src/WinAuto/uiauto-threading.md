---
title: Understanding Threading Issues
description: This topic describes common threading scenarios for Microsoft UI Automation client implementations and explains how to avoid problems that can occur if a client uses threading incorrectly.
ms.assetid: 0772969a-da55-488e-8b21-7368434df8a9
keywords:
- clients,UI Automation threading issues
- clients,threading issues
- clients,event handler threading model
- clients,UI Automation event handler threading model
- clients,UI Automation affinity
- clients,affinity
- UI Automation,threading issues
- UI Automation,event handler threading model
- UI Automation,affinity
- threading issues
- event handler threading model
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Threading Issues

This topic describes common threading scenarios for Microsoft UI Automation client implementations and explains how to avoid problems that can occur if a client uses threading incorrectly.

This topic contains the following sections:

-   [UI Automation and the UI Thread](#ui-automation-and-the-ui-thread)
-   [Threading Model for Event Handlers](#threading-model-for-event-handlers)
-   [COM Apartment Affinity on 64-bit Windows](#com-apartment-affinity-on-64-bit-windows)
-   [Related topics](#related-topics)

## UI Automation and the UI Thread

Because of the way UI Automation uses Windows messages, conflicts can occur when a client application attempts to interact with its own UI on the UI thread. These conflicts can lead to very slow performance, or even cause the application to stop responding.

If your client application is intended to interact with all elements on the desktop, including its own UI, you should make all UI Automation calls from a separate thread. This includes locating elements, for example, by using [**IUIAutomationTreeWalker**](/windows/desktop/api/UIAutomationClient/nn-uiautomationclient-iuiautomationtreewalker) or the [**IUIAutomationElement::FindAll**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomationelement-findall) method and using control patterns. This thread should not own any windows, and should be a Component Object Model (COM) Multithreaded Apartment (MTA) model thread (one that initializes COM by calling [CoInitializeEx](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) with the **COINIT\_MULTITHREADED** flag.)

It is safe to make UI Automation calls in a UI Automation event handler, because the event handler is always called on a non-UI thread. However, when subscribing to events that may originate from your client application UI, you must make the call to [**IUIAutomation::AddAutomationEventHandler**](/windows/desktop/api/UIAutomationClient/nf-uiautomationclient-iuiautomation-addautomationeventhandler), or a related method, on a non-UI thread (which should also be an MTA thread). Remove event handlers on the same thread.

A UI Automation client should not use multiple threads to add or remove event handlers. Unexpected behavior can result if one event handler is being added or removed while another is being added or removed in the same client process.

## Threading Model for Event Handlers

A UI Automation client should use the COM MTA threading model for threads that implement event handlers. Using the Single-threaded Apartment (STA) model can cause problems such as preventing clients from removing event handlers from the thread.

## COM Apartment Affinity on 64-bit Windows

According to the COM specification, the lifetime of a remote object is governed by the lifetime of the apartment where the [CoCreateInstance](/windows/win32/api/combaseapi/nf-combaseapi-cocreateinstance) function is called to create the object. When the original apartment shuts down, the remote object is also released.

For UI Automation clients, this COM behavior can mean that the lifetime of the remote 32/64 helper (created by UIAutomationCore.dll) used by a 32-bit element is governed by the apartment lifetime of the thread that created the element. If the UI Automation client marshals the element to another thread, the element can become invalidated when the originating apartment shuts down. The UI Automation client should handle these issues gracefully by catching errors while using marshaled automation elements.

The same issue can occur with a 32-bit UI Automation client that has 64-bit elements.

## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[Obtaining UI Automation Elements](uiauto-obtainingelements.md)
</dt> <dt>

[Subscribing to UI Automation Events](uiauto-eventsforclients.md)
</dt> <dt>

[UI Automation Events Overview](uiauto-eventsoverview.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[INFO: Descriptions and Workings of OLE Threading Models](https://support.microsoft.com/kb/150777)
</dt> </dl>

 

 