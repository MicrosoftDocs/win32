---
description: The MULTICAST\_LOOPBACK\_MODE enum describes the multicast loopback mode.
ms.assetid: bf9c3665-71cc-4cde-9ad4-1a8b62eddf9f
title: MULTICAST_LOOPBACK_MODE enumeration (Confpriv.h)
ms.topic: reference
ms.date: 05/31/2018
---

# MULTICAST\_LOOPBACK\_MODE enumeration

\[**MULTICAST\_LOOPBACK\_MODE** is not available for use in Windows Vista, Windows Server 2008, and subsequent versions of the operating system. The RTC Client API provides similar functionality.\]

The **MULTICAST\_LOOPBACK\_MODE** enum describes the multicast loopback mode.

## Syntax


```C++
} MULTICAST_LOOPBACK_MODE;
```



## Constants

<dl> <dt>

<span id="MM_NO_LOOPBACK"></span><span id="mm_no_loopback"></span>**MM\_NO\_LOOPBACK**
</dt> <dd>

Multicast loopback is disabled. That means two applications on the same machine joining the same multicast group can get each other's packets.

</dd> <dt>

<span id="MM_FULL_LOOPBACK"></span><span id="mm_full_loopback"></span>**MM\_FULL\_LOOPBACK**
</dt> <dd>

All the packets sent out are looped back as well. This mode is useful only for testing.

</dd> <dt>

<span id="MM_SELECTIVE_LOOPBACK"></span><span id="mm_selective_loopback"></span>**MM\_SELECTIVE\_LOOPBACK**
</dt> <dd>

Selective loopback is enabled. That means enabled multiple applications on one machine can join the same multicast group without confusion. The packets are looped back from the stack and each RTP session is responsible for filtering out unwanted packets.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------|---------------------------------------------------------------------------------------|
| TAPI version<br/> | Requires TAPI 3.0 or later<br/>                                                 |
| Header<br/>       | <dl> <dt>Confpriv.h</dt> </dl> |



## See also

<dl> <dt>

[**IMulticastControl::get\_LoopbackMode**](imulticastcontrol-get-loopbackmode.md)
</dt> <dt>

[**IMulticastControl::put\_LoopbackMode**](imulticastcontrol-put-loopbackmode.md)
</dt> </dl>

 

 




