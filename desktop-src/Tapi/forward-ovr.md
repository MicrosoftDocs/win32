---
Description: Forwarding is the deflection of an incoming session to a different destination address.
ms.assetid: c70bf596-b2a4-46ec-9b1a-c9d948768b51
title: Forward
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Forward

Forwarding is the deflection of an incoming session to a different destination address. TAPI allows an application to specify a list of forwarding conditions for an address. Forwarding conditions can be as finely grained as a different destination and [**forwarding mode**](https://msdn.microsoft.com/en-us/library/ms735649(v=VS.85).aspx) for each caller address.

The forwarding operation can also be used to implement a selective do-not-disturb feature, by forwarding some callers to voice mail and allowing others to attempt completion.

The forwarding operation can also cancel any forwarding currently in effect.

Some service providers require that an application create a consultation call prior to a forwarding operation. The forwarding operation is then passed a pointer to the consultation call.

Not all service providers support use of this operation.

**TAPI 2.x:** To set [**lineForward**](https://msdn.microsoft.com/en-us/library/ms735640(v=VS.85).aspx) to get [**lineGetAddressStatus**](https://msdn.microsoft.com/en-us/library/ms735683(v=VS.85).aspx), change the [**LINE\_ADDRESSSTATE**](https://msdn.microsoft.com/en-us/library/ms736484(v=VS.85).aspx) notification message with LINEADDRESSSTATE\_FORWARD.

**TAPI 3.x:** See [**ITAddress::Forward**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddress-forward), [**ITAddress::get\_CurrentForwardInfo**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddress-get_currentforwardinfo), change notification: [**ITAddressEvent::get\_Event**](/windows/desktop/api/tapi3if/nf-tapi3if-itaddressevent-get_event) with AE\_FORWARD.

> [!Note]  
> It may be impossible for a service provider to know at all times what forwarding is in effect for an address. Forwarding can be canceled or changed in ways that do not result in notification to the service provider.

 

 

 



