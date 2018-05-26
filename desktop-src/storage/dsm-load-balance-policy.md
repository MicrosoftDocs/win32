---
title: DSM\_Load\_Balance\_Policy structure
description: The DSM\_Load\_Balance\_Policy structure is used to represent a load balance policy that is applied to a LUN.
ms.assetid: 4338e496-99e8-47d2-ba97-ce661c9cb025
keywords:
- DSM_Load_Balance_Policy structure Storage Devices
- PDSM_Load_Balance_Policy structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DSM_Load_Balance_Policy
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

# DSM\_Load\_Balance\_Policy structure

The DSM\_Load\_Balance\_Policy structure is used to represent a load balance policy that is applied to a LUN.

## Syntax


```C++
typedef struct _DSM_Load_Balance_Policy {
  ULONG         Version;
  ULONG         LoadBalancePolicy;
  ULONG         DSMPathCount;
  ULONG         Reserved;
  MPIO_DSM_Path DSM_Paths[1];
} DSM_Load_Balance_Policy, *PDSM_Load_Balance_Policy;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of WMI class supported. Set to 1.

</dd> <dt>

**LoadBalancePolicy**
</dt> <dd>

An unsigned 32-bitfield that represents the load balance policy type that is currently being applied to the LUN if the LUN is queried, or the new policy to apply to the LUN if the LUN is being set.

</dd> <dt>

**DSMPathCount**
</dt> <dd>

An unsigned 32-bitfield that represents the number of paths that expose the LUN's instances.

</dd> <dt>

**Reserved**
</dt> <dd>

Should be zero.

</dd> <dt>

**DSM\_Paths**
</dt> <dd>

An array of MPIO\_DSM\_Path structures that represent path attributes for each of the LUN's instances.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DSM_Load_Balance_Policy%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





