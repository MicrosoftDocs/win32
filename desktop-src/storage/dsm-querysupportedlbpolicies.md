---
title: DSM\_QuerySupportedLBPolicies structure
description: The DSM\_QuerySupportedLBPolicies structure is used to query the list of load balance policies that are supported on the LUN.
ms.assetid: c9c04601-783a-454d-a80e-be8aa5df519a
keywords:
- DSM_QuerySupportedLBPolicies structure Storage Devices
- PDSM_QuerySupportedLBPolicies structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DSM_QuerySupportedLBPolicies
api_location:
- mpiodisk.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DSM\_QuerySupportedLBPolicies structure

The DSM\_QuerySupportedLBPolicies structure is used to query the list of load balance policies that are supported on the LUN.

## Syntax


```C++
typedef struct _DSM_QuerySupportedLBPolicies {
  ULONG                   SupportedLBPoliciesCount;
  ULONG                   Reserved;
  DSM_Load_Balance_Policy Supported_LB_Policies[1];
} DSM_QuerySupportedLBPolicies, *PDSM_QuerySupportedLBPolicies;
```



## Members

<dl> <dt>

**SupportedLBPoliciesCount**
</dt> <dd>

An unsigned 32-bitfield that returns the number of policies that are supported for the LUN by the controlling DSM.

</dd> <dt>

**Reserved**
</dt> <dd>

Should be zero.

</dd> <dt>

**Supported\_LB\_Policies**
</dt> <dd>

An array of DSM\_Load\_Balance\_Policy structures, one for each of the supported load balance policies. The number of array elements will be the same as *SupportedLBPoliciesCount*. Each element of the array lists only the supported load balance policy type.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DSM_QuerySupportedLBPolicies%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





