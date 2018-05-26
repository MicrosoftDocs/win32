---
title: SM\_SendSMPPassThru\_OUT structure
description: The SM\_SendSMPPassThru\_OUT structure is used to receive output parameters from the SM\_SendSMPPassThru method.
ms.assetid: eb173171-3990-405e-b740-8c1a0c915165
keywords:
- SM_SendSMPPassThru_OUT structure Storage Devices
- PSM_SendSMPPassThru_OUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SM_SendSMPPassThru_OUT
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

# SM\_SendSMPPassThru\_OUT structure

The SM\_SendSMPPassThru\_OUT structure is used to receive output parameters from the SM\_SendSMPPassThru method.

## Syntax


```C++
typedef struct _SM_SendSMPPassThru_OUT {
  ULONG HBAStatus;
  ULONG TotalRespBufferSize;
  ULONG OutRespBufferSize;
  UCHAR RespBuffer[1];
} SM_SendSMPPassThru_OUT, *PSM_SendSMPPassThru_OUT;
```



## Members

<dl> <dt>

**HBAStatus**
</dt> <dd>

The status of the operation. For a list of allowed values and their descriptions, see [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233).

</dd> <dt>

**TotalRespBufferSize**
</dt> <dd>

The size, in bytes, of the results common transport (CT) command.

</dd> <dt>

**OutRespBufferSize**
</dt> <dd>

The size, in bytes, of the data that was actually retrieved.

</dd> <dt>

**RespBuffer**
</dt> <dd>

The results of the common transport command.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SM\_SendSMPPassThru\_OUT structure in *Hbapiwmi.h* when it compiles the MS\_SM\_FabricAndDomainManagementMethod WMI class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SM_SendSMPPassThru_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





