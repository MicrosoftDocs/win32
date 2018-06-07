---
title: AddLink\_OUT structure
description: The AddLink\_OUT structure is used by an HBA miniport driver to report the status of a call to the AddLink WMI method.
ms.assetid: fe088ec7-2577-488d-a1c7-a7e2a1f86f6a
keywords:
- AddLink_OUT structure Storage Devices
- PAddLink_OUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- AddLink_OUT
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

# AddLink\_OUT structure

The AddLink\_OUT structure is used by an HBA miniport driver to report the status of a call to the [**AddLink**](https://msdn.microsoft.com/library/windows/hardware/ff550128) WMI method.

## Syntax


```C++
typedef struct _AddLink_OUT {
  ULONG HBAStatus;
} AddLink_OUT, *PAddLink_OUT;
```



## Members

<dl> <dt>

**HBAStatus**
</dt> <dd>

Contains a value associated with the WMI class qualifier [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the result of an HBA query operation.

</dd> </dl>

## Remarks

The WMI tool suite generates a declaration of the AddLink\_OUT structure in *Hbapiwmi.h* when it compiles the [MSFC\_EventControl WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562490).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**AddLink**](https://msdn.microsoft.com/library/windows/hardware/ff550128)
</dt> <dt>

[HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233)
</dt> <dt>

[MSFC\_EventControl WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562490)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20AddLink_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






