---
Description: 'The fax server sends a WM\_FAX\_MESSAGE message to a window to notify a fax client application when asynchronous events occur within the fax server.'
ms.assetid: 'c70dc3e8-2525-44b8-a7e3-0be1af40a8c9'
title: 'WM\_FAX\_MESSAGE message'
---

# WM\_FAX\_MESSAGE message

The fax server sends a **WM\_FAX\_MESSAGE** message to a window to notify a fax client application when asynchronous events occur within the fax server. The application will receive messages only if it calls the [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md) function and registers to receive events as notification messages.

The message definition provided here is for explanation only; it is not present in any standard header file.

## Parameters

<dl> <dt>

*EventId* 
</dt> <dd>

Specifies the event identifier of the message.

To determine if an event is a fax event, subtract the value of the application's base event from the value of this parameter. If the result is between zero and **FEI\_NEVENTS**, the window can process the event as a fax event. For more information, see the following Remarks section.

</dd> <dt>

*wParam* 
</dt> <dd>

Value of *wParam*. Specifies the device identifier to associate with fax events that are related to devices.

</dd> <dt>

*lParam* 
</dt> <dd>

Value of *lParam*. Specifies the job identifier to associate with fax events that are related to fax jobs.

</dd> </dl>

## Return value

An application returns zero if it processes this message.

## Remarks

The fax server sends notification messages to the window specified by the *hWnd* parameter to the [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md) function.

A window can process a message as a fax message if the message falls between the range of the client application's base window message and the base window message + **FEI\_NEVENTS**. An application specifies the base window message using the *MessageStart* parameter of the [**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md) function. A **WM\_FAX\_MESSAGE** is an event that falls within the range of *MessageStart* to *MessageStart* + **FEI\_NEVENTS**.

For a list of the asynchronous events that can occur within the fax server, see [**FAX\_EVENT**](-mfax-fax-event-str.md). For more information, see [Enabling an Application to Receive Notifications of Fax Events](-mfax-enabling-an-application-to-receive-notifications-of-fax-events.md).

## Requirements



|                                     |                                                            |
|-------------------------------------|------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/> |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>       |



## See also

<dl> <dt>

[Fax Service Client API for Windows 2000](-mfax-fax-service-client-api-for-windows-2000.md)
</dt> <dt>

[**FaxInitializeEventQueue**](-mfax-faxinitializeeventqueue.md)
</dt> <dt>

[**FAX\_EVENT**](-mfax-fax-event-str.md)
</dt> </dl>

 

 




