---
title: IMessenger GetContact method
description: Creates a MessengerContact object that can be used to call methods of the Windows Messenger interfaces, such as IMessenger, IMessengerContact, and IMessengerContacts.
ms.assetid: '9036782c-1248-44f9-b674-2a69b5b24014'
keywords: ["GetContact method Windows Messenger", "GetContact method Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , GetContact method"]
topic_type:
- apiref
api_name:
- IMessenger.GetContact
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::GetContact method

\[**GetContact** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Creates a [**MessengerContact**](im-messengercontact.md) object that can be used to call methods of the Windows Messenger interfaces, such as [**IMessenger**](im-imessenger.md), [**IMessengerContact**](im-imessengercontact.md), and [**IMessengerContacts**](im-imessengercontacts.md).

## Syntax


```C++
HRESULT GetContact(
  [in]          BSTR      bstrSigninName,
  [in]          BSTR      bstrServiceId,
  [out, retval] IDispatch **ppMContact
);
```



## Parameters

<dl> <dt>

*bstrSigninName* \[in\]
</dt> <dd>

Type: **BSTR**

A **BSTR** that contains the sign-in name of the remote user to create as a local [**MessengerContact**](im-messengercontact.md) object.

</dd> <dt>

*bstrServiceId* \[in\]
</dt> <dd>

Type: **BSTR**

A **BSTR** that contains the GUID service ID of the remote user being created. Clients with secondary services can potentially create [**MessengerContact**](im-messengercontact.md) objects for any currently supported service. If this parameter is used, the method will search the specified service for a person whose name matches *bstrSigninName* by calling CreateUser on the service. If this parameter is not used, by passing in an empty string, the method will search the local user's contact list and not the services.

</dd> <dt>

*ppMContact* \[out, retval\]
</dt> <dd>

Type: **IDispatch\*\***

A pointer to a pointer to the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on the new (or existing) [**MessengerContact**](im-messengercontact.md) object. The new object can now be accessed through the [**IMessengerContact**](im-imessengercontact.md) interface.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Success. <br/>                                                                                                                                                                                                                                                                                                    |
| <dl> <dt>**RPC\_X\_NULL\_REF\_POINTER**</dt> </dl> | *ppMContact* is a **NULL** pointer.<br/>                                                                                                                                                                                                                                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | *bstrSigninName* exceeded 129 characters.<br/> - or -<br/> *bstrSigninName* contains spaces, a carriage return, or linefeed. <br/> - or -<br/> *bstrServiceId* exceeded 38 characters.<br/> - or -<br/> *bstrServiceId* contains spaces, a carriage return, or linefeed.<br/> |
| <dl> <dt>**MSGR\_E\_USER\_NOT\_FOUND**</dt> </dl>  | A [**MessengerContact**](im-messengercontact.md) object for a contact who is not in the contact list.<br/>                                                                                                                                                                                                       |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl>   | Client is not signed in. Client must be signed in to check this value.<br/>                                                                                                                                                                                                                                       |
| <dl> <dt>**E\_FAIL**</dt> </dl>                    | *bstrSigninName* is a **NULL** string.<br/> - or -<br/> *bstrServiceId* is a **NULL** string.<br/>                                                                                                                                                                                                    |



 

## Remarks

Service-specific variations in the [**MessengerContact**](im-messengercontact.md) object may include the initial defaults for property values in cases in which the object is created but no update is possible because the contact is offline or not in the contact list. For Microsoft .NET Messenger Service and Instant Messaging Service (IM), the behavior is identical.

*ppMContact* should be released when it is no longer needed. Even if you remove the [**MessengerContact**](im-messengercontact.md) object from all lists, the reference count does not reach zero until you release the pointer.

If **GetContact** is invoked more than once using the same *bstrSigninName* input string, the same pointer will be returned each time as long as *ppMContact* was not released or otherwise destroyed.

Syntax of the **BSTR** used to specify the sign-in name varies between services. For the Microsoft .NET Messenger Service, sign-in names are expected to contain an "at" sign (@) and a domain name. Other services have different requirements.

Creating a [**MessengerContact**](im-messengercontact.md) object for a contact who is not in the contact list is not well supported by the architecture and should be avoided. If you are creating a **MessengerContact** object for a contact who is not in the contact list, be aware of the following considerations:

-   The [**MessengerContact**](im-messengercontact.md) object will not be fully valid initially. It is an object in the Component Object Model (COM) sense, but not a fully working object from the perspective of the properties it stores. [**Status**](im-imessengercontact-status.md) will initially return **MISTATUS\_UNKNOWN** and [**FriendlyName**](im-imessengercontact-friendlyname.md) will return the sign-in name for the Microsoft .NET Messenger Service.
-   The initial *bstrSigninName* input value will be returned for [**SigninName**](im-imessengercontact-signinname.md).
-   The missing properties will not be filled in until the [**MessengerContact**](im-messengercontact.md) object is successfully added to the local client's contact list and the local client receives the [**OnContactListAdd**](im-dmessengerevents-oncontactlistadd.md) event. These properties will be refreshed, if necessary, upon each local client sign-in or on a [**OnContactStatusChange**](im-dmessengerevents-oncontactstatuschange.md) event.
-   Creating a [**MessengerContact**](im-messengercontact.md) object for a user or contact that does not exist in the server-side user store will initially return S\_OK. Attempting to add this unverified **MessengerContact** object to the contact list, however, will result in a **MSGR\_E\_USER\_NOT\_FOUND** error on the [**OnContactListAdd**](im-dmessengerevents-oncontactlistadd.md) event.

> [!Note]  
> The following remarks apply to scripting languages.
>
> -   This method is scriptable.
> -   You should not return MSGR\_E\_NOT\_LOGGED\_ON to avoid an exception.
> -   Clear the value returned to the user.

 

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

[**IMessenger**](im-imessenger.md)
</dt> <dt>

[**IMessengerContacts**](im-imessengercontacts.md)
</dt> </dl>

 

 





