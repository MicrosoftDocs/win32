---
title: MSiSCSI\_QueryLBPolicy structure
description: This MSiSCSI\_QueryLBPolicy method returns the MCS load balancing policy for each information if any that has been set across different iSCSI session.
ms.assetid: da45810a-12f2-4242-8428-a1717ecf8af3
keywords:
- MSiSCSI_QueryLBPolicy structure Storage Devices
- PMSiSCSI_QueryLBPolicy structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSiSCSI_QueryLBPolicy
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

# MSiSCSI\_QueryLBPolicy structure

This MSiSCSI\_QueryLBPolicy method returns the MCS load balancing policy for each information if any that has been set across different iSCSI session.

## Syntax


```C++
typedef struct _MSiSCSI_QueryLBPolicy {
  ULONGLONG                   UniqueAdapterId;
  ULONG                       Reserved;
  ULONG                       SessionCount;
  ISCSI_Supported_LB_Policies LoadBalancePolicies[1];
} MSiSCSI_QueryLBPolicy, *PMSiSCSI_QueryLBPolicy;
```



## Members

<dl> <dt>

**UniqueAdapterId**
</dt> <dd>

This is a unique connection identifier that the initiator uses to identify a connection. The [LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599) and [AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121) methods both return this value in the UniqueConnectionId parameter.

</dd> <dt>

**Reserved**
</dt> <dd>

Reserved for Microsoft use only.

</dd> <dt>

**SessionCount**
</dt> <dd>

This specifies the number of active sessions for this adapater ID.

</dd> <dt>

**LoadBalancePolicies**
</dt> <dd>

This is an enumeration that contains information required to set the load balance policy. For more information about how to set the load balance policy, see [**ISCSI\_Supported\_LB\_Policies**](iscsi-supported-lb-policies.md). There will be as many of these structures as the number of sessions available for this adapter.

</dd> </dl>

## Remarks

You must implement this class only if the adapter supports MCS. Otherwise, it is optional.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Iscsimgt.h (include Iscsimgt.h)</dt> </dl> |



## See also

<dl> <dt>

[AddConnectionToSession](https://msdn.microsoft.com/library/windows/hardware/ff550121)
</dt> <dt>

[**ISCSI\_Supported\_LB\_Policies**](iscsi-supported-lb-policies.md)
</dt> <dt>

[LoginToTarget](https://msdn.microsoft.com/library/windows/hardware/ff561599)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSiSCSI_QueryLBPolicy%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






