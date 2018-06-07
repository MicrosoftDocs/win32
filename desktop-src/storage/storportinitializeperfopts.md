---
title: StorPortInitializePerfOpts function
description: The StorPortInitializePerfOpts function initializes the performance optimizations that both the miniport driver and the Storport driver support using a PERF\_CONFIGURATION\_DATA structure.
ms.assetid: fbaf864c-d499-456c-be3b-b486c637877e
keywords:
- StorPortInitializePerfOpts function Storage Devices
topic_type:
- apiref
api_name:
- StorPortInitializePerfOpts
api_location:
- Storport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# StorPortInitializePerfOpts function

The **StorPortInitializePerfOpts** function initializes the performance optimizations that both the miniport driver and the Storport driver support using a [**PERF\_CONFIGURATION\_DATA**](perf-configuration-data.md) structure.

## Syntax


```C++
ULONG StorPortInitializePerfOpts(
  _In_    PVOID                    HwDeviceExtension,
  _In_    BOOLEAN                  Query,
  _Inout_ PPERF_CONFIGURATION_DATA PerfConfigData
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

A pointer to the hardware device extension for the host bus adapter (HBA). This parameter must not be **NULL**.

</dd> <dt>

*Query* \[in\]
</dt> <dd>

If set to **TRUE**, Storport will set the flags in *PerfConfigData* corresponding to the optimizations Storport supports. If set to **FALSE**, Storport will initialize the optimizations specified by the flags in *PerfConfigData*.

</dd> <dt>

*PerfConfigData* \[in, out\]
</dt> <dd>

A pointer to a PERF\_CONFIGURATION\_DATA structure that is supplied by the miniport driver. This parameter must not be **NULL**.

</dd> </dl>

## Return value

StorPortInitializePerfOpts returns one of the following status values:



| Return code                                                                                                          | Description                                                                                                                                                                                                                                   |
|----------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**STOR\_STATUS\_NOT\_IMPLEMENTED**</dt> </dl>        | This function is not implemented on the active operating system.<br/>                                                                                                                                                                   |
| <dl> <dt>**STOR\_STATUS\_SUCCESS**</dt> </dl>                 | Indicates that the performance optimization settings have been applied.<br/> Or if *Query* is set to **TRUE**, the **Flags** member of the structure pointed to by *PerfConfigData* contains the supported flags.<br/>            |
| <dl> <dt>**STOR\_STATUS\_UNSUCCESSFUL**</dt> </dl>            | The miniport driver set a flag in *PerfConfigData* that Storport did not recognize, or the miniport driver has called this routine from outside the miniport-driver-supplied [**HwStorInitialize**](hwstorinitialize.md) routine.<br/> |
| <dl> <dt>**STOR\_STATUS\_INSUFFICIENT\_RESOURCES**</dt> </dl> | Unable to allocate internal structures to support the requested optimizations.<br/>                                                                                                                                                     |
| <dl> <dt>**STOR\_STATUS\_INVALID\_PARAMETER**</dt> </dl>      | Either the *HwDeviceExtension* parameter or the *PerfConfigData* parameter was **NULL**.<br/>                                                                                                                                           |



 

## Remarks

The miniport driver can call **StorPortInitializePerfOpts** only during the miniport-supplied [**HwStorInitialize**](hwstorinitialize.md) routine or [**HwStorPassiveInitializeRoutine**](hwstorpassiveinitializeroutine.md) routine.

Available performance optimizations depend on the version of [**PERF\_CONFIGURATION\_DATA**](perf-configuration-data.md). Setting the **Version** member to **STOR\_PERF\_VERSION** will allow all supported optimizations to be selected.

## Requirements



|                                 |                                                                                                                                         |
|---------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl> |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                              |
| DDI compliance rules<br/> | [**StorPortPerfOpts**](https://msdn.microsoft.com/library/windows/hardware/hh454270)                                                                               |



## See also

<dl> <dt>

[**PERF\_CONFIGURATION\_DATA**](perf-configuration-data.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortInitializePerfOpts%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






