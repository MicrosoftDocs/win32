---
title: IVideoDisplayProperties get\_Subtitle method
description: Gets the subtitle of the video.
ms.assetid: F14C6E94-A14F-4A98-8ED3-E4295ABDF4AC
keywords:
- get_Subtitle method
- get_Subtitle method, IVideoDisplayProperties interface
- IVideoDisplayProperties interface, get_Subtitle method
topic_type:
- apiref
api_name:
- IVideoDisplayProperties.get_Subtitle
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

# IVideoDisplayProperties::get\_Subtitle method

Gets the subtitle of the video.

## Syntax


```C++
HRESULT get_Subtitle(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**HSTRING**](https://msdn.microsoft.com/library/windows/desktop/br205775)\***

The subtitle of the video.

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

[**IVideoDisplayProperties**](ivideodisplayproperties.md)
</dt> </dl>

 

 





