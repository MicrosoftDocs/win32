---
title: ISystemMediaTransportControls put\_IsStopEnabled method
description: Sets a value that specifies if the stop button should be enabled.
ms.assetid: 'F94064DE-8185-4C53-A633-92F99F873119'
keywords: ["put_IsStopEnabled method", "put_IsStopEnabled method, ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, put_IsStopEnabled method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsStopEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls::put\_IsStopEnabled method

Sets a value that specifies if the stop button should be enabled.

## Syntax


```C++
HRESULT put_IsStopEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the stop button. Set to false to disable it.

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

 

 





