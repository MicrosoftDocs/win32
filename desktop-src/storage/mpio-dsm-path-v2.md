---
title: MPIO\_DSM\_Path\_V2 structure
description: The MPIO\_DSM\_Path\_V2 structure is used to represent the DSM's definition of a path. It is a superset of the previously existing MPIO\_DSM\_Path class.
ms.assetid: '8ebbb4c0-c761-42a5-a41a-9d661a6126d9'
keywords: ["MPIO_DSM_Path_V2 structure Storage Devices", "PMPIO_DSM_Path_V2 structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MPIO_DSM_Path_V2
api_location:
- mpiodisk.h
api_type:
- HeaderDef
---

# MPIO\_DSM\_Path\_V2 structure

The MPIO\_DSM\_Path\_V2 structure is used to represent the DSM's definition of a path. It is a superset of the previously existing MPIO\_DSM\_Path class.

## Syntax


```C++
typedef struct _MPIO_DSM_Path_V2 {
  ULONGLONG DsmPathId;
  ULONGLONG Reserved;
  ULONG     PathWeight;
  ULONG     PrimaryPath;
  ULONG     OptimizedPath;
  ULONG     PreferredPath;
  ULONG     FailedPath;
  ULONG     TargetPortGroup_State;
  ULONG     ALUASupport;
  UCHAR     SymmetricLUA;
  UCHAR     TargetPortGroup_Preferred;
  USHORT    TargetPortGroup_Identifier;
  ULONG     TargetPort_Identifier;
  ULONG     Reserved32;
  ULONGLONG Reserved64;
} MPIO_DSM_Path_V2, *PMPIO_DSM_Path_V2;
```



## Members

<dl> <dt>

**DsmPathId**
</dt> <dd>

An unsigned 64-bitfield that is used as a unique identifier to distinguish paths known to the DSM.

</dd> <dt>

**Reserved**
</dt> <dd>

Should be zero.

</dd> <dt>

**PathWeight**
</dt> <dd>

An unsigned 32-bitfield that holds the weight associated with the given path.

</dd> <dt>

**PrimaryPath**
</dt> <dd>

An unsigned 32-bitfield that is used as a flag to indicate the path state when accessing a particular LUN.

</dd> <dt>

**OptimizedPath**
</dt> <dd>

An unsigned 32-bitfield that is used in conjunction with *PrimaryPath* to indicate the path state for accessing a LUN.

</dd> <dt>

**PreferredPath**
</dt> <dd>

An unsigned 32-bitfield that is used as a flag to indicate whether this is the preferred path for accessing the LUN.

</dd> <dt>

**FailedPath**
</dt> <dd>

A 32-bit unsigned field that is used as a flag to indicate if the path has failed.

</dd> <dt>

**TargetPortGroup\_State**
</dt> <dd>

An unsigned 32-bitfield that is used to indicate the access state of the target port group to which this instance of the LUN belongs.

</dd> <dt>

**ALUASupport**
</dt> <dd>

An unsigned 32-bitfield that returns the Asymmetrical Logical Unit Access (ALUA) state transition support that is indicated by the LUN.

</dd> <dt>

**SymmetricLUA**
</dt> <dd>

An unsigned 8-bitfield that is used as a flag to indicate to the application if logical unit access is symmetric.

</dd> <dt>

**TargetPortGroup\_Preferred**
</dt> <dd>

An unsigned 8-bitfield that is used as a flag. This field indicates if the LUN's target port group that corresponds to this path is preferred for the LUN access.

</dd> <dt>

**TargetPortGroup\_Identifier**
</dt> <dd>

An unsigned 16-bitfield that contains the identifier of the LUN's target port group that corresponds to this path.

</dd> <dt>

**TargetPort\_Identifier**
</dt> <dd>

An unsigned 32-bitfield that contains the identifier of the target port that corresponds to this path through which the LUN has been exposed.

</dd> <dt>

**Reserved32**
</dt> <dd>

Should be zero.

</dd> <dt>

**Reserved64**
</dt> <dd>

Should be zero.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_DSM_Path_V2%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





