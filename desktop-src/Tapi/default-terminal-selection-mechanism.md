---
description: The concept of multitrack terminal makes it even more desirable for TAPI to provide a simplified method of selecting a terminal on a stream or streams. The Default Terminal Selection mechanism is designed to address this.
ms.assetid: fbdc7359-b44e-4605-baea-eef5155340c7
title: Default Terminal Selection Mechanism
ms.topic: article
ms.date: 05/31/2018
---

# Default Terminal Selection Mechanism

The concept of [multitrack terminal](multitrack-terminals.md) makes it even more desirable for TAPI to provide a simplified method of selecting a terminal on a stream or streams. The Default Terminal Selection mechanism is designed to address this.

## Selecting a Terminal on a Call

The Default Terminal Selection feature is provided via the ability to select a terminal on a call.

The [call object](call-object.md) exposes a new interface, [**ITBasicCallControl2**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasiccallcontrol2). The interface exposes the same methods as [**ITBasicCallControl**](/windows/desktop/api/tapi3if/nn-tapi3if-itbasiccallcontrol), plus three new methods: [**RequestTerminal**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol2-requestterminal), [**SelectTerminalOnCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol2-selectterminaloncall), and [**UnselectTerminalOnCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol2-unselectterminaloncall).

**ITBasicCallControl2::RequestTerminal** creates a terminal, given the terminal class, direction, and media type. It looks through the lists of supported static and dynamic terminals to find and create the requested terminal.

[**ITBasicCallControl2::SelectTerminalOnCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol2-selectterminaloncall) selects the terminal (or, in the case of a multitrack terminal, enumerates, creates if needed, and selects the track terminals) on the stream (or streams) available on the call.

The algorithm for matching call streams to the terminal (or tracks available on the terminal) is described in the documentation for [**ITBasicCallControl2::SelectTerminalOnCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol2-selectterminaloncall).

Calling [**ITBasicCallControl2::UnselectTerminalOnCall**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol2-unselectterminaloncall) causes the terminal (single-track or multitrack) to be unselected from the call. See the method's documentation for more details.

## Selecting a Terminal on ITStream

Selecting a single-track terminal on [**ITStream**](/windows/win32/api/tapi3if/nn-tapi3if-itstream) (by calling [**ITStream::SelectTerminal**](/windows/win32/api/tapi3if/nf-tapi3if-itstream-selectterminal)) selects the terminal on the stream. This is the usual TAPI 3 terminal selection procedure.

Only single-tracks terminals can be selected on a stream. Selecting a multitrack terminal on a stream will fail, because the stream will not recognize the media type and direction.

 

 
