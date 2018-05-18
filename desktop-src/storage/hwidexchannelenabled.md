---
title: HwIdeXChannelEnabled routine
description: The HwIdeXChannelEnabled routine is called to determine whether Channel is enabled.
ms.assetid: '44c70df5-0b39-4a19-b354-7b6bab882a45'
keywords: ["HwIdeXChannelEnabled routine Storage Devices", "PCIIDE_CHANNEL_ENABLED"]
topic_type:
- apiref
api_name:
- HwIdeXChannelEnabled
api_location:
- ide.h
api_type:
- UserDefined
---

# HwIdeXChannelEnabled routine

The *HwIdeXChannelEnabled* routine is called to determine whether *Channel* is enabled.

## Syntax


```C++
PCIIDE_CHANNEL_ENABLED HwIdeXChannelEnabled;

IDE_CHANNEL_STATE HwIdeXChannelEnabled(
  _In_ PVOID DeviceExtension,
  _In_ ULONG Channel
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Contains a pointer to the controller minidriver's device extension.

</dd> <dt>

*Channel* \[in\]
</dt> <dd>

Specifies which channel is being queried. This parameter must be assigned a value of 0 or 1.

</dd> </dl>

## Return value

*HwIdeXChannelEnabled* must return one of three enumeration values of type IDE\_CHANNEL\_STATE:



| Return code                                                                                        | Description |
|----------------------------------------------------------------------------------------------------|-------------|
| <dl> <dt>****ChannelDisabled****</dt> </dl> |             |



 

## Remarks

An IDE controller minidriver must implement an *HwIdeXChannelEnabled* routine to report whether the specified channel is enabled or not. *HwIdeXChannelEnabled* retrieves the needed information from the PCI configuration space by calling the minidriver library routine [**PciIdeXGetBusData**](pciidexgetbusdata.md).

When the controller driver calls minidriver's [**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md) routine, it passes an [**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md) structure to the minidriver. The minidriver must store a pointer to *HwIdeXChannelEnabled* in this structure.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Ide.h (include Ide.h)</dt> </dl> |



## See also

<dl> <dt>

[**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md)
</dt> <dt>

[**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md)
</dt> <dt>

[**PciIdeXGetBusData**](pciidexgetbusdata.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HwIdeXChannelEnabled%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






