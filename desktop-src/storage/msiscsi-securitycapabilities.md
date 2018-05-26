---
title: MSiSCSI\_SecurityCapabilities structure
description: The MSiSCSI\_SecurityCapabilities structure describes the security capabilities of an initiator.
ms.assetid: a385283a-7b24-43aa-b291-541bfd6a91a6
keywords:
- MSiSCSI_SecurityCapabilities structure Storage Devices
- PMSiSCSI_SecurityCapabilities structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_SecurityCapabilities
api_location:
- iscsicfg.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSiSCSI\_SecurityCapabilities structure

The MSiSCSI\_SecurityCapabilities structure describes the security capabilities of an initiator.

## Syntax


```C++
typedef struct _MSiSCSI_SecurityCapabilities {
  BOOLEAN ProtectiScsiTraffic;
  BOOLEAN ProtectiSNSTraffic;
  BOOLEAN CertificatesSupported;
  ULONG   EncryptionAvailableCount;
  ULONG   EncryptionAvailable[1];
} MSiSCSI_SecurityCapabilities, *PMSiSCSI_SecurityCapabilities;
```



## Members

<dl> <dt>

**ProtectiScsiTraffic**
</dt> <dd>

A Boolean value that indicates whether the initiator can use IPsec to protect iSCSI traffic. If this member is **TRUE**, the initiator can use IPsec to protect iSCSI traffic. If **FALSE**, the initiator cannot use IPsec.

</dd> <dt>

**ProtectiSNSTraffic**
</dt> <dd>

A Boolean value that indicates whether the initiator can use IPsec to protect iSNS traffic. If this member is **TRUE**, the initiator can use IPsec to protect iSNS traffic. If **FALSE**, the initiator cannot use IPsec.

</dd> <dt>

**CertificatesSupported**
</dt> <dd>

A Boolean value that indicates whether the initiator supports certificates. If this member is **TRUE**, the initiator supports certificates. If this member is **FALSE**, the initiatiator does not support certificates.

</dd> <dt>

**EncryptionAvailableCount**
</dt> <dd>

The number of encryption types that the initiator supports.

</dd> <dt>

**EncryptionAvailable**
</dt> <dd>

A variable length array of [**ISCSI\_ENCRYPTION\_TYPES**](iscsi-encryption-types.md) structures, which indicate types of encryption that the initiator supports.

</dd> </dl>

## Remarks

The WMI tool suite automatically generates a declaration of the MSiSCSI\_SecurityCapabilities structure when it compiles the [MSiSCSI\_SecurityCapabilities WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563131) in *Config.mof*.

Initiators that support IPsec must implement the MSiSCSI\_SecurityCapabilities class.

Initiators must register the MSiSCSI\_SecurityCapabilities class using the name of the physical device object (PDO) for the HBA. You must implement this class if the adapter supports IPsec.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsicfg.h (include Iscsicfg.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_ENCRYPTION\_TYPES**](iscsi-encryption-types.md)
</dt> <dt>

[MSiSCSI\_SecurityCapabilities WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff563131)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_SecurityCapabilities%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






