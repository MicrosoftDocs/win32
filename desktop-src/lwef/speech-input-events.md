---
title: Speech Input Events
description: Speech Input Events
ms.assetid: d7b621fe-9274-4b16-af8a-664b0b296c89
ms.topic: article
ms.date: 05/31/2018
---

# Speech Input Events

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

In addition, to the [**Command**](command-event.md) event notification, Agent also notifies the input-active client when the server turns the Listening mode on or off, using the [**ListenStart**](listenstart-event.md) and [**ListenComplete**](listencomplete-event.md) events ([**IAgentNotifySinkEx::ListeningState**](iagentnotifysinkex--listeningstate.md)). However, if the user presses the Listening mode key and there is no matching speech recognition engine available for the topmost character of the input-active client, the server starts the Listening hotkey mode time-out, but does not generate a **ListenStart** event for the active client of the character. If, before the time-out completes, the user activates another character with speech recognition engine support, the server attempts to activate speech input and generates the **ListenStart** event.

Similarly, if a client attempts to turn on the Listening mode using the [**Listen**](listen-method.md) method and there is no matching speech recognition engine available, the call fails and the server does not generate a [**ListenStart**](listenstart-event.md)event. In the Microsoft Agent control, the **Listen** method returns **False**, but the call does not raise an error.

When the Listening key mode is on and the user switches to a character that uses a different speech recognition engine, the server switches to and activates that engine and triggers a [**ListenComplete**](listencomplete-event.md) and then a [**ListenStart**](listenstart-event.md) event. If the activated character does not have an available speech recognition engine (because one is not installed or none match the activated character's language ID setting), the server will trigger the **ListenComplete** event for the previously activated character and passes back a value in the **Cause** parameter. However, the server does not generate **ListenStart** or **ListenComplete** events for the clients that do not have speech recognition support.

If a client successfully calls the [**Listen**](listen-method.md) method and a character without speech recognition engine support becomes input-active before the Listening mode time-out completes, and then the user switches back to the character of the original client, the server will generate a [**ListenStart**](listenstart-event.md) event for that client.

If the input-active client switches speech recognition engines by changing [**SRModeID**](srmodeid-property.md) while in Listening mode, the server switches to and activates that engine without re-triggering the [**ListenStart**](listenstart-event.md) event. However, if the specified engine is not available, the call fails (raises an error in the control) and the server also calls the [**ListenComplete**](listencomplete-event.md) event.

 

 




