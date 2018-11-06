---
title: Input-Active Client
description: Input-Active Client
ms.assetid: b46e91d3-eca7-4a4a-b1ce-27b5e6ad92a5
ms.topic: article
ms.date: 05/31/2018
---

# Input-Active Client

\[Microsoft Agent is deprecated as of Windows 7, and may be unavailable in subsequent versions of Windows.\]

Because multiple client applications can share the same character and because multiple clients can use different characters at the same time, the server designates one client as the *input-active* client and sends mouse and voice input only to that client application. This maintains the orderly management of user input, so that an appropriate client responds to the input.

Typically, user interaction determines which client application becomes input-active. For example, if the user clicks a character, that character's client application becomes input-active. Similarly, if a user speaks the name of a character, it becomes input-active. Also, when the server processes a character's [**Show**](show-method.md) method, the client of that character becomes input-active.

When a character is hidden, the client of that character will no longer be input-active for that character. The server automatically makes the active client of any remaining character(s) input-active. When all characters are hidden, no client is input-active. However, in this situation, if the user presses the Listening hotkey, Agent will continue to listen for its commands (using the speech recognition engine matching the topmost character of the last input-active client).

If multiple clients are sharing the same character, the server will designate its *active client* as input-active client. The active character is the topmost in the client order. You can set your client to be the active or not-active client using the [**Activate**](activate-method.md) method. You can also use the **Activate** method to explicitly make your client input-active; but to avoid disrupting other clients of the character, you should do so only when your client application is active. For example, if the user clicks your application's window, activating your application, you can call the **Activate** method to receive and process mouse and speech input directed to the character.

 

 




