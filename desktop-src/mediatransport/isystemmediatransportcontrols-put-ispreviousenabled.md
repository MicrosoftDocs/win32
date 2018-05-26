---
title: ISystemMediaTransportControls put\_IsPreviousEnabled method
description: Sets a value that specifies if the previous button should be enabled.
ms.assetid: 21CC1A21-9C0A-47C0-B00E-2E31F9B1BC22
keywords:
- put_IsPreviousEnabled method
- put_IsPreviousEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, put_IsPreviousEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsPreviousEnabled
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

# ISystemMediaTransportControls::put\_IsPreviousEnabled method

Sets a value that specifies if the previous button should be enabled.

## Syntax


```C++
HRESULT put_IsPreviousEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the previous button. Set to false to disable it.

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

 

 





