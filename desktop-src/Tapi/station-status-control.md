---
description: There are three major station status functions that need control Message Waiting lights, Forwarding, and Do Not Disturb.
ms.assetid: 4a6dc47f-caff-4f2b-8858-0e9bec32b137
title: Station Status Control
ms.topic: article
ms.date: 05/31/2018
---

# Station Status Control

There are three major station status functions that need control: Message Waiting lights, Forwarding, and Do Not Disturb. Forwarding and Do Not Disturb are controllable through the existing [**lineForward**](/windows/desktop/api/Tapi/nf-tapi-lineforward) function (which is address-specific), and queried using [**lineGetAddressStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus). The LINEDEVSTATUSFLAGS\_MSGWAIT bit in the **dwDevStatusFlags** member of [**LINEDEVSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linedevstatus) indicates the status of the message waiting light on the device, and a LINEDEVSTATE\_MSGWAITON or LINEDEVSTATE\_MSGWAITOFF message is sent to indicate when the state changes. The [**lineSetLineDevStatus**](/windows/desktop/api/Tapi/nf-tapi-linesetlinedevstatus) function allows the message waiting light to be controlled without having to implement a TAPI phone device just for that purpose. The LINEFEATURE\_SETDEVSTATUS bit (in the **dwLineFeatures** member of [**LINEDEVCAPS**](/windows/desktop/api/Tapi/ns-tapi-linedevcaps) and **LINEDEVSTATUS**) indicates when it can be called, and the **dwSettableDevStatus** member of **LINEDEVCAPS** allows the application to detect which device status settings can be controlled from the application. In addition to allowing the message waiting feature to be controlled, it also allows the device's Connected, Inservice, and Locked status to be set, to the extent that these are supported by the switch or other hardware. Calls to this function result in appropriate [**LINE\_LINEDEVSTATE**](line-linedevstate.md) messages being sent to reflect the new status.

 

 



