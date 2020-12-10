---
title: Control Events (COM)
description: In addition to providing properties and methods, a control also provides outgoing interfaces to notify its client of events.
ms.assetid: e7085bc0-c087-4cc8-9c69-ba05b0923b74
ms.topic: article
ms.date: 05/31/2018
---

# Control Events (COM)

In addition to providing properties and methods, a control also provides outgoing interfaces to notify its client of events. The client must support handling of these events. See [Events in COM and Connectable Objects](events-in-com-and-connectable-objects.md) for more information on how connectable objects work.

A control can support different outgoing interfaces for different purposes. All outgoing interfaces are marked as source interfaces in the control's type information, but only one is marked default to indicate that it is the primary outgoing interface.

A container can support one or more of the outgoing interfaces defined by a control. The control should be prepared to deal with containers that only provide support for some of their outgoing interfaces.

Controls support four kinds of events:

-   Request events. A control requests permission from its client to do something by calling a method in the outgoing interface, thus triggering a request event. The client signals the control through a boolean, out-parameter in the method that the control called. The client can thus prevent the control from performing the action.
-   Before events. A control notifies its client hat it is going to do something by calling a method in the outgoing interface, thus triggering a before event. The client does not have the opportunity to prevent the action, but it can take any necessary steps given the action that is about to occur.
-   After events. A control notifies its client that it has just done something by calling a method in the outgoing interface, thus triggering an after event. Again, the client cannot cancel this action, but it can take necessary steps given the action that has occurred.
-   Do events. A control triggers a do event to allow its client to override the control's action and provide some alternative or supplementary actions. Usually, the method that a control calls for a do event has a number of parameters for negotiating with the client about the actions that will occur.

The following dispids are defined for standard events that controls can support: Click, DblClick, KeyDown, KeyPress, KeyUp, MouseMove, MouseUp, and Error. All of these standard events have negative DISPID values, indicating their standard status.

The [**IOleControl::FreezeEvents**](/windows/desktop/api/OCIdl/nf-ocidl-iolecontrol-freezeevents) method, when called with **TRUE**, tells a control whether the container will bother handling events from the control until **FreezeEvents** is again called with **FALSE**. During this time control cannot depend on the container actually handling any events. If an event must be handled, the control should queue the event in order to fire it when **FreezeEvents** is called with **FALSE**.

## Related topics

<dl> <dt>

[ActiveX Controls](activex-controls.md)
</dt> </dl>

 

 




