---
title: PciIdeXInitialize routine
description: The PciIdeXInitialize routine initializes a controller minidriver.
ms.assetid: a4326cd7-673e-43b2-9f62-5a9277f6b9e8
keywords:
- PciIdeXInitialize routine Storage Devices
topic_type:
- apiref
api_name:
- PciIdeXInitialize
api_location:
- Pciidex.lib
- Pciidex.dll
api_type:
- LibDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# PciIdeXInitialize routine

The **PciIdeXInitialize** routine initializes a controller minidriver.

## Syntax


```C++
NTSTATUS PciIdeXInitialize(
  _In_ PDRIVER_OBJECT         DriverObject,
  _In_ PUNICODE_STRING        RegistryPath,
  _In_ PCONTROLLER_PROPERTIES HwGetControllerProperties,
  _In_ ULONG                  ExtensionSize
);
```



## Parameters

<dl> <dt>

*DriverObject* \[in\]
</dt> <dd>

Contains a pointer to the controller minidriver's driver object.

</dd> <dt>

*RegistryPath* \[in\]
</dt> <dd>

Contains a Unicode string that indicates the location in the registry where the minidriver's configuration information is stored.

</dd> <dt>

*HwGetControllerProperties* \[in\]
</dt> <dd>

Contains a pointer to the [**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md) controller minidriver routine that queries for the PCI IDE controller properties.

</dd> <dt>

*ExtensionSize* \[in\]
</dt> <dd>

Specifies the size in bytes of the driver extension.

</dd> </dl>

## Return value

**PciIdeXInitialize** returns STATUS\_SUCCESS if the allocation of the driver extension succeeds, and the appropriate error code otherwise.

## Remarks

An IDE controller minidriver must call **PciIdeXInitialize** from its [**DriverEntry of IDE Controller Minidriver**](https://msdn.microsoft.com/library/windows/hardware/ff552651) routine **PciIdeXInitialize** initializes the controller minidriver's dispatch tables and allocates an extension for the *DriverObject*. This routine then stores the *ExtensionSize* and a pointer to the [**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md) routine in the *DriverObject* extension.

An IDE controller minidriver must also implement a routine that reports the properties of the IDE controller. A pointer to this routine is passed to **PciIdeXInitialize** in its **HwGetControllerProperties** parameter.

## Requirements



|                            |                                                                                                  |
|----------------------------|--------------------------------------------------------------------------------------------------|
| Target platform<br/> | <dl> <dt>Desktop</dt> </dl>               |
| Header<br/>          | <dl> <dt>Ide.h (include Ide.h)</dt> </dl> |
| Library<br/>         | <dl> <dt>Pciidex.lib</dt> </dl>           |



## See also

<dl> <dt>

[**IDE\_CONTROLLER\_PROPERTIES**](ide-controller-properties.md)
</dt> <dt>

[**HwIdeXGetControllerProperties**](hwidexgetcontrollerproperties.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20PciIdeXInitialize%20routine%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






