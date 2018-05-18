---
title: Register the device interface as restricted to privileged apps
description: This topic shows how to add the Restricted property that indicates that only privileged apps can access a device interface class.
ms.assetid: 'BCEB1FBF-3D3F-45B8-A92B-7C5FBF6745C0'
---

# Register the device interface as restricted to privileged apps

Applications are denied access to custom driver functionality, unless they're granted permissions through signed device metadata. This topic shows how to add the **Restricted** property that indicates that only privileged apps can access a device interface class. Custom device drivers must have this property.

## Instructions

### Setting the Restricted property in an information (INF) file

In the `InterfaceInstall32` section, the GUID of the device interface class is registered.

The lines under the **AddProperty** directive set the device class properties. The second line sets a custom property in a custom property category. The property-category GUID is **14c83a99-0b3f-44b7-be4c-a178d3990564**, and the property identifier is **2**. The optional `Flags` entry value is not present, and the type is **17** (**DEVPROP\_TYPE\_BOOLEAN**). The value of the property is **1**.


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

Instead of the **AddInterface** directive, the driver can also call the [**IoRegisterDeviceInterface**](https://msdn.microsoft.com/library/windows/hardware/ff549704) routine to register the device interface class.

You can also set the restricted interface property by calling the [**IoSetDeviceInterfacePropertyData**](https://msdn.microsoft.com/library/windows/hardware/hh439388) routine.

## Related topics

<dl> <dt>

**Samples**
</dt> <dt>

[Custom Driver Access Sample](http://go.microsoft.com/fwlink/p/?linkid=242014)
</dt> <dt>

**White papers**
</dt> <dt>

[Windows Store device app Design Guide for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

**Other resources**
</dt> <dt>

[Device Experience for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

[Device Experience for Windows 8](http://go.microsoft.com/fwlink/p/?linkid=241442)
</dt> </dl>

 

 




