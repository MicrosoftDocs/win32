---
title: MCI Command Strings and Messages
description: MCI Command Strings and Messages
ms.assetid: eb60c96b-e89e-4673-a8e0-98fabe4af7ca
keywords:
- MCI command strings,about
- MCI command messages,about
ms.topic: article
ms.date: 05/31/2018
---

# MCI Command Strings and Messages

MCI supports [Command Strings](command-strings.md) and [Command Messages](command-messages.md). You can use either strings or messages, or both, in your MCI application.

-   The *command-message interface* consists of constants and structures. Use the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function to send messages to an MCI device.
-   The *command-string interface* provides a textual version of the command messages. Use the [**mciSendString**](/previous-versions//dd757161(v=vs.85)) function to send strings to an MCI device. Command strings duplicate the functionality of the command messages. The operating system converts the command strings to command messages before sending them to the MCI driver for processing.

The command messages that retrieve information do so in the form of structures, which are easy to interpret in a C application. These structures can contain information on many different aspects of a device. The command strings that retrieve information do so in the form of strings, and can only retrieve one string at a time. Your application must parse or test each string to interpret it. You might find that the command messages are easier to use than the command strings in some cases, but the command strings are easy to remember and implement. Some MCI applications use command strings when the return value will not be used (other than to verify success) and command messages when retrieving information from the device.

When commands are discussed, this overview uses the string form of the command followed by the message form in parentheses.

 

 