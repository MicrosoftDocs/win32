---
description: This section contains a list of the messages in the Telephony Service Provider Interface (TSPI).
ms.assetid: 3d8bf980-81d6-49db-954f-af72458365dc
title: TSPI Messages
ms.topic: article
ms.date: 05/31/2018
---

# TSPI Messages

This section contains a list of the messages in the Telephony Service Provider Interface (TSPI). These messages are used to notify TAPI of the occurrence of asynchronous events that spontaneously occur within the service provider. The service provider passes these events to TAPI by calling a [**LINEEVENT**](/windows/win32/api/tspi/nc-tspi-lineevent) or [**PHONEEVENT**](/windows/desktop/api/tspi/nc-tspi-phoneevent) callback function, depending on whether the service provider is reporting an event on a line, call, or phone device. The **LINEEVENT** procedure for reporting events occurring on a line or call is supplied to the service provider at the time the line is opened with the [**TSPI\_lineOpen**](/windows/win32/api/tspi/nf-tspi-tspi_lineopen) function. The **PHONEEVENT** procedure for reporting events occurring on a phone is supplied with the [**TSPI\_phoneOpen**](/windows/win32/api/tspi/nf-tspi-tspi_phoneopen) function.

These spontaneous events are unsolicited by TAPI in the sense that they are not a direct response to any request. These events contrast with those reporting completion of requests made by TAPI. Such completion events are reported through the [**ASYNC\_COMPLETION**](/windows/win32/api/tspi/nc-tspi-async_completion) callback function.

The parameter profiles for the spontaneous event procedures include parameters that identify the relevant object for which the event is being reported (phone, line, or call). The identification is in the form of an opaque handle whose exact interpretation is not published by TSPI. TAPI internally determines the relationship between these opaque handles and whatever data structures it used to represent the devices.

The parameter profile for spontaneous event procedures also includes a message parameter identifying the type of the message. Each message type has a corresponding definition that determines the handles that are included, along with other parameters and their meanings. There is a very strong correspondence between the messages appearing at the TSPI level and those that appear at the TAPI level. These are the general rules of correspondence:

-   The set of messages is nearly identical. Where messages correspond, the same message name and value is used at the TSPI level.
-   Handles appearing at the TSPI level are the opaque types defined by the TSPI specification. These types (and their interpretation) differ from those at the TAPI level, although they refer to the same class of device. For example, where a TAPI message includes an HLINE handle, the corresponding TSPI message would typically include an [**HTAPILINE**](htapiline.md) handle.
-   There is no *dwCallbackInstance* data passed to the callback.
-   The *dwParam1*, *dwParam2*, and *dwParam3* parameters are usually identical to the corresponding parameters for the TAPI message.
-   Line-oriented and call-oriented messages are passed to a different callback procedure than phone-oriented messages.

For each message, this section lists the following items:

-   The purpose of the message
-   The callback procedure to which this message is passed
-   A description of the message parameters
-   Optional comments about using the message
-   Optional references to other functions, messages, and data structures
-   Optional comments comparing this message to the TAPI interface

Certain messages are used to notify TAPI about a change in an object's status. These messages provide the TAPI opaque object handle and an indication of which status item has changed. TAPI can subsequently call an appropriate "get status" function of the object to obtain the object's full status.

When an event occurs, a message may or may not be sent to TAPI. For some event types, such as status changes, TAPI specifies a set of status changes in which it is interested. The service provider is advised to limit the status-change message events it reports to those included in this set. The service provider is not required to adhere to this limit. In other words, it may report more changes than are strictly necessary. However, it should try to observe the limit for performance reasons.

The LINE\_REPLY message is not used at the TSPI level. Completion of an asynchronous request is reported using the [**ASYNC\_COMPLETION**](/windows/win32/api/tspi/nc-tspi-async_completion) callback.

The PHONE\_REPLY message is not used at the TSPI level. Completion of an asynchronous request is reported using the [**ASYNC\_COMPLETION**](/windows/win32/api/tspi/nc-tspi-async_completion) callback.

For more information see the following topics:

-   [TSPI Line Device Messages](tspi-line-device-messages.md)
-   [TSPI Phone Device Messages](tspi-phone-device-messages.md)

 

 
