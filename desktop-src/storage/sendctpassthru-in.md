---
title: SendCTPassThru\_IN structure
description: The SendCTPassThru\_IN structure is used to deliver input parameter data to the SendCTPassThru WMI method.
ms.assetid: '5a3e06f5-f7f7-4e89-b78e-d6658c34ba9e'
keywords: ["SendCTPassThru_IN structure Storage Devices", "PSendCTPassThru_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- SendCTPassThru_IN
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# SendCTPassThru\_IN structure

The SendCTPassThru\_IN structure is used to deliver input parameter data to the [**SendCTPassThru**](https://msdn.microsoft.com/library/windows/hardware/ff565409) WMI method.

## Syntax


```C++
typedef struct _SendCTPassThru_IN {
  UCHAR PortWWN[8];
  ULONG RequestBufferCount;
  UCHAR RequestBuffer[1];
} SendCTPassThru_IN, *PSendCTPassThru_IN;
```



## Members

<dl> <dt>

**PortWWN**
</dt> <dd>

Contains a worldwide name for the HBA through which the target is accessed.

</dd> <dt>

**RequestBufferCount**
</dt> <dd>

Indicates the size in bytes of the buffer that will hold the results of the common transport command.

</dd> <dt>

**RequestBuffer**
</dt> <dd>

Contains the results of the common transport command.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SendCTPassThru\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SendCTPassThru**](https://msdn.microsoft.com/library/windows/hardware/ff565409)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SendCTPassThru_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






