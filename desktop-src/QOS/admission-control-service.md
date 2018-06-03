---
title: Admission Control Service
description: Admission control service (ACS) is a QOS component that regulates subnet usage for QOS-enabled applications.
ms.assetid: d256392d-b1a1-4864-a766-6a9a2d4af183
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Admission Control Service

\[Admission Control Service (ACS) is not supported except on Windows 2000. See [RSVP Operates Only on Windows 2000](rsvp-operates-only-on-windows-2000.md) for more information on ACS and RSVP.\]

Admission control service (ACS) is a QOS component that regulates subnet usage for QOS-enabled applications. The ACS exerts its authority over QOS-aware applications or clients by placing itself within the RSVP message path. With this placement, ACS effectively intercepts RSVP PATH, RESV, PATH\_ERR, RESV\_ERR, PATH\_TEAR, and RESV\_TEAR messages and passes the messages' policy information to [Local Policy Modules](local-policy-module.md) (LPMs) for authentication. This exertion of ACS authority occurs on each interface (or shared medium) over which a given QOS flow must traverse. For a simplified example, if ACS is functioning on a source subnet and a (different) destination subnet for a given flow, policy restrictions are enforced by the ACS on each subnet.

ACS regulation is based on available network resources and on administratively-configurable information on users, or group policy. ACS is implemented as a service.

Local policy modules (LPMs) fall within the fold of ACS functionality, and can be considered an integral part of the ACS. With the default LPM, Microsoft Identity LPM (MSIDLPM) user information in the intercepted RSVP message is used to look up user policy in Active Directory services. MSIDLPM then makes policy decisions based on information found in Active Directory services.

Another ACS component, the Policy Control Module (PCM), actually mediates the interaction between the ACS and LPMs. If there are multiple residential LPMs, the PCM will send all policy data objects contained in the received RSVP messages to each LPM, gather all responses, perform logical checks on the information, aggregate it, and return the combined response to the ACS.

If network resources are available and if the policy check succeeds, the RSVP message and its policy information is sent to the next hop (or the previous hop, if it is a PATH or RESV message). In this way, ACS acts as the logical gatekeeper for RSVP message propagation across the network by rejecting requests under the following conditions:

-   If local segment resources are not available to provide the requested level of QOS (the SBM functionality of the ACS)
-   If the sender or receiver does not have appropriate policy permission to transmit data with the requested parameters

When such conditions occur, no network nodes beyond the ACS (in the appropriate direction) receive any of the RSVP messages rejected by the ACS. However, the error messages due to the rejection will traverse the network to reach the network mode that made the request.

This regulation does two things: it keeps unnecessary RSVP signaling traffic from traversing the network, and it restricts access to network resources, allowing only authorized requests to create reservations in the network. As an additional benefit, this also preserves processing resources for routers and WAN Interface Cards (WANICs) since they will not have to handle such RSVP messages. Note that any node that declines requests based on policy failure will return an RSVP error message to the sender. Clients will not transmit anything if their request is rejected by ACS.

Though ACS is a QOS component, its services include other QOS components, such as the Subnet Bandwidth Manager (SBM) and its LPM interface.

 

 




