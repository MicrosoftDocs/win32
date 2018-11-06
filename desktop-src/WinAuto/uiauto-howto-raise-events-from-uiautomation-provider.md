---
title: How to Raise Events from a UI Automation Provider
description: This topic contains example code that shows how a Microsoft UI Automation provider raises an event.
ms.assetid: 43826258-9321-4d44-bd31-6a3b42f00d39
ms.topic: article
ms.date: 05/31/2018
---

# How to Raise Events from a UI Automation Provider

This topic contains example code that shows how a Microsoft UI Automation provider raises an event.

The following example code shows a method from an application that implements a custom button. The application calls the method whenever the custom button is invoked. The method checks whether any clients are listening for events and, if so, raises the [**UIA\_Invoke\_InvokedEventId**](uiauto-event-ids.md) event to notify the clients that the button was invoked.


```C++
// Responds to a button click. The source of the click could 
// be the mouse, the keyboard, or a client's call to 
// IUIAutomationInvokePattern::Invoke.
void CustomButton::InvokeButton(HWND hwnd)
{
    // TODO: Perform program actions invoked by the control.

    // Check whether any clients are listening for UI Automation 
    // events.
    if (UiaClientsAreListening())
    {
        // Raise an Invoked event. GetUIAutomationProvider is an
        // application-defined method that returns a pointer to
        // the application's IRawElementProviderSimple interface.
        UiaRaiseAutomationEvent(
            GetUIAutomationProvider(hwnd), UIA_Invoke_InvokedEventId); 
    }
}
```



## Related topics

<dl> <dt>

**Conceptual**
</dt> <dt>

[UI Automation Events Overview](uiauto-eventsoverview.md)
</dt> <dt>

[How-To Topics for UI Automation Providers](uiauto-howto-topics-for-uiautomation-providers.md)
</dt> </dl>

 

 




