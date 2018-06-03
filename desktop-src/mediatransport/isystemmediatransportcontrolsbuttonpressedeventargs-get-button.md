---
title: ISystemMediaTransportControlsButtonPressedEventArgs get\_Button method
description: Gets a value indicating the button that was pressed to trigger the event.
ms.assetid: 169E2EE6-1AB0-42A4-8DEB-8E45FB03B696
keywords:
- get_Button method
- get_Button method, ISystemMediaTransportControlsButtonPressedEventArgs interface
- ISystemMediaTransportControlsButtonPressedEventArgs interface, get_Button method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsButtonPressedEventArgs.get_Button
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

# ISystemMediaTransportControlsButtonPressedEventArgs::get\_Button method

Gets a value indicating the button that was pressed to trigger the event.

## Syntax


```C++
HRESULT get_Button(
  [out] SystemMediaTransportControlsButton *value
);
```



## Parameters

<dl> <dt>

*value* \[out\]
</dt> <dd>

Type: **[**SystemMediaTransportControlsButton**](https://www.bing.com/search?q=**SystemMediaTransportControlsButton**)\***

A value indicating the button that was pressed to trigger the event.

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

[**ISystemMediaTransportControlsButtonPressedEventArgs**](isystemmediatransportcontrolsbuttonpressedeventargs.md)
</dt> </dl>

 

 





