---
title: DMsgrObjectEvents OnTextReceived event
description: Indicates that a message has been received.
ms.assetid: '15c6e599-422e-4c01-8ae5-07c555a55102'
keywords: ["OnTextReceived event Windows Messenger", "OnTextReceived event Windows Messenger , DMsgrObjectEvents interface", "DMsgrObjectEvents interface Windows Messenger , OnTextReceived event"]
topic_type:
- apiref
api_name:
- DMsgrObjectEvents.OnTextReceived
api_type:
- COM
---

# DMsgrObjectEvents::OnTextReceived event

\[**OnTextReceived** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Indicates that a message has been received.

> [!Note]  
> The **OnTextReceived** event is available for use in Windows Messenger 4.7. It might be altered or unavailable in subsequent versions of Windows Messenger.

 

## Syntax


```C++
void OnTextReceived(
  [in]      IMsgrIMSession *pIMSession,
  [in]      IMsgrUser      *pSourceUser,
  [in]      BSTR           bstrMsgHeader,
  [in]      BSTR           bstrMsgText,
  [in, out] VARIANT_BOOL   *pfEnableDefault
);
```



## Parameters

<dl> <dt>

*pIMSession* \[in\]
</dt> <dd>

Pointer to an [**IMsgrIMSession**](im-imsgrimsession.md) interface.

</dd> <dt>

*pSourceUser* \[in\]
</dt> <dd>

Pointer to an [**IMsgrUser**](im-imsgruser.md) interface.

</dd> <dt>

*bstrMsgHeader* \[in\]
</dt> <dd>

**BSTR** that contains the header text.

</dd> <dt>

*bstrMsgText* \[in\]
</dt> <dd>

**BSTR** that contains the message text.

</dd> <dt>

*pfEnableDefault* \[in, out\]
</dt> <dd>

Pointer to a **VARIANT\_BOOL** that indicates whether the default is enabled.

</dd> </dl>

## Return value

This event does not return a value.

## Requirements



|                                  |                                |
|----------------------------------|--------------------------------|
| End of client support<br/> | Windows XP<br/>          |
| End of server support<br/> | Windows Server 2003<br/> |



 

 





