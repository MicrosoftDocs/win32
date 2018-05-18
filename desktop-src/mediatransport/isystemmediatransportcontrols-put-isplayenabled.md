---
title: ISystemMediaTransportControls put\_IsPlayEnabled method
description: Sets a value that specifies if the play button should be enabled.
ms.assetid: '09EBF9E7-555E-4C47-A4CC-DF5C19DE13B2'
keywords: ["put_IsPlayEnabled method", "put_IsPlayEnabled method, ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, put_IsPlayEnabled method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsPlayEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls::put\_IsPlayEnabled method

Sets a value that specifies if the play button should be enabled.

## Syntax


```C++
HRESULT put_IsPlayEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the play button. Set to false to disable it.

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

 

 





