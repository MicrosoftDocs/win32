---
title: IMessengerConversationWnd AddContact method
description: Adds another user to the current conversation.
ms.assetid: 31500cbb-68d7-45f4-95af-2ebd8b557823
keywords:
- AddContact method Windows Messenger
- AddContact method Windows Messenger , IMessengerConversationWnd interface
- IMessengerConversationWnd interface Windows Messenger , AddContact method
topic_type:
- apiref
api_name:
- IMessengerConversationWnd.AddContact
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

# IMessengerConversationWnd::AddContact method

\[**AddContact** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Adds another user to the current conversation.

## Syntax


```C++
HRESULT AddContact(
  [in] VARIANT vContact
);
```



## Parameters

<dl> <dt>

*vContact* \[in\]
</dt> <dd>

Type: **VARIANT**

**VARIANT** that can take as its value either a **VT\_BSTR** or a **VT\_DISPATCH** pointer to an existing [**MessengerContact**](im-messengercontact.md) object. If the input value type is a string, this method creates a new **MessengerContact** object internally. The string should be the full sign-in name. For a Microsoft .NET Messenger Service contact, this should include an "at" sign (@) and domain name. If the input value type is a pointer to an existing **MessengerContact** object (should be type **VT\_DISPATCH**), the existing object is used for contact information.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values. 



| Return code                                                                                              | Description                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                     | Success. <br/>                                                                                                                                                                                                                                                                    |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>             | *vContact* is **NULL**, the wrong type, points to a **NULL** string, or points to a string that has a space as the first character; or, *vContact* is **VT\_BSTR** that exceeded 129 characters; or, *vContact* is **VT\_BSTR** and contains a carriage return or linefeed. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                   | Client was not signed in to the primary service at the time this method was called; or, this method was called against the local client user.<br/>                                                                                                                                |
| <dl> <dt>**S\_FALSE**</dt> </dl>                  | String comparison failed.<br/>                                                                                                                                                                                                                                                    |
| <dl> <dt>**MSGR\_E\_SESSION\_FULL**</dt> </dl>    | The current conversation window is hosting a voice or video conversation; or, the maximum number of participants allowed in the session has been reached.<br/>                                                                                                                    |
| <dl> <dt>**MSGR\_E\_INVALID\_SERVICE**</dt> </dl> | Called this method against a user belonging to a service other than the one to which the current conversation members belong.<br/>                                                                                                                                                |



 

## Remarks

The following table lists error codes returned by this method.



| Error Code                | Meaning                                                                                                                                                                                                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x80004005                | Client was not signed in to the primary service at the time this method was called; or, this method was called against the local client user.                                                                                                                               |
| 0x80070057                | *vContact* is **NULL**, the wrong type, points to a **NULL** string, or points to a string that has a space as the first character; or, *vContact* is **VT\_BSTR** that exceeded 129 characters; or, *vContact* is **VT\_BSTR** and contains a carriage return or linefeed. |
| MSGR\_E\_SESSION\_FULL    | The current conversation window is hosting a voice or video conversation; or, the maximum number of participants allowed in the session has been reached.                                                                                                                   |
| MSGR\_E\_INVALID\_SERVICE | Called this method against a user belonging to a service other than the one to which the current conversation members belong.                                                                                                                                               |



 

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

The **AddContact** method is scriptable. However, contacts cannot be added to a conversation automatically by calling this method from script. When this method is called from script, the **Contact Picker** dialog is always displayed to the user so the user can select the online contact to be added to the conversation.

This method does not have a return value. Therefore, parenthetical syntax should be used for JScript, but not for Microsoft Visual Basic Scripting Edition (VBScript). All parameters of this method are required.

> [!Note]  
> This method is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger 
Public mWindow2 As MessengerAPI.IMessengerConversationWnd 

Private Sub btnWindow2AddContact_Click() 
    On Error Resume Next 
    FormContactName.Show vbModal 'Get user input 
    Dim strContactName_0 as String 
    'Launch a Conversation window with an online contact 
    '(where strContactName_0 is the online contact's signinname) 
    If bDialogCancel = False Then 
        Set mWindow2 = MsgrUIA.InstantMessage (strContactName_0) 
        mWindow2.AddContact strContactName 
    End If 
    ErrorTrap ("IMessengerConversationWnd.AddContact") 'Error handling routine 
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

 

 





