---
title: IMsRdpClientNonScriptable3 DriveCollection property
description: Retrieves the collection of drive objects to be redirected.
ms.assetid: 5aaac605-584b-442e-9d67-1cb8213a70b3
ms.tgt_platform: multiple
keywords:
- DriveCollection property Remote Desktop Services
- DriveCollection property Remote Desktop Services , IMsRdpClientNonScriptable3 interface
- IMsRdpClientNonScriptable3 interface Remote Desktop Services , DriveCollection property
- DriveCollection property Remote Desktop Services , IMsRdpClientNonScriptable4 interface
- IMsRdpClientNonScriptable4 interface Remote Desktop Services , DriveCollection property
- DriveCollection property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , DriveCollection property
- DriveCollection property Remote Desktop Services , MsRdpClient5 object
- MsRdpClient5 object Remote Desktop Services , DriveCollection property
- DriveCollection property Remote Desktop Services , MsRdpClient6 object
- MsRdpClient6 object Remote Desktop Services , DriveCollection property
- DriveCollection property Remote Desktop Services , MsRdpClient7 object
- MsRdpClient7 object Remote Desktop Services , DriveCollection property
- DriveCollection property Remote Desktop Services , MsRdpClient8 object
- MsRdpClient8 object Remote Desktop Services , DriveCollection property
- DriveCollection property Remote Desktop Services , MsRdpClient9 object
- MsRdpClient9 object Remote Desktop Services , DriveCollection property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable3.DriveCollection
- IMsRdpClientNonScriptable3.get_DriveCollection
- IMsRdpClientNonScriptable4.DriveCollection
- IMsRdpClientNonScriptable4.get_DriveCollection
- IMsRdpClientNonScriptable5.DriveCollection
- IMsRdpClientNonScriptable5.get_DriveCollection
- MsRdpClient5.DriveCollection
- MsRdpClient6.DriveCollection
- MsRdpClient7.DriveCollection
- MsRdpClient8.DriveCollection
- MsRdpClient9.DriveCollection
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable3::DriveCollection property

Retrieves the collection of drive objects to be redirected.

This property is read-only.

## Syntax


```C++
HRESULT get_DriveCollection(
  [out] IMsRdpDriveCollection **ppDriveCollection
);
```



## Property value

Retrieves the collection of drive objects of type [**IMSRdpDrive**](imsrdpdrive.md).

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

 

 





