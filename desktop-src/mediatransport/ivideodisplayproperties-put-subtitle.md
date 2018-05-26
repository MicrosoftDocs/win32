---
title: IVideoDisplayProperties put\_Subtitle method
description: Sets the subtitle of the video.
ms.assetid: D0053707-70DA-457D-9A04-7ECB8F5105D9
keywords:
- put_Subtitle method
- put_Subtitle method, IVideoDisplayProperties interface
- IVideoDisplayProperties interface, put_Subtitle method
topic_type:
- apiref
api_name:
- IVideoDisplayProperties.put_Subtitle
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

# IVideoDisplayProperties::put\_Subtitle method

Sets the subtitle of the video.

## Syntax


```C++
HRESULT put_Subtitle(
   HSTRING value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **[**HSTRING**](https://msdn.microsoft.com/library/windows/desktop/br205775)**

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

 

 





