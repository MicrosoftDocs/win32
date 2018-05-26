---
title: DMessengerAppEvents interface
description: Do not use. The DMessengerAppEvents dispinterface handles events that are generated or received by a MessengerApp object.
ms.assetid: 5cbe8b44-4334-4861-b4c9-e7b04c2b0208
keywords:
- DMessengerAppEvents interface Windows Messenger
- DMessengerAppEvents interface Windows Messenger , described
topic_type:
- apiref
api_name:
- DMessengerAppEvents
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# DMessengerAppEvents interface

\[**DMessengerAppEvents** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The **DMessengerAppEvents** dispinterface handles events that are generated or received by a [**MessengerApp**](im-messengerapp.md) object.

## Members

The **DMessengerAppEvents** interface inherits from the [**IUnknown**](https://msdn.microsoft.com/library/windows/desktop/ms680509) interface. **DMessengerAppEvents** also has these types of members:

-   [Events](#events)

### Events

The **DMessengerAppEvents** interface has these events.



| Event                                                                                       | Description                         |
|:--------------------------------------------------------------------------------------------|:------------------------------------|
| [**OnBeforeLaunchIMUI**](im-dmsgrobjectevents-onbeforelaunchimui.md)                       | Not currently supported.<br/> |
| [**OnDestroyIMUI**](im-dmsgrobjectevents-ondestroyimui.md)                                 | Not currently supported.<br/> |
| [**OnFileTransferIMUI**](im-dmsgrobjectevents-onfiletransferimui.md)                       | Not currently supported.<br/> |
| [**OnIndicateMessageReceivedIMUI**](im-dmsgrobjectevents-onindicatemessagereceivedimui.md) | Not currently supported.<br/> |
| [**OnInfobarTextIMUI**](im-dmsgrobjectevents-oninfobartextimui.md)                         | Not currently supported.<br/> |
| [**OnMicrophoneMuteIMUI**](im-dmsgrobjectevents-onmicrophonemuteimui.md)                   | Not currently supported.<br/> |
| [**OnSendEnabledIMUI**](im-dmsgrobjectevents-onsendenabledimui.md)                         | Not currently supported.<br/> |
| [**OnShowIMUI**](im-dmsgrobjectevents-onshowimui.md)                                       | Not currently supported.<br/> |
| [**OnStatusTextIMUI**](im-dmsgrobjectevents-onstatustextimui.md)                           | Not currently supported.<br/> |
| [**OnTitlebarTextIMUI**](im-dmsgrobjectevents-ontitlebartextimui.md)                       | Not currently supported.<br/> |
| [**OnVoiceSessionStateIMUI**](im-dmsgrobjectevents-onvoicesessionstateimui.md)             | Not currently supported.<br/> |



 

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                          |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows XP<br/>                                                                |
| End of server support<br/>    | Windows Server 2003<br/>                                                       |
| Product<br/>                  | Messenger 4.0<br/>                                                             |
| Header<br/>                   | <dl> <dt>Mdisp.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Mdisp.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl> |



 

 





