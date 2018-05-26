---
title: ISystemMediaTransportControlsDisplayUpdater get\_Thumbnail method
description: Gets the thumbnail image associated with the currently playing media.
ms.assetid: 371993E7-92A9-42DE-A32E-2451857A92FA
keywords:
- get_Thumbnail method
- get_Thumbnail method, ISystemMediaTransportControlsDisplayUpdater interface
- ISystemMediaTransportControlsDisplayUpdater interface, get_Thumbnail method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsDisplayUpdater.get_Thumbnail
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

# ISystemMediaTransportControlsDisplayUpdater::get\_Thumbnail method

Gets the thumbnail image associated with the currently playing media.

## Syntax


```C++
HRESULT get_Thumbnail(
  [out] IRandomAccessStreamReference **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**IRandomAccessStreamReference**](https://msdn.microsoft.com/library/windows/apps/hh701664)\*\***

The thumbnail image.

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

[**ISystemMediaTransportControlsDisplayUpdater**](isystemmediatransportcontrolsdisplayupdater.md)
</dt> </dl>

 

 





