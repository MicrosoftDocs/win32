---
description: Providers, unless they are decoupled providers running within an application, are loaded in a Wmiprvse.exe process, and not through Svchost.exe with a Winmgmt.exe process. For more information, see Provider Hosting and Security.
ms.assetid: 8958669e-07e6-458c-a7f3-2df21cacc007
ms.tgt_platform: multiple
title: Debugging Providers
ms.topic: article
ms.date: 05/31/2018
---

# Debugging Providers

Providers, unless they are [*decoupled providers*](gloss-d.md) running within an application, are loaded in a Wmiprvse.exe process, and not through Svchost.exe with a Winmgmt.exe process. For more information, see [Provider Hosting and Security](provider-hosting-and-security.md).

When stopping at a breakpoint, the Visual Studio debugger freezes the entire provider host process, which is usually the shared host Wmiprvse.exe. This prevents the operation of any other components hosted in that process, including the WMI Server Explorer extension. Client applications that call into the provider are also blocked. The problems that result are worse in Windows 2000 and earlier because the provider is loaded into the WMI service process (Winmgmt.exe).

If you run WMI Server Explorer in another instance then Visual Studio IDE does not freeze and you are able to release the breakpoint. It is recommended that you run your provider in a separate hosting process during the development phase, so that stopping at a breakpoint only freezes the process hosting your provider. The other functions in WMI continue to be accessible to WMI Server Explorer and any other WMI-based applications or scripts. Also, if your provider crashes, it does not affect the operation of other providers loaded into the same host process.

To make your provider load in its own host process, modify the provider registration to set the [**\_\_Win32Provider.HostingModel**](--win32provider.md) property to `NetworkServiceHost:[MyProvider]` where MyProvider can be any string that uniquely identifies your provider. For example, use the **\_\_Win32Provider.ClsId** value. When your provider is ready to ship, return **\_\_Win32Provider.HostingModel** to the intended value, such as **NetworkServiceHost**.

If you are not debugging provider loading, you can call the [**Load method of the MSFT\_Providers class**](/previous-versions/windows/desktop/wmisystemprov/load-method-in-class-msft-providers) to force your provider to load, then attach to the Wmiprvse.exe process that has the DLL loaded, and debug as needed.

## Related topics

<dl> <dt>

[WMI Troubleshooting](wmi-troubleshooting.md)
</dt> <dt>

[WMI Troubleshooting Classes](wmi-troubleshooting-classes.md)
</dt> </dl>

 

 
