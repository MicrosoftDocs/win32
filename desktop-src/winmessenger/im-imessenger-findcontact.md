---
title: IMessenger FindContact method
description: Launches the Add a Contact wizard to the screen used for finding a contact based on information supplied as input parameters.
ms.assetid: 021493f3-88b4-42d2-a2e1-489f332fc709
keywords:
- FindContact method Windows Messenger
- FindContact method Windows Messenger , IMessenger interface
- IMessenger interface Windows Messenger , FindContact method
topic_type:
- apiref
api_name:
- IMessenger.FindContact
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

# IMessenger::FindContact method

\[**FindContact** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the **Add a Contact** wizard to the screen used for finding a contact based on information supplied as input parameters.

## Syntax


```C++
HRESULT FindContact(
  [in]           long    hwndParent,
  [in]           BSTR    bstrFirstName,
  [in]           BSTR    bstrLastName,
  [in, optional] VARIANT vbstrCity,
  [in, optional] VARIANT vbstrState,
  [in, optional] VARIANT vbstrCountry
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **long**

A **LONG**. Reserved. All current implementations and calls should set this parameter to 0 or **NULL**.

</dd> <dt>

*bstrFirstName* \[in\]
</dt> <dd>

Type: **BSTR**

A **BSTR** that specifies the first name of the potential contact. Required.

</dd> <dt>

*bstrLastName* \[in\]
</dt> <dd>

Type: **BSTR**

A **BSTR** that specifies the last name of the potential contact. Required.

</dd> <dt>

*vbstrCity* \[in, optional\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that specifies the city name that is used to narrow search criteria and match the given first and last names with the city provided in the contact's personal information. Applicable only when *vbstrCountry* is "United States."

</dd> <dt>

*vbstrState* \[in, optional\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that specifies the state name that is used to narrow search criteria and match the given first and last names with the state provided in the contact's personal information. Applicable only when *vbstrCountry* is "United States." If no state name is provided, this value defaults to "(any)".

</dd> <dt>

*vbstrCountry* \[in, optional\]
</dt> <dd>

Type: **VARIANT**

A **VARIANT** that specifies the country/region name that is used to narrow search criteria and match the given first and last names with the country/region provided in the contact's personal information. If no country/region name is provided, this value defaults to "(any)".

This is not an ISO 3166 value or other standard means of specifying a country/region or locale. The value passed will be compared as the closest literal match to the available countries/regions in the client's **Country** drop-down list. For the United States only, pass the string "United States".

The string passed to this API must be aware of the locale of the client against which it is being implemented. Although it is possible to obtain the client locale in Visual C++ and Visual Basic, it is difficult to determine with certainty when using scripting languages.

</dd> </dl>

## Return value

Type: **HRESULT**

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md). Returns one of the following values.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Return code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><dl> <dt><strong>S_OK</strong></dt> </dl></td>
<td>Success. <br/></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>E_INVALIDARG</strong></dt> </dl></td>
<td><em>bstrFirstName</em> and/or <em>bstrLastName</em> values are <strong>NULL</strong> or one of the required or optional string parameters exceeds the maximum allowed string length. <br/> 
<table>
<tbody>
<tr class="odd">
<td><em>bstrFirstName</em></td>
<td>63 characters maximum, 1 character minimum.</td>
</tr>
<tr class="even">
<td><em>bstrLastName</em></td>
<td>63 characters maximum, 1 character minimum.</td>
</tr>
<tr class="odd">
<td><em>bstrCity</em></td>
<td>If given, 63 characters maximum.</td>
</tr>
<tr class="even">
<td><em>bstrState</em></td>
<td>If given, 63 characters maximum.</td>
</tr>
<tr class="odd">
<td><em>bstrCountry</em></td>
<td>If given, 63 characters maximum. No carriage return (0x0D), linefeed (0x0A), or ANSI characters with values greater than 126 (0x7E).</td>
</tr>
</tbody>
</table>

<p> </p></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>S_FALSE</strong></dt> </dl></td>
<td><p>The <strong>Add a Contact</strong> wizard is already displayed. The supplied parameters will be ignored and the wizard will be brought to the foreground with preexisting values. It may be necessary to go back in the wizard sequence in order to see the parameters that were populated. S_FALSE cannot typically be captured in scripting error trapping because the initial 'error' bit is not 1 in this HResult.</p></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>E_FAIL</strong></dt> </dl></td>
<td><p>An unspecified error has occurred.</p></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>MSGR_E_AUDIO_UI_ACTIVE</strong></dt> </dl></td>
<td><p>The <strong>Audio and Video Tuning Wizard</strong> was enabled and visible when this method was called.</p></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>MSGR_E_LOGON_UI_ACTIVE</strong></dt> </dl></td>
<td><p>The <strong>Sign In</strong> dialog box was enabled and visible when this method was called.</p></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>MSGR_E_NOT_LOGGED_ON</strong></dt> </dl></td>
<td><p>Client was not signed in to the primary service at the time this method was called.</p></td>
</tr>
<tr class="even">
<td><dl> <dt><strong>MSGR_E_OPTIONS_UI_ACTIVE</strong></dt> </dl></td>
<td><p>The <strong>Options</strong> dialog box was enabled and visible when this method was called.</p></td>
</tr>
<tr class="odd">
<td><dl> <dt><strong>MSGR_E_OTHER_UI_ACTIVE</strong></dt> </dl></td>
<td><p>The <strong>Customer Experience Improvement Program</strong> (CEIP) dialog box was enabled and visible when this method was called.</p></td>
</tr>
</tbody>
</table>



 

## Remarks

**FindContact** searches for the contact in the primary service of the primary client.

Entering a blank (empty string) value for the *bstrFirstName* and *bstrLastName* parameters is common usage and presents a true dialog box to the user.

**Find a Contact** is actually the **Search By Name** screen of the **Add a Contact** wizard. Users can also add a contact with a known e-mail address by clicking the **Back** button, which switches to the **Add a Contact** screen. The **Add a Contact** screen can be displayed initially by calling the [**AddContact**](im-imessenger-addcontact.md) method.

Search results cannot be obtained through an event in the Windows Messenger APIs. Only the user can see results through the UI.

The actual UI has field size restrictions that do not necessarily match the input limits of this API. For example, the English version of the client restricts the field size to 40 characters. Users can scroll through fields that were populated through the API to be longer than 40 characters in the English client, but cannot enter them using the UI. The API limit is set to a higher value than the UI to allow the use of double-byte character strings (DBCS).

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



 

 





