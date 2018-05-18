---
title: ISCSI\_Supported\_LB\_Policies structure
description: The ISCSI\_Supported\_LB\_Policies structure contains information about load balancing policies for multiple connections per session (MCS).
ms.assetid: '053b9f14-7319-4599-886e-3c03c717b348'
keywords: ["ISCSI_Supported_LB_Policies structure Storage Devices", "PISCSI_Supported_LB_Policies structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- ISCSI_Supported_LB_Policies
api_location:
- iscsimgt.h
api_type:
- HeaderDef
---

# ISCSI\_Supported\_LB\_Policies structure

The ISCSI\_Supported\_LB\_Policies structure contains information about load balancing policies for multiple connections per session (MCS).

## Syntax


```C++
typedef struct _ISCSI_Supported_LB_Policies {
  ULONGLONG  UniqueSessionId;
  ULONG      LoadBalancePolicy;
  ULONG      iSCSI_PathCount;
  ISCSI_Path iSCSI_Paths[1];
} ISCSI_Supported_LB_Policies, *PISCSI_Supported_LB_Policies;
```



## Members

<dl> <dt>

**UniqueSessionId**
</dt> <dd>

A 64-bit integer that uniquely identifies the session. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in their UniqueSessionId parameter. Do not confuse this value with the values in the ISID and TSID members.

</dd> <dt>

**LoadBalancePolicy**
</dt> <dd>

This specifies the type of load balance policy that has been established on a multiconnection session.



| Type                                               | Meaning                                                                                                                                                                         |
|----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSiSCSI\_LB\_FAILOVER<br/>                   | An alternate path is used only for failover.<br/>                                                                                                                         |
| MSiSCSI\_LB\_ROUND\_ROBIN<br/>               | I/O operations are scheduled to all active paths in a round-robin fashion.<br/>                                                                                           |
| MSiSCSI\_LB\_ROUND\_ROBIN\_WITH\_SUBSET<br/> | I/O operations are scheduled to all paths within a subset in a round-robin fashion.<br/>                                                                                  |
| MSiSCSI\_LB\_DYN\_LEAST\_QUEUE\_DEPTH<br/>   | I/O operations are balanced across a set of paths based on the least queue depth mechanism (I/O is scheduled to the path with the fewest pending I/Os in its queue).<br/> |
| MSiSCSI\_LB\_WEIGHTED\_PATHS<br/>            | I/O operations are scheduled based on the weights assigned to a path by an administrator.<br/>                                                                            |
| MSiSCSI\_LB\_VENDOR\_SPECIFIC<br/>           | Vendor-specific I/O policies are in effect.<br/>                                                                                                                          |



 

</dd> <dt>

**iSCSI\_PathCount**
</dt> <dd>

The number of paths associated with a target in the context of this session.

</dd> <dt>

**iSCSI\_Paths**
</dt> <dd>

Path information as shown in the [**ISCSI\_Path**](iscsi-path.md) structure.

</dd> </dl>

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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20ISCSI_Supported_LB_Policies%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






