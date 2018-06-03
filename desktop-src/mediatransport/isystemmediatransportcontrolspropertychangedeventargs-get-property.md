---
title: ISystemMediaTransportControlsPropertyChangedEventArgs get\_Property method
description: Gets a value indicating the property that was changed.
ms.assetid: 10FF73FF-1D2F-4754-8427-A2433815FB1E
keywords:
- get_Property method
- get_Property method, ISystemMediaTransportControlsPropertyChangedEventArgs interface
- ISystemMediaTransportControlsPropertyChangedEventArgs interface, get_Property method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControlsPropertyChangedEventArgs.get_Property
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

# ISystemMediaTransportControlsPropertyChangedEventArgs::get\_Property method

Gets a value indicating the property that was changed.

## Syntax


```C++
HRESULT get_Property(
  [out] SystemMediaTransportControlsProperty *
);
```



## Parameters

<dl> <dt>

 \[out\]
</dt> <dd>

A value indicating the property that was changed.

</dd> </dl>

## Return value

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

[**ISystemMediaTransportControlsPropertyChangedEventArgs**](isystemmediatransportcontrolspropertychangedeventargs.md)
</dt> </dl>

 

 





