---
description: When an application has owner privilege for a communications session, the application may choose to hand off ownership to another application.
ms.assetid: d6d188c9-9cbd-45af-93f0-b78850374919
title: Handoffs
ms.topic: article
ms.date: 05/31/2018
---

# Handoffs

When an application has owner [privilege](privilege-ovr.md) for a communications session, the application may choose to hand off ownership to another application. The handoff operation is normally used to allow the call's media type to be changed. The highest-priority application for the new media type should take and handle the call. Media type changing usually occurs for one of the following reasons.

**User command:** Through a user interface or through window messages, the application learns that the local user wants to change media type. For example, the user has told the new target application (which is not yet an owner) to obtain an existing voice call for transmitting data. The target application must now take control of the call. In this case, the current owner notices the number of owners increase, and then relinquishes its control of the call. Alternatively, the user could instruct the current owner of the call to hand it off to an application that can handle the new media type.

**Media type change:** The service provider can detect a media type change. For example, the local application is playing a recorded voice message to the caller. During this message, the caller spontaneously decides to transmit a fax calling tone, and the local application can respond accordingly by changing the media type to fax and, if necessary, handing the call off to a fax application. Another way this can work is for a monitoring application to enable media type monitoring, and, when the media type in which it is interested is detected on a call, it can request ownership of the call. This mechanism makes it unnecessary for every application to monitor every call for every media type.

**Remote party command:** The remote party can interactively indicate a change in media types during an existing call, such as if the local application is monitoring DTMF input by the remote caller. Through this monitoring, the caller indicates, for example, that a fax is about to be sent. Other ways the caller can control local applications are with commands received on other data connections and through ISDN user-user information messages.

A call handoff will have one of these outcomes:

-   The call is given to another application (SUCCESS).
-   The handing-off application is itself the target (TARGETSELF).
-   The handoff fails (TARGETNOTFOUND).

If the application that is receiving the handed-off call already has a call handle to the call, this old call handle is used. Otherwise, a new call handle is created. In either case, the application ends up with owner privileges to the call. Whenever the handing-off application is not the same as the target application, the target is informed about the handoff in a session state message as if it were receiving a new call.

If the current owner application is told to change media types, it does so by handing off the call to an application used for the target media type. The two types of call handoffs are described in [Directed Handoffs](#directed-handoffs) and [Media type Handoffs](#media-type-handoffs).

Not all service providers support use of this operation.

**TAPI 2.x:** See [**lineHandoff**](/windows/win32/api/tapi/nf-tapi-linehandoff), with *lpszFileName* set to the application name for a direct handoff or *dwMediaMode* set to one media type for an indirect handoff.

**TAPI 3.x:** See [**ITBasicCallControl::HandoffDirect**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-handoffdirect), [**ITBasicCallControl::HandoffIndirect**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-handoffindirect).

## Directed Handoffs

A *directed handoff* takes place when the target application is known by name to the original application. This situation would occur, for example, among a set of applications written by the same vendor. The user can usually configure control of directed handoffs. With such a handoff, the call is given to the specified application if it has opened the line on which the call exists. The media type specified at the time the application opened the line is ignored. One common example is a voice call followed by a fax transmission in the same call. Directed handoff would most often be used by applications from the same developer that are linked in other ways as well.

Directed handoff may also be used in future versions as part of the process of arbitrating multiple applications waiting for incoming calls of the same media type, with the selection of the application to handle the call being based on data-link or higher-level protocol detection rather than media type. An example of its use would be an incoming data modem line with applications such as remote takeover, bulletin board, remote network access, and remote e-mail access all waiting for calls simultaneously.

## Media Type Handoffs

A *media type handoff* takes place when there is a new, targeted media type, usually when the owning application determines that the media type needed for the call is not present or is about to change.

The process for a media-dependent handoff can be a probing process if the media type UNKNOWN bit is on. It is the responsibility of the owning application to cycle through media types to find the highest-priority application. TAPI does this cycling only on the initial incoming call to find the first owner. It does not do this for a handoff operation. Otherwise, a handoff is virtually the same as for the initial assignment of a call to an application. The difference is the fact that only one media type can be set for an indirect (media type) handoff.

Because only a single media type bit can be specified, the call is given to the highest priority application for that media type. However, it is possible that more than one media type is to be considered for the handoff. In this case, the handing-off application should specify the highest priority of the possible media types as a parameter.

If an application specifies the UNKNOWN bit when performing a media-type handoff and the handoff fails, this means that an unknown application capable of performing media type determination is not currently running. The application that is handing off should then try to hand the call off to the highest-priority application registered for the next-higher media type.

The receiving application is now responsible for the call. It now probes for the call's actual media type. If the application can handle the call's media type, it must ensure that it is the highest-priority application registered for that media type. If so, it keeps the call and processes it normally. If not, it hands the call off to another application registered for that media type.

If, however, the probe for that media type fails, the application probes again, attempting the remaining media-mode possibilities. It must first turn off the current media type bit, then try another handoff with a different type.

This process of probing and handing off continues, and the remaining media types are eliminated one by one. Along the way, one of the applications may see that the media type it handles is on the call, and the handoff is successful.

The application should then set the correct media type and clear all other media-type bits. This informs other interested applications of the correct media type. These other applications receive an event notification message stating that the call's media type has changed.

 

 
