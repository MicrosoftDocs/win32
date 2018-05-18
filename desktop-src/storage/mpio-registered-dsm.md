---
title: MPIO\_REGISTERED\_DSM structure
description: The MPIO\_REGISTERED\_DSM structure represents the top-level view of the registered DSMs on the system. To query this information, the request must be sent to the MPIO control object by using its WMI instance name.
ms.assetid: 'c1be07b7-ebce-422f-83f2-890adc71655b'
keywords: ["MPIO_REGISTERED_DSM structure Storage Devices", "PMPIO_REGISTERED_DSM structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- MPIO_REGISTERED_DSM
api_location:
- mpiowmi.h
api_type:
- HeaderDef
---

# MPIO\_REGISTERED\_DSM structure

The MPIO\_REGISTERED\_DSM structure represents the top-level view of the registered DSMs on the system. To query this information, the request must be sent to the MPIO control object by using its WMI instance name.

## Syntax


```C++
typedef struct _MPIO_REGISTERED_DSM {
  ULONG          NumberDSMs;
  DSM_PARAMETERS DsmParameters[1];
} MPIO_REGISTERED_DSM, *PMPIO_REGISTERED_DSM;
```



## Members

<dl> <dt>

**NumberDSMs**
</dt> <dd>

An unsigned 32-bitfield that specifies the number of DSMs that are registered in the system.

</dd> <dt>

**DsmParameters**
</dt> <dd>

An array that returns information about each of the registered DSMs. The number of elements in the array is given by *NumberDSMs* and each element is an instance of the DSM\_PARAMETERS structure.

</dd> </dl>

## Requirements



|                   |                                                                                                          |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Mpiowmi.h (include Mpiowmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MPIO_REGISTERED_DSM%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





