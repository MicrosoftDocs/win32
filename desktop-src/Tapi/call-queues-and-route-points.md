---
description: A call queue or route point is a special address within the switch where calls are temporarily held pending action.
ms.assetid: 1c801401-be05-4b5f-bc4f-628dde0f3cf7
title: Call Queues and Route Points
ms.topic: article
ms.date: 05/31/2018
---

# Call Queues and Route Points

A call queue or route point is a special address within the switch where calls are temporarily held pending action. This characteristic is represented by the bits LINEADDRCAPFLAGS\_QUEUE and LINEADDRCAPFLAGS\_ROUTEPOINT in the **dwAddrCapFlags** member in [**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps). All calls appearing on such an address are awaiting action by the application, and there can be default actions that take place (for example, transfer to an agent or trunk) if the application takes no action within a defined period of time. The application must be configured by the system administrator so that it knows what actions it should take regarding calls appearing on each queue or route point address, and the amount of time available to decide on the action to take.

Applications can determine the number of calls pending in a queue or route point using [**lineGetAddressStatus**](/windows/desktop/api/Tapi/nf-tapi-linegetaddressstatus). The [**lineGetCallInfo**](/windows/desktop/api/Tapi/nf-tapi-linegetcallinfo) function can be used to obtain information such as calling ID, called ID, incoming or outgoing origin, and so on, and used by the application to make decisions on call handling; calls can be redirected, blind-transferred, dropped, and so on, or just allowed to automatically pass out of the queue to a destination. A call goes to LINECALLSTATE\_DISCONNECTED if it is abandoned. Calls go *idle* when they leave the queue; **lineGetCallInfo** can be used to read the redirection identifier to determine where they were transferred.

Some switches allow calls in a queue or on hold to receive particular treatment such as silence, ringback, busy signal, music, or listening to a recorded announcement. The [**lineSetCallTreatment**](/windows/desktop/api/Tapi/nf-tapi-linesetcalltreatment) function allows the application to control the treatment. The structure delimited by the **dwCallTreatmentListSize** and **dwCallTreatmentListOffset** members in [**LINEADDRESSCAPS**](/windows/desktop/api/Tapi/ns-tapi-lineaddresscaps) allows applications to determine the supported treatments. The **dwCallTreatment** member in [**LINECALLINFO**](/windows/desktop/api/Tapi/ns-tapi-linecallinfo) indicates the current treatment, and a [**LINE\_CALLINFO**](line-callinfo.md) message with LINECALLINFOSTATE\_TREATMENT indicates when this changes. The LINECALLFEATURE\_SETTREATMENT bit in the **dwCallFeatures** member in [**LINECALLSTATUS**](/windows/desktop/api/Tapi/ns-tapi-linecallstatus) indicates when the application is permitted to change the treatment. The LINECALLTREATMENT\_ set of constants defines a limited set of predefined call treatments; service providers can define many more.

 

 



