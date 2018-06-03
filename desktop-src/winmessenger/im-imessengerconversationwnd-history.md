---
title: IMessengerConversationWnd History property
description: Returns the text from the history of the conversation window.
ms.assetid: 346b628c-1503-4899-944d-7a60305b588c
keywords:
- History property Windows Messenger
- History property Windows Messenger , IMessengerConversationWnd interface
- IMessengerConversationWnd interface Windows Messenger , History property
topic_type:
- apiref
api_name:
- IMessengerConversationWnd.History
- IMessengerConversationWnd.get_History
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

# IMessengerConversationWnd::History property

\[**History** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Returns the text from the history of the conversation window.

This property is read-only.

## Syntax


```C++
HRESULT get_History(
  [out, retval] BSTR *bstrHistoryText
);
```



## Property value

Pointer to a **BSTR** that contains the text of the conversation window.

## Error codes

Returns one of the following values. 



| Name                                                                                                  | Meaning                                                                                                                               |
|-------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                                                                  |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Client was not signed in to the primary service at the time this method was called; or, the conversation window is closed.<br/> |
| <dl> <dt>S\_FALSE</dt> </dl>                   | Could not bring focus to the window.<br/>                                                                                       |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *bstrHistoryText* is a **NULL** pointer.<br/>                                                                                   |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                                    |
|------------|----------------------------------------------------------------------------------------------------------------------------|
| 0x80004005 | Client was not signed in to the primary service at the time this method was called; or, the conversation window is closed. |



 

The **History** property not scriptable.

> [!Note]  
> This property is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger 
Public mWindow2 As MessengerAPI.IMessengerConversationWnd 

Private Sub btnWindow2History_Click() 
    On Error Resume Next 
    Dim strContactName_0 as String 
    'Launch a Conversation window with an online contact 
    '(where strContactName_0 is the online contact's signinname) 
    Set mWindow2 = MsgrUIA.InstantMessage (strContactName_0) 
    MsgBox mWindow2.History 
    ErrorTrap ("IMessengerConversationWnd.History") 'Error handling routine 
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



## See also

<dl> <dt>

[**IMessengerConversationWnd**](im-imessengerconversationwnd.md)
</dt> </dl>

 

 





