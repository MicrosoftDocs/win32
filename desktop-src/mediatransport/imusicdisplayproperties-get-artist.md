---
title: IMusicDisplayProperties get\_Artist method
description: Gets the artist of the music item.
ms.assetid: '9DE7A440-E397-4026-B90B-F53139091408'
keywords: ["get_Artist method", "get_Artist method, IMusicDisplayProperties interface", "IMusicDisplayProperties interface, get_Artist method"]
topic_type:
- apiref
api_name:
- IMusicDisplayProperties.get_Artist
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# IMusicDisplayProperties::get\_Artist method

Gets the artist of the music item.

## Syntax


```C++
HRESULT get_Artist(
  [out] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**HSTRING**](https://msdn.microsoft.com/library/windows/desktop/br205775)\***

The artist of the music item.

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

 

 





