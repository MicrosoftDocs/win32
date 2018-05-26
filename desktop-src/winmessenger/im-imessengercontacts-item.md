---
title: IMessengerContacts Item method
description: Retrieves a specific service by index.
ms.assetid: f77c0cc7-a1e8-4167-a21b-20dc61b0ff43
keywords:
- Item method Windows Messenger
- Item method Windows Messenger , IMessengerContacts interface
- IMessengerContacts interface Windows Messenger , Item method
topic_type:
- apiref
api_name:
- IMessengerContacts.Item
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

# IMessengerContacts::Item method

\[**Item** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a specific service by index.

## Syntax


```C++
HRESULT Item(
  [in]          long      Index,
  [out, retval] IDispatch **ppMContact
);
```



## Parameters

<dl> <dt>

*Index* \[in\]
</dt> <dd>

Type: **long**

**LONG** that specifies the index of the desired [**MessengerContacts**](im-messengercontacts.md) object in the collection.

</dd> <dt>

*ppMContact* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

Address of a pointer to an [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a [**MessengerContacts**](im-messengercontacts.md) object requested with *Index*. The object can now be accessed through the [**IMessengerContact**](im-imessengercontact.md) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values. 



| Return code                                                                                               | Description                                                                                  |
|-----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success. <br/>                                                                         |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl> | *ppMContact* is a **NULL** pointer.<br/>                                               |
| <dl> <dt>**E\_FAIL**</dt> </dl>                    | Invalid collection or index number provided exceeds the length of the collection.<br/> |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | *Index* is not a positive integer.<br/>                                                |



 

## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                            |
|------------|------------------------------------------------------------------------------------|
| 0x80004005 | Invalid collection, or index number provided exceeds the length of the collection. |
| 0x80070057 | *Index* is not a positive integer.                                                 |



 

The [**Contacts**](im-imessengerconversationwnd-contacts.md) property is scriptable, but read-only.

If you know the sign-in name for a user, you can get the MessengerContact object by creating an object for it explicitly by calling [**GetContact**](im-imessenger-getcontact.md). Even if that contact is already present in a list, the same pointer is returned (as it would have been by retrieving that object from an existing collection).

> [!Note]  
> This method is available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrContacts As MessengerAPI.IMessengerContacts

Private Sub btnItem_Click()
    On Error Resume Next
    FormItem.Show vbModal   'Get user input
    If bDialogCancel = False Then
        MsgBox("Contacts Item " & lItem & " = " & _
        MsgrContacts.Item(lItem).SigninName & " : " & _
        MsgrContacts.Item(lItem).FriendlyName)
    End If
    ErrorTrap ("Contact.Item")  'Error handling routine
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

[**IMessengerContacts**](im-imessengercontacts.md)
</dt> <dt>

[**MessengerContact**](im-messengercontact.md)
</dt> </dl>

 

 





