---
Description: TAPI responds to device changes such as a phone that has started ringing or a modem that has been removed by firing device events.
ms.assetid: afa504ca-6e70-4076-a179-31002d3b38e2
title: Device Events
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Device Events

TAPI responds to device changes such as a phone that has started ringing or a modem that has been removed by firing device events. A TAPI application should respond to a device event by querying for the specific change that has occurred and then taking appropriate action. An application may screen for events it will receive using [event notification](event-notification.md).

**TAPI 2.x:** Applications receive notification of device events using the [**LINE\_LINEDEVSTATE**](https://msdn.microsoft.com/en-us/library/ms736554(v=VS.85).aspx) message. The current status of an address is determined by calling [**lineGetAddressStatus**](https://msdn.microsoft.com/en-us/library/ms735683(v=VS.85).aspx), which returns its information in a [**LINEADDRESSSTATUS**](https://msdn.microsoft.com/en-us/library/ms734938(v=VS.85).aspx) structure. The status of a specified open line device is obtained by calling [**lineGetLineDevStatus**](https://msdn.microsoft.com/en-us/library/ms735753(v=VS.85).aspx), which returns its information in a [**LINEDEVSTATUS**](https://msdn.microsoft.com/en-us/library/ms735610(v=VS.85).aspx) structure.

**TAPI 3.x:** Applications receive an [**ADDRESS\_EVENT**](/windows/desktop/api/Tapi3if/ne-tapi3if-address_event) notification, which is processed using the [**ITAddressEvent**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddressevent) interface. The [**ITAddressCapabilities**](/windows/desktop/api/tapi3if/nn-tapi3if-itaddresscapabilities) can then be used to acquire more detail information.

 

 



