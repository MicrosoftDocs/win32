---
title: SendLIRR\_IN structure
description: The SendLIRR\_IN structure is used to deliver parameter data to the SendLIRR WMI method.
ms.assetid: 774acafb-c929-483a-82b0-2a358054dc7f
keywords:
- SendLIRR_IN structure Storage Devices
- PSendLIRR_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SendLIRR_IN
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# SendLIRR\_IN structure

The SendLIRR\_IN structure is used to deliver parameter data to the [**SendLIRR**](https://msdn.microsoft.com/library/windows/hardware/ff565419) WMI method.

## Syntax


```C++
typedef struct _SendLIRR_IN {
  UCHAR SourceWWN[8];
  UCHAR DestWWN[8];
  UCHAR Function;
  UCHAR Type;
} SendLIRR_IN, *PSendLIRR_IN;
```



## Members

<dl> <dt>

**SourceWWN**
</dt> <dd>

Contains a worldwide name for the local port through which the link incident record registration (LIRR) command is sent.

</dd> <dt>

**DestWWN**
</dt> <dd>

Contains a worldwide name for the destination port.

</dd> <dt>

**Function**
</dt> <dd>

Contains the code that identifies which registration function is to be performed. For an explanation of which values can be assigned to this member, see the T11 committee's *Fibre Channel Framing and Signaling* specification.

</dd> <dt>

**Type**
</dt> <dd>

Indicates the device type for which link information is requested. For an explanation of which values can be assigned to this member, see the T11 committee's *Fibre Channel Framing and Signaling* specification.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SendLIRR\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SendLIRR**](https://msdn.microsoft.com/library/windows/hardware/ff565419)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SendLIRR_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






