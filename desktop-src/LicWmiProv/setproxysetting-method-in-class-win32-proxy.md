---
Description: The SetProxySetting&\#8194;WMI class method creates a persistent Internet connection for Windows Product Activation (WPA) using the specified address and port number.
ms.assetid: 431fb980-6518-4b9b-8ca3-6e6d5471abf5
title: SetProxySetting method of the Win32\_Proxy class
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetProxySetting method of the Win32\_Proxy class

The **SetProxySetting** [WMI class](https://msdn.microsoft.com/library/aa393244) method creates a persistent Internet connection for Windows Product Activation (WPA) using the specified address and port number.

This topic uses Managed Object Format (MOF) syntax. For more information about using this method see [Calling a Method](https://msdn.microsoft.com/library/aa384832).

## Syntax


```mof
uint32 SetProxySetting(
  [in] string ProxyAddress,
  [in] string ProxyPortNumber
);
```



## Parameters

<dl> <dt>

*ProxyAddress* \[in\]
</dt> <dd>

Server name or IP address of the proxy server.

</dd> <dt>

*ProxyPortNumber* \[in\]
</dt> <dd>

Proxy port number.

</dd> </dl>

## Remarks

Because the proxy server setting is persistent, it may be advisable to query the class's properties before calling **SetProxySetting**. The original properties could then be restored if required.

This method is the scriptable equivalent to setting the proxy server using the **Connections** tab of the **Internet Options** dialog in Internet Explorer or in Control Panel.

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

[**Win32\_Proxy**](win32-proxy.md)
</dt> <dt>

[Windows Product Activation Provider](windows-product-activation-provider.md)
</dt> </dl>

 

 




