---
title: SendRNIDV2\_OUT structure
description: The SendRNIDV2\_OUT structure is used to report the output parameter data of the SendRNIDV2 WMI method to the WMI client.
ms.assetid: '2d8f1b49-5add-4dd9-998f-d0c1e79f3e7d'
keywords: ["SendRNIDV2_OUT structure Storage Devices", "PSendRNIDV2_OUT structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SendRNIDV2_OUT
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# SendRNIDV2\_OUT structure

The SendRNIDV2\_OUT structure is used to report the output parameter data of the [**SendRNIDV2**](https://msdn.microsoft.com/library/windows/hardware/ff565463) WMI method to the WMI client.

## Syntax


```C++
typedef struct _SendRNIDV2_OUT {
  ULONG HBAStatus;
  ULONG TotalRspBufferSize;
  ULONG ActualRspBufferSize;
  UCHAR RspBuffer[1];
} SendRNIDV2_OUT, *PSendRNIDV2_OUT;
```



## Members

<dl> <dt>

**HBAStatus**
</dt> <dd>

Contains the status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233).

</dd> <dt>

**TotalRspBufferSize**
</dt> <dd>

Contains the size in bytes of the results of the version 2 request node identification data (RNIDV2) command.

</dd> <dt>

**ActualRspBufferSize**
</dt> <dd>

Contains the size in bytes of the data that was actually retrieved.

</dd> <dt>

**RspBuffer**
</dt> <dd>

Contains the results of the RNIDV2 command.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SendRNIDV2\_OUT structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SendRNIDV2**](https://msdn.microsoft.com/library/windows/hardware/ff565463)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SendRNIDV2_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






