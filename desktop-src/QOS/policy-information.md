---
title: Policy Information
description: Microsoft provides identity policy information through a DLL installed on QOS-enabled Windows clients such as Windows 2000 Server and Windows 2000 Professional.
ms.assetid: '1a053a7e-eff0-491e-a12c-b273b666f8ca'
---

# Policy Information

Microsoft provides identity policy information through a DLL installed on QOS-enabled Windows clients such as Windows 2000 Server and Windows 2000 Professional.

The policy information is incorporated in RSVP resource reservation requests, which in turn get sent out onto the network in the form of RSVP messages. This policy information is intercepted by the Admission Control Service (ACS), which includes SBM functionality as part of its fundamental service suite. The ACS services these requests by checking whether the requesting client has authorization to use network resources on the local subnet. If successful, the policy information is forwarded to the next network node for subsequent policy checking, and such activity continues toward the intended receiver, along the data path of network nodes, until the request is rejected or the intended receiver (the node with which the sending client wishes to communicate) is reached.

 

 




