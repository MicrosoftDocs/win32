---
title: DriverEntry routine
description: The DriverEntry miniport driver routine is called when the miniport driver is loaded.Note The ATA port driver and ATA miniport driver models may be altered or unavailable in the future.
ms.assetid: f756e66b-7e66-4a27-9327-70608207d99b
keywords:
- DriverEntry routine Storage Devices
topic_type:
- apiref
api_name:
- DriverEntry
api_location:
- NtosKrnl.exe
api_type:
- DllExport
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DriverEntry routine

The ***DriverEntry*** miniport driver routine is called when the miniport driver is loaded.

> [!Note]  
> The ATA port driver and ATA miniport driver models may be altered or unavailable in the future. Instead, we recommend using the [Storport driver](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-driver) and [Storport miniport](https://msdn.microsoft.com/windows/hardware/drivers/storage/storport-miniport-drivers) driver models.

 

## Syntax


```C++
NTSTATUS DriverEntry(
  _In_ struct _DRIVER_OBJECT *DriverObject,
  _In_ PUNICODE_STRING       RegistryPath
);
```



## Parameters

<dl> <dt>

*DriverObject* \[in\]
</dt> <dd>

A pointer to an opaque structure to be used as the first parameter when this routine calls the [**AtaPortInitializeEx**](ataportinitializeex.md) routine.

</dd> <dt>

*RegistryPath* \[in\]
</dt> <dd>

A pointer to an opaque structure to be used as the second parameter when this routine calls the [**AtaPortInitializeEx**](ataportinitializeex.md) routine.

</dd> </dl>

## Return value

The return values for this routine are recommended to mirror the return values of [**AtaPortInitializeEx**](ataportinitializeex.md).

## Remarks

**DriverEntry** is the first function that is called in an ATA miniport driver. The ATA miniport driver must allocate an [**IDE\_CONTROLLER\_INTERFACE**](ide-controller-interface.md) structure, initialize it, and send it to [**AtaPortInitializeEx**](ataportinitializeex.md). The ATA miniport driver indicates its support for the channel interface by setting the ChannelExtensionSize and the ***AtaChannelInitRoutine*** entry point in the **IDE\_CONTROLLER\_INTERFACE** structure. This causes the ATA port driver to call the function that is specified in the ***AtaChannelInitRoutine*** field that has a ChannelExtension of size ChannelExtensionSize. The function is called one time for every NumberOfChannels specified in the ControllerConfiguration structure that are returned by [**AtaAdapterControl**](ataadaptercontrol.md) when **AtaAdapterControl** handles an IdeStart action.

## Requirements



|                            |                                                                                                             |
|----------------------------|-------------------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>                          |
| Header<br/>          | <dl> <dt>Wdm.h (include Ntddk.h or Mcd.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>NtosKrnl.lib</dt> </dl>                     |
| DLL<br/>             | <dl> <dt>NtosKrnl.exe</dt> </dl>                     |



## See also

<dl> <dt>

[**AtaPortInitializeEx**](ataportinitializeex.md)
</dt> <dt>

[**AtaAdapterControl**](ataadaptercontrol.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20DriverEntry%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






