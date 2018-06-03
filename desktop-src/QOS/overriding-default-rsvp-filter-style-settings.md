---
title: Overriding Default RSVP Filter Style Settings
description: Default RSVP filter style settings can be overridden through the use of the RSVP\_RESERVE\_INFO object by specifying one of the following values in the Style member of the RSVP\_RESERVE\_INFO object, along with required flowdescriptors.
ms.assetid: b429b268-adb6-4457-a458-ed3ed4b6c46d
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Overriding Default RSVP Filter Style Settings

Default RSVP filter style settings can be overridden through the use of the [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) object by specifying one of the following values in the **Style** member of the **RSVP\_RESERVE\_INFO** object, along with required **flowdescriptors**.

**Note**  RSVP signaling is not supported on Windows XP, Windows Server 2003, or later versions of Windows.

## The RSVP\_FIXED\_FILTER\_STYLE Object

The RSVP\_FIXED\_FILTER\_STYLE object may be specified in the **Style** member of the [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) object to override default settings of the Wildcard Filter (WF) RSVP filter style setting for multicast or unconnected UDP unicast receivers. This capability is useful when a multicast session has multiple senders; rather than accepting the default WF reservation that provides a shared reservation among all senders, you can use RSVP\_FIXED\_FILTER\_STYLE to set up individual reservations for each sender. Another similar situation is when the receiver is using unconnected UDP to receive from multiple senders, in which an RSVP\_FIXED\_FILTER\_STYLE object can again be used to set up individual reservations for each sender.

Note that flowdescriptors must be specified when using the RSVP\_FIXED\_FILTER\_STYLE object, and the **NumFlowDesc** member of [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) is set to the number of senders, and **FlowDescList** of **RSVP\_RESERVE\_INFO** is set to each sender's address/port. This is only appropriate when multiple senders are involved.

## The RSVP\_WILDCARD\_STYLE Object

The RSVP\_WILDCARD\_STYLE object may be specified in the **Style** member of the [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) object to override default settings of the Fixed Filter (FF) RSVP filter style setting for unicast receivers.

Note that flowdescriptors must not be specified when using the RSVP\_WILDCARD\_STYLE object, such that the **NumFlowDesc** member of [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) is set to zero, and **FlowDescList** of **RSVP\_RESERVE\_INFO** is set to **NULL**.

## The RSVP\_SHARED\_EXPLICIT\_STYLE Object

The RSVP\_SHARED\_EXPLICIT\_STYLE object may be specified in the Style member of the [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) object to override default RSVP filter style settings. The RSVP\_SHARED\_EXPLICIT\_STYLEobject is used to create an RSVP Shared Explicit (SE) reservation (see [Base RSVP Reservation Styles](base-rsvp-reservation-styles.md)). Note that the only way to create connections that use the Shared Explicit (SE) RSVP filter style is through this mechanism.

The RSVP\_SHARED\_EXPLICIT\_STYLE object cannot be applied to TCP receivers or to connected UDP receivers.

When the RSVP\_SHARED\_EXPLICIT\_STYLE is used, the flow's resources are shared between all senders listed in the FilterSpec. Also, when using the RSVP\_SHARED\_EXPLICIT\_STYLE object, flowdescriptors must be specified, such that the **NumFlowDesc** member of [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) is set to 1, and **FlowDescList** of **RSVP\_RESERVE\_INFO** is not set to **NULL**.

It is important to note that the number of senders included in any individual Shared Explicit reservation should be limited to a reasonable number of senders (such as 10). If more than 10 senders will be included in a given reservation, receivers should use the WF reservation style.

## Generating Multiple Fixed Filter Reservations in a Single Reservation

It may be useful in certain situations to enable a receiver to reserve mutually exclusive flows for multiple, explicitly identified sources. This is achieved by generating multiple Fixed Filter (FF) RSVP reservations in a single reservation.

To do this, specify RSVP\_FIXED\_FILTER\_STYLE in the Style member of the [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) object, followed by a list of multiple flowdescriptors. So for n explicitly identified sources, the **NumFlowDesc** member of the **RSVP\_RESERVE\_INFO** object is set to n, and the **FlowDescList** member of the **RSVP\_RESERVE\_INFO** object is set to n sender addresses/ports.

Note that this cannot be done with TCP receivers, as TCP receivers are assumed connected to a single-peer sender. This should not be applied to UDP receivers that have been connected using the [**WSAConnect**](https://msdn.microsoft.com/library/windows/desktop/ms741559) function. In these cases, the transport discards data from all senders other than the sender specified in the **WSAConnect** function call.

 

 




