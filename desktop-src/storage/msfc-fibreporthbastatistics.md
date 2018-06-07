---
title: MSFC\_FibrePortHBAStatistics structure
description: The MSFC\_FibrePortHBAStatistics structure is used by an HBA miniport driver that is a WMI provider to report statistics related to a fibre channel port.
ms.assetid: 8b365e7a-6d52-417f-8c0b-78feac24602f
keywords:
- MSFC_FibrePortHBAStatistics structure Storage Devices
- PMSFC_FibrePortHBAStatistics structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MSFC_FibrePortHBAStatistics
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MSFC\_FibrePortHBAStatistics structure

The MSFC\_FibrePortHBAStatistics structure is used by an HBA miniport driver that is a WMI provider to report statistics related to a fibre channel port.

## Syntax


```C++
typedef struct _MSFC_FibrePortHBAStatistics {
  ULONGLONG              UniquePortId;
  ULONG                  HBAStatus;
  MSFC_HBAPortStatistics Statistics;
} MSFC_FibrePortHBAStatistics, *PMSFC_FibrePortHBAStatistics;
```



## Members

<dl> <dt>

**UniquePortId**
</dt> <dd>

Contains a unique identifier for the port.

</dd> <dt>

**HBAStatus**
</dt> <dd>

Contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233).

</dd> <dt>

**Statistics**
</dt> <dd>

Contains a structure of type [**MSFC\_HBAPortStatistics**](msfc-hbaportstatistics.md) with statistical information about the port.

</dd> </dl>

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[MSFC\_FibrePortHBAStatistics WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562505)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MSFC_FibrePortHBAStatistics%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






