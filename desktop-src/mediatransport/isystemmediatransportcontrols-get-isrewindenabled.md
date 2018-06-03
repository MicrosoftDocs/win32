---
title: ISystemMediaTransportControls get\_IsRewindEnabled method
description: Gets a value that indicates if the rewind button is enabled.
ms.assetid: 9A92E9B2-2CE5-4A93-AB2C-BEF52DDEC9E6
keywords:
- get_IsRewindEnabled method
- get_IsRewindEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, get_IsRewindEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_IsRewindEnabled
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

# ISystemMediaTransportControls::get\_IsRewindEnabled method

Gets a value that indicates if the rewind button is enabled.

## Syntax


```C++
HRESULT get_IsRewindEnabled(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **boolean\***

True if the rewind button is enabled; otherwise false.

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

 

 





