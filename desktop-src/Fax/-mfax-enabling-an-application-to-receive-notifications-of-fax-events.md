---
Description: This topic describes how to enable an application to receive notifications of fax events in the Microsoft Win32 environment.
ms.assetid: f226b757-af51-4161-95d5-1c73bf1ccbef
title: Enabling an Application to Receive Notifications of Fax Events
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Enabling an Application to Receive Notifications of Fax Events

This functionality is currently available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

Call the [**FaxInitializeEventQueue**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxinitializeeventqueue) function to create a fax event queue for a fax client application. The queue enables the application to receive notifications of asynchronous events from the fax server.

An application can specify how the fax server should inform the client application of events. The application can request that the fax server queue I/O completion packets to an I/O completion port, or it can specify that the fax service post notification messages. For more information, see the following topics.

-   [Receiving Notification Messages from the Fax Service](-mfax-receiving-notification-messages-from-the-fax-service.md)
-   [Receiving I/O Completion Packets from the Fax Service](-mfax-receiving-i-o-completion-packets-from-the-fax-service.md)

A fax client application can call the [**FaxInitializeEventQueue**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxinitializeeventqueue) function only once per fax service session. (A fax service session begins when the service sends the FEI\_FAXSVC\_STARTED message, and ends when it sends the FEI\_FAXSVC\_ENDED message.) This prevents the fax service from posting duplicate messages to the client computer. In Windows 2000, if you call **FaxInitializeEventQueue** more than once during the same session, the function fails and it returns an ERROR\_INVALID\_DATA error code. In Windows XP and Windows Server 2003, if you call **FaxInitializeEventQueue** more than once during the same session the function will succeed, and you will receive duplicate event notifications.

A fax client application continues to receive fax events from the fax service after the application closes the handle to a fax server. For more information, see [**FaxClose**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxclose) and [**FaxInitializeEventQueue**](/previous-versions/windows/desktop/api/Winfax/nc-winfax-pfaxinitializeeventqueue).

For a list of the asynchronous events that can occur within the fax server, see [**FAX\_EVENT**](/previous-versions/windows/desktop/api/Winfax/ns-winfax-_fax_eventa).

 

 



