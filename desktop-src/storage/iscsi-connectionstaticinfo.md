---
title: ISCSI\_ConnectionStaticInfo structure
description: The ISCSI\_ConnectionStaticInfo structure contains information about the characteristics of an established connection.
ms.assetid: 14d4464e-d4e8-446c-8822-0b16c984313c
keywords:
- ISCSI_ConnectionStaticInfo structure Storage Devices
- PISCSI_ConnectionStaticInfo structure pointer Storage Devices
topic_type:
- apiref
api_name:
- ISCSI_ConnectionStaticInfo
api_location:
- iscsimgt.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISCSI\_ConnectionStaticInfo structure

The ISCSI\_ConnectionStaticInfo structure contains information about the characteristics of an established connection.

## Syntax


```C++
typedef struct _ISCSI_ConnectionStaticInfo {
  ULONGLONG        UniqueConnectionId;
  USHORT           CID;
  UCHAR            State;
  UCHAR            Protocol;
  UCHAR            HeaderIntegrity;
  UCHAR            DataIntegrity;
  USHORT           Reserved;
  ULONG            MaxRecvDataSegmentLength;
  ULONG            AuthType;
  ISCSI_IP_Address LocalAddr;
  ULONG            LocalPort;
  ISCSI_IP_Address RemoteAddr;
  ULONG            RemotePort;
  ULONGLONG        EstimatedThroughput;
  ULONG            MaxDatagramSize;
} ISCSI_ConnectionStaticInfo, *PISCSI_ConnectionStaticInfo;
```



## Members

<dl> <dt>

**UniqueConnectionId**
</dt> <dd>

The connection identifier (ID) that the operating system and application software use to uniquely identify the connection. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in the *UniqueConnectionId* parameter. Do not confuse this value with the connection ID (CID).

</dd> <dt>

**CID**
</dt> <dd>

The iSCSI connection ID (CID) for this connection instance. The iSCSI protocol uses this value to identify the connection.

</dd> <dt>

**State**
</dt> <dd>

The type of connection state. This member can have the following symbolic constant values, which are defined in *Iscsimgt.h*.



| State             | Meaning                                                                                                                                                                                   |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| login<br/>  | The TCP connection has been established, but the target still has not sent a valid logon response with the final bit set. <br/>                                                     |
| full<br/>   | The target has sent a valid logon response with the final bit set, and the connection is in the full feature phase. The initiator can send SCSI commands and data to targets. <br/> |
| logout<br/> | The initiator has sent a valid logoff command, but the connection has not yet been closed.<br/>                                                                                     |



 

</dd> <dt>

**Protocol**
</dt> <dd>

The transport protocol that is used to establish this connection instance. For a list of values that you can assign to this member, see [ISCSI\_CONNECTION\_PROTOCOL\_TYPE\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561494).

</dd> <dt>

**HeaderIntegrity**
</dt> <dd>

The name of the iSCSI header digest scheme that is associated with this connection session. This member can have the following symbolic constant values, which are defined in *Iscsimgt.h*.



| HeaderIntegrity   | Meaning                                               |
|-------------------|-------------------------------------------------------|
| None<br/>   | The session is not using a header digest. <br/> |
| crc32c<br/> | The session is using a 32-bit CRC digest.<br/>  |



 

</dd> <dt>

**DataIntegrity**
</dt> <dd>

The name of the iSCSI data digest scheme that is associated with this connection session. This member can have the following symbolic constant values, which are defined in *Iscsimgt.h*.



| HeaderIntegrity   | Meaning                                              |
|-------------------|------------------------------------------------------|
| None<br/>   | The session is not using a data digest. <br/>  |
| crc32c<br/> | The session is using a 32-bit CRC digest.<br/> |



 

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for Microsoft use only. You must set this member to 0.

</dd> <dt>

**MaxRecvDataSegmentLength**
</dt> <dd>

The maximum data payload size, in bytes, that is supported for command or data PDUs within this connection session.

</dd> <dt>

**AuthType**
</dt> <dd>

The type of authentication that is used to establish a connection. The [ISCSI\_ConnectionStaticInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561490), which is defined in *Mgmt.mof*, does specify values for this member; but if your software includes *Iscsidsc.h*, it can use the [**ISCSI\_AUTH\_TYPES**](iscsi-auth-types.md) enumeration to assign values to this member.

</dd> <dt>

**LocalAddr**
</dt> <dd>

A [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure that holds the IP address of the local network card that the initiator uses to connect to the network.

</dd> <dt>

**LocalPort**
</dt> <dd>

The local port number that this connection instance uses.

</dd> <dt>

**RemoteAddr**
</dt> <dd>

A [**ISCSI\_IP\_Address**](iscsi-ip-address.md) structure that holds the IP address of the remote network card that this connection instance uses.

</dd> <dt>

**RemotePort**
</dt> <dd>

The remote port number that the initiator used to make the connection.

</dd> <dt>

**EstimatedThroughput**
</dt> <dd>

The estimated throughput, in bytes per second, of the connection.

</dd> <dt>

**MaxDatagramSize**
</dt> <dd>

The maximum size, in bytes, of the datagram that the transport supports.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[**ISCSI\_AUTH\_TYPES**](iscsi-auth-types.md)
</dt> <dt>

[ISCSI\_CONNECTION\_PROTOCOL\_TYPE\_QUALIFIERS](https://msdn.microsoft.com/library/windows/hardware/ff561494)
</dt> <dt>

[ISCSI\_ConnectionStaticInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff561490)
</dt> <dt>

[**ISCSI\_IP\_Address**](iscsi-ip-address.md)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_ConnectionStaticInfo%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






