---
title: SendRNIDV2\_IN structure
description: The SendRNIDV2\_IN structure is used to deliver input parameter data to the SendRNIDV2 WMI method.
ms.assetid: b9c0833d-96ac-41cb-815f-b2df27f46cb4
keywords:
- SendRNIDV2_IN structure Storage Devices
- PSendRNIDV2_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SendRNIDV2_IN
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

# SendRNIDV2\_IN structure

The SendRNIDV2\_IN structure is used to deliver input parameter data to the [**SendRNIDV2**](https://msdn.microsoft.com/library/windows/hardware/ff565463) WMI method.

## Syntax


```C++
typedef struct _SendRNIDV2_IN {
  UCHAR PortWWN[8];
  UCHAR DestWWN[8];
  ULONG DestFCID;
  ULONG NodeIdDataFormat;
} SendRNIDV2_IN, *PSendRNIDV2_IN;
```



## Members

<dl> <dt>

**PortWWN**
</dt> <dd>

Contains a worldwide name for the local port through which the version 2 request node identification data (RNIDV2) command is sent.

</dd> <dt>

**DestWWN**
</dt> <dd>

Contains a worldwide name for the destination port.

</dd> <dt>

**DestFCID**
</dt> <dd>

Contains an address identifier of the destination port. For a description of the values that this member can have, see the T11 committee's specification for *Fibre Channel HBA API*.

</dd> <dt>

**NodeIdDataFormat**
</dt> <dd>

Indicates the node identification data format. For a description of the values that this member can have, see the T11 committee's specification for *Fibre Channel HBA API*.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SendRNIDV2\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SendRNIDV2**](https://msdn.microsoft.com/library/windows/hardware/ff565463)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SendRNIDV2_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






