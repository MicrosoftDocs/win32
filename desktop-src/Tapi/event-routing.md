---
description: With the lineSetTerminal function, the application can control or suppress the routing of specified low-level events (exchanged between the switch and the station) to a device.
ms.assetid: 36658d83-0ea4-4f62-b2e5-c0f6d6569d0d
title: Event Routing
ms.topic: article
ms.date: 05/31/2018
---

# Event Routing

With the [**lineSetTerminal**](/windows/desktop/api/Tapi/nf-tapi-linesetterminal) function, the application can control or suppress the routing of specified low-level events (exchanged between the switch and the station) to a device. With **lineSetTerminal**, the application specifies the terminal device to which these events (such as line, address, or call media-stream events) are routed.

The routing of the different classes of events can be individually controlled, allowing separate terminals to be specified for each event class. Event classes include lamps, buttons, display, ringer, hookswitch, and media stream.

For example, the media stream of a call (voice, for example) can be sent to any transducer device if the service provider and the hardware is capable of doing so. In general, a *transducer* means the same as what is referred to as a *hookswitch* device in TAPI, something that has a microphone and a speaker. Ring events from the switch to the phone can be mapped into a visual alert on the computer's screen or they can be routed to a phone device. Lamp events and display events can be ignored or routed to a phone device (which appears to behave as a normal phone set). Finally, button presses at a phone device may or may not be passed to the line. In any case, this routing of low-level signals from the line does not affect the operation of the line portion of TAPI, which always maps low-level events to their functional equivalent. To determine the terminals a line device has available (and their capabilities), consult the line device's capabilities with [**lineGetDevCaps**](/windows/desktop/api/Tapi/nf-tapi-linegetdevcaps).

Assume initially that the application has suppressed the routing of all events (with [**lineSetTerminal**](/windows/desktop/api/Tapi/nf-tapi-linesetterminal)), and the user selects a headset as the current I/O device. An incoming call sends a [**LINE\_CALLSTATE**](line-callstate.md) message, and a [**LINE\_LINEDEVSTATE**](line-linedevstate.md) message with the *ringing* indication. Because routing of all events is suppressed, ring events are not routed to the phone, so ringing is suppressed. Instead, the application notifies the user with a pop-up dialog box and a system beep in the headset.

The user decides to answer the call. Because the user's current I/O device is the headset, the telephony application invokes [**lineSetTerminal**](/windows/desktop/api/Tapi/nf-tapi-linesetterminal) on the incoming call to route the call's media to the headset and answer the call. The application may also invoke **lineSetTerminal** to route lamp and display information events to the phone set so that it will behave as usual.

As a second example, assume that an incoming call is alerting at the user's computer. Instead of selecting the answer option with the mouse, the user decides to just pick up the phone's handset to answer the call. The offhook status at the phone sends a message to the application. The application can interpret this status as a request by the user to select the phone handset to conduct the conversation. The application then invokes [**lineSetTerminal**](/windows/desktop/api/Tapi/nf-tapi-linesetterminal) to route the voice data on the call to the phone set.

 

 



