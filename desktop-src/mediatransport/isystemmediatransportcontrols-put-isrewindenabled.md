---
title: ISystemMediaTransportControls put\_IsRewindEnabled method
description: Sets a value that specifies if the rewind button should be enabled.
ms.assetid: '31A7853D-15EA-4CD2-9A8A-D54A970B606B'
keywords: ["put_IsRewindEnabled method", "put_IsRewindEnabled method, ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, put_IsRewindEnabled method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsRewindEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls::put\_IsRewindEnabled method

Sets a value that specifies if the rewind button should be enabled.

## Syntax


```C++
HRESULT put_IsRewindEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the rewind button. Set to false to disable it.

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

 

 





