---
title: ISystemMediaTransportControlsDisplayUpdater put\_Type method
description: Sets the type of media currently playing.
ms.assetid: 280034B3-8B5E-4AD1-8214-642564F669BC
keywords:
- put_Type method
- put_Type method, ISystemMediaTransportControlsDisplayUpdater interface
- ISystemMediaTransportControlsDisplayUpdater interface, put_Type method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsDisplayUpdater.put_Type
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

# ISystemMediaTransportControlsDisplayUpdater::put\_Type method

Sets the type of media currently playing.

## Syntax


```C++
HRESULT put_Type(
   MediaPlaybackType value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **[**MediaPlaybackType**](https://msdn.microsoft.com/library/windows/apps/dn278668)**

The type of media currently playing.

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

[**ISystemMediaTransportControlsDisplayUpdater**](isystemmediatransportcontrolsdisplayupdater.md)
</dt> </dl>

 

 





