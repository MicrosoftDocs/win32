---
title: MSiSCSI\_DiscoveryConfig structure
description: The MSiSCSI\_DiscoveryConfig structure contains information that indicates what methods an initiator uses to do discovery.
ms.assetid: 'fe2f4a93-3fdd-422b-afce-8def3ed6688e'
keywords: ["MSiSCSI_DiscoveryConfig structure Storage Devices", "PMSiSCSI_DiscoveryConfig structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MSiSCSI_DiscoveryConfig
api_location:
- iscsicfg.h
api_type:
- HeaderDef
---

# MSiSCSI\_DiscoveryConfig structure

The MSiSCSI\_DiscoveryConfig structure contains information that indicates what methods an initiator uses to do discovery.

## Syntax


```C++
typedef struct _MSiSCSI_DiscoveryConfig {
  BOOLEAN          PerformiSNSDiscovery;
  BOOLEAN          PerformSLPDiscovery;
  BOOLEAN          AutomaticiSNSDiscovery;
  WCHAR            InitiatorName[256 + 1];
  ISCSI_IP_Address iSNSServer;
} MSiSCSI_DiscoveryConfig, *PMSiSCSI_DiscoveryConfig;
```



## Members

<dl> <dt>

**PerformiSNSDiscovery**
</dt> <dd>

A Boolean value that indicates whether the initiator performs target discovery by using iSNS and a predetermined iSNS server. If this member is **TRUE**, the initiator performs target discovery by using iSNS and a predetermined iSNS server. If this member is **FALSE**, the initiator does not do discovery with iSNS.

</dd> <dt>

**PerformSLPDiscovery**
</dt> <dd>

A Boolean value that indicates whether the initiator performs target discovery by using SLP. If this member is **TRUE**, the initiator performs target discovery by using SLP.

</dd> <dt>

**AutomaticiSNSDiscovery**
</dt> <dd>

A Boolean value that indicates whether the initiator should automatically search for an iSNS server and then perform target discovery by using iSNS. If this member is **TRUE**, the initiator should automatically search for an iSNS server and then perform target discovery by using iSNS.

</dd> <dt>

**InitiatorName**
</dt> <dd>

The default initiator name to register with the iSNS server.

</dd> <dt>

**iSNSServer**
</dt> <dd>

If **AutomaticiSNSDiscovery** is **FALSE**, **iSNSServer** contains a [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure that provides a fixed address of the iSNS server that is independent of the version of the IP protocol in use.

</dd> </dl>

## Remarks

The WMI tool suite automatically generates a declaration of the MSiSCSI\_DiscoveryConfig structure when it compiles the [MSiSCSI\_DiscoveryConfig WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562995) in *Config.mof*.

Initiators are required to implement the MSiSCSI\_DiscoveryConfig class. You must implement this class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsicfg.h (include Iscsicfg.h)</dt> </dl> |



## See also

<dl> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[MSiSCSI\_DiscoveryConfig WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562995)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_DiscoveryConfig%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






