---
title: IMessengerWindow HWND property
description: Retrieves a window handle to a Messenger window.
ms.assetid: 74b8af5b-7e17-4202-a21a-3595e3e6c2fe
keywords:
- HWND property Windows Messenger
- HWND property Windows Messenger , IMessengerWindow interface
- IMessengerWindow interface Windows Messenger , HWND property
topic_type:
- apiref
api_name:
- IMessengerWindow.HWND
- IMessengerWindow.get_HWND
api_location:
- Msgsc.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMessengerWindow::HWND property

\[**HWND** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a window handle to a Messenger window.

This property is read-only.

## Syntax


```C++
HRESULT get_HWND(
  [out, retval] long *phWnd
);
```



## Property value

Pointer to a **LONG** that receives a HWND handle to this Messenger window.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                           |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                              |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *phWnd* is a **NULL** pointer.<br/>         |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Could not get window handle. <br/>          |
| <dl> <dt>E\_NOTIMPL</dt> </dl>                 | Cannot be accessed through scripting. <br/> |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                                                |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004001 | Cannot be accessed through scripting.                                                                                                  |
| 0x80004005 | Messenger application window or conversation window has been closed either through user action or the method that launched the window. |



 

Unlike the Messenger application, there can be more than one conversation window and therefore multiple HWNDs.

If called on the IMessengerWindow interface of the application's Messenger window, it will return an HWND for the parent application.

> [!Note]  
> This property is not available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessengerWindow**](im-imessengerwindow.md)
</dt> <dt>

[**IMessenger**](im-imessenger.md)
</dt> </dl>

 

 





