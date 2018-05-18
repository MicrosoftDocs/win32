---
title: ISystemMediaTransportControls get\_IsNextEnabled method
description: Gets a value that indicates if the next button is enabled.
ms.assetid: 'AE74671D-8060-430E-AF9C-3696FC692CEC'
keywords: ["get_IsNextEnabled method", "get_IsNextEnabled method, ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, get_IsNextEnabled method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_IsNextEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls::get\_IsNextEnabled method

Gets a value that indicates if the next button is enabled.

## Syntax


```C++
HRESULT get_IsNextEnabled(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **boolean\***

True if the next button is enabled.; otherwise false.

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

[**ISystemMediaTransportControls**](isystemmediatransportcontrols.md)
</dt> </dl>

 

 





