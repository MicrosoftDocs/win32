---
Description: Events are a crucial part of call handling under TAPI 3. Event handling includes four stages.
ms.assetid: eaf4b014-1cab-4707-b750-9088e745083e
title: Events
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Events

Events are a crucial part of call handling under TAPI 3. Event handling includes four stages.

**To register for and enable the reception of events**

1.  Implement the [**ITTAPIEventNotification::Event**](/windows/desktop/api/Tapi3if/nf-tapi3if-ittapieventnotification-event) method. (TAPI calls this method when an event occurs.) Typically, this implementation does no more than **AddRef** the **IDispatch** interface pointer, then post to the application's message pump.
2.  Register the [**ITTAPIEventNotification**](/windows/desktop/api/Tapi3if/nn-tapi3if-ittapieventnotification) outgoing interface using the COM standard [**IConnectionPointContainer**](https://msdn.microsoft.com/en-us/library/ms683857(v=VS.85).aspx) and [**IConnectionPoint**](https://msdn.microsoft.com/en-us/library/ms694318(v=VS.85).aspx) interfaces, and pass the [**IConnectionPoint::Advise**](https://msdn.microsoft.com/en-us/library/ms678815(v=VS.85).aspx) method a pointer to [**ITTAPIEventNotification::Event**](/windows/desktop/api/Tapi3if/nf-tapi3if-ittapieventnotification-event).
3.  Call the [**ITTAPI::put\_EventFilter**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-put_eventfilter) method to tell TAPI which events the application will handle. The event filter consists of **OR**ed members of the [**TAPI\_EVENT**](/windows/desktop/api/Tapi3if/ne-tapi3if-tapi_event) enumeration.
    > [!Note]  
    > You must call the **ITTAPI::put\_EventFilter** method to set the event filter mask and enable reception of events. If you do not call **ITTAPI::put\_EventFilter**, your application will not receive any events.

     

You must also call the [**ITTAPI::RegisterCallNotifications**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-registercallnotifications) method for each address object on which the application will handle calls.

See [Event Interfaces](https://msdn.microsoft.com/en-us/library/ms734880(v=VS.85).aspx) for a list of all event interfaces. See [Register Events](register-events.md) for code examples that illustrate the registration process and [Receive a Call](receive-a-call.md) for a code example that shows one use of events.

 

 



