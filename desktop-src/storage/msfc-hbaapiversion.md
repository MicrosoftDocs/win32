---
title: MSFC\_HbaApiVersion structure
description: The MSFC\_HbaApiVersion structure contains information about the HBA version that a miniport driver supports.
ms.assetid: cab3e40d-585b-4d66-87ed-3dc7fdebf36d
keywords:
- MSFC_HbaApiVersion structure Storage Devices
- PMSFC_HbaApiVersion structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSFC_HbaApiVersion
api_location:
- Hbapiwmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MSFC\_HbaApiVersion structure

The MSFC\_HbaApiVersion structure contains information about the HBA version that a miniport driver supports.

## Syntax


```C++
typedef struct _MSFC_HbaApiVersion {
  uint32 WmiHbaApiVersion;
  uint32 HbaApiVersion;
  string Description;
} MSFC_HbaApiVersion, *PMSFC_HbaApiVersion;
```



## Members

<dl> <dt>

**WmiHbaApiVersion**
</dt> <dd>

The version information that the WMI provider supports.

</dd> <dt>

**HbaApiVersion**
</dt> <dd>

The version that the miniport driver supports.

</dd> <dt>

**Description**
</dt> <dd>

The description of the HBA.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_HbaApiVersion%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





