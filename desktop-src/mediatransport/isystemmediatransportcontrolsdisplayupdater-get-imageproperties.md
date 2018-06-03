---
title: ISystemMediaTransportControlsDisplayUpdater get\_ImageProperties method
description: Gets the image properties associated with the currently playing media.
ms.assetid: C4BDCF05-5439-4486-B42E-B881A29221F4
keywords:
- get_ImageProperties method
- get_ImageProperties method, ISystemMediaTransportControlsDisplayUpdater interface
- ISystemMediaTransportControlsDisplayUpdater interface, get_ImageProperties method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsDisplayUpdater.get_ImageProperties
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

# ISystemMediaTransportControlsDisplayUpdater::get\_ImageProperties method

Gets the image properties associated with the currently playing media.

## Syntax


```C++
HRESULT get_ImageProperties(
  [out] IImageDisplayProperties **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**IImageDisplayProperties**](https://www.bing.com/search?q=**IImageDisplayProperties**)\*\***

The image properties

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

 

 





