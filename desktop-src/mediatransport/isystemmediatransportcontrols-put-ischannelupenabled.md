---
title: ISystemMediaTransportControls put\_IsChannelUpEnabled method
description: Sets a value that specifies if the channel up button should be enabled.
ms.assetid: E3A53502-AAA8-405B-9D18-3D7D7EA9794C
keywords:
- put_IsChannelUpEnabled method
- put_IsChannelUpEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, put_IsChannelUpEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsChannelUpEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ISystemMediaTransportControls::put\_IsChannelUpEnabled method

Sets a value that specifies if the channel up button should be enabled.

## Syntax


```C++
HRESULT put_IsChannelUpEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the channel up button. Set to false to disable it.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

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

 

 





