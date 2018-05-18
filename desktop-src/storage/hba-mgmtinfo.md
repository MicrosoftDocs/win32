---
title: HBA\_MgmtInfo structure
description: The HBA\_MgmtInfo structure is used in conjunction with the HBA\_SetRNIDMgmtInfo routine to program the HBA to return the indicated request node identification information data (RNID).
ms.assetid: 'a4ccb122-ae90-4b06-a40d-21f131add99b'
keywords: ["HBA_MgmtInfo structure Storage Devices", "HBA_MGMTINFO structure Storage Devices", "PHBA_MGMTINFO structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- HBA_MGMTINFO
api_location:
- hbaapi.h
api_type:
- HeaderDef
---

# HBA\_MgmtInfo structure

The HBA\_MgmtInfo structure is used in conjunction with the [**HBA\_SetRNIDMgmtInfo**](hba-setrnidmgmtinfo.md) routine to program the HBA to return the indicated request node identification information data (RNID).

## Syntax


```C++
typedef struct HBA_MgmtInfo {
  HBA_WWN    wwn;
  HBA_UINT32 unittype;
  HBA_UINT32 PortId;
  HBA_UINT32 NumberOfAttachedNodes;
  HBA_UINT16 IPVersion;
  HBA_UINT16 UDPPort;
  HBA_UINT8  IPAddress[16];
  HBA_UINT16 reserved;
  HBA_UINT16 TopologyDiscoveryFlags;
} HBA_MGMTINFO, *PHBA_MGMTINFO;
```



## Members

<dl> <dt>

**wwn**
</dt> <dd>

Contains a 64 bit world-wide name (WWN) that uniquely identifies the primary fibre channel node (host system) to which the HBA is attached. This information is returned in an RNID Accept payload in response to an RNID request. For more information about the meaning of this member, see the description of the RNID Accept payload in the *Fibre Channel Framing and Signaling (FC-FS)* specification, published by the T11 committee. For a discussion of worldwide names, see the T11 committee's *Fibre Channel HBA API* specification.

</dd> <dt>

**unittype**
</dt> <dd>

Contains a value that indicates the unit type. Unit types include such things as gateways, switches, hubs, storage subsystems, etc. For a list of values that can be assigned to this field and their corresponding units, see the *Fibre Channel Framing and Signaling (FC-FS)* specification, published by the T11 committee.

</dd> <dt>

**PortId**
</dt> <dd>

Contains a vendor-specific value that identifies the physical port on the HBA that has a Fibre-Channel link attached. For more information about the meaning of this member, see the *Fibre Channel Framing and Signaling (FC-FS)* specification, published by the T11 committee.

</dd> <dt>

**NumberOfAttachedNodes**
</dt> <dd>

Indicates the number of nodes to which the HBA is attached. For more information about the meaning of this member, see the description of the RNID Accept payload in the *Fibre Channel Framing and Signaling (FC-FS)* specification, published by the T11 committee.

</dd> <dt>

**IPVersion**
</dt> <dd>

Indicates the version of the IP protocol used by the HBA. For more information about the meaning of this member, see the *Fibre Channel Framing and Signaling (FC-FS)* specification, published by the T11 committee.

</dd> <dt>

**UDPPort**
</dt> <dd>

Indicates the UDP/TCP port number used by the HBA. For more information about the meaning of this member, see the *Fibre Channel Framing and Signaling (FC-FS)* specification, published by the T11 committee.

</dd> <dt>

**IPAddress**
</dt> <dd>

Contains the IP address f the HBA.

</dd> <dt>

**reserved**
</dt> <dd>

Reserved.

</dd> <dt>

**TopologyDiscoveryFlags**
</dt> <dd>

Contains the topology discovery flags. For an explanation of this member, see the *Fibre Channel Framing and Signaling (FC-FS)* specification, published by the T11 committee.

</dd> </dl>

## Requirements



|                   |                                                                                                        |
|-------------------|--------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbaapi.h (include Hbaapi.h)</dt> </dl> |



## See also

<dl> <dt>

[**HBA\_GetRNIDMgmtInfo**](hba-getrnidmgmtinfo.md)
</dt> <dt>

[**HBA\_SetRNIDMgmtInfo**](hba-setrnidmgmtinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HBA_MgmtInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






