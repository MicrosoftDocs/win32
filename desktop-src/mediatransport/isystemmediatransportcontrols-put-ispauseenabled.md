---
title: ISystemMediaTransportControls put\_IsPauseEnabled method
description: Sets a value that specifies if the pause button should be enabled.
ms.assetid: CC07E4A0-0427-4EF5-AD87-AD824CACAC5F
keywords:
- put_IsPauseEnabled method
- put_IsPauseEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, put_IsPauseEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsPauseEnabled
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

# ISystemMediaTransportControls::put\_IsPauseEnabled method

Sets a value that specifies if the pause button should be enabled.

## Syntax


```C++
HRESULT put_IsPauseEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the pause button. Set to false to disable it.

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

 

 





