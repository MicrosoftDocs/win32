---
title: GetEventBuffer\_OUT structure
description: The GetEventBuffer\_OUT structure is used to report the output parameter data of the GetEventBuffer WMI method to the WMI client.
ms.assetid: 1ba41017-8c4b-49eb-b0ec-8e58c2673314
keywords:
- GetEventBuffer_OUT structure Storage Devices
- PGetEventBuffer_OUT structure pointer Storage Devices
topic_type:
- apiref
api_name:
- GetEventBuffer_OUT
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

# GetEventBuffer\_OUT structure

The GetEventBuffer\_OUT structure is used to report the output parameter data of the [**GetEventBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff553935) WMI method to the WMI client.

## Syntax


```C++
typedef struct _GetEventBuffer_OUT {
  ULONG            HBAStatus;
  ULONG            EventCount;
  MSFC_EventBuffer Events[1];
} GetEventBuffer_OUT, *PGetEventBuffer_OUT;
```



## Members

<dl> <dt>

**HBAStatus**
</dt> <dd>

Contains a value associated with the WMI class qualifier [HBA\_STATUS](https://msdn.microsoft.com/library/windows/hardware/ff557233) that indicates the result of an HBA query operation.

</dd> <dt>

**EventCount**
</dt> <dd>

Indicates the number of events in **Events** that were retrieved by the [**GetEventBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff553935) WMI method.

</dd> <dt>

**Events**
</dt> <dd>

Contains an array of type [**MSFC\_EventBuffer**](msfc-eventbuffer.md) that contains the next events in the HBA's event queue.

</dd> </dl>

## Remarks

The [**GetEventBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff553935) method retrieves the next events in the HBA's event queue.

The WMI tool suite generates a declaration of the GetEventBuffer\_OUT structure in *Hbapiwmi.h* when it compiles the [MSFC\_HBAAdapterMethods WMI Class](https://msdn.microsoft.com/library/windows/hardware/ff562506).

## Requirements



|                   |                                                                                                            |
|-------------------|------------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Hbapiwmi.h (include Hbapiwmi.h)</dt> </dl> |



## See also

<dl> <dt>

[**GetEventBuffer**](https://msdn.microsoft.com/library/windows/hardware/ff553935)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20GetEventBuffer_OUT%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






