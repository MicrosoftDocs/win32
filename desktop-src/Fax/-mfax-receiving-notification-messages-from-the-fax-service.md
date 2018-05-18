---
Description: 'This topic describes how to receive notification messages from the fax service in the Microsoft Win32 environment.'
ms.assetid: 'd2562506-bc02-4b78-bc5d-68b9a4570ae5'
title: Receiving Notification Messages from the Fax Service
---

# Receiving Notification Messages from the Fax Service

This functionality is currently available only in the Microsoft Win32 environment. It is not available in the Component Object Model (COM) implementation environment.

When a client application calls the [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md) function, it can specify notification using notification messages instead of I/O completion packets. The application does this by specifying a valid window handle in the *hWnd* parameter, and a value in the *MessageStart* parameter.

The fax service calls the [PostMessage](http://msdn.microsoft.com/library/en-us/winui/winui/windowsuserinterface/windowing/messagesandmessagequeues/messagesandmessagequeuesreference/messagesandmessagequeuesfunctions/postmessage.asp) function to post the notification message to the destination window specified by the client application in the *hWnd* parameter. The client application's window procedure receives the message. For information about the structure of a fax notification message, see WM\_FAX\_MESSAGE.

In addition, you must consider the following to ensure that client applications receive notification messages.

## Running the Fax Service Under the LocalSystem Account

The fax service and the local logged-on user running a fax client application run on different desktops. Because notification messages do not cross desktops, the Services application in Control Panel must have the **Allow Service To Interact With Desktop** option selected for the fax service in the local computer's [LocalSystem](http://msdn.microsoft.com/library/en-us/dllproc/base/localsystem_account.asp) account. This enables the fax service to access the client's desktop and post messages to the client.

## Running the Fax Service Under a User Account

A user can configure the fax service to run under a user account instead of the [LocalSystem](http://msdn.microsoft.com/library/en-us/dllproc/base/localsystem_account.asp) account. In this situation, the **Allow Service To Interact With Desktop** option will not be selected for the fax service. To enable the reception of notification messages, the fax service opens an impersonation access token for the fax client application. The service opens the token when the client calls the [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md) function, specifying notification messages. When the fax service has a message for the client, the service impersonates the client and posts the message to the client. You do not need to incorporate any code in the client application to enable the preceding functionality.

However, the application must incorporate code to enable the client to log off successfully when the fax service runs under a user account. This is because a user cannot log off if the fax service has an open handle to the client's desktop. When the client application receives the WM\_ENDSESSION message or the WM\_DESTROY message, it must call the [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md) function again, specifying the same window handle it initially specified in the *hWnd* parameter. However, it must specify a value of 1 in the *CompletionKey* parameter. This informs the fax service that the client is logging off and the service should close the impersonation access token it opened for the client. This enables the client to log off. Note that the fax service does not need to run under the [LocalSystem](http://msdn.microsoft.com/library/en-us/dllproc/base/localsystem_account.asp) account to enable this feature.

To optimize performance, the client application can determine if the fax service is running when the user attempts to log off. If the client has received the FEI\_FAXSVC\_ENDED message, the fax service is no longer running. The client does not need to call the [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md) function because the service has closed the impersonation access token it opened for the client.

 

 



