---
description: TAPI responds to device changes such as a phone that has started ringing or a modem that has been removed by firing device events.
ms.assetid: afa504ca-6e70-4076-a179-31002d3b38e2
title: Device Events (Telephony API)
ms.topic: article
ms.date: 05/31/2018
---

# Device Events (Telephony API)

TAPI responds to device changes such as a phone that has started ringing or a modem that has been removed by firing device events. A TAPI application should respond to a device event by querying for the specific change that has occurred and then taking appropriate action. An application may screen for events it will receive using [event notification](event-notification.md).

**TAPI 2.x:** Applications receive notification of device events using the [**LINE\_LINEDEVSTATE**](./line-linedevstate.md) message. The current status of an address is determined by calling [**lineGetAddressStatus**](/windows/win32/api/tapi/nf-tapi-linegetaddressstatus), which returns its information in a [**LINEADDRESSSTATUS**](/windows/win32/api/tapi/ns-tapi-lineaddressstatus) structure. The status of a specified open line device is obtained by calling [**lineGetLineDevStatus**](/windows/win32/api/tapi/nf-tapi-linegetlinedevstatus), which returns its information in a [**LINEDEVSTATUS**](/windows/win32/api/tapi/ns-tapi-linedevstatus) structure.

**TAPI 3.x:** Applications receive an [**ADDRESS\_EVENT**](/windows/desktop/api/Tapi3if/ne-tapi3if-address_event) notification, which is processed using the [**ITAddressEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddressevent) interface. The [**ITAddressCapabilities**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresscapabilities) can then be used to acquire more detail information.

 

 
