---
title: SetPersistentEntry\_IN structure
description: The SetPersistentEntry\_IN structure is used by a WMI client to deliver the input parameter data of the SetPersistentEntry WMI method to the HBA miniport driver.
ms.assetid: f088a623-e6e8-4810-a7ab-90348f669dac
keywords:
- SetPersistentEntry_IN structure Storage Devices
- PSetPersistentEntry_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SetPersistentEntry_IN
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

# SetPersistentEntry\_IN structure

The SetPersistentEntry\_IN structure is used by a WMI client to deliver the input parameter data of the [**SetPersistentEntry**](https://msdn.microsoft.com/library/windows/hardware/ff565783) WMI method to the HBA miniport driver.

## Syntax


```C++
typedef struct _SetPersistentEntry_IN {
  UCHAR               PortWWN[8];
  HBAFCPBindingEntry2 Binding;
} SetPersistentEntry_IN, *PSetPersistentEntry_IN;
```



## Members

<dl> <dt>

**PortWWN**
</dt> <dd>

Contains a worldwide name that indicates the port whose persistent bindings will be changed.

</dd> <dt>

**Binding**
</dt> <dd>

Contains a structure of type [**HBAFCPBindingEntry2**](hbafcpbindingentry2.md) that indicates the binding to be removed from the indicated port's list of bindings.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SetPersistentEntry\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAFCPInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562509).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SetPersistentEntry**](https://msdn.microsoft.com/library/windows/hardware/ff565783)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SetPersistentEntry_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






