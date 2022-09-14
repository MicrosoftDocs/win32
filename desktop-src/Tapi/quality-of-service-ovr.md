---
description: Asynchronous Transfer Mode (ATM) networking is emerging into the mainstream of computing, and support for ATM has been added to many parts of the operating system.
ms.assetid: 0ca0ecf3-2b67-4925-a6fc-3edfaad2c0e2
title: Quality of Service (Telephony API)
ms.topic: article
ms.date: 05/31/2018
---

# Quality of Service (Telephony API)

Asynchronous Transfer Mode (ATM) networking is emerging into the mainstream of computing, and support for ATM has been added to many parts of the operating system. TAPI also supports key attributes of establishing calls on ATM facilities. The most important of these from an application perspective is the ability to request, negotiate, renegotiate, and receive indications of Quality of Service (QOS) parameters on incoming and outgoing calls.

QOS information in TAPI is exchanged between applications and service providers in [**FLOWSPEC**](/windows/desktop/api/qos/ns-qos-flowspec) structures that are defined in Windows Sockets 2.0.

Applications request QOS on outgoing calls by setting session information values prior to starting a communications session. The service provider will try to provide the specified QOS, and fail the call if it cannot. The application can then adjust its parameters and try the call again. After a call is established, an application can request a change in the QOS.

TAPI provides event notifications to owner or monitor applications if there is any change in QOS levels.

Support for QOS is not restricted to ATM transports; any service provider can implement QOS features.

Not all service providers support use of this information.

**TAPI 2.x:  **[**lineSetCallQualityOfService**](/windows/win32/api/tapi/nf-tapi-linesetcallqualityofservice), [**lineGetCallInfo**](/windows/win32/api/tapi/nf-tapi-linegetcallinfo), **dwSendingFlowspecSize**, **dwSendingFlowspecOffset**, **dwReceivingFlowspecSize**, and **dwReceivingFlowspecOffset** members of [**LINECALLPARAMS**](/windows/win32/api/tapi/ns-tapi-linecallparams)

**TAPI 3.x:  **[**ITBasicCallControl::SetQOS**](/windows/desktop/api/tapi3if/nf-tapi3if-itbasiccallcontrol-setqos), [**ITQOSEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itqosevent)

 

 
