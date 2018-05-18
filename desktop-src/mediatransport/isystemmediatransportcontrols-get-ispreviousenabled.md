---
title: ISystemMediaTransportControls get\_IsPreviousEnabled method
description: Gets a value that indicates if the previous button is enabled.
ms.assetid: 'C8956829-51FE-47CC-A75D-80EE23957D6B'
keywords: ["get_IsPreviousEnabled method", "get_IsPreviousEnabled method, ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, get_IsPreviousEnabled method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_IsPreviousEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls::get\_IsPreviousEnabled method

Gets a value that indicates if the previous button is enabled.

## Syntax


```C++
HRESULT get_IsPreviousEnabled(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **boolean\***

True if the previous button is enabled.; otherwise false.

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

 

 





