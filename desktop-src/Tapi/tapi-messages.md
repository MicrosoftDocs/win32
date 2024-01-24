---
description: Messages are used to notify the application of asynchronous events. All of these messages are sent to the application through the message notification mechanism that the application specified in lineInitializeEx.
ms.assetid: d302819e-c522-470a-be5e-52625c9223a4
title: TAPI Messages
ms.topic: article
ms.date: 05/31/2018
---

# TAPI Messages

Messages are used to notify the application of asynchronous events. All of these messages are sent to the application through the message notification mechanism that the application specified in [**lineInitializeEx**](/windows/desktop/api/Tapi/nf-tapi-lineinitializeexa).

The message always contains a handle to the relevant object (phone, line, or call), which the application can use to determine the message type.

Certain messages are used to notify the application about a change in an object's status. These messages provide the object handle and give an indication of which status item has changed. The application can call the appropriate "get status" function of the object to obtain the object's full status.

When an event occurs, messages can be sent to zero, one, or more applications. The target applications for a message are determined by a number of different factors including the meaning of the message, the application's privilege to the object, whether or not the application initiated the request for which the message is a direct result, and the message masking that has been set by the application. Note the following points about messages:

-   Asynchronous reply messages are only sent to the application that originated the request and cannot be masked.
-   Messages that signal the completion of digit or tone generation or the gathering of digits are only sent to the application that requested the digit or tone generation.
-   Messages that indicate line or address state changes are sent to all applications that have opened the line, so long as the message has been enabled through [**lineSetStatusMessages**](/windows/desktop/api/Tapi/nf-tapi-linesetstatusmessages).
-   Messages that indicate call state and call information changes are sent to all applications that have a handle to the call.
-   Messages that signal a digit detection, tone detection, or media type detection are sent to the applications that requested monitoring of that event.

This section contains the reference information for the following TAPI messages:

-   [Assisted Telephony Messages](assisted-telephony-messages.md)
-   [Call Center Messages](call-center-messages.md)
-   [Formatted Error Messages](formatted-error-messages.md)
-   [Line Device Messages](line-device-messages.md)
-   [Phone Device Messages](phone-device-messages.md)

 

 



