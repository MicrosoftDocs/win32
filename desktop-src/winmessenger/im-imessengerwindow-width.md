---
title: IMessengerWindow Width property
description: Sets or retrieves the horizontal dimension of a Messenger window, in pixels.
ms.assetid: 3676f484-ddd8-4e40-b8f1-36d239dfbe64
keywords:
- Width property Windows Messenger
- Width property Windows Messenger , IMessengerWindow interface
- IMessengerWindow interface Windows Messenger , Width property
topic_type:
- apiref
api_name:
- IMessengerWindow.Width
- IMessengerWindow.get_Width
- IMessengerWindow.put_Width
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

# IMessengerWindow::Width property

\[**Width** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves the horizontal dimension of a Messenger window, in pixels.

This property is read/write.

## Syntax


```C++
HRESULT put_Width(
  [in]          LONG lWidth
);

HRESULT get_Width(
  [out, retval] LONG *plWidth
);
```



## Property value

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                       |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                          |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *plWidth* is a **NULL** pointer.<br/>                   |
| <dl> <dt>E\_INVALIDARG</dt> </dl>              | Attempted to set window to zero or negative width.<br/> |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Could not get window handle. <br/>                      |
| <dl> <dt>E\_NOTIMPL</dt> </dl>                 | Cannot be accessed through scripting. <br/>             |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                      |
|------------|------------------------------|
| 0x80004005 | Could not get window handle. |



 

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



 

 





