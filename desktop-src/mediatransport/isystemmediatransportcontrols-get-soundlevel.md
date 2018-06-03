---
title: ISystemMediaTransportControls get\_SoundLevel method
description: Gets the sound level of the media for the capture and render streams.
ms.assetid: 892837F1-8387-423A-BE61-9A244C5F5B90
keywords:
- get_SoundLevel method
- get_SoundLevel method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, get_SoundLevel method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_SoundLevel
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

# ISystemMediaTransportControls::get\_SoundLevel method

Gets the sound level of the media for the capture and render streams.

## Syntax


```C++
HRESULT get_SoundLevel(
   SoundLevel *value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **[**SoundLevel**](https://msdn.microsoft.com/library/windows/apps/hh700852)\***

The sound level.

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

 

 





