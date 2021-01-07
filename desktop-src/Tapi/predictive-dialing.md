---
description: Predictive dialing is an application that typically runs on a call center telephony server.
ms.assetid: c8d0b2b5-61eb-4ab0-b09d-c54c282b730e
title: Predictive Dialing
ms.topic: article
ms.date: 05/31/2018
---

# Predictive Dialing

Predictive dialing is an application that typically runs on a call center telephony server. It uses a list of phone numbers, often obtained from a database, to attempt outgoing calls; when a call is *completed*, the call is automatically assigned to an agent for handling. The application can make use of a *predictive dialing port* on a switch, which is a device that can make outgoing calls and has special abilities (through DSP, and so on) to detect call progress tones and other audible indications of call state. When a call is made on a predictive dialing port, typically it is automatically transferred to another device on the switch when the call reaches a particular state or upon detection of a particular media type; this target device can be a queue for agents handling outgoing calls.

Applications identify a device as having predictive dialing capability by the LINEADDRCAPFLAGS\_PREDICTIVEDIALER bit in the **dwAddrCapFlags** member in [**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps). The **dwPredictiveAutoTransferStates** member in **LINEADDRESSCAPS** indicates the states upon which the predictive dialing port can be commanded to automatically transfer a call; if this member is zero, it indicates that automatic transfer is not available, and that it is the responsibility of the application to transfer calls explicitly upon detecting the appropriate call state (or media type or other criteria). Preferably, switch manufacturers will make available both automatic and manual transfer, and allow applications to select the preferred mechanism, but service providers would have to model the behavior of legacy equipment. A single predictive dialing port (line device/address) can support making several outgoing calls simultaneously, as indicated by the **dwMaxNumActiveCalls** member in **LINEADDRESSCAPS**. Predictive dialing capability can also be made available on any device, using a shared pool of predictive dialing signal processors, which are bridged onto the line being dialed upon request.

When the [**lineMakeCall**](/windows/desktop/api/Tapi/nf-tapi-linemakecall) function is used on a line capable of predictive dialing (a port with the LINEADDRCAPFLAGS\_PREDICTIVEDIALER set) and predictive dialing is requested using LINECALLPARAMFLAGS\_PREDICTIVEDIAL, then the call is made in a predictive fashion with enhanced audible call progress detection. Additional fields and constants are defined in the [**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams) structure passed in to **lineMakeCall** to control the behavior of the predictive dialing port. The **dwPredictiveAutoTransferStates** member indicates the line call states that, upon entry of the call into any of them, the predictive dialing port should automatically transfer the call to the designated target (the bits must be a proper subset of the supported auto-transfer states indicated in [**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps)); the application can leave the field set to 0 if it desires to monitor call states itself and use [**lineBlindTransfer**](/windows/desktop/api/Tapi/nf-tapi-lineblindtransfer) to transfer the call when it reaches the desired condition. The application must specify the desired address to which the call should be automatically transferred in the variable field defined by the **dwTargetAddressSize** and **dwTargetAddressOffset** members in **LINECALLPARAMS**.

Applications can also set a timeout for outgoing calls so that the service provider automatically transitions them to a disconnected state if they are not answered. This is controlled using the **dwNoAnswerTimeout** member in [**LINECALLPARAMS**](/windows/desktop/api/Tapi/ns-tapi-linecallparams).

 

 



