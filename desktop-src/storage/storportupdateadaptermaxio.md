---
title: StorPortUpdateAdapterMaxIO function
description: This function can be called by a miniport to update the maximum IOs supported by an adapter. This function is valid during HwInitialize/HwPassiveInitRoutine callback and has effect only during adapter initialization.
ms.assetid: BB18925D-ACFA-426D-ADD3-33C1D8A99396
keywords:
- StorPortUpdateAdapterMaxIO function Storage Devices
topic_type:
- apiref
api_name:
- StorPortUpdateAdapterMaxIO
api_location:
- Storport.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# StorPortUpdateAdapterMaxIO function

This function can be called by a miniport to update the maximum IO's supported by an adapter. This function is valid during HwInitialize/HwPassiveInitRoutine callback and has effect only during adapter initialization.

## Syntax


```C++
ULONG StorPortUpdateAdapterMaxIO(
   PVOID HwDeviceExtension,
   ULONG MaxIoCount
);
```



## Parameters

<dl> <dt>

*HwDeviceExtension* 
</dt> <dd>

A pointer to miniport's device extension.

</dd> <dt>

*MaxIoCount* 
</dt> <dd>

Maximum IO's supported by the adapter.

</dd> </dl>

## Return value

This function returns of the following values.



| Value                                  | Description                                                                   |
|----------------------------------------|-------------------------------------------------------------------------------|
| STOR\_STATUS\_SUCCESS                  | The telemetry event was successfully logged.                                  |
| STOR\_STATUS\_NOT\_IMPLEMENTED         | The function is called on the OS that does not support it.                    |
| STOR\_STATUS\_INVALID\_PARAMETER       | There is an invalid parameter.                                                |
| STOR\_STATUS\_INVALID\_DEVICE\_REQUEST | The function was called outside of **HwInitialize**/**HwPassiveInitRoutine**. |



 

## Requirements



|                    |                                                                                       |
|--------------------|---------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 10, version 1709.<br/>                          |
| Header<br/>  | <dl> <dt>Storport.h</dt> </dl> |



## See also

<dl> <dt>

[****HwInitialize****](hw-initialization-data--storport-.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20StorPortUpdateAdapterMaxIO%20function%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






