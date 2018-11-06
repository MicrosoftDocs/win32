---
title: Device Parameters
description: Device Parameters
ms.assetid: d8774c85-b5c0-4d9e-8a8e-d60ffdf59549
keywords:
- Windows Media Device Manager,device parameters
- Device Manager,device parameters
- programming guide,device parameters
- service providers,device parameters
- creating service providers,device parameters
- device parameters
ms.topic: article
ms.date: 05/31/2018
---

# Device Parameters

Windows Media Device Manager uses device parameters to control the behavior of a device. These parameters are added to the registry as specified in the device's installation file (INF file). The following table lists the device parameters that Windows Media Device Manager queries.



| Device parameter name | Registry data type | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *WMDMSPCLSID*         | **REG\_SZ**        | Value that specifies the CLSID of the service provider controlling this device. This parameter is mandatory for PnP support.<br/> The parameter value must be the CLSID, not the ProgID of the service provider. This parameter is mandatory to support Plug and Play (PnP) under Windows Media Device Manager. For more information, see [Enabling PnP for Devices](enabling-pnp-for-devices.md).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| *OptimalTransferSize* | **REG\_DWORD**     | Optional value that specifies the preferred transfer size that Windows Media Device Manager uses during read and write operations. If it is not supplied, a default transfer size is used.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| *UseMetadataViews*    | **REG\_DWORD**     | Optional parameter that specifies whether Windows Media Device Manager organizes the content by metadata while presenting device content to applications. If not specified, the default value is 0.<br/> When applications enumerate the content on the storages of a portable audio player, Windows Media Device Manager can present the content organized by metadata. This is especially useful for devices with large storage capacity.<br/> Applications and devices have the ability to control this behavior. Devices indicate their preference through the device parameter *UseMetadataViews*.<br/> The following two integer values are supported:<br/> Requests that content be presented to the applications exactly as organized on the file system of the device.<br/> Requests that the content be presented to the applications organized by metadata.<br/> |
| *ShowInShell*         | **REG\_DWORD**     | Optional parameter that specifies whether the device should appear in Windows Explorer. The value 1 indicates that the device should appear in Windows Explorer. For more information, see [Requirements for Portable Audio Players to Appear in Windows Explorer](requirements-for-portable-audio-players-to-appear-in-windows-explorer.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *UseExtendedWmdm*     | **REG\_DWORD**     | Optional parameter that alerts Windows Media Device Manager that the service provider supports **IMDSPDevice3**, **IMDSPObject2**, and **IMDSPStorage4**. Without this flag, Windows Media Device Manager will never call these interfaces. The value 1 indicates that these interfaces are supported.<br/> This flag is required for service providers that synchronize with Windows Media Player. (See [Enabling Synchronization with Windows Media Player](enabling-synchronization-with-windows-media-player.md)).<br/>                                                                                                                                                                                                                                                                                                                                                                        |



 

**Coding the INF file**

The following example code from a device's INF file demonstrates setting some device parameters during device installation.


```C++
; Set parameters on Windows 95 and Windows 98 operating systems.
[DriverInstall.hw]
AddReg=DriverHwPropReg

; Set parameters on Windows NT-based operating systems.
[DriverInstall.NT.hw]
AddReg=DriverHwPropReg

; Related section that specifies the device parameters.
[DriverHwPropReg]
; Add your own CLSID here.
HKR,,WMDMSPCLSID,,"{00000000-0000-0000-0000-000000000000}"
HKR,,OptimalTransferSize,0x10001,0x10000
HKR,,UseMetadataViews,0x10001,0x1
```



## Related topics

<dl> <dt>

[**Creating a Service Provider**](creating-a-service-provider.md)
</dt> <dt>

[**IMDServiceProvider2 Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-imdserviceprovider2)
</dt> <dt>

[**IMDServiceProvider2::CreateDevice**](/windows/desktop/api/mswmdm/nf-mswmdm-imdserviceprovider2-createdevice)
</dt> <dt>

[**IWMDMDevice Interface**](/windows/desktop/api/mswmdm/nn-mswmdm-iwmdmdevice)
</dt> </dl>

 

 





