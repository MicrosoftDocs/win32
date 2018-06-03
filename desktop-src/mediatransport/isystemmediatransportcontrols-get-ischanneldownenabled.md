---
title: ISystemMediaTransportControls get\_IsChannelDownEnabled method
description: Gets a value that indicates if the channel down button is enabled.
ms.assetid: CDE64484-F876-42E5-AA86-CABA0AA4EA03
keywords:
- get_IsChannelDownEnabled method
- get_IsChannelDownEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, get_IsChannelDownEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.get_IsChannelDownEnabled
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

# ISystemMediaTransportControls::get\_IsChannelDownEnabled method

Gets a value that indicates if the channel down button is enabled.

## Syntax


```C++
HRESULT get_IsChannelDownEnabled(
  [out] boolean *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **boolean\***

True if the channel down button is enabled.; otherwise false.

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

 

 





