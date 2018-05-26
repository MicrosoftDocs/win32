---
title: ISystemMediaTransportControls add\_ButtonPressed method
description: Adds an event handler for the ButtonPressed event.
ms.assetid: BF105CD7-03EA-4B40-A38C-D4F50180D46F
keywords:
- add_ButtonPressed method
- add_ButtonPressed method, ISystemMediaTransportControls interface
- ISystemMediaTransportControls interface, add_ButtonPressed method
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.add_ButtonPressed
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

# ISystemMediaTransportControls::add\_ButtonPressed method

Adds an event handler for the [**ButtonPressed**](https://msdn.microsoft.com/library/windows/apps/dn278706) event.

## Syntax


```C++
HRESULT add_ButtonPressed(
        IEventHandler<ISystemMediaTransportControlsButtonPressedEventArgs*> *handler,
  [out] EventRegistrationToken                                              *token
);
```



## Parameters

<dl> <dt>

*handler* 
</dt> <dd>

Type: **[**IEventHandler&lt;ISystemMediaTransportControlsButtonPressedEventArgs\*&gt;**](https://msdn.microsoft.com/library/windows/desktop/hh438385)\***

The delegate to a method that handles the button pressed event.

</dd> <dt>

*token* \[out\]
</dt> <dd>

Type: **[**EventRegistrationToken**](https://msdn.microsoft.com/library/windows/desktop/br205773)\***

A token that identifies the registered event handler.

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

 

 





