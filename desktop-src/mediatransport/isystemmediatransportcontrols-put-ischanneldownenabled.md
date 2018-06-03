---
title: ISystemMediaTransportControls put\_IsChannelDownEnabled method
description: Sets a value that specifies if the channel down button should be enabled.
ms.assetid: C85F8793-5DC0-48C0-8AC5-4FBE957EC3AB
keywords:
- put_IsChannelDownEnabled method
- put_IsChannelDownEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, put_IsChannelDownEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsChannelDownEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ISystemMediaTransportControls::put\_IsChannelDownEnabled method

Sets a value that specifies if the channel down button should be enabled.

## Syntax


```C++
HRESULT put_IsChannelDownEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the channel down button. Set to false to disable it.

</dd> </dl>

## Return value

Type: **[**HRESULT**](https://msdn.microsoft.com/windows/desktop/455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**ISystemMediaTransportControls**](isystemmediatransportcontrols.md)
</dt> </dl>

 

 





