---
title: MSiSCSI\_MMIPSECStats structure
description: The MSiSCSI\_MMIPSECStats structure is used to report main mode IPsec statistics.
ms.assetid: 75b11689-f940-467e-92ee-59b5e0adbf70
keywords:
- MSiSCSI_MMIPSECStats structure Storage Devices
- PMSiSCSI_MMIPSECStats structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_MMIPSECStats
api_location:
- iscsiprf.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSiSCSI\_MMIPSECStats structure

The MSiSCSI\_MMIPSECStats structure is used to report main mode IPsec statistics.

## Syntax


```C++
typedef struct _MSiSCSI_MMIPSECStats {
  ULONGLONG ActiveAcquire;
  ULONGLONG ActiveReceive;
  ULONGLONG AcquireFailures;
  ULONGLONG ReceiveFailures;
  ULONGLONG SendFailures;
  ULONGLONG AcquireHeapSize;
  ULONGLONG ReceiveHeapSize;
  ULONGLONG NegotiationFailures;
  ULONGLONG AuthenticationFailures;
  ULONGLONG InvalidCookiesReceived;
  ULONGLONG TotalGetSPI;
  ULONGLONG KeyAdditions;
  ULONGLONG KeyUpdates;
  ULONGLONG GetSPIFailures;
  ULONGLONG KeyAdditionFailures;
  ULONGLONG KeyUpdateFailures;
  ULONGLONG ConnectionListSize;
  ULONGLONG OakleyMainMode;
  ULONGLONG OakleyQuickMode;
  ULONGLONG InvalidPackets;
  ULONGLONG SoftAssociations;
} MSiSCSI_MMIPSECStats, *PMSiSCSI_MMIPSECStats;
```



## Members

<dl> <dt>

**ActiveAcquire**
</dt> <dd>

The number of active require requests that the IPsec driver has sent to the Internet Key Exchange (IKE) service. Typically, the number of active acquire requests is 1. Under a heavy load, the number of active acquire requests is 1 plus the number of requests that are waiting in the queue of the IKE service.

</dd> <dt>

**ActiveReceive**
</dt> <dd>

The number of IKE messages (that is, active receive requests) that are queued for processing.

</dd> <dt>

**AcquireFailures**
</dt> <dd>

The number of active acquire requests that have failed.

</dd> <dt>

**ReceiveFailures**
</dt> <dd>

The number of failures that have occurred while drivers in the TCP stack are receiving IKE messages.

</dd> <dt>

**SendFailures**
</dt> <dd>

The number of failures that have occurred while drivers in the TCP stack are sending IKE messages.

</dd> <dt>

**AcquireHeapSize**
</dt> <dd>

The number of IKE messages that the acquire heap can hold. This number increases under a heavy load and then gradually decreases over time, as the acquire heap is emptied.

</dd> <dt>

**ReceiveHeapSize**
</dt> <dd>

The number of incoming IKE messages that the IKE receive buffers can hold.

</dd> <dt>

**NegotiationFailures**
</dt> <dd>

The total number of negotiation failures that occurred during main mode (also known as *phase 1*) negotiation or during quick mode (also known as *phase 2*) negotiation.

</dd> <dt>

**AuthenticationFailures**
</dt> <dd>

The number of identity authentication failures that occurred during main mode negotiation. This number includes kerberos failures, certificate failures, and preshared key failures.

</dd> <dt>

**InvalidCookiesReceived**
</dt> <dd>

The number of invalid cookies that the initiator has received in IKE messages. Cookies are invalid if the cookie state does not correspond to the state of an active main mode security association (SA).

</dd> <dt>

**TotalGetSPI**
</dt> <dd>

The number of requests that the IKE service submitted to obtain a unique security parameters index (SPI).

</dd> <dt>

**KeyAdditions**
</dt> <dd>

The number of outbound quick mode SAs that the IKE service has added.

</dd> <dt>

**KeyUpdates**
</dt> <dd>

The number of inbound quick mode SAs that the IKE service has added.

</dd> <dt>

**GetSPIFailures**
</dt> <dd>

The total number of unsuccessful attempts that the IKE service has made to obtain a unique SPI.

</dd> <dt>

**KeyAdditionFailures**
</dt> <dd>

The number of outbound quick-mode SAs that the IKE service has submitted unsuccessfully.

</dd> <dt>

**KeyUpdateFailures**
</dt> <dd>

The number of inbound quick-mode SAs that the IKE service has added.

</dd> <dt>

**ConnectionListSize**
</dt> <dd>

The number of quick-mode state entries.

</dd> <dt>

**OakleyMainMode**
</dt> <dd>

The number of successful SAs that are created during main mode negotiations.

</dd> <dt>

**OakleyQuickMode**
</dt> <dd>

The number of successful SAs that are created during quick-mode negotiations.

</dd> <dt>

**InvalidPackets**
</dt> <dd>

The number of received IKE messages that are invalid, including IKE messages with invalid header fields, incorrect payload lengths, or incorrect (nonzero) responder cookies that should be 0.

</dd> <dt>

**SoftAssociations**
</dt> <dd>

The number of negotiations that resulted in the use of plaintext SAs (also known as *soft SAs*). This value typically reflects the number of associations that the initiator established with computers that did not respond to main mode negotiation attempts. Computers that do not respond might not support IPSec, or they might support IPSec but not have an IPSec policy with which to negotiate security with an IPSec peer.

</dd> </dl>

## Remarks

It is optional that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiprf.h (include Iscsiprf.h)</dt> </dl> |



## See also

<dl> <dt>

[MSiSCSI\_MMIPSECStats WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563077)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_MMIPSECStats%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






