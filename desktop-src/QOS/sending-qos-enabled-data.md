---
title: Sending QOS-enabled Data
description: As a sender on a QOS-enabled connection, the events differ somewhat from the receiver's collection of available actions.
ms.assetid: 06709495-5321-4832-9b1d-dd43feb36094
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sending QOS-enabled Data

As a sender on a QOS-enabled connection, the events differ somewhat from the receiver's collection of available actions. Where senders initiate connections and request certain QOS-specific parameters, receivers respond to such requests (note that network devices between the receiver and sender also react to receiver requests, and may reject requests before they ever reach the sender).

> [!Note]  
> RSVP signaling is not supported on Windows XP or later versions of Windows.

 

As a sender on a QOS-enabled connection, a host may initiate some or all of the following actions:

-   Sending hosts must inform the RSVP SP of QOS-specific parameters in order to enable the RSVP SP to interact with other QOS components on the sending host's behalf. QOS-specific parameters are provided to the RSVP SP through the SendingFlowspec member of the [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure, which itself is a parameter of the WSAConnect function, the WSAAccept function's ConditionFunc placeholder, and the WSAJoinLeaf function. The SendingFlowspec member can also be provided through the use of the SIO\_SET\_QOS IOCTL opcode.
-   The QOS-specific members (SendingFlowspec) are based on the application's knowledge of the data transmission characteristics appropriate for the application. For example, bandwidth requirements for database queries of a mission-critical application may be different than bandwidth requirements for low-quality audio broadcasts. Latency boundaries may also be different for those types of applications (note that latency boundaries are only available with Guaranteed Service). Therefore, the application is best equipped to provide appropriate QOS-specific transmission parameters, perhaps through the use of a QOS template.
-   Senders may use the [**WSAGetQOSByName**](https://msdn.microsoft.com/library/windows/desktop/ms741587) function to enumerate, and then retrieve preinstalled QOS templates that include QOS-specific parameters with appropriate transmission characteristics based on the type of application. For example, there may be a template called RADIOBCAST associated with a [**QOS**](/windows/desktop/api/Winsock2/ns-winsock2-_qualityofservice) structure that automatically applies the most appropriate QOS settings for radio broadcast senders. It is the application's responsibility to ensure that its traffic remains within the bounds of [**FLOWSPEC**](/previous-versions/windows/desktop/api/Qos/ns-qos-_flowspec) members obtained using WSAGetQosByName; traffic that exceeds those parameters will be treated as nonconforming, and may result in degradation of quality.
-   Senders may configure additional traffic control parameters by including objects in the [ProviderSpecific](the-providerspecific-buffer.md) buffer, such as handling nonconforming packets through setting of the SD\_MODE.
-   The sender may monitor RSVP SP events to maintain the QOS-enabled connection, such as the arrival of RESV messages. Often, the sender will want to monitor status information and error codes provided with FD\_QOS events. For example, the sender may choose to stop transmission when the FD\_QOS event WSA\_QOS\_NO\_RECEIVER occurs, indicating that there are no QOS-enabled receivers for the transmission.
-   The sending application may want to use the Windows Sockets 2 SIO\_GET\_QOS IOCTL opcode to look up QOS-specific parameters associated with the arrival of a RESV message.
-   The sending application may want to use the Windows Sockets 2 SIO\_CHK\_QOS IOCTL opcode to query parameters that provide information about the QOS connection such as allowed sending rate, line rate, and others.

 

 




