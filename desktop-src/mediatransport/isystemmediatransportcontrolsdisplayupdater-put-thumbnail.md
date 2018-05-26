---
title: ISystemMediaTransportControlsDisplayUpdater put\_Thumbnail method
description: Sets the thumbnail image associated with the currently playing media.
ms.assetid: 3ABDF548-6895-4D74-BD0B-40CC18A893EF
keywords:
- put_Thumbnail method
- put_Thumbnail method, ISystemMediaTransportControlsDisplayUpdater interface
- ISystemMediaTransportControlsDisplayUpdater interface, put_Thumbnail method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsDisplayUpdater.put_Thumbnail
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

# ISystemMediaTransportControlsDisplayUpdater::put\_Thumbnail method

Sets the thumbnail image associated with the currently playing media.

## Syntax


```C++
HRESULT put_Thumbnail(
   IRandomAccessStreamReference *value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **[**IRandomAccessStreamReference**](https://msdn.microsoft.com/library/windows/apps/hh701664)\***

The thumbnail image

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

 

 





