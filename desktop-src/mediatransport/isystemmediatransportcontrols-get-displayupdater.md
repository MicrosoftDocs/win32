---
title: ISystemMediaTransportControls get\_DisplayUpdater method
description: Gets the display updater for the ISystemMediaTransportControls which enables updating the information displayed about the currently playing media item.
ms.assetid: 08A534DF-FBF1-4C0B-BB95-8E8F8ED36CA5
keywords:
- get_DisplayUpdater method
- get_DisplayUpdater method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, get_DisplayUpdater method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_DisplayUpdater
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

# ISystemMediaTransportControls::get\_DisplayUpdater method

Gets the display updater for the [**ISystemMediaTransportControls**](https://www.bing.com/search?q=**ISystemMediaTransportControls**) which enables updating the information displayed about the currently playing media item.

## Syntax


```C++
HRESULT get_DisplayUpdater(
  [out] ISystemMediaTransportControlsDisplayUpdater **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**ISystemMediaTransportControlsDisplayUpdater**](https://www.bing.com/search?q=**ISystemMediaTransportControlsDisplayUpdater**)\*\***

The display updater for the [**ISystemMediaTransportControls**](https://www.bing.com/search?q=**ISystemMediaTransportControls**).

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

 

 





