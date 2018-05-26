---
title: SM\_SendTEST\_IN structure
description: The SM\_SendTEST\_IN structure is used to provide input parameters to the SM\_SendTEST method.
ms.assetid: 5bb0620e-b271-4af6-b528-b904910b8a6c
keywords:
- SM_SendTEST_IN structure Storage Devices
- PSM_SendTEST_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SM_SendTEST_IN
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

# SM\_SendTEST\_IN structure

The SM\_SendTEST\_IN structure is used to provide input parameters to the SM\_SendTEST method.

## Syntax


```C++
typedef struct _SM_SendTEST_IN {
  UCHAR HbaPortWWN[8];
  UCHAR DestWWN[8];
  ULONG DestFCID;
  ULONG ReqBufferSize;
  UCHAR ReqBuffer[1];
} SM_SendTEST_IN, *PSM_SendTEST_IN;
```



## Members

<dl> <dt>

**HbaPortWWN**
</dt> <dd>

The local HBA port worldwide name (WWN).

</dd> <dt>

**DestWWN**
</dt> <dd>

The remote HBA port worldwide name (WWN) to which the command will be sent.

</dd> <dt>

**DestFCID**
</dt> <dd>

The address identifier of the remote port.

</dd> <dt>

**ReqBufferSize**
</dt> <dd>

The request buffer size.

</dd> <dt>

**ReqBuffer**
</dt> <dd>

The request buffer data.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SM\_SendTEST\_IN structure in *Hbapiwmi.h* when it compiles the MS\_SM\_FabricAndDomainManagementMethod WMI class.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SM_SendTEST_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





