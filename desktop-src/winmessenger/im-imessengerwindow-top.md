---
title: IMessengerWindow Top property
description: Sets or retrieves the vertical position of a Messenger window relative to the screen, in pixels.
ms.assetid: 'c468e128-728b-4e8a-a648-bd39c51fd639'
keywords: ["Top property Windows Messenger", "Top property Windows Messenger , IMessengerWindow interface", "IMessengerWindow interface Windows Messenger , Top property"]
topic_type:
- apiref
api_name:
- IMessengerWindow.Top
- IMessengerWindow.get_Top
- IMessengerWindow.put_Top
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerWindow::Top property

\[**Top** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves the vertical position of a Messenger window relative to the screen, in pixels.

This property is read/write.

## Syntax


```C++
HRESULT put_Top(
  [in]          LONG lTop
);

HRESULT get_Top(
  [out, retval] LONG *plTop
);
```



## Property value

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                                                                                           |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success.<br/>                                                                                                                               |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *plTop* is a **NULL** pointer.<br/>                                                                                                         |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Messenger application window or conversation window has been closed either through user action or the method that launched the window.<br/> |
| <dl> <dt>E\_NOTIMPL</dt> </dl>                 | Cannot be accessed through scripting. <br/>                                                                                                 |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                       |
|------------|---------------------------------------------------------------------------------------------------------------|
| 0x80004001 | Cannot be accessed through scripting.                                                                         |
| 0x80004005 | Messenger window was invisible or not responding, cannot be moved or resized, or its HWND could not be found. |



 

If the Messenger window is minimized, the value retrieved will be a seemingly out-of-range value (&gt;= -32000). This behavior is fairly common in automation APIs. If the Messenger window is closed through API or user action, this method fails to get a value and returns E\_FAIL.

If this method is called on the [**IMessengerWindow**](im-imessengerwindow.md) interface of the parent application's Messenger window, it returns the top screen position value of the parent application window.

> [!Note]  
> This property is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrWindow As MessengerAPI.IMessengerWindow

Private Sub Form_Load()
    Text_Top.Text = CStr(MsgrWindow.Top)
    Text_Height.Text = CStr(MsgrWindow.Height)
    Text_Left.Text = CStr(MsgrWindow.Left)
    Text_Width.Text = CStr(MsgrWindow.Width)
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



 

 





