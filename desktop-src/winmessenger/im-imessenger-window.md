---
title: IMessenger Window property
description: Gets a pointer to a MessengerWindow object that is used to control automation properties of the main application window, including dimensions, positioning, and visibility.
ms.assetid: 0b6eb741-29b3-48dd-8c67-8a07f486bb6c
keywords:
- Window property Windows Messenger
- Window property Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , Window property
topic_type:
- apiref
api_name:
- IMessenger.Window
- IMessenger.get_Window
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessenger::Window property

\[**Window** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Gets a pointer to a [**MessengerWindow**](im-messengerwindow.md) object that is used to control automation properties of the main application window, including dimensions, positioning, and visibility.

This property is read-only.

## Syntax


```C++
HRESULT get_Window(
  [out, retval] IDispatch **ppMWindow
);
```



## Property value

Return value. Address of a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerWindow**](im-messengerwindow.md) object. This object can now be accessed through its [**IMessengerWindow**](im-imessengerwindow.md) interface.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. See Remarks.<br/>               |
| <dl> <dt>E\_INVALIDARG</dt> </dl>              | Client not responding.<br/>              |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Client not responding.<br/>              |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *ppMWindow* is a **NULL** pointer. <br/> |



## Remarks

This property allows access to an object with the [**IMessengerWindow**](im-imessengerwindow.md) interface that is used to implement a number of other common automation properties, including [**Height**](im-imessengerwindow-height.md), [**Width**](im-imessengerwindow-width.md), [**Top**](im-imessengerwindow-top.md), [**Left**](im-imessengerwindow-left.md), and [**Show**](im-imessengerwindow--show.md).

> [!Note]  
> This property is available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





