---
title: ISystemMediaTransportControls get\_IsEnabled method
description: Gets a value that indicates if the system media transport controls are enabled for the calling app.
ms.assetid: 3543D6C8-A929-4575-AAB3-154AF4C39DD9
keywords:
- get_IsEnabled method
- get_IsEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, get_IsEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_IsEnabled
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

# ISystemMediaTransportControls::get\_IsEnabled method

Gets a value that indicates if the system media transport controls are enabled for the calling app.

## Syntax


```C++
HRESULT get_IsEnabled(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **boolean\***

True if the the system media transport controls are enabled; otherwise false.

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

 

 





