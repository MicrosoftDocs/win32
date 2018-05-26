---
title: MS\_SMHBA\_FC\_PHY structure
description: The MS\_SMHBA\_FC\_PHY structure is used to report the physical attributes of a fibre channel port.
ms.assetid: 7fb199b6-dcdb-41fc-b1c4-4eef2177018e
keywords:
- MS_SMHBA_FC_PHY structure Storage Devices
- PMS_SMHBA_FC_PHY structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MS_SMHBA_FC_PHY
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MS\_SMHBA\_FC\_PHY structure

The MS\_SMHBA\_FC\_PHY structure is used to report the physical attributes of a fibre channel port.

## Syntax


```C++
typedef struct _MS_SMHBA_FC_PHY {
  ULONG PhySupportSpeed;
  ULONG PhySpeed;
  UCHAR PhyType;
  ULONG MaxFrameSize;
} MS_SMHBA_FC_PHY, *PMS_SMHBA_FC_PHY;
```



## Members

<dl> <dt>

**PhySupportSpeed**
</dt> <dd>

The signaling bit rates at which the port can operate. For a list of the values that this member supports, see PhySpeed.

</dd> <dt>

**PhySpeed**
</dt> <dd>

The signaling bit rates at which PortWWN is currently operating. This member must have one of the values in the following table.



|                                            |                                                                                    |
|--------------------------------------------|------------------------------------------------------------------------------------|
| **Value**<br/>                       | **Meaning**<br/>                                                             |
| HBA\_PORTSPEED\_UNKNOWN<br/>         | Speed unknown. The transceiver is incapable of reporting the speed. <br/>    |
| HBA\_PORTSPEED\_1GBIT<br/>           | 1 gigabit per sec.<br/>                                                      |
| HBA\_PORTSPEED\_2GBIT<br/>           | 2 gigabits per sec.<br/>                                                     |
| HBA\_PORTSPEED\_10GBIT<br/>          | 10 gigabits per sec.<br/>                                                    |
| HBA\_PORTSPEED\_4GBIT<br/>           | 4 gigabits per sec.<br/>                                                     |
| HBA\_PORTSPEED\_NOT\_NEGOTIATED<br/> | The speed at which the port will operate has not yet been established. <br/> |



 

</dd> <dt>

**PhyType**
</dt> <dd>

The port type. This member must have one of the values in the following table.



|                                      |                                            |
|--------------------------------------|--------------------------------------------|
| **Value**<br/>                 | **Meaning**<br/>                     |
| HBA\_PORTTYPE\_UNKNOWN<br/>    | Unknown port type. <br/>             |
| HBA\_PORTTYPE\_OTHER<br/>      | Value that is not a port type. <br/> |
| HBA\_PORTTYPE\_NOTPRESENT<br/> | Port not present.<br/>               |
| HBA\_PORTTYPE\_NPORT<br/>      | Fabric. <br/>                        |
| HBA\_PORTTYPE\_NLPORT<br/>     | Public loop.<br/>                    |
| HBA\_PORTTYPE\_FLPORT<br/>     | Fabric on a loop. <br/>              |
| HBA\_PORTTYPE\_FPORT<br/>      | Fabric port. <br/>                   |
| HBA\_PORTTYPE\_EPORT<br/>      | Fabric expansion port. <br/>         |
| HBA\_PORTTYPE\_GPORT<br/>      | Generic fabric. <br/>                |
| HBA\_PORTTYPE\_LPORT<br/>      | Private loop port. <br/>             |
| HBA\_PORTTYPE\_PTP<br/>        | Point to point. <br/>                |



 

</dd> <dt>

**MaxFrameSize**
</dt> <dd>

The maximum frame size, in bytes, that is supported by PortWWN.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MS_SMHBA_FC_PHY%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





