---
title: DSM\_Load\_Balance\_Policy\_V2 structure
description: The DSM\_Load\_Balance\_Policy\_V2 structure is used to represent a load balance policy that is applied to a LUN.
ms.assetid: 'b1522320-110c-46dc-be50-df7c05d61351'
keywords: ["DSM_Load_Balance_Policy_V2 structure Storage Devices", "PDSM_Load_Balance_Policy_V2 structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- DSM_Load_Balance_Policy_V2
api_location:
- mpiodisk.h
api_type:
- HeaderDef
---

# DSM\_Load\_Balance\_Policy\_V2 structure

The DSM\_Load\_Balance\_Policy\_V2 structure is used to represent a load balance policy that is applied to a LUN. It is similar to the DSM\_Load\_Balance\_Policy structure, except that it uses the MPIO\_DSM\_Path\_V2 structure to capture and expose path information.

## Syntax


```C++
typedef struct _DSM_Load_Balance_Policy_V2 {
  ULONG            Version;
  ULONG            LoadBalancePolicy;
  ULONG            DSMPathCount;
  ULONG            Reserved;
  MPIO_DSM_Path_V2 DSM_Paths[1];
} DSM_Load_Balance_Policy_V2, *PDSM_Load_Balance_Policy_V2;
```



## Members

<dl> <dt>

**Version**
</dt> <dd>

The version of WMI class supported. Set to 2.

</dd> <dt>

**LoadBalancePolicy**
</dt> <dd>

An unsigned 32-bitfield that represents the load balance policy type that is currently being applied to the LUN if the LUN is being queried, or the new policy to apply to the LUN if the LUN is being set.

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

An array of MPIO\_DSM\_Path\_V2 structures that represent path attributes for each of the LUN's instances.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DSM_Load_Balance_Policy_V2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





