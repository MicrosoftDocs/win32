---
title: Battery Miniclass Driver Routines
description: Battery Miniclass Driver Routines
ms.assetid: de362d42-0185-4519-a5a6-b16e76d4dc4c
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Battery Miniclass Driver Routines

## 

Battery miniclass drivers must include routines to support Plug and Play (PnP) and to support battery management and monitoring. Entry points for the following routines are required to support standard operating system and PnP manager functionality:

<dl>

[*DriverEntry*](https://msdn.microsoft.com/library/windows/hardware/ff544113)  
[*AddDevice*](https://msdn.microsoft.com/library/windows/hardware/ff540521)  
[*DispatchDeviceControl*](https://www.bing.com/search?q=*DispatchDeviceControl*)  
[*DispatchPnP*](https://www.bing.com/search?q=*DispatchPnP*)  
[*DispatchPower*](https://www.bing.com/search?q=*DispatchPower*)  
[*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886)  
</dl>

For details on a battery minidriver's support for any of the above routines, see [Writing Battery Miniclass Drivers](https://msdn.microsoft.com/library/windows/hardware/ff536322).

Entry points for the following routines, described in this section, are required in all battery miniclass drivers:

<dl>

[*BatteryMiniDisableStatusNotify*](/windows/desktop/api/Batclass/nc-batclass-bclass_disable_status_notify_callback)  
[*BatteryMiniQueryInformation*](/windows/desktop/api/Batclass/nc-batclass-bclass_query_information_callback)  
[*BatteryMiniQueryStatus*](/windows/desktop/api/Batclass/nc-batclass-bclass_query_status_callback)  
[*BatteryMiniQueryTag*](/windows/desktop/api/Batclass/nc-batclass-bclass_query_tag_callback)  
[*BatteryMiniSetInformation*](/windows/desktop/api/Batclass/nc-batclass-bclass_set_information_callback)  
[*BatteryMiniSetStatusNotify*](/windows/desktop/api/Batclass/nc-batclass-bclass_set_status_notify_callback)  
</dl>

The battery class driver calls BatteryMini*Xxx* routines to get and set information about a specific battery device. Battery miniclass drivers must supply entry points for these routines. The BatteryMini*Xxx* routines can have any name chosen by the driver writer. Prototypes appear in the Batclass.h header file.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bbattery\battery%5D:%20Battery%20Miniclass%20Driver%20Routines%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




