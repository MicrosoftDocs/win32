---
title: IMusicDisplayProperties get\_AlbumArtist method
description: Gets the album artist of the music item.
ms.assetid: '60C41B1F-8509-4AE0-B11D-90E645AA8071'
keywords: ["get_AlbumArtist method", "get_AlbumArtist method, IMusicDisplayProperties interface", "IMusicDisplayProperties interface, get_AlbumArtist method"]
topic_type:
- apiref
api_name:
- IMusicDisplayProperties.get_AlbumArtist
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# IMusicDisplayProperties::get\_AlbumArtist method

Gets the album artist of the music item.

## Syntax


```C++
HRESULT get_AlbumArtist(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**HSTRING**](https://msdn.microsoft.com/library/windows/desktop/br205775)\***

The album artist of the music item.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                                                           |
|-------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                                                      |
| Header<br/>                   | <dl> <dt>Windows.Media.SystemMediaTransportControls.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Windows.Media.SystemMediaTransportControls.idl</dt> </dl> |



## See also

<dl> <dt>

[**IMusicDisplayProperties**](imusicdisplayproperties.md)
</dt> </dl>

 

 





