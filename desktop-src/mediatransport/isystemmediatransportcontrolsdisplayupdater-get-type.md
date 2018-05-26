---
title: ISystemMediaTransportControlsDisplayUpdater get\_Type method
description: Gets the type of media currently playing.
ms.assetid: ED10E7AD-96AD-48A8-918E-57CA7DAF93FB
keywords:
- get_Type method
- get_Type method, ISystemMediaTransportControlsDisplayUpdater interface
- ISystemMediaTransportControlsDisplayUpdater interface, get_Type method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsDisplayUpdater.get_Type
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

# ISystemMediaTransportControlsDisplayUpdater::get\_Type method

Gets the type of media currently playing.

## Syntax


```C++
HRESULT get_Type(
  [out] MediaPlaybackType *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**MediaPlaybackType**](https://msdn.microsoft.com/library/windows/apps/dn278668)\***

The type of media currently playing.

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

 

 





