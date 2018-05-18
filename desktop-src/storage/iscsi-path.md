---
title: ISCSI\_Path structure
description: The ISCSI\_Path structure contains information about a connection of the iSCSI portal.
ms.assetid: 'eebc3e2e-41fe-4087-8916-7c8a71929913'
keywords: ["ISCSI_Path structure Storage Devices", "PISCSI_Path structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_Path
api_location:
- iscsimgt.h
api_type:
- HeaderDef
---

# ISCSI\_Path structure

The ISCSI\_Path structure contains information about a connection of the iSCSI portal.

## Syntax


```C++
typedef struct _ISCSI_Path {
  ULONGLONG UniqueConnectionId;
  ULONGLONG EstimatedLinkSpeed;
  ULONG     PathWeight;
  ULONG     PrimaryPath;
  ULONG     ConnectionStatus;
  ULONG     TCPOffLoadAvailable;
} ISCSI_Path, *PISCSI_Path;
```



## Members

<dl> <dt>

**UniqueConnectionId**
</dt> <dd>

This is a unique connection identifier that the initiator uses to identify a connection. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in the UniqueConnectionId parameter. This value is not to be confused with the connection ID (CID).

</dd> <dt>

**EstimatedLinkSpeed**
</dt> <dd>

This specifies the connection speed in megabits per second (Mbps).

</dd> <dt>

**PathWeight**
</dt> <dd>

This specifies the weight assigned to this path. The value can be any 32-bit number, with a higher number that signifies a higher priority. If more than one path is available, this path weight value is compared against each other path weight and will be prioritized accordingly. For example, if a value of 1 is used for path1 and a value of 2 for path2, path2 has higher priority.

</dd> <dt>

**PrimaryPath**
</dt> <dd>

This specifies the state of the path: primary or secondary. If the value is 1, it means the path is the primary path, and if it is 0, it is a secondary path.

</dd> <dt>

**ConnectionStatus**
</dt> <dd>

This indicates the status of the connection.



| Type                                           | Meaning                                      |
|------------------------------------------------|----------------------------------------------|
| CONNECTION\_STATE\_CONNECTED (1)<br/>    | The path is connected and active.<br/> |
| CONNECTION\_STATE\_DISCONNECTED (2)<br/> | The path is disconnected.<br/>         |
| CONNECTION\_STATE\_RECONNECTING(3)<br/>  | The path is reconnecting.<br/>         |



 

</dd> <dt>

**TCPOffLoadAvailable**
</dt> <dd>

This indicates whether the connection supports TCP offload or not.

</dd> </dl>

## Remarks

The iSCSI headers and MOF are included in the platform SDK and WDK.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_Path%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






