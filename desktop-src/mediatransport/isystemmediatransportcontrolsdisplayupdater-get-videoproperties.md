---
title: ISystemMediaTransportControlsDisplayUpdater get\_VideoProperties method
description: Gets the video properties associated with the currently playing media.
ms.assetid: '21BF262A-E8EB-4207-8FC3-2DCF20D3DFA1'
keywords: ["get_VideoProperties method", "get_VideoProperties method, ISystemMediaTransportControlsDisplayUpdater interface", "ISystemMediaTransportControlsDisplayUpdater interface, get_VideoProperties method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsDisplayUpdater.get_VideoProperties
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControlsDisplayUpdater::get\_VideoProperties method

Gets the video properties associated with the currently playing media.

## Syntax


```C++
HRESULT get_VideoProperties(
  [out] IVideoDisplayProperties **value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**IVideoDisplayProperties**](winrt-ivideodisplayproperties)\*\***

The video properties.

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

 

 





