---
title: IMessengerWindow IsClosed property
description: Retrieves a Boolean value that indicates the open or closed state of the window.
ms.assetid: '609041c7-4c36-4d8d-9257-93c724cef941'
keywords: ["IsClosed property Windows Messenger", "IsClosed property Windows Messenger , IMessengerWindow interface", "IMessengerWindow interface Windows Messenger , IsClosed property"]
topic_type:
- apiref
api_name:
- IMessengerWindow.IsClosed
- IMessengerWindow.get_IsClosed
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerWindow::IsClosed property

\[**IsClosed** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a Boolean value that indicates the open or closed state of the window.

This property is read-only.

## Syntax


```C++
HRESULT get_IsClosed(
  [out, retval] VARIANT_BOOL *pBoolClose
);
```



## Property value

Pointer to a **VARIANT\_BOOL** that defines the open and closed state for the Messenger window with one of the following possible values.



| Value                                                                                                                                                                                                                    | Meaning                                                                                                                                                                                                                                                                                                                                                                       |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="VARIANT_TRUE"></span><span id="variant_true"></span><dl> <dt>**VARIANT\_TRUE**</dt> <dt>true</dt> </dl>     | Messenger window is closed. This means that it has no HWND or window handle either numerically or on a system level. Attempts to reference some Win32 functions against the window will fail. The client can continue to exist as a running executable and can potentially be seen in process lists and in minimized form in the notification area or system tray.<br/> |
| <span id="VARIANT_FALSE"></span><span id="variant_false"></span><dl> <dt>**VARIANT\_FALSE**</dt> <dt>false</dt> </dl> | Messenger application window is either visible or minimized and has a valid HWND or window handle.<br/>                                                                                                                                                                                                                                                                 |



 

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                           |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pBoolClose* is a **NULL** pointer.<br/> |



## Remarks

This method is useful when this interface is called against the **Messenger** application window. The method can be called against a conversation window, but will return **FALSE** for any case in which a valid [**MessengerWindow**](im-messengerwindow.md) object existed to call the method against. If the conversation window that corresponds to the object had been closed by client action, then the object would have become unassigned and thrown an object reference error. A minimized window is considered to be closed or not closed based on the visibility settings through **Show**, **Close**, or equivalent user interface (UI) settings.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrWindow As MessengerAPI.IMessengerWindow

Private Sub Cmd_W_IsClosed_Click()
    If MsgrWindow.IsClosed = True Then
        MsgBox "Closed"
    Else
        MsgBox "Showed"
    End If
End Sub
```



## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IMessengerWindow**](im-imessengerwindow.md)
</dt> <dt>

[**Show**](im-imessengerwindow--show.md)
</dt> </dl>

 

 





