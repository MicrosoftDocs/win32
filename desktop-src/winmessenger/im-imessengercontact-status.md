---
title: IMessengerContact Status property
description: Retrieves the connection status of the contact associated with the MessengerContact object.
ms.assetid: 50bec125-a4ba-4f06-a413-a6c25b70733f
keywords:
- Status property Windows Messenger
- Status property Windows Messenger , IMessengerContact interface
- IMessengerContact interface Windows Messenger , Status property
topic_type:
- apiref
api_name:
- IMessengerContact.Status
- IMessengerContact.get_Status
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

# IMessengerContact::Status property

\[**Status** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the connection status of the contact associated with the [**MessengerContact**](im-messengercontact.md) object.

This property is read-only.

## Syntax


```C++
HRESULT get_Status(
  [out, retval] MISTATUS *pMstate
);
```



## Property value

Pointer to the [**MISTATUS**](im-mistatus.md) of the user. Can be one of the following **MISTATUS** constant values:



|                           |                                                                                                                                                                                                                                                   |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MISTATUS\_BUSY            | The remote client is connected to a server, but busy (a user-selected state).                                                                                                                                                                     |
| MISTATUS\_OFFLINE         | The remote client is not connected to a server.                                                                                                                                                                                                   |
| MISTATUS\_ONLINE          | The remote client is connected to a server.                                                                                                                                                                                                       |
| MISTATUS\_BE\_RIGHT\_BACK | The remote client user is away from the computer for a short time (a user-selected state).                                                                                                                                                        |
| MISTATUS\_IDLE            | The remote client's computer has not detected mouse or keyboard input for a determined time. The user is most likely away from the computer (an automatic state). The user can select whether to transmit the idle state and idle time threshold. |
| MISTATUS\_AWAY            | The remote client user is away from the computer (a user-selected state).                                                                                                                                                                         |
| MISTATUS\_ON\_THE\_PHONE  | The remote client user is on the phone (a user-selected state).                                                                                                                                                                                   |
| MISTATUS\_OUT\_TO\_LUNCH  | The remote client user is at lunch (a user-selected state).                                                                                                                                                                                       |
| MISTATUS\_UNKNOWN         | The state of the remote client is unknown.                                                                                                                                                                                                        |



 

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                     |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                        |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pMstate* is a **NULL** pointer.<br/> |



## Remarks

Status information for a user is maintained by the server and must be kept synchronized in a client by checking for [**OnContactStatusChange**](im-dmessengerevents-oncontactstatuschange.md) events through the event sink.

It is possible to create a [**MessengerContact**](im-messengercontact.md) object that represents the local client user and query it, but local client information is easier to obtain with [**MyStatus**](im-imessengerservice-mystatus.md).

The value of a remote client's status is reset automatically when events fire. The Messenger object receives the [**OnContactStatusChange**](im-dmessengerevents-oncontactstatuschange.md) event and writes to the protected properties of the [**MessengerContact**](im-messengercontact.md) object that specify its state. However, client implementers must write code within a customized event handler to update any custom user interface (UI) that displays user states. Because the event returns the previous status of the user before the change, **Status** should be called upon receipt of each event so that the client can be updated.

Several other states (such as MISTATUS\_LOCAL\_CONNECTING\_TO\_SERVER) are temporary states that are valid for a local client, but are not usually passed as part of the Messenger protocol. These states will not be possible values for a remote client's state.

MISTATUS\_INVISIBLE is a state that can be selected by the user and will appear as MISTATUS\_OFFLINE to any subscribers. MISTATUS\_INVISIBLE will never be returned through **Status**.

All online [**MISTATUS**](im-mistatus.md) results are grouped by a common factor in the constant. For more information, see **MISTATUS**.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContact As MessengerAPI.IMessengerContact

Private Sub btnStatus_Click()
    On Error Resume Next
    Dim strSigninName As String
    Dim strServiceID As String
    'Get selected contact
    strSigninName = ListContact.SelectedItem.SubItems(2)
    strServiceID = ListContact.SelectedItem.SubItems(5)
    Set MsgrContact = Nothing
    Set MsgrContact = MsgrUIA.GetContact(strSigninName, strServiceID)
    ErrorTrap ("GetContact")    'Error handling routine
    MsgBox("Contact Status: " & Module1.StatusLookup(MsgrContact.Status))
    ErrorTrap ("Contact.Status")    'Error handling routine
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



 

 





