---
title: HBAFC3MgmtInfo structure
description: The HBAFC3MgmtInfo structure is used to report FC3 management information associated with a fibre channel adapter.
ms.assetid: '96236605-36b0-48f5-85d6-512160692b5f'
keywords: ["HBAFC3MgmtInfo structure Storage Devices", "PHBAFC3MgmtInfo structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBAFC3MgmtInfo
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# HBAFC3MgmtInfo structure

The HBAFC3MgmtInfo structure is used to report FC3 management information associated with a fibre channel adapter.

## Syntax


```C++
typedef struct _HBAFC3MgmtInfo {
  ULONGLONG UniqueAdapterId;
  UCHAR     wwn[8];
  ULONG     unittype;
  ULONG     PortId;
  ULONG     NumberOfAttachedNodes;
  USHORT    IPVersion;
  USHORT    UDPPort;
  UCHAR     IPAddress[16];
  USHORT    reserved;
  USHORT    TopologyDiscoveryFlags;
  ULONG     reserved1;
} HBAFC3MgmtInfo, *PHBAFC3MgmtInfo;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

Contains a unique identifier for the adapter.

</dd> <dt>

**wwn**
</dt> <dd>

Contains a worldwide name for the adapter, as described in the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**unittype**
</dt> <dd>

Describes the type of HBA, as described in the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**PortId**
</dt> <dd>

Contains a value corresponding to the physical port number field of the specific identification data as described in the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**NumberOfAttachedNodes**
</dt> <dd>

Contains the number of nodes attached to the topology as described in the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**IPVersion**
</dt> <dd>

Contains the concatenated node management and IP version fields of the specific identification data as described in the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**UDPPort**
</dt> <dd>

Indicates the value of the UDP/TCP port number field of the specific identification data as described in the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**IPAddress**
</dt> <dd>

Indicates the value of the IP address field of the specific identification data as described in the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**TopologyDiscoveryFlags**
</dt> <dd>

Indicates the value of the vendor specific field in word 12 of the specific identification data as described in the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**reserved1**
</dt> <dd>

Reserved.

</dd> </dl>

## Remarks

FC-3 refers to the common services layer of the fibre channel protocol. It defines a set of services which are common across multiple ports of a node. For an explanation of the common services layer, see the T11 committee's *Fibre Channel HBA API* specification.

The WMI tool suite generates a declaration of this structure automatically when it compiles the **HBAFC3MgmtInfo** WMI Class in *hbaapi.mof*.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetFC3MgmtInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553939)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBAFC3MgmtInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






