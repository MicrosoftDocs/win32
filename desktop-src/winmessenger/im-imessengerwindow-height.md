---
title: IMessengerWindow Height property
description: Sets or retrieves the height of a Messenger window.
ms.assetid: 97e49f04-18ec-443e-aae2-1ba5784a1f82
keywords:
- Height property Windows Messenger
- Height property Windows Messenger , IMessengerWindow interface
- IMessengerWindow interface Windows Messenger , Height property
topic_type:
- apiref
api_name:
- IMessengerWindow.Height
- IMessengerWindow.get_Height
- IMessengerWindow.put_Height
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

# IMessengerWindow::Height property

\[**Height** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves the height of a Messenger window.

This property is read/write.

## Syntax


```C++
HRESULT put_Height(
           LONG lHeight
);

HRESULT get_Height(
  [retval] LONG *plHeight
);
```



## Property value

**LONG** that sets the height of the Messenger window in pixels.

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                       |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                          |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *plHeight* is a **NULL** pointer.<br/>                  |
| <dl> <dt>E\_INVALIDARG</dt> </dl>              | Attempted to set window to zero or negative width.<br/> |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Could not get window handle. <br/>                      |
| <dl> <dt>E\_NOTIMPL</dt> </dl>                 | Cannot be accessed through scripting. <br/>             |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                                                |
|------------|----------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004001 | Cannot be accessed through scripting.                                                                                                  |
| 0x80004005 | Messenger application window or conversation window has been closed either through user action or the method that launched the window. |
| 0x80070057 | Attempted to set window to zero or negative height.                                                                                    |



 

If the Messenger window is closed (only available from the taskbar), not responding, or if the HWND could not be found, this method will fail.

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
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





