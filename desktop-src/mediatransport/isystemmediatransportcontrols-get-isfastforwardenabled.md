---
title: ISystemMediaTransportControls get\_IsFastForwardEnabled method
description: Gets a value that indicates if the fast forward button is enabled.
ms.assetid: 'B8B13B3A-25A5-4D24-A824-AC7BCB1FFD72'
keywords: ["get_IsFastForwardEnabled method", "get_IsFastForwardEnabled method, ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, get_IsFastForwardEnabled method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_IsFastForwardEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls::get\_IsFastForwardEnabled method

Gets a value that indicates if the fast forward button is enabled.

## Syntax


```C++
HRESULT get_IsFastForwardEnabled(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **boolean\***

True if the fast forward button is enabled.; otherwise false.

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

 

 





