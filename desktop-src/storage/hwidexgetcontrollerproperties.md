---
title: HwIdeXGetControllerProperties routine
description: The HwIdeXGetControllerProperties routine reports properties of the IDE controller hardware in the IDE\_CONTROLLER\_PROPERTIES structure.
ms.assetid: '880bf39e-b8a1-4a9f-96d0-e879df1121db'
keywords: ["HwIdeXGetControllerProperties routine Storage Devices", "PCONTROLLER_PROPERTIES"]
topic_type:
- apiref
api_name:
- HwIdeXGetControllerProperties
api_location:
- ide.h
api_type:
- UserDefined
---

# HwIdeXGetControllerProperties routine

The *HwIdeXGetControllerProperties* routine reports properties of the IDE controller hardware in the [**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md) structure.

## Syntax


```C++
PCONTROLLER_PROPERTIES HwIdeXGetControllerProperties;

NTSTATUS HwIdeXGetControllerProperties(
  _In_ PVOID                      DeviceExtension,
  _In_ PIDE_CONTROLLER_PROPERTIES ControllerProperties
)
{ ... }
```



## Parameters

<dl> <dt>

*DeviceExtension* \[in\]
</dt> <dd>

Contains a pointer to the controller minidriver's device extension.

</dd> <dt>

*ControllerProperties* \[in\]
</dt> <dd>

Points to an [**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md) structure that specifies various properties of the IDE controller.

</dd> </dl>

## Return value

*HwIdeXGetControllerProperties* returns STATUS\_SUCCESS if the controller information was successfully retrieved or STATUS\_REVISION\_MISMATCH if the **Size** member of the *ControllerProperties* structure does not have the expected value of **sizeof**(IDE\_CONTROLLER\_PROPERTIES). This probably indicates that the structure passed to *HwIdeXGetControllerProperties* in the *ControllerProperties* parameter is not suitable for the current version of the OS/PCI IDE controller driver.

## Remarks

*HwIdeXGetControllerProperties* examines the controller's configuration data to determine what transfer modes it supports. *HwIdeXGetControllerProperties* then returns the transfer mode information, along with pointers to a standard set of controller minidriver routines and the values of various flags, in the IDE\_CONTROLLER\_PROPERTIES structure.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Ide.h (include Ide.h)</dt> </dl> |



## See also

<dl> <dt>

[**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md)
</dt> <dt>

[**PciIdeXGetBusData**](pciidexgetbusdata.md)
</dt> <dt>

[**PciIdeXInitialize**](pciidexinitialize.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20HwIdeXGetControllerProperties%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






