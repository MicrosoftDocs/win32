---
title: MS\_SMHBA\_SAS\_Port structure
description: The MS\_SMHBA\_SAS\_Port structure is used to report the SAS port information.
ms.assetid: 'd294d97a-e6b2-4ab3-bebf-e545aa2f862d'
keywords: ["MS_SMHBA_SAS_Port structure Storage Devices", "PMS_SMHBA_SAS_Port structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MS_SMHBA_SAS_Port
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# MS\_SMHBA\_SAS\_Port structure

The MS\_SMHBA\_SAS\_Port structure is used to report the SAS port information.

## Syntax


```C++
typedef struct _MS_SMHBA_SAS_Port {
  ULONG PortProtocol;
  UCHAR LocalSASAddress[8];
  UCHAR AttachedSASAddress[8];
  ULONG NumberofDiscoveredPorts;
  ULONG NumberofPhys;
} MS_SMHBA_SAS_Port, *PMS_SMHBA_SAS_Port;
```



## Members

<dl> <dt>

**PortProtocol**
</dt> <dd>

The protocols that are supported by this SAS port.

</dd> <dt>

**LocalSASAddress**
</dt> <dd>

The Port\_Identifier of this SAS port

</dd> <dt>

**AttachedSASAddress**
</dt> <dd>

The SAS address of the entity that is at the opposite end of the SAS link from this local SAS port.

</dd> <dt>

**NumberofDiscoveredPorts**
</dt> <dd>

The number of end ports that are visible to the local SAS port. The discovered ports might also include SMP ports that are contained within SAS expander devices.

</dd> <dt>

**NumberofPhys**
</dt> <dd>

The number of physical ports that are associated with this SAS port. If the value is more than one, this SAS port is considered to be a wide port.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MS_SMHBA_SAS_Port%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





