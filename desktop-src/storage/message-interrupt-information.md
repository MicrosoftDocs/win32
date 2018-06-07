---
title: MESSAGE\_INTERRUPT\_INFORMATION structure
description: The MESSAGE\_INTERRUPT\_INFORMATION structure describes a message signaled interrupt (MSI).
ms.assetid: 469896b3-3ae0-4edd-9fb0-ee5869633872
keywords:
- MESSAGE_INTERRUPT_INFORMATION structure Storage Devices
- PMESSAGE_INTERRUPT_INFORMATION structure pointer Storage Devices
topic_type:
- apiref
api_name:
- MESSAGE_INTERRUPT_INFORMATION
api_location:
- storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# MESSAGE\_INTERRUPT\_INFORMATION structure

The **MESSAGE\_INTERRUPT\_INFORMATION** structure describes a message signaled interrupt (MSI).

## Syntax


```C++
typedef struct _MESSAGE_INTERRUPT_INFORMATION {
  ULONG                 MessageId;
  ULONG                 MessageData;
  STOR_PHYSICAL_ADDRESS MessageAddress;
  ULONG                 InterruptVector;
  ULONG                 InterruptLevel;
  KINTERRUPT_MODE       InterruptMode;
} MESSAGE_INTERRUPT_INFORMATION, *PMESSAGE_INTERRUPT_INFORMATION;
```



## Members

<dl> <dt>

**MessageId**
</dt> <dd>

An identifier identifies the MSI interrupt. A miniport driver can pass this value to [**StorPortAcquireMSISpinLock**](storportacquiremsispinlock.md) in the *MessageId* parameter to obtain a spin lock for synchronization purposes.

</dd> <dt>

**MessageData**
</dt> <dd>

The data associated with the message.

</dd> <dt>

**MessageAddress**
</dt> <dd>

The physical address associated with the message.

</dd> <dt>

**InterruptVector**
</dt> <dd>

The interrupt vector associated with the message.

</dd> <dt>

**InterruptLevel**
</dt> <dd>

The interrupt level associated with the message.

</dd> <dt>

**InterruptMode**
</dt> <dd>

A value of type [**KINTERRUPT\_MODE**](https://msdn.microsoft.com/library/windows/hardware/ff554239) that specifies the interrupt mode associated with the message.

</dd> </dl>

## Remarks

Miniport drivers retrieve the MSI information in a **MESSAGE\_INTERRUPT\_INFORMATION** structure by calling the [**StorPortGetMSIInfo**](storportgetmsiinfo.md) routine.

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Storport.h (include Storport.h)</dt> </dl> |



## See also

<dl> <dt>

[**StorPortGetMSIInfo**](storportgetmsiinfo.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20MESSAGE_INTERRUPT_INFORMATION%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






