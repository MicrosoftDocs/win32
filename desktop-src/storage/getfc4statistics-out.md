---
title: GetFC4Statistics\_OUT structure
description: The GetFC4Statistics\_OUT structure is used to report the output parameter data of the GetFC4Statistics WMI method to the WMI client.
ms.assetid: fc747ff1-cc84-4863-a66a-ae172f45f2bd
keywords:
- GetFC4Statistics_OUT structure Storage Devices
- PGetFC4Statistics_OUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- GetFC4Statistics_OUT
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

# GetFC4Statistics\_OUT structure

The GetFC4Statistics\_OUT structure is used to report the output parameter data of the [**GetFC4Statistics**](https://msdn.microsoft.com/library/windows/hardware/ff553949) WMI method to the WMI client.

## Syntax


```C++
typedef struct _GetFC4Statistics_OUT {
  ULONG              HBAStatus;
  MSFC_FC4STATISTICS FC4Statistics;
} GetFC4Statistics_OUT, *PGetFC4Statistics_OUT;
```



## Members

<dl> <dt>

**HBAStatus**
</dt> <dd>

Contains a value associated with the WMI class qualifier [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the result of an HBA query operation.

</dd> <dt>

**FC4Statistics**
</dt> <dd>

Contains a structure of type [**MSFC\_FC4STATISTICS**](msfc-fc4statistics.md) that holds statistics for the specified FC-4 protocol.

</dd> </dl>

## Remarks

The [**GetFC4Statistics**](https://msdn.microsoft.com/library/windows/hardware/ff553949) WMI method reports traffic statistics for a specific FC-4 protocol via a specific local HBA and port of type Nx\_Port.

The WMI tool suite generates a declaration of the GetFC4Statistics\_OUT structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetFC4Statistics**](https://msdn.microsoft.com/library/windows/hardware/ff553949)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GetFC4Statistics_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






