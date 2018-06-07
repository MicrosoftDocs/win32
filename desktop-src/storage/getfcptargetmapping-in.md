---
title: GetFcpTargetMapping\_IN structure
description: The GetFcpTargetMapping\_IN structure is used to report the output parameter data of the GetFcpTargetMapping WMI method to the WMI client.
ms.assetid: a07a97ea-17f0-4e24-89c5-1b24600ac497
keywords:
- GetFcpTargetMapping_IN structure Storage Devices
- PGetFcpTargetMapping_IN structure pointer Storage Devices
topic_type:
- apiref
api_name:
- GetFcpTargetMapping_IN
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

# GetFcpTargetMapping\_IN structure

The GetFcpTargetMapping\_IN structure is used to report the output parameter data of the [**GetFcpTargetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff554948) WMI method to the WMI client.

## Syntax


```C++
typedef struct _GetFcpTargetMapping_IN {
  UCHAR HbaPortWWN[8];
  ULONG InEntryCount;
} GetFcpTargetMapping_IN, *PGetFcpTargetMapping_IN;
```



## Members

<dl> <dt>

**HbaPortWWN**
</dt> <dd>

Contains a worldwide name for the port whose table of mappings is to be retrieved.

</dd> <dt>

**InEntryCount**
</dt> <dd>

Indicates the total number of persistent bindings associated with the HBA.

</dd> </dl>

## Remarks

The [**GetFcpTargetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff554948) WMI method queries a WMI provider for mappings between the information that uniquely identifies a set of logical units for the operating system and the fibre channel protocol (FCP) identifiers for the logical units.

The WMI tool suite generates a declaration of the GetFcpTargetMapping\_IN structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAFCPInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562509).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetFcpTargetMapping**](https://msdn.microsoft.com/library/windows/hardware/ff554948)
</dt> <dt>

[MSFC\_HBAFCPInfo WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562509)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GetFcpTargetMapping_IN%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






