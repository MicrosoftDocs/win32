---
title: How to Use the Device Access API
description: This topic contains tasks and design considerations for using the Device Access API.
ms.assetid: '8D951EB5-4AFB-4051-8F1F-30F847F1A757'
---

# How to Use the Device Access API

This topic contains tasks and design considerations for using the Device Access API.

## Steps



| Topic                                                                                                                              | Description                                                                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Design Considerations for Custom Devices](design.md)<br/>                                                                  | This topic describes design considerations that can help you determine whether your device needs a custom driver.<br/>                                                               |
| [Implement the Device Access Object](create-the-device-access-object.md)<br/>                                               | This topic explains how to instantiate the device access object and use it to access a device. <br/>                                                                                 |
| [Declaring the Device Capability](declaring-the-device-capability.md)<br/>                                                  | This topic explains how to declare the device capability GUID.<br/>                                                                                                                  |
| [Register the device interface as restricted to privileged apps](register-the-device-interface-class-as-privileged.md)<br/> | This topic shows how to add the **Restricted** property that indicates that only privileged apps can access a device interface class.<br/>                                           |
| [Create a Windows Runtime Extension](create-a-windows-runtime-extension.md)<br/>                                            | You can create a Windows Runtime component to wrap the component that accesses your driver. You can then write a Windows Store device app for your device in C# or JavaScript.<br/> |



 

## Additional resources

-   The [Custom Driver Access Sample](http://go.microsoft.com/fwlink/p/?linkid=242014) demonstrates how to use the Device Access API to access a custom driver from a Windows Store device app.
-   The [Windows Store device app design guide for specialized devices](http://go.microsoft.com/fwlink/p/?linkid=242009) provides design guidance on what types of specialized devices require custom driver access via the Device Access API.
-   This [Device Experience for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009) page provides resources for learning more about how to developWindows Store device apps for specialized devices.
-   The [Device Experience for Windows 8](http://go.microsoft.com/fwlink/p/?linkid=241442) page provides general resources for Windows Store device app development tasks that are common to all types of devices.

## Related topics

<dl> <dt>

[Windows Store device app Design Guide for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

[Device Experience for Specialized Devices](http://go.microsoft.com/fwlink/p/?linkid=242009)
</dt> <dt>

[Device Experience for Windows 8](http://go.microsoft.com/fwlink/p/?linkid=241442)
</dt> <dt>

[Custom Driver Access Sample](http://go.microsoft.com/fwlink/p/?linkid=242014)
</dt> </dl>

 

 





