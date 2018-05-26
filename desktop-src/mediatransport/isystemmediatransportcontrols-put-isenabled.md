---
title: ISystemMediaTransportControls put\_IsEnabled method
description: Sets a value that specifies if the system media transport controls should be enabled for the calling app.
ms.assetid: C342E6EC-8F0D-42B7-B1CB-18363DCE4457
keywords:
- put_IsEnabled method
- put_IsEnabled method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, put_IsEnabled method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.put_IsEnabled
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

# ISystemMediaTransportControls::put\_IsEnabled method

Sets a value that specifies if the system media transport controls should be enabled for the calling app.

## Syntax


```C++
HRESULT put_IsEnabled(
   boolean value
);
```



## Parameters

<dl> <dt>

*value* 
</dt> <dd>

Type: **boolean**

Set to true to enable the system media transport controls. Set to false to disable them.

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

 

 





