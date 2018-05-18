---
title: MSiSCSI\_QMIPSECStats structure
description: The MSiSCSI\_QMIPSECStats structure can be used by an iSCSI initiator to report IPsec statistics for an HBA.
ms.assetid: '265ed956-1065-44be-ac8e-94bab2e4e8b8'
keywords: ["MSiSCSI_QMIPSECStats structure Storage Devices", "PMSiSCSI_QMIPSECStats structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSiSCSI_QMIPSECStats
api_location:
- iscsiprf.h
api_type:
- HeaderDef
---

# MSiSCSI\_QMIPSECStats structure

The MSiSCSI\_QMIPSECStats structure can be used by an iSCSI initiator to report IPsec statistics for an HBA.

## Syntax


```C++
typedef struct _MSiSCSI_QMIPSECStats {
  ULONGLONG ActiveSA;
  ULONGLONG PendingKeyOperations;
  ULONGLONG KeyAdditions;
  ULONGLONG KeyDeletions;
  ULONGLONG ReKeys;
  ULONGLONG ActiveTunnels;
  ULONGLONG BadSPIPackets;
  ULONGLONG PacketsNotDecrypted;
  ULONGLONG PacketsNotAuthenticated;
  ULONGLONG PacketsWithReplayDetection;
  ULONGLONG ConfidentialBytesSent;
  ULONGLONG ConfidentialBytesReceived;
  ULONGLONG AuthenticatedBytesSent;
  ULONGLONG AuthenticatedBytesReceived;
  ULONGLONG TransportBytesSent;
  ULONGLONG TransportBytesReceived;
  ULONGLONG TunnelBytesSent;
  ULONGLONG TunnelBytesReceived;
} MSiSCSI_QMIPSECStats, *PMSiSCSI_QMIPSECStats;
```



## Members

<dl> <dt>

**ActiveSA**
</dt> <dd>

The number of active IPsec security associations (SAs).

</dd> <dt>

**PendingKeyOperations**
</dt> <dd>

The number of IPsec key operations that are in progress.

</dd> <dt>

**KeyAdditions**
</dt> <dd>

The number of successful IPsec SA negotiations.

</dd> <dt>

**KeyDeletions**
</dt> <dd>

The number of IPsec SA key deletions.

</dd> <dt>

**ReKeys**
</dt> <dd>

The number of re-key operations for IPsec SAs.

</dd> <dt>

**ActiveTunnels**
</dt> <dd>

The number of active IPsec tunnels.

</dd> <dt>

**BadSPIPackets**
</dt> <dd>

The number of packets for which the security parameters index (SPI) was incorrect.

</dd> <dt>

**PacketsNotDecrypted**
</dt> <dd>

The number of failed decryption packets.

</dd> <dt>

**PacketsNotAuthenticated**
</dt> <dd>

The number of packets for which data could not be verified.

</dd> <dt>

**PacketsWithReplayDetection**
</dt> <dd>

The number of packets that contained a valid sequence number field.

</dd> <dt>

**ConfidentialBytesSent**
</dt> <dd>

The number of bytes that are sent by using the encapsulating security payload (ESP) protocol.

</dd> <dt>

**ConfidentialBytesReceived**
</dt> <dd>

The number of bytes that are received by using the ESP protocol.

</dd> <dt>

**AuthenticatedBytesSent**
</dt> <dd>

The number of bytes that are sent by using the authentication header (AH) protocol.

</dd> <dt>

**AuthenticatedBytesReceived**
</dt> <dd>

The number of bytes that are received by using the AH protocol.

</dd> <dt>

**TransportBytesSent**
</dt> <dd>

The number of bytes that are sent by using the IPsec protocol.

</dd> <dt>

**TransportBytesReceived**
</dt> <dd>

The number of bytes that are received by using the IPsec protocol.

</dd> <dt>

**TunnelBytesSent**
</dt> <dd>

The number of bytes that are sent by using the IPsec tunnel mode.

</dd> <dt>

**TunnelBytesReceived**
</dt> <dd>

The number of bytes that are received by using the IPsec tunnel mode.

</dd> </dl>

## Remarks

It is optional that you implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsiprf.h (include Iscsiprf.h)</dt> </dl> |



## See also

<dl> <dt>

[MSiSCSI\_QMIPSECStats WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563105)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_QMIPSECStats%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






