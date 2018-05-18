---
title: IMessenger OptionsPages method
description: Launches the Options dialog box with a specified tab displayed.
ms.assetid: '62b37eb0-dc7e-4f58-8063-ef42943b0d8d'
keywords: ["OptionsPages method Windows Messenger", "OptionsPages method Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , OptionsPages method"]
topic_type:
- apiref
api_name:
- IMessenger.OptionsPages
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::OptionsPages method

\[**OptionsPages** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the **Options** dialog box with a specified tab displayed.

## Syntax


```C++
HRESULT OptionsPages(
  [in] long        hwndParent,
  [in] MOPTIONPAGE mOptionPage
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **long**

A **LONG**. Reserved. Implementations should set this parameter to 0 or **NULL**.

</dd> <dt>

*mOptionPage* \[in\]
</dt> <dd>

Type: **MOPTIONPAGE**

A value of the [**MOPTIONPAGE**](im-moptionpage.md) enumeration. Allowed values are as follows:



| Constant                | Value | Description                                                                                                                                                                                                                                                   |
|-------------------------|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MOPT\_GENERAL\_PAGE     | 0     | Displays the **General** tab of the **Options** dialog box (default).                                                                                                                                                                                         |
| MOPT\_PRIVACY\_PAGE     | 1     | Displays the **Privacy** tab of the **Options** dialog box.                                                                                                                                                                                                   |
| MOPT\_EXCHANGE\_PAGE    | 2     | Displays the **Exchange** tab of the **Options** dialog box. Because this tab does not exist in the version 4.0 client, this value should not generally be used. Service configuration information appears in the **Accounts** tab of the version 4.0 client. |
| MOPT\_ACCOUNTS\_PAGE    | 3     | Displays the **Accounts** tab of the **Options** dialog box.                                                                                                                                                                                                  |
| MOPT\_CONNECTION\_PAGE  | 4     | Displays the **Connection** tab of the **Options** dialog box.                                                                                                                                                                                                |
| MOPT\_PREFERENCES\_PAGE | 5     | Displays the **Preferences** tab of the **Options** dialog box.                                                                                                                                                                                               |
| MOPT\_SERVICES\_PAGE    | 6     | Displays the **Services** tab of the **Options** dialog box. This tab is enabled only on a client that can use multiple services.                                                                                                                             |
| MOPT\_PHONE\_PAGE       | 7     | Displays the **Phone** tab of the **Options** dialog box.                                                                                                                                                                                                     |



 

</dd> </dl>

## Return value

Type: **HRESULT**

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Success. <br/>                                                                                                                                                                                                                                                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Could not create the **Options** dialog box, or the [**Messenger**](im-messenger.md) object has not been created or is not responding.<br/>                                                                                                                                               |
| <dl> <dt>**E\_FALSE**</dt> </dl>                     | The **Options** dialog box is already open. The second call will change the *mOptionPage* value (**Option** tab) in the foreground if the value is different. S\_FALSE cannot usually be captured in scripting error trapping because the initial error bit is not 1 in this HResult.<br/> |
| <dl> <dt>**MSGR\_E\_AUDIO\_UI\_ACTIVE**</dt> </dl>   | Called this method while the **Media Wizard** dialog box was enabled and visible.<br/>                                                                                                                                                                                                     |
| <dl> <dt>**MSGR\_E\_CONTACT\_UI\_ACTIVE**</dt> </dl> | The **Add a Contact** or **Find a Contact** dialog box of the Messenger client (modal dialog box) is currently open.<br/>                                                                                                                                                                  |
| <dl> <dt>**MSGR\_E\_LOGON\_UI\_ACTIVE**</dt> </dl>   | The **Sign In** dialog box of the Messenger client (modal dialog box) is currently open. <br/>                                                                                                                                                                                             |
| <dl> <dt>**MSGR\_E\_OTHER\_UI\_ACTIVE**</dt> </dl>   | Called this method while the **Customer Experience Improvement Program**(CEIP) dialog box was enabled and visible. <br/>                                                                                                                                                                   |



 

## Remarks

Because some options can be checked or changed while the client is offline, this method does not fail for offline clients. However, some of the dialog boxes will initially display a grayed-out UI for an offline local client use

> [!Note]  
> This method is available for scripting languages.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





