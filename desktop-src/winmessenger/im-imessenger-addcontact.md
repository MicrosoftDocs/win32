---
title: IMessenger AddContact method
description: Launches the Add a Contact wizard.
ms.assetid: e0b495c6-72e5-493a-8be0-d738612daf30
keywords:
- AddContact method Windows Messenger
- AddContact method Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , AddContact method
topic_type:
- apiref
api_name:
- IMessenger.AddContact
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

# IMessenger::AddContact method

\[**AddContact** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the **Add a Contact** wizard.

## Syntax


```C++
HRESULT AddContact(
  [in] long hwndParent,
  [in] BSTR bstrEMail
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **long**

Sets Reserved. Current implementations should set this parameter to 0 or **NULL**.

</dd> <dt>

*bstrEMail* \[in\]
</dt> <dd>

Type: **BSTR**

Sign-in name to be added as a contact. If this string value is **NULL**, the first page of the **Add a Contact** wizard is displayed and the user is prompted to specify the contact to add. If *bstrEMail* specifies a contact to add, the **Add a Contact** wizard will step through the first page automatically, without the user clicking **Next**. If there is a problem adding the contact (for example, if the contact does not map to a known Windows Messenger sign-in name), the user will be prompted to take appropriate corrective action.

</dd> </dl>

## Return value

Type: **HRESULT**

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md). Returns one of the following values.



| Return code                                                                                                | Description                                                                                                                                                                                                                                                                                                       |
|------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                       | Success. <br/>                                                                                                                                                                                                                                                                                              |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl>              | The system could not allocate enough memory. <br/>                                                                                                                                                                                                                                                          |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>               | *bstrEMail* has invalid characters.<br/> - or -<br/> *bstrEMail* exceeded 129 characters.<br/> - or -<br/> *bstrEMail* contains a carriage return or linefeed.<br/>                                                                                                                 |
| <dl> <dt>**S\_FALSE**</dt> </dl>                    | The **Add a Contact** wizard is already displayed. The supplied parameters will be ignored and the wizard will be brought to the foreground with already existing values. S\_FALSE cannot typically be captured in scripting error trapping because the initial 'error' bit is not 1 in this HResult. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                     | Unspecified internal error. <br/>                                                                                                                                                                                                                                                                           |
| <dl> <dt>**MSGR\_E\_AUDIO\_UI\_ACTIVE**</dt> </dl>  | Called this method while the **Audio and Video Tuning Wizard** was enabled and visible.<br/>                                                                                                                                                                                                                |
| <dl> <dt>**MSGR\_E\_OPTION\_UI\_ACTIVE**</dt> </dl> | The **Options** dialog box was enabled and visible when this method was called.<br/>                                                                                                                                                                                                                        |
| <dl> <dt>**MSGR\_E\_NOT\_LOGGED\_ON**</dt> </dl>    | The **Sign In** dialog box was enabled and visible when this method was called.<br/>                                                                                                                                                                                                                        |
| <dl> <dt>**MSGR\_E\_LOGON\_UI\_ACTIVE**</dt> </dl>  | The **Customer Experience Improvement Program** (CEIP) dialog box was enabled and visible when this method was called. <br/>                                                                                                                                                                                |



 

## Remarks

The contact is added to the primary service of the primary client.

If the supplied input parameter is other than a blank string, this method populates the input in the **Add a Contact** wizard with the specified string.

Entering a blank (**NULL** string) value for the *bstrEMail* parameter is common usage because it launches the **Add a Contact** wizard and allows the user to specify the e-mail address of the new contact.

From the **Add a Contact** wizard, the user can search for a contact by name or e-mail name if the contact's sign-in name is unknown. When the user selects a name from the search results and clicks **Next** in the wizard, a [**OnContactListAdd**](im-dmessengerevents-oncontactlistadd.md) event that contains the results of the add request is received.

The format of the string entered to identify a Windows Messenger user by sign-in name depends on the service. For some services, the parameter name *bstrEMail* is a misnomer. No validation is performed on the supplied *bstrEMail* by the API; however, the service that is being connected to may apply validation.

Calling this API while the client is offline does not throw an error. To determine if a contact was added successfully, check the result in the [**OnContactListAdd**](im-dmessengerevents-oncontactlistadd.md) event.

> [!Note]  
> This method is not available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





