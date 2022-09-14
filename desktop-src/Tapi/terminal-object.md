---
description: In TAPI version 3.0 and later, the TAPI object model uses terminal objects to represent the source or sink of a media stream associated with a call or communications session.
ms.assetid: 0d96f229-76c0-46a3-bc4b-6f558b9956c6
title: Terminal Object
ms.topic: article
ms.date: 05/31/2018
---

# Terminal Object

In TAPI version 3.0 and later, the TAPI object model uses terminal objects to represent the source or sink of a media stream associated with a call or communications session. This object model enables an application to specify, at a detailed level, how media are processed on a call. This model also enables multiple terminals to be selected simultaneously, so for example, a call can be output to an audio speaker and recorded simultaneously.

The Terminal object represents a source or renderer, such as a microphone or a speaker. An application chooses among available terminals based on the media direction and type or types involved in a communications session. Each associated media stream is then selected onto the appropriate terminal in order to start streaming.

Terminals are normally implemented by a media service provider (MSP) and terminal objects will not be available if there is no MSP associated with a communications session. One exception is that with Windows 2000 SP1 and later, an application can implement a form of [pluggable terminal](pluggable-terminals.md). This enables a conference server to create bridging terminals so that non-Windows 2000 SP1 or non-multicast H323 clients can be added to TAPI 3 multi-party SDP/IP multicast conferences.

Each terminal belongs to a [terminal class](terminal-class.md). A terminal class represents a set of source or render features. For example, a terminal that maps to a set of audio speakers would be identified as CLSID\_SpeakersTerminal, and the service provider would be expected to implement volume control. TAPI 3 defines a set of terminal classes, an MSP can define additional classes, and an application can register new terminal classes. Each terminal class is assigned a globally unique identifier (GUID).

From the point of view of an application, a terminal is described by its [terminal type](/windows/desktop/api/Tapi3if/ne-tapi3if-terminal_type) and [direction](/windows/desktop/api/Tapi3if/ne-tapi3if-terminal_direction). The type may be either static or dynamic. A static terminal maps to hardware, such as a telephone or microphone. A dynamic terminal maps to a transient object, such as a file or a video window. Direction describes whether a given terminal is a source or a renderer.

The capabilities of a given terminal object can vary considerably depending on the current service provider pair in use. The MSP for a specialized device might implement an interface with methods appropriate to that device. That interface could be aggregated onto the terminal object and the methods made available to an application. For more information and reference material, see the media service provider documentation.

For more information about terminal interfaces and methods implemented by TAPI 3, see [Terminal Object Interfaces](terminal-object-interfaces.md).

If the authors of a media service provider use the MSP Base Classes, they may implement some of the Media Streaming Terminal features.

For more information and code examples that show illustrations of using a Terminal object, see [Make a Call](make-a-call.md) and [Receive a Call](receive-a-call.md).

**Windows XP:** For more information about how the Terminal object has been expanded in Windows XP, see [File terminals](file-terminals.md), [Multitrack terminals](multitrack-terminals.md), and [Pluggable terminals](pluggable-terminals.md).

For more information and code examples, see [Using File Terminals](using-file-terminals.md), [Using Multitrack Terminals and the Default Selection Mechanism](using-multitrack-terminals-and-the-default-selection-mechanism.md), and [Pluggable Terminal Registration](pluggable-terminal-registration.md).

 

 



