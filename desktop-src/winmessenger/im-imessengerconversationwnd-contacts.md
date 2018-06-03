---
title: IMessengerConversationWnd Contacts property
description: Retrieves a read-only collection of contacts in the conversation window.
ms.assetid: ab3b7d7a-5916-403d-9a39-a3ee062401a9
keywords:
- Contacts property Windows Messenger
- Contacts property Windows Messenger , IMessengerConversationWnd interface
- IMessengerConversationWnd interface Windows Messenger , Contacts property
topic_type:
- apiref
api_name:
- IMessengerConversationWnd.Contacts
- IMessengerConversationWnd.get_Contacts
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

# IMessengerConversationWnd::Contacts property

\[**Contacts** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a read-only collection of contacts in the conversation window.

This property is read-only.

## Syntax


```C++
HRESULT get_Contacts(
  [out, retval] IDispatch **pContacts
);
```



## Property value

Address of a pointer to an [IDispatch](https://msdn.microsoft.com/windows/desktop/c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerContacts**](im-messengercontacts.md) object that contains the participants of that conversation, excluding the local user.

## Error codes

Returns one of the following values. 



| Name                                                                                                  | Meaning                                                                                        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                           |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pContacts* is a **NULL** pointer.<br/>                                                  |
| <dl> <dt>E\_FAIL</dt> </dl>                    | Client was not signed in to the primary service at the time this method was called.<br/> |
| <dl> <dt>S\_FALSE</dt> </dl>                   | Could not bring focus to the window.<br/>                                                |
| <dl> <dt>E\_OUTOFMEMORY</dt> </dl>             | Error during list creation.<br/>                                                         |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                             |
|------------|-------------------------------------------------------------------------------------|
| 0x80004005 | Client was not signed in to the primary service at the time this method was called. |
| 0x8007000E | Error during list creation.                                                         |



 

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger 
Public mWindow2 As MessengerAPI.IMessengerConversationWnd 
Public MsgrContacts As MessengerAPI.IMessengerContacts 

Private Sub btnWindow2Contacts_Click() 
    On Error Resume Next 
    Set MsgrContacts = Nothing 
    Dim strContactName_0 as String 
    'Launch a Conversation window with an online contact 
    '(where strContactName_0 is the online contact's signinname) 
    Set mWindow2 = MsgrUIA.InstantMessage (strContactName_0) 
    Set MsgrContacts = mWindow2.Contacts 
    ErrorTrap ("IMessengerConversationWnd.Contacts") 'Error handling routine 
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

 

 





