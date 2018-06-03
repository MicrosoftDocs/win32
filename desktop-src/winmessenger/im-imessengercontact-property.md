---
title: IMessengerContact Property property
description: Reserved.
ms.assetid: ad25b4f8-0304-4986-94a9-c7755dc9472f
keywords:
- Property property Windows Messenger
- Property property Windows Messenger , IMessengerContact interface
- IMessengerContact interface Windows Messenger , Property property
topic_type:
- apiref
api_name:
- IMessengerContact.Property
- IMessengerContact.get_Property
- IMessengerContact.put_Property
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

# IMessengerContact::Property property

\[**Property** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Reserved.

This property is read/write.

## Syntax


```C++
HRESULT put_Property(
  [in]          MPHONE_TYPE ePropType,
  [in]          VARIANT     vPropVal
);

HRESULT get_Property(
  [in]          MPHONE_TYPE ePropType,
  [out, retval] VARIANT     *pvPropVal
);
```



## Property value

A pointer to a **VARIANT** that contains the property value. (Variant type differs depending on the property being set or retrieved.)

## Error codes

Returns one of the following values.



| Name                                                                                                  | Meaning                                                                                                    |
|-------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                      | Success. <br/>                                                                                       |
| <dl> <dt>E\_INVALIDARG</dt> </dl>              | *ePropType* is out of range (not within [**MCONTACTPROPERTY**](im-mcontactproperty.md) range).<br/> |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl> | *vPropVal* is a **NULL** pointer.<br/>                                                               |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                                                                                                                                                         |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x80070057 | *ePropType* is out of range (not within [**MCONTACTPROPERTY**](im-mcontactproperty.md) range); or, attempted to write to the property (property is read-only). |



 

The **Property** property is scriptable for MCONTACTPROPERTY = MCONTACTPROP\_GROUPS\_PROPERTY, but read-only. The **Property** property is not scriptable for MCONTACTPROPERTY = MCONTACTPROP\_EMAIL.

The *bstrNumber* return value may contain punctuation. Most APIs used for Internet telephony will either ignore or strip punctuation.

E\_FAIL HRESULT will be returned for a contact who does not have phone information for the specified *PhoneType* parameter.

> [!Note]  
> This property is not available for scripting languages.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger 
Public MsgrContact As MessengerAPI.IMessengerContact 
Public MsgrGroups As MessengerAPI.IMessengerGroups 

Private Sub ContactGetProperty_Click() 
    On Error Resume Next 
    FormContactName.Show vbModal 
    'Get user input - select the contact 
    Set MsgrContact = Nothing 
    Set MsgrContact = MsgrUIA.GetContact(strContactName, strServiceID) 
    ... 
    ' Retrieves the number of groups the contact belongs 
    Set MsgrGroups = MsgrContact.Property(MCONTACTPROP_GROUPS_PROPERTY) 
    MsgBox(MsgrContact.SignInName & " is a member of " & MsgrGroups.Count & " groups") 
    ... 
    ' Retrieves the e-mail address of the contact 
    MsgBox(MsgrContact.SignInName & " e-mail address is " & MsgrContact.Property(MCONTACTPROP_EMAIL)) 
    ErrorTrap ("IMessengerContact.Property") 
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

[**IMessengerContact**](im-imessengercontact.md)
</dt> <dt>

[**OnContactPagerChange**](im-dmessengerevents-oncontactpagerchange.md)
</dt> </dl>

 

 





