---
title: IMessenger2 ContactsSortOrder property
description: Sets or retrieves the current sort order for the local client, which is used to determine if the contacts should be sorted by groups or by their online/offline status.
ms.assetid: 75cbe224-23be-4e93-aefa-24c3f7f2ea47
keywords:
- ContactsSortOrder property Windows Messenger
- ContactsSortOrder property Windows Messenger , IMessenger2 interface
- IMessenger2 interface Windows Messenger , ContactsSortOrder property
topic_type:
- apiref
api_name:
- IMessenger2.ContactsSortOrder
- IMessenger2.get_ContactsSortOrder
- IMessenger2.put_ContactsSortOrder
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

# IMessenger2::ContactsSortOrder property

\[**ContactsSortOrder** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Sets or retrieves the current sort order for the local client, which is used to determine if the contacts should be sorted by groups or by their online/offline status.

This property is read/write.

## Syntax


```C++
HRESULT put_ContactsSortOrder(
  [in]          MUASORT Sort
);

HRESULT get_ContactsSortOrder(
  [out, retval] MUASORT *pSort
);
```



## Property value

## Error codes

Returns one of the following values.



| Name                                                                                                     | Meaning                                                   |
|----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------|
| <dl> <dt>S\_OK</dt> </dl>                         | Success. <br/>                                      |
| <dl> <dt>E\_INVALIDARG</dt> </dl>                 | [**MUASORT**](im-muasort.md) is out of range.<br/> |
| <dl> <dt>E\_FAIL</dt> </dl>                       | The Messenger application window is closed.<br/>    |
| <dl> <dt>MSGR\_E\_NOT\_LOGGED\_ON</dt> </dl>      | The local client is not logged on. <br/>            |
| <dl> <dt>MSGR\_E\_GROUPS\_NOT\_ENABLED</dt> </dl> | Groups are not supported. <br/>                     |
| <dl> <dt>RPC\_X\_NULL\_REF\_POINTER</dt> </dl>    | *pSort* is a **NULL** pointer. <br/>                |



## Remarks

Some services, such as Microsoft Exchange Instant Messaging Service (IM), do not support groups. The use of this property on these services will return the error **MSGR\_E\_GROUPS\_NOT\_ENABLED**.

> [!Note]  
> The following remarks apply to scripting languages. The **get\_ContactsSort** property is available for scripting languages; **put\_ContactsSort** is not.

 

## Requirements



|                                  |                                                                                       |
|----------------------------------|---------------------------------------------------------------------------------------|
| End of client support<br/> | Windows XP<br/>                                                                 |
| End of server support<br/> | Windows Server 2003<br/>                                                        |
| Header<br/>                | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                   | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                   | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





