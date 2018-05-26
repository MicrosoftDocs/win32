---
title: Using WPD Automation
description: WPD Automation is available in Windows 7. The starting point for using WPD Automation is to instantiate the Device object. There are two ways to instantiate the Device object from a scripting host and from C++/COM.
ms.assetid: 356f2b98-fe90-41d1-983b-cc1690600884
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using WPD Automation

WPD Automation is available in Windows 7. The starting point for using WPD Automation is to instantiate the Device object. There are two ways to instantiate the Device object: from a scripting host and from C++/COM.

## Instantiating the Device Object from a Scripting Host

WPD Automation can be used from script within a scripting host that is specifically designed to instantiate the WPD Automation factory interface. For an example, refer to [Instantiating the WPD Automation Factory](instantiating-the-wpd-automation-factory-interface.md).

## Instantiating the Device Object from C++/COM

WPD Automation can be instantiated from C++/COM outside of script. Because the **IDispatch** interface was specifically designed for use by script, this approach is somewhat cumbersome and not recommended. However, the approach can offer a simplified way of programming against WPD; it is not explained further in this documentation.

## Related topics

<dl> <dt>

[About the WPD Automation Object Model](about-the-wpd-automation-object-model.md)
</dt> <dt>

[Instantiating the WPD Automation Factory](instantiating-the-wpd-automation-factory-interface.md)
</dt> <dt>

[WPD Automation Programming Guide](wpd-automation-programming-guide.md)
</dt> </dl>

 

 




