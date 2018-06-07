---
title: SetBindingSupport\_IN structure
description: The SetBindingSupport\_IN structure is used to deliver input parameter data to the SetBindingSupport WMI method.
ms.assetid: bdcd6f76-9a45-4687-b3ab-ece3e9419c44
keywords:
- SetBindingSupport_IN structure Storage Devices
- PSetBindingSupport_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- SetBindingSupport_IN
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

# SetBindingSupport\_IN structure

The SetBindingSupport\_IN structure is used to deliver input parameter data to the [**SetBindingSupport**](https://msdn.microsoft.com/library/windows/hardware/ff565565) WMI method.

## Syntax


```C++
typedef struct _SetBindingSupport_IN {
  UCHAR PortWWN[8];
  ULONG BindType;
} SetBindingSupport_IN, *PSetBindingSupport_IN;
```



## Members

<dl> <dt>

**PortWWN**
</dt> <dd>

Contains a worldwide name that indicates the port whose persistent bindings are to be retrieved.

</dd> <dt>

**BindType**
</dt> <dd>

Contains a bitmap that indicates the ability of an HBA and its miniport driver to provide a specific set of features related to persistent binding. For a list of values that this parameter can have, see the description of the HBA\_BIND\_TYPE WMI class qualifier.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the SetBindingSupport\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAFCPInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562509).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**SetBindingSupport**](https://msdn.microsoft.com/library/windows/hardware/ff565565)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20SetBindingSupport_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






