---
title: IMessengerWindow Left property
description: Sets or retrieves the left screen position of a Messenger window, in pixels.
ms.assetid: 'a83b972d-e5de-4547-9b0e-3a060aa99674'
keywords: ["Left property Windows Messenger", "Left property Windows Messenger , IMessengerWindow interface", "IMessengerWindow interface Windows Messenger , Left property"]
topic_type:
- apiref
api_name:
- IMessengerWindow.Left
- IMessengerWindow.get_Left
- IMessengerWindow.put_Left
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerWindow::Left property

\[**Left** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves the left screen position of a Messenger window, in pixels.

This property is read/write.

## Syntax


```C++
HRESULT put_Left(
  [in]          LONG lLeft
);

HRESULT get_Left(
  [out, retval] LONG *plLeft
);
```



## Property value

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                           |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                              |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *plLeft* is a **NULL** pointer.<br/>        |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Could not get window handle. <br/>          |
| <dl> <dt>E\_NOTIMPL</dt> </dl>                 | Cannot be accessed through scripting. <br/> |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                                                |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004001 | Cannot be accessed through scripting.                                                                                                  |
| 0x80004005 | Messenger application window or conversation window has been closed either through user action or the method that launched the window. |



 

If the Messenger window is minimized, the value retrieved will appear to be out of range (&gt;= -32000). If the Messenger window is closed through application programming interface (API) or user action, this method fails to get a value.

If this method called on the [**IMessengerWindow**](im-imessengerwindow.md) object of the parent application's Messenger window, it returns the left screen position value of the parent application window.

There is no bounds-checking on input values for *lLeft*. Negative integer values are accepted, but the window will go no further off the left side than half its width.

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



 

 





