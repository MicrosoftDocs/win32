---
title: StorPortEnablePassiveInitialization routine
description: The StorPortEnablePassiveInitialization routine enables the miniports HwStorPassiveInitializeRoutine callback routine to execute at PASSIVE\_LEVEL during miniport initialization.
ms.assetid: 881253d2-b44d-4c41-ad72-b0143dc50803
keywords:
- StorPortEnablePassiveInitialization routine Storage Devices
topic_type:
- apiref
api_name:
- StorPortEnablePassiveInitialization
api_location:
- storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortEnablePassiveInitialization routine

The **StorPortEnablePassiveInitialization** routine enables the miniport's [**HwStorPassiveInitializeRoutine**](hwstorpassiveinitializeroutine.md) callback routine to execute at PASSIVE\_LEVEL during miniport initialization.

## Syntax


```C++
BOOLEAN StorPortEnablePassiveInitialization(
  _In_ PVOID                          HwDeviceExtension,
  _In_ PHW_PASSIVE_INITIALIZE_ROUTINE HwPassiveInitialization
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* \[in\]
</dt> <dd>

Pointer to the per-adapter device extension.

</dd> <dt>

*HwPassiveInitialization* \[in\]
</dt> <dd>

Pointer to a callback routine that the port driver calls at PASSIVE\_LEVEL to initialize the DPCs that the miniport driver will use. For a description of this callback routine, see [**HwStorPassiveInitializeRoutine**](hwstorpassiveinitializeroutine.md).

</dd> </dl>

## Return value

The **StorPortEnablePassiveInitialization** routine returns **TRUE** if the operating system supports DPCs, and **FALSE** if not.

## Remarks

A miniport must call the **StorPortEnablePassiveInitialization** routine only from within [**HwStorInitialize**](hwstorinitialize.md). Otherwise, **StorPortEnablePassiveInitialization** will return **FALSE** and the [**HwStorPassiveInitializeRoutine**](hwstorpassiveinitializeroutine.md) routine will not execute.

This routine is implemented using inline function definitions, so that miniport drivers that use this routine will not have to link to libraries that are dependent on the version of the operating system. Miniport drivers can use this routine without sacrificing backward compatibility with versions of the operating system that do not support DPCs in storage miniport drivers.

## Requirements



|                                 |                                                                                                                                                  |
|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| Target platform<br/>      | <dl> <dt>[Universal](http://go.microsoft.com/fwlink/p/?linkid=531356)</dt> </dl>          |
| Header<br/>               | <dl> <dt>Storport.h (include Storport.h)</dt> </dl>                                       |
| IRQL<br/>                 | DIRQL<br/>                                                                                                                                 |
| DDI compliance rules<br/> | [**StorPortEnablePassive**](https://msdn.microsoft.com/library/windows/hardware/hh454264), [**StorPortPassiveFromHwInit**](https://msdn.microsoft.com/library/windows/hardware/hh454269) |



## See also

<dl> <dt>

[**HwStorPassiveInitializeRoutine**](hwstorpassiveinitializeroutine.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortEnablePassiveInitialization%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






