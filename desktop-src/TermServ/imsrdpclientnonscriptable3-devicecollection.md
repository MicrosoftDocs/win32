---
title: IMsRdpClientNonScriptable3 DeviceCollection property
description: Retrieves the collection of Plug and Play (PnP) device objects to be redirected.
ms.assetid: dd5fe4c7-58bf-4e7a-b066-59278419ea6f
ms.tgt_platform: multiple
keywords:
- DeviceCollection property Remote Desktop Services
- DeviceCollection property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , DeviceCollection property
- DeviceCollection property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , DeviceCollection property
- DeviceCollection property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , DeviceCollection property
- DeviceCollection property Remote Desktop Services , MsRdpClient5 object
- MsRdpClient5 object Remote Desktop Services , DeviceCollection property
- DeviceCollection property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , DeviceCollection property
- DeviceCollection property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , DeviceCollection property
- DeviceCollection property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , DeviceCollection property
- DeviceCollection property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , DeviceCollection property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable3.DeviceCollection
- IMsRdpClientNonScriptable3.get_DeviceCollection
- IMsRdpClientNonScriptable4.DeviceCollection
- IMsRdpClientNonScriptable4.get_DeviceCollection
- IMsRdpClientNonScriptable5.DeviceCollection
- IMsRdpClientNonScriptable5.get_DeviceCollection
- MsRdpClient5.DeviceCollection
- MsRdpClient6.DeviceCollection
- MsRdpClient7.DeviceCollection
- MsRdpClient8.DeviceCollection
- MsRdpClient9.DeviceCollection
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable3::DeviceCollection property

Retrieves the collection of Plug and Play (PnP) device objects to be redirected.

This property is read-only.

## Syntax


```C++
HRESULT get_DeviceCollection(
  [out] IMSRdpDeviceCollection **ppDeviceCollection
);
```



## Property value

Retrieves the collection of PnP device objects of type [**IMSRdpDevice**](imsrdpdevice.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| IID<br/>                      | IID\_IMsRdpClientNonScriptable3 is defined as b3378d90-0728-45c7-8ed7-b6159fb92219<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
</dt> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> <dt>

[**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md)
</dt> </dl>

 

 





