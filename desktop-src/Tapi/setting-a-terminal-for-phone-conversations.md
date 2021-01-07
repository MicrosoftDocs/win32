---
description: The users computer may have access to multiple devices that are selectable by the user and used to conduct interactive voice conversations.
ms.assetid: cc7ad70a-157e-4db4-b5e4-00d25686a9dd
title: Setting a Terminal for Phone Conversations
ms.topic: article
ms.date: 05/31/2018
---

# Setting a Terminal for Phone Conversations

The user's computer may have access to multiple devices that are selectable by the user and used to conduct interactive voice conversations. First, there is the phone device itself, complete with lamps, buttons, display, ringer, and voice I/O device (handset, speakerphone, headset). The user's computer may also have a separate voice I/O device (such as a headset or a microphone/speaker combination attached to a sound card) for use with phone conversations.

TSPI enables the user to select where to route the information that the switch sends over the line, address, or call. The switch normally expects this to be one of its phone sets, and sends ring requests, lamp events (for stimulus phones), display data, and voice data as appropriate. The phone in turn sends hookswitch events, button press events (for stimulus phones), and voice data back to the switch.

The *line* portion of TSPI makes lamp events, display events, and ring events available, either as functional return codes to the various line operations in TSPI, or as unsolicited functional call status messages that are sent to the application callback. The service provider implementation is responsible for mapping between the functional TSPI level and the underlying stimulus or functional messages used by the telephony network. In functional telephony environments, TSPI functions are mapped to the functional protocol.

Using the [**TSPI\_lineSetTerminal**](/windows/win32/api/tspi/nf-tspi-tspi_linesetterminal) function, TAPI can control the routing of different low-level events exchanged between the switch and the station; it can also decide not to route some of these low-level events to a device. The routing of the different classes of events can be individually controlled. For example, the media stream of a call (such as voice) can be sent to any transducer device if the service provider and hardware are capable of doing so. Ring events from the switch to the phone can be mapped into a visual alert on the computer's screen or they can be routed to a phone device. Lamp events and display events can be ignored or routed to a phone device (which appears to behave as a normal phone set). Finally, button presses at a phone device may or may not be passed on to the line. In any case, this routing of low-level signals from the line does not affect the operation of TSPI's line portion, which always maps the low-level events to their functional equivalent. Applications can consult a line's device capabilities to determine the terminals it has available.

In other words, the [**TSPI\_lineSetTerminal**](/windows/win32/api/tspi/nf-tspi-tspi_linesetterminal) function specifies the terminal device to which the specified line, address events or call media stream events are routed. Separate terminals can be specified for each event class. Event classes include lamps, buttons, display, ringer, hookswitch, and media stream.

 

 
