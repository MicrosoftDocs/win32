---
title: DSM\_QueryUniqueId structure
description: The DSM\_QueryUniqueId structure is used to query the DSM for a unique identifier.
ms.assetid: 023390a1-e878-4f1f-a5c2-1545a6786aaa
keywords:
- DSM_QueryUniqueId structure Storage Devices
- PDSM_QueryUniqueId structure pointer Storage Devices
topic_type:
- apiref
api_name:
- DSM_QueryUniqueId
api_location:
- mpiodisk.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# DSM\_QueryUniqueId structure

The DSM\_QueryUniqueId structure is used to query the DSM for a unique identifier. This unique identifier can be used together with the DsmPathId to create a 128-bit identifier for a path that is unique among all paths, as well as all DSMs, that are known to a management application. This is especially useful if the management application is managing devices that are spread across various systems. To query for this 64-bit unique identifier, the application must target the request to a pseudo-LUN that is addressed by its WMI instance name. This class is mandatory for any DSM that supports VDS.

## Syntax


```C++
typedef struct _DSM_QueryUniqueId {
  ULONGLONG DsmUniqueId;
} DSM_QueryUniqueId, *PDSM_QueryUniqueId;
```



## Members

<dl> <dt>

**DsmUniqueId**
</dt> <dd>

An unsigned 64-bitfield that represents an identifier that must be set by DSMs that want management applications, such as VDS, to be able to manage the devices that are controlled by the particular DSM. This structure is used together with the DsmPathId structure to create a 128-bit identifier that is unique, not just among all the paths that are known to this DSM, but also among all the DSMs that are present in the system.

</dd> </dl>

## Requirements



|                   |                                                                                                           |
|-------------------|-----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiodisk.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DSM_QueryUniqueId%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





