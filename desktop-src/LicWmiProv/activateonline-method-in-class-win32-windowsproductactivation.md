---
Description: Exchanges license-related data with the Microsoft Clearinghouse license server.
ms.assetid: fb0b6862-1466-4ef9-8231-4b287a9bdc41
title: ActivateOnline method of the Win32\_WindowsProductActivation class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ActivateOnline method of the Win32\_WindowsProductActivation class

The **ActivateOnline** [WMI class](https://msdn.microsoft.com/library/aa393244) method exchanges license-related data with the Microsoft Clearinghouse license server. If the exchange succeeds, this method completes system activation. This method requires that the target computer communicate through the Internet using the HTTPS protocol.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method, see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 ActivateOnline();
```



## Parameters

This method has no parameters.

## Remarks

You can call the [**SetProxySetting**](setproxysetting-method-in-class-win32-proxy.md) method before calling **ActivateOnline** to connect to the Internet through a firewall.

> [!Note]  
> Windows Product Activation is not available on the Itanium-based versions of the Windows operating system.

 

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2003<br/>                                                        |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003 R2<br/>                                                     |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                |
| MOF<br/>                      | <dl> <dt>Licwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Licwmi.dll</dt> </dl> |



## See also

<dl> <dt>

[**Win32\_WindowsProductActivation**](win32-windowsproductactivation.md)
</dt> <dt>

[Windows Product Activation Provider](windows-product-activation-provider.md)
</dt> </dl>

 

 




