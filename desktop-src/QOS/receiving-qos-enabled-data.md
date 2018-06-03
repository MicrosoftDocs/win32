---
title: Receiving QOS-enabled Data
description: An application can begin receiving data from its QOS-enabled sender before the QOS-enabled reservation is established.
ms.assetid: 075ca5f9-39f6-420c-8172-852c28ad36df
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Receiving QOS-enabled Data

An application can begin receiving data from its QOS-enabled sender before the QOS-enabled reservation is established. The result of receiving data before the QOS reservation is established is that data is transmitted over the network without QOS guarantees (as it would be in a non-QOS network). Once the QOS-enabled reservation is established, the receiver can receive data that conforms to the established QOS-parameters for the reservation.

Inherent in the occurrence of events (such as the establishment of the QOS-enabled connection) is the need for an application to query for events. The RSVP SP provides mechanisms that enable event notification. These mechanisms differ depending on whether the application is receiving or sending data.

As a receiver on a QOS-enabled connection, a host may initiate some or all of the following actions:

-   As implied in the section [Providing the RSVP SP with QOS-specific parameters](providing-the-rsvp-sp-with-qos-specific-parameters.md), a receiver must provide QOS-specific parameters to the RSVP SP. These parameters are provided in the ReceivingFlowSpec parameter of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure, which is provided through the use of the WSAConnect function, the WSAJoinLeaf function, the WSAAccept callback function, or through the Windows Sockets 2 SIO\_SET\_QOS IOCTL opcode.
-   To streamline the establishment of existing, common settings for the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure, an application can use the [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587) function to enumerate, and then retrieve an existing QOS template, and apply the values in that template (in the form of a **QOS** structure) to the **QOS** structure in the Windows Sockets function call. See the section [QOS Templates](qos-templates.md) for more information on QOS templates.
-   The application may then send data. Data sent that complies to the constraints of the established QOS-specific parameters is considered conforming data. Data that falls outside those parameters, or nonconforming data, is handled differently based on the QOS\_SD\_MODE setting, which is particular to traffic control. Options for nonconforming data include relegating it to a best-effort transmission to discarding nonconforming packets.
-   The application may want to track RSVP SP events in order to monitor the QOS-enabled connection status. For example, the application uses the status information and error codes provided with FD\_QOS events. Other RSVP SP events that an application may want to monitor include using an [**RSVP\_RESERVE\_INFO**](/previous-versions/windows/desktop/api/Qossp/ns-qossp-_rsvp_reserve_info) object to request arrival confirmation of a RESV message.
-   When the application receives notification of certain events, it may take appropriate action to modify its QOS settings or parameters. For example, if an application is notified of the arrival of a PATH message, it must use the Windows Sockets 2 SIO\_GET\_QOS IOCTL opcode to retrieve pertinent QOS information, such as the sender's Tspec and the path's Adspec. Information provided in the PATH message may be used by the application to modify its initial QOS-specific parameters to match the sender's Tspec. For more information on Tspec and Adspec, see the section [RSVP SP and RSVP](rsvp-sp-and-rsvp.md)).

 

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

 

 




