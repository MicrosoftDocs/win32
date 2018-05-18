---
title: ISystemMediaTransportControlsDisplayUpdater get\_MusicProperties method
description: Gets the music properties associated with the currently playing media.
ms.assetid: 'D6F89D71-FEA8-4C23-AE74-FAAC2A587C29'
keywords: ["get_MusicProperties method", "get_MusicProperties method, ISystemMediaTransportControlsDisplayUpdater interface", "ISystemMediaTransportControlsDisplayUpdater interface, get_MusicProperties method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsDisplayUpdater.get_MusicProperties
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControlsDisplayUpdater::get\_MusicProperties method

Gets the music properties associated with the currently playing media.

## Syntax


```C++
HRESULT get_MusicProperties(
  [out] IMusicDisplayProperties **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**IMusicDisplayProperties**](winrt-imusicdisplayproperties)\*\***

The music properties.

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

[**ISystemMediaTransportControlsDisplayUpdater**](isystemmediatransportcontrolsdisplayupdater.md)
</dt> </dl>

 

 





