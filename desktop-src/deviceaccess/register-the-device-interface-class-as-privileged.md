---
title: Register the device interface as restricted to privileged apps
description: This topic shows how to add the Restricted property that indicates that only privileged apps can access a device interface class.
ms.assetid: BCEB1FBF-3D3F-45B8-A92B-7C5FBF6745C0
ms.topic: article
ms.date: 02/11/2020
---

# Register the device interface as restricted to privileged apps

Applications are denied access to custom driver functionality, unless they're granted permissions through signed device metadata. This topic shows how to add the **Restricted** property that indicates that only privileged apps can access a device interface class. Custom device drivers must have this property.

## Instructions

### Setting the Restricted property in an information (INF) file

In the `InterfaceInstall32` section, the GUID of the device interface class is registered.

The lines under the **AddProperty** directive set the device class properties. The second line sets a custom property in a custom property category. The property-category GUID is **14c83a99-0b3f-44b7-be4c-a178d3990564**, and the property identifier is **2**. The optional `Flags` entry value is not present, and the type is **17** (**DEVPROP_TYPE_BOOLEAN**). The value of the property is **1**.

```Text
; Below, {11111111-0000-1111-0000-111111111111} is the GUID of the
; new device interface class in an AddInterface directive



; -- Interface installation
[InterfaceInstall32]
{11111111-0000-1111-0000-111111111111}=NewInterfaceInstall

[NewInterfaceInstall]
AddProperty=PrivilegedProperties

[PrivilegedProperties]
; DEVPKey_DeviceInterfaceClass_Restricted
{14c83a99-0b3f-44b7-be4c-a178d3990564}, 2, 17,,1 ; -- non-zero indicates privileged
```

## Remarks

Instead of the **AddInterface** directive, the driver can also call the [**IoRegisterDeviceInterface**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacepropertydata) routine to register the device interface class.

You can also set the restricted interface property by calling the [**IoSetDeviceInterfacePropertyData**](/windows-hardware/drivers/ddi/wdm/nf-wdm-iosetdeviceinterfacepropertydata) routine.

## Related topics

[Custom Driver Access Sample](https://github.com/microsoftarchive/msdn-code-gallery-microsoft/tree/411c271e537727d737a53fa2cbe99eaecac00cc0/Official%20Windows%20Platform%20Sample/Custom%20driver%20access%20sample), [UWP device apps for internal devices](/windows-hardware/drivers/devapps/uwp-device-apps-for-specialized-devices), [Hardware Dev Center](/windows-hardware/drivers/)
