---
title: GetFCPStatistics\_IN structure
description: The GetFCPStatistics\_IN structure is used to deliver input parameter data to the GetFCPStatistics WMI method.
ms.assetid: 'f6cb4532-fc66-45e7-a779-0981465d69fc'
keywords: ["GetFCPStatistics_IN structure Storage Devices", "PGetFCPStatistics_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- GetFCPStatistics_IN
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# GetFCPStatistics\_IN structure

The GetFCPStatistics\_IN structure is used to deliver input parameter data to the [**GetFCPStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff554939) WMI method.

## Syntax


```C++
typedef struct _GetFCPStatistics_IN {
  HBAScsiID ScsiId;
} GetFCPStatistics_IN, *PGetFCPStatistics_IN;
```



## Members

<dl> <dt>

**ScsiId**
</dt> <dd>

Contains a structure of type [**HBAScsiID**](hbascsiid.md) that uniquely identifies a logical unit and the bus and HBA that the logical unit is connected to.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the GetFCPStatistics\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetFCPStatistics**](https://msdn.microsoft.com/library/windows/hardware/ff554939)
</dt> <dt>

[**HBAScsiID**](hbascsiid.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GetFCPStatistics_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






