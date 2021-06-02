---
description: Events are a crucial part of call handling under TAPI 3. Event handling includes four stages.
ms.assetid: 'db43f4e0-f2f5-49b1-a03d-3df3de0e5611'
title: Events (Telephony API)
ms.topic: article
ms.date: 05/31/2018
---

# Events (Telephony API)

Events are a crucial part of call handling under TAPI 3. Event handling includes four stages.

**To register for and enable the reception of events**

1.  Implement the [**ITTAPIEventNotification::Event**](/windows/desktop/api/Tapi3if/nf-tapi3if-ittapieventnotification-event) method. (TAPI calls this method when an event occurs.) Typically, this implementation does no more than **AddRef** the **IDispatch** interface pointer, then post to the application's message pump.
2.  Register the [**ITTAPIEventNotification**](/windows/desktop/api/Tapi3if/nn-tapi3if-ittapieventnotification) outgoing interface using the COM standard [**IConnectionPointContainer**](/windows/win32/api/ocidl/nn-ocidl-iconnectionpointcontainer) and [**IConnectionPoint**](/windows/win32/api/ocidl/nn-ocidl-iconnectionpoint) interfaces, and pass the [**IConnectionPoint::Advise**](/windows/win32/api/ocidl/nf-ocidl-iconnectionpoint-advise) method a pointer to [**ITTAPIEventNotification::Event**](/windows/desktop/api/Tapi3if/nf-tapi3if-ittapieventnotification-event).
3.  Call the [**ITTAPI::put\_EventFilter**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-put_eventfilter) method to tell TAPI which events the application will handle. The event filter consists of **OR**ed members of the [**TAPI\_EVENT**](/windows/desktop/api/Tapi3if/ne-tapi3if-tapi_event) enumeration.
    > [!Note]  
    > You must call the **ITTAPI::put\_EventFilter** method to set the event filter mask and enable reception of events. If you do not call **ITTAPI::put\_EventFilter**, your application will not receive any events.

     

You must also call the [**ITTAPI::RegisterCallNotifications**](/windows/desktop/api/tapi3if/nf-tapi3if-ittapi-registercallnotifications) method for each address object on which the application will handle calls.

See [Event Interfaces](./event-interfaces.md) for a list of all event interfaces. See [Register Events](register-events.md) for code examples that illustrate the registration process and [Receive a Call](receive-a-call.md) for a code example that shows one use of events.

 

 
