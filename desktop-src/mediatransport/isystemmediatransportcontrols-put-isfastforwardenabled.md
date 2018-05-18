---
title: ISystemMediaTransportControls put\_IsFastForwardEnabled method
description: Sets a value that specifies if the fast forward button should be enabled.
ms.assetid: 'C0D771A4-C65D-4A09-9229-C519EF17E0F4'
keywords: ["put_IsFastForwardEnabled method", "put_IsFastForwardEnabled method, ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, put_IsFastForwardEnabled method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsFastForwardEnabled
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls::put\_IsFastForwardEnabled method

Sets a value that specifies if the fast forward button should be enabled.

## Syntax


```C++
HRESULT put_IsFastForwardEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the channel up button. Set to false to disable it.

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

 

 





