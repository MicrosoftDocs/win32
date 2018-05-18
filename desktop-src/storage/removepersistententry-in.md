---
title: RemovePersistentEntry\_IN structure
description: The RemovePersistentEntry\_IN structure is used by a WMI client to deliver input parameter data to the RemovePersistentEntry WMI method.
ms.assetid: '7019ee37-2080-4ba3-ba39-977e575ec04e'
keywords: ["RemovePersistentEntry_IN structure Storage Devices", "PRemovePersistentEntry_IN structure pointer Storage Devices"]
topic_type:
- apiref
api_name:
- RemovePersistentEntry_IN
api_location:
- hbapiwmi.h
api_type:
- HeaderDef
---

# RemovePersistentEntry\_IN structure

The RemovePersistentEntry\_IN structure is used by a WMI client to deliver input parameter data to the [**RemovePersistentEntry**](https://msdn.microsoft.com/library/windows/hardware/ff563988) WMI method.

## Syntax


```C++
typedef struct _RemovePersistentEntry_IN {
  UCHAR               PortWWN[8];
  HBAFCPBindingEntry2 Binding;
} RemovePersistentEntry_IN, *PRemovePersistentEntry_IN;
```



## Members

<dl> <dt>

**PortWWN**
</dt> <dd>

Contains a worldwide name that indicates the port for which a persistent binding will be removed.

</dd> <dt>

**Binding**
</dt> <dd>

Contains a structure of type [**HBAFCPBindingEntry2**](hbafcpbindingentry2.md) that indicates the binding to be removed from the indicated port's list of bindings.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the RemovePersistentEntry\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAFCPInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562509).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**RemovePersistentEntry**](https://msdn.microsoft.com/library/windows/hardware/ff563988)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20RemovePersistentEntry_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






