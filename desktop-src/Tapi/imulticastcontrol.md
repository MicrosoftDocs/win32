---
description: The IMulticastControl interface is implemented by the IPConf MSP and available only on multicast call objects.
ms.assetid: 9bdb4ab9-30b3-46fb-b13a-de9c294c8046
title: IMulticastControl interface (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# IMulticastControl interface

\[**IMulticastControl** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **IMulticastControl** interface is implemented by the IPConf MSP and available only on multicast call objects. This interface exposes methods that enable creation and manipulation of terminals that can communicate between H323 and SDP clients. The **IMulticastControl** interface controls the multicast loopback mode.

In the MM\_NO\_LOOPBACK mode, multicast loopback is disabled, which means two applications on the same machine who join the same multicast group will get each other's packets. This mode has the best performance if there is always only one application joining the multicast group on the machine. MM\_NO\_LOOPBACK mode is the default mode.

The MM\_FULL\_LOOPBACK mode is good only for testing. All the packets sent out are looped back as well. This can be used to test if the devices are working.

The MM\_SELECTIVE\_LOOPBACK mode is used to enable multiple applications on one machine to join the same multicast group. The packets are looped back from the stack, and each RTP session is responsible for filtering out unwanted packets.

## Members

The **IMulticastControl** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IMulticastControl** also has these types of members:

-   [Methods](#methods)

### Methods

The **IMulticastControl** interface has these methods.



| Method                                                          | Description                                  |
|:----------------------------------------------------------------|:---------------------------------------------|
| [**get\_LoopbackMode**](imulticastcontrol-get-loopbackmode.md) | Gets the multicast loopback mode.<br/> |
| [**put\_LoopbackMode**](imulticastcontrol-put-loopbackmode.md) | Sets the multicast loopback mode.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |
| Library<br/>      | <dl> <dt>Uuid.lib</dt> </dl>   |
| DLL<br/>          | <dl> <dt>Tapi3.dll</dt> </dl>  |



## See also

<dl> <dt>

[IPConf MSP](ipconf-msp.md)
</dt> </dl>

 

