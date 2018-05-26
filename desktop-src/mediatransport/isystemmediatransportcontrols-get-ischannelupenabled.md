---
title: ISystemMediaTransportControls get\_IsChannelUpEnabled method
description: Gets a value that indicates if the channel up button is enabled.
ms.assetid: 7954C08A-2596-4C55-9D57-9B6E8850A8AC
keywords:
- get_IsChannelUpEnabled method
- get_IsChannelUpEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, get_IsChannelUpEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_IsChannelUpEnabled
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

# ISystemMediaTransportControls::get\_IsChannelUpEnabled method

Gets a value that indicates if the channel up button is enabled.

## Syntax


```C++
HRESULT get_IsChannelUpEnabled(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **boolean\***

True if the channel up button is enabled.; otherwise false.

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

[**ISystemMediaTransportControls**](isystemmediatransportcontrols.md)
</dt> </dl>

 

 





