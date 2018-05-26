---
title: ISystemMediaTransportControls get\_IsPauseEnabled method
description: Gets a value that indicates if the pause button is enabled.
ms.assetid: 758811B0-3F04-4D11-9783-1D046A63BA57
keywords:
- get_IsPauseEnabled method
- get_IsPauseEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, get_IsPauseEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_IsPauseEnabled
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

# ISystemMediaTransportControls::get\_IsPauseEnabled method

Gets a value that indicates if the pause button is enabled.

## Syntax


```C++
HRESULT get_IsPauseEnabled(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **boolean\***

True if the pause button is enabled.; otherwise false.

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

 

 





