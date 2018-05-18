---
title: IMessenger MediaWizard method
description: Launches the Audio and Video Tuning Wizard dialog box.
ms.assetid: '69dfafd5-ae1a-4e22-88a1-3e1ad52f5fef'
keywords: ["MediaWizard method Windows Messenger", "MediaWizard method Windows Messenger , IMessenger interface", "IMessenger interface Windows Messenger , MediaWizard method"]
topic_type:
- apiref
api_name:
- IMessenger.MediaWizard
api_location:
- Msgsc.dll
api_type:
- COM
---

# IMessenger::MediaWizard method

\[**MediaWizard** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Launches the **Audio and Video Tuning Wizard** dialog box.

## Syntax


```C++
HRESULT MediaWizard(
  [in] long hwndParent
);
```



## Parameters

<dl> <dt>

*hwndParent* \[in\]
</dt> <dd>

Type: **long**

A **LONG**. Reserved. All current implementations or calls should set this parameter to 0 or **NULL**.

</dd> </dl>

## Return value

Type: **HRESULT**

For a table of MSGR\_E\_\* constants, see [**MSGRConstants**](im-msgrconstants.md).

Returns one of the following values.



| Return code                                                                                                 | Description                                                                                                                    |
|-------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                        | Success. <br/> - or -<br/> The client is offline.<br/>                                                       |
| <dl> <dt>**MSGR\_E\_CONTACT\_UI\_ACTIVE**</dt> </dl> | Called this method while the **Add a Contact** or **Find a Contact** dialog box was enabled and visible.<br/>            |
| <dl> <dt>**MSGR\_E\_LOGON\_UI\_ACTIVE**</dt> </dl>   | Called this method while the **Sign In** dialog box was enabled and visible. <br/>                                       |
| <dl> <dt>**MSGR\_E\_OPTION\_UI\_ACTIVE**</dt> </dl>  | Called this method while the **Options** dialog box was enabled and visible. <br/>                                       |
| <dl> <dt>**MSGR\_E\_OTHER\_UI\_ACTIVE**</dt> </dl>   | Called this method while the **Customer Experience Improvement Program**(CEIP) dialog box was enabled and visible. <br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>                      | Could not create the dialog box or the [**Messenger**](im-messenger.md) object is not responding.<br/>                  |



 

## Remarks

Only one **Audio and Video Tuning Wizard** dialog box can be active at one time. Calling **MediaWizard** multiple times returns S\_OK.

Calling **MediaWizard** while the client is offline will display the dialog box with S\_OK as HResult. This is identical to the behavior that results if a client user selects the **Audio and Video Tuning Wizard** menu option while offline.

If audio levels have not been set previously on the client, calling [**StartVoice**](im-imessenger-startvoice.md) will display the **Audio and Video Tuning Wizard**. Without properly tuned levels, voice communication is difficult or impossible.

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



 

 





