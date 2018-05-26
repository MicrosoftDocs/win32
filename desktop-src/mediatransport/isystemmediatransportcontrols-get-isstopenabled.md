---
title: ISystemMediaTransportControls get\_IsStopEnabled method
description: Gets a value that indicates if the stop button is enabled.
ms.assetid: EA7BA62E-2095-4314-8ACB-6C2D2BB119A5
keywords:
- get_IsStopEnabled method
- get_IsStopEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, get_IsStopEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_IsStopEnabled
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

# ISystemMediaTransportControls::get\_IsStopEnabled method

Gets a value that indicates if the stop button is enabled.

## Syntax


```C++
HRESULT get_IsStopEnabled(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **boolean\***

True if the stop button is enabled; otherwise false.

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

 

 





