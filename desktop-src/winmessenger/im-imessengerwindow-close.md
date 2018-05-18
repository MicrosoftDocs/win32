---
title: IMessengerWindow Close method
description: Closes a Messenger window. If the window is a conversation window, terminates any sessions contained in it.
ms.assetid: '8231ab48-f4fa-4ade-9b04-67f9dd6ed282'
keywords: ["Close method Windows Messenger", "Close method Windows Messenger , IMessengerWindow interface", "IMessengerWindow interface Windows Messenger , Close method"]
topic_type:
- apiref
api_name:
- IMessengerWindow.Close
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerWindow::Close method

\[**Close** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Closes a Messenger window. If the window is a conversation window, terminates any sessions contained in it.

## Syntax


```C++
HRESULT Close();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                      |
|-----------------------------------------------------------------------------------------|--------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Success. <br/>                             |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Messenger window was already closed. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>  | Could not get window handle. <br/>         |



 

## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                      |
|------------|------------------------------|
| 0x80004005 | Could not get window handle. |



 

Windows that are being closed while some actions are still in progress may return confirmation dialog boxes to the user, which will hang up the application until the user responds.

Closing the main application window effectively "knocks it into the tray." The object is still active and maintains a process, but does not appear on the taskbar. Closing a conversation window essentially de-references it. Further [**IMessengerWindow**](im-imessengerwindow.md) calls against that window will be invalid because the window and its internal object have been completely removed, not just hidden, from the client. After a conversation window has been closed, any pointers to it should be cleaned up.

> [!Note]  
> This method is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrWindow As MessengerAPI.IMessengerWindow

Private Sub cmd_W_Close_Click()
    MsgrWindow.Close
End Sub
```



## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>    | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>    | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessengerWindow**](im-imessengerwindow.md)
</dt> <dt>

[**IsClosed**](im-imessengerwindow-isclosed.md)
</dt> </dl>

 

 





