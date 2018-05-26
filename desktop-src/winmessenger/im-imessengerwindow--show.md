---
title: IMessengerWindow Show method
description: Sets the visibility status of a Messenger window.
ms.assetid: 344c0f38-982f-4cd0-813c-4e683efbc470
keywords:
- Show method Windows Messenger
- Show method Windows Messenger , IMessengerWindow interface
- IMessengerWindow interface Windows Messenger , Show method
topic_type:
- apiref
api_name:
- IMessengerWindow.Show
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

# IMessengerWindow::Show method

\[**Show** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets the visibility status of a Messenger window.

## Syntax


```C++
HRESULT Show();
```



## Parameters

This method has no parameters.

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                            | Description                                                                                                                  |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>   | Success. The window might already have been in that visibility state, in which case no separate code is returned.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl> | Window instance destroyed. <br/>                                                                                       |



 

## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                    |
|------------|----------------------------|
| 0x80004005 | Window instance destroyed. |



 

This method is generally called in cases in which [**IsClosed**](im-imessengerwindow-isclosed.md) returns **TRUE**. Calling **Show** will redisplay the Messenger application window or a conversation window (depending on the type of window to which the [**MessengerWindow**](im-messengerwindow.md) object corresponds).

If the last state of the window was minimized by user action, then the window will become both visible and drawn to the last default sizing. A minimized window is the only scenario in which calling **Show** on a conversation rather than main application window would be useful. Had the conversation window been previously closed, then the object itself would have disappeared. Calling the **Show** method, or at least verifying that [**IsClosed**](im-imessengerwindow-isclosed.md) does not return **TRUE**, is a prerequisite to calling a number of other automation interfaces that require a valid window handle. For example, calling [**Left**](im-imessengerwindow-left.md) while the window is closed will return E\_FAIL as the HRESULT. The visibility of the Messenger application window is not parallel to the **Visible** properties and methods implemented in other application automation interfaces, such as the Microsoft Office automation APIs. When the Messenger application window is closed, it is not just sent and processed in the background. A closed Messenger application is sent to the background on the process level (in the notification area), not just on a windowing or display level.

> [!Note]  
> This method is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrWindow As MessengerAPI.IMessengerWindow

Private Sub cmd_W_Show_Click()
    MsgrWindow.Show
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



 

 





