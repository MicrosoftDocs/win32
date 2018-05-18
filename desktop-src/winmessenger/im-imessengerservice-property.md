---
title: IMessengerService Property property
description: Retrieves a specific property of the service.
ms.assetid: '10cd0e33-e0f3-404e-9c09-da1ea9d2b2dd'
keywords: ["Property property Windows Messenger", "Property property Windows Messenger , IMessengerService interface", "IMessengerService interface Windows Messenger , Property property"]
topic_type:
- apiref
api_name:
- IMessengerService.Property
- IMessengerService.get_Property
- IMessengerService.put_Property
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessengerService::Property property

\[**Property** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Retrieves a specific property of the service.

This property is read/write.

## Syntax


```C++
HRESULT put_Property(
  [in]          MSERVICEPROPERTY ePropType,
  [in]          VARIANT          vPropVal
);

HRESULT get_Property(
  [in]          MSERVICEPROPERTY ePropType,
  [out, retval] VARIANT          *pvPropVal
);
```



## Property value

A pointer to a **VARIANT** that contains the property value. (Variant type differs depending on the property being set or retrieved.)

## Error codes

Returns one of the following values. 



| Name                                                                                     | Meaning                                      |
|------------------------------------------------------------------------------------------|----------------------------------------------|
| <dl> <dt>E\_INVALIDARG</dt> </dl> | Returned in all cases. Reserved. <br/> |



## Remarks

The following table lists error codes returned by this method.



| Error Code | Meaning                          |
|------------|----------------------------------|
| 0x80070057 | Returned in all cases. Reserved. |



 

This method exists for later expansions of properties that can be associated with a contact but that will not require another iteration of the [**Messenger**](im-messenger.md) interfaces. For the current properties ([**CanPage**](im-imessengercontact-canpage.md), [**Phone**](im-imessenger-phone.md), [**FriendlyName**](im-imessengercontact-friendlyname.md), and [**Blocked**](im-imessengercontact-blocked.md)), each property has its own change event and method for accessing the property.

> [!Note]  
> This property is available for scripting languages but returns E\_INVALIDARG.

 

## Examples

The following Visual Basic example shows the use of this method.


```VB
Public WithEvents MsgrUIA As MessengerAPI.Messenger
Public MsgrService As MessengerAPI.IMessengerService

Private Sub btnServiceProperty_Click()
    On Error Resume Next
    FormPPType.Show vbModal 'Get user input
    If bDialogCancel = False Then
        MsgBox("Service Property type" & lppType & " = " & CStr(MsgrService.Property(MSERVICEPROP_INVALID_PROPERTY)))
    End If
    ErrorTrap ("MsgrService.Property")  'Error handling routine

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



 

 





