---
title: StorPortStallExecution routine
description: The StorPortStallExecution routine stalls the miniport driver.
ms.assetid: 'd635d93b-3e69-4ce5-9dc0-60186417d009'
keywords: ["StorPortStallExecution routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortStallExecution
api_location:
- Storport.lib
- Storport.dll
api_type:
- LibDef
---

# StorPortStallExecution routine

The **StorPortStallExecution** routine stalls the miniport driver.

## Syntax


```C++
STORPORT_API VOID StorPortStallExecution(
  _In_ ULONG Delay
);
```



## Parameters

<dl> <dt>

*Delay* \[in\]
</dt> <dd>

Specifies the delay interval, in microseconds. The given value must be less than a full millisecond.

</dd> </dl>

## Return value

None

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| Library<br/>              | <dl> <dt>Storport.lib</dt> </dl>                                                 |
| DDI compliance rules<br/> | [**SpNoWait**](https://msdn.microsoft.com/library/windows/hardware/hh454255)                                                                                               |



## See also

<dl> <dt>

[**ScsiPortStallExecution**](scsiportstallexecution.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortStallExecution%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






