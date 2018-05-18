---
title: IMessengerContacts Count property
description: Retrieves the number of MessengerContacts objects in the collection.
ms.assetid: '06b78022-64fc-4a0f-b641-835019aa8ac4'
keywords: ["Count property Windows Messenger", "Count property Windows Messenger , IMessengerContacts interface", "IMessengerContacts interface Windows Messenger , Count property"]
topic_type:
- apiref
api_name:
- IMessengerContacts.Count
- IMessengerContacts.get_Count
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerContacts::Count property

\[**Count** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves the number of [**MessengerContacts**](im-messengercontacts.md) objects in the collection.

This property is read-only.

## Syntax


```C++
HRESULT get_Count(
  [out, retval] long *pcContacts
);
```



## Property value

**LONG** that provides the number of [**MessengerContacts**](im-messengercontacts.md) objects in the collection.

## Error codes

Returns one of the following values. 



| Name                                                                                                  | Meaning                                        |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                           |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *pcContacts* is a **NULL** pointer.<br/> |



## Remarks

If there are no active [**MessengerContacts**](im-messengercontacts.md) objects in the Contact List, *pcContacts* will return zero.

If this method is called while the client is offline, the method call will not fail, but the Contact List will always have zero members and zero count.

> [!Note]  
> This property is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContacts As MessengerAPI.IMessengerContacts

Private Sub btnCount_Click()
    On Error Resume Next
    MsgBox("Contacts Count = " & CStr(MsgrContacts.Count))
    ErrorTrap ("Contacts.Count")    'Error handling routine
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

[**IMessengerContacts**](im-imessengercontacts.md)
</dt> <dt>

[**Item**](im-imessengercontacts-item.md)
</dt> </dl>

 

 





