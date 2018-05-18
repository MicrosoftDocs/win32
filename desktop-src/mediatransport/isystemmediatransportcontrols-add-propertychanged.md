---
title: ISystemMediaTransportControls add\_PropertyChanged method
description: Adds an event handler for the PropertyChanged event.
ms.assetid: '8C3B2EBD-1D60-427E-893D-0F8B4977A70D'
keywords: ["add_PropertyChanged method", "add_PropertyChanged method, ISystemMediaTransportControls interface", "ISystemMediaTransportControls interface, add_PropertyChanged method"]
topic_type:
- apiref
api_name:
- ISystemMediaTransportControls.add_PropertyChanged
api_location:
- Windows.Media.SystemMediaTransportControls.h
api_type:
- COM
---

# ISystemMediaTransportControls::add\_PropertyChanged method

Adds an event handler for the [**PropertyChanged**](https://msdn.microsoft.com/library/windows/apps/dn278720) event.

## Syntax


```C++
HRESULT add_PropertyChanged(
   IEventHandler<ISystemMediaTransportControlsPropertyChangedEventArgs*> *handler,
   EventRegistrationToken                                                *token
);
```



## Parameters

<dl> <dt>

*handler* 
</dt> <dd>

Type: **[**IEventHandler&lt;ISystemMediaTransportControlsPropertyChangedEventArgs\*&gt;**](https://msdn.microsoft.com/library/windows/desktop/hh438385)\***

The delegate to a method that handles the button pressed event.

</dd> <dt>

*token* 
</dt> <dd>

Type: **[**EventRegistrationToken**](https://msdn.microsoft.com/library/windows/desktop/br205773)\***

A token that identifies the registered event handler.

</dd> </dl>

## Return value

Type: **[**HRESULT**](455d07e9-52c3-4efb-a9dc-2955cbfd38cc)**

This method returns one of the Direct3D 12 Return Codes.

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

 

 





