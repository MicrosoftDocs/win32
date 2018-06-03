---
Description: The Windows Product Activation (WPA) provider is an anti-piracy technology aimed at reducing the casual copying of software.
ms.assetid: 2d68caa8-76b0-44fe-96cd-ecbde075760e
title: Windows Product Activation Provider
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Windows Product Activation Provider

The Windows Product Activation (WPA) provider is an anti-piracy technology aimed at reducing the casual copying of software. WPA applies to all boxed 32-bit Microsoft product versions. WPA requires customers to contact a Microsoft Clearinghouse license server either online or by phone, to create an association between the product ID (PID) and the hardware ID of a computer. The association is required for system activation. The PID is derived from the customer's unique product key and the Microsoft product code. The hardware ID is derived from a number of machine characteristics. Successful system activation results in the installation of a unique, tamper-resistant license on the customer's system, which is then unlocked for normal use. Note that Windows Product Activation is not available on the Itanium-based versions of the Windows operating system.

The WMI WPA provider supports WPA administration using WMI interfaces, allowing uniform server administration. Administration is possible using the methods implemented by the provider. The WPA provider is a dynamic provider, implemented as a [Win32 Provider](https://msdn.microsoft.com/library/aa394388) object. The WPA provider is registered as both an instance provider and a method provider. The provider is an in-process dynamic-link library (DLL).

As a dynamic instance and class provider, the WPA provider supports the standard [**IWbemProviderInit**](https://msdn.microsoft.com/library/aa391853) interface, as well as the following methods of the [**IWbemServices**](https://msdn.microsoft.com/library/aa392093) interface:

-   [**CreateInstanceEnumAsync**](https://msdn.microsoft.com/library/aa392098)
-   [**ExecMethodAsync**](https://msdn.microsoft.com/library/aa392104)
-   [**GetObjectAsync**](https://msdn.microsoft.com/library/aa392110)
-   [**PutInstanceAsync**](https://msdn.microsoft.com/library/aa392116)

Because class properties are applicable to the local system but are not applicable on a per-client basis, there is one instance of the [**Win32\_WindowsProductActivation**](win32-windowsproductactivation.md) class.

The WPA provider supports the following classes, located in the \\root\\cimv2 namespace:

-   [**Win32\_ComputerSystemWindowsProductActivationSetting**](win32-computersystemwindowsproductactivationsetting.md)
-   [**Win32\_Proxy**](win32-proxy.md)
-   [**Win32\_WindowsProductActivation**](win32-windowsproductactivation.md)

## Related topics

<dl> <dt>

[WMI Providers](https://msdn.microsoft.com/library/aa394570)
</dt> </dl>

 

 



