---
title: StorPortQueryPerformanceCounter routine
description: The current system performance counter value is queried is returned by the StorPortQueryPerformanceCounter routine.
ms.assetid: '6502E3AE-5841-41C9-BEB7-B00620DBF02D'
keywords: ["StorPortQueryPerformanceCounter routine Storage Devices"]
topic_type:
- apiref
api_name:
- StorPortQueryPerformanceCounter
api_location:
- Storport.h
api_type:
- HeaderDef
---

# StorPortQueryPerformanceCounter routine

The current system performance counter value is queried is returned by the **StorPortQueryPerformanceCounter** routine.. The performance frequency is also returned as an optional parameter.

## Syntax


```C++
ULONG StorPortQueryPerformanceCounter(
  _In_      PVOID          HwDeviceExtension,
  _Out_opt_ PLARGE_INTEGER PerformanceFrequency,
  _Out_     PLARGE_INTEGER PerformanceCounter
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA).

</dd> <dt>

*PerformanceFrequency* \[out, optional\]
</dt> <dd>

A pointer to a large integer to receive the current system performance frequency value. This parameter is optional and can be NULL.

</dd> <dt>

*PerformanceCounter* \[out\]
</dt> <dd>

A pointer to a large integer to receive the current system performance counter value.

</dd> </dl>

## Return value

**StorPortQueryPerformanceCounter** returns one of the following status codes:



| Return code                                                                                                     | Description                                                                                                   |
|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>            | The performance counter value is returned in the large integer pointed to by *PerformanceCounter*.<br/> |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl> | The *PerformanceCounter* parameter is **NULL**.<br/>                                                    |



 

## Requirements



|                            |                                                                                                                                         |
|----------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Version<br/>         | Available starting with Windows 8.<br/>                                                                                           |
| Header<br/>          | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| IRQL<br/>            | Any<br/>                                                                                                                          |



## See also

<dl> <dt>

[**StorPortQuerySystemTime**](storportquerysystemtime.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortQueryPerformanceCounter%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






