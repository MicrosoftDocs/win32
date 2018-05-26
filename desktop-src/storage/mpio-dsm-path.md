---
title: MPIO\_DSM\_Path structure
description: The MPIO\_DSM\_Path structure is used to represent the DSMs definition of a path.
ms.assetid: 17338526-d682-4d11-89b9-730b1a275870
keywords:
- MPIO_DSM_Path structure Storage Devices
- PMPIO_DSM_Path structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MPIO_DSM_Path
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

# MPIO\_DSM\_Path structure

The MPIO\_DSM\_Path structure is used to represent the DSM's definition of a path.

## Syntax


```C++
typedef struct _MPIO_DSM_Path {
  ULONGLONG DsmPathId;
  ULONGLONG Reserved;
  ULONG     PathWeight;
  ULONG     PrimaryPath;
} MPIO_DSM_Path, *PMPIO_DSM_Path;
```



## Members

<dl> <dt>

**DsmPathId**
</dt> <dd>

An unsigned 64-bitfield that is used as a unique identifier to distinguish paths that are known to the DSM.

</dd> <dt>

**Reserved**
</dt> <dd>

Should be zero.

</dd> <dt>

**PathWeight**
</dt> <dd>

An unsigned 32-bitfield that holds the weight associated with the given path. The assigned value determines the order in which the DSM will pick the paths if the load balance policy is set to Weighted Path. This means that a user can assign weights to each path that is available for a device and if the Load Balance Policy for the device is set as "Weighted Path," MPIO uses this PathWeight value to determine which path to use.

</dd> <dt>

**PrimaryPath**
</dt> <dd>

An unsigned 32-bitfield that is used as a flag to indicate the path state when accessing a particular LUN.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_DSM_Path%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





