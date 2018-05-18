---
title: IStoreFolder RegisterNotification method
description: Registers a window to receive notification messages whenever an operation is performed on the folder associated with this interface.
ms.assetid: '0ca50bd7-f706-4fbb-90a5-0e48f2fcb698'
keywords: ["RegisterNotification method Windows Mail (formerly Outlook Express)", "RegisterNotification method Windows Mail (formerly Outlook Express) , IStoreFolder interface", "IStoreFolder interface Windows Mail (formerly Outlook Express) , RegisterNotification method"]
topic_type:
- apiref
api_name:
- IStoreFolder.RegisterNotification
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreFolder::RegisterNotification method

Registers a window to receive notification messages whenever an operation is performed on the folder associated with this interface.

## Syntax


```C++
HRESULT RegisterNotification(
  [in] DWORD dwReserved,
  [in] HWND  hwnd
);
```



## Parameters

<dl> <dt>

*dwReserved* \[in\]
</dt> <dd>

Type: **DWORD**

Reserved value. Must be 0.

</dd> <dt>

*hwnd* \[in\]
</dt> <dd>

Type: **HWND**

Handle to a window that will receive the notifications.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                  | Description                                                                                                                                                                     |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *dwReserved* parameter is not 0, or the *hwnd* value is **NULL** or does not specify a valid window.<br/>                                                             |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | A notification has already been registered. To remove the notification, call [**IStoreFolder::UnregisterNotification**](oe-istorefolder-unregisternotification.md).<br/> |



 

## Remarks

Once registered, the window specified by *hwnd* can receive the following messages.



|                    |                                                                                                                                                                                                                   |
|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| WM\_NEWMSGS        | Sent when a new message has arrived. The **WPARAM** value is a pointer to the ID of the new message.                                                                                                              |
| WM\_MARKEDASREAD   | Sent when a message has been marked as read. The **WPARAM** value is a pointer to the ID of the message. If the **WPARAM** value is equal to 0xffffffff, all messages in the folder have been marked as read.     |
| WM\_MARKEDASUNREAD | Sent when a message has been marked as unread. The **WPARAM** value is a pointer to the ID of the message. If the **WPARAM** value is equal to 0xffffffff, all messages in the folder have been marked as unread. |
| WM\_DELETEMSGS     | Sent when a message has been deleted. **WPARAM** is a pointer to the ID of the message.                                                                                                                           |
| WM\_DELETEFOLDER   | Sent when a folder has been deleted. The **WPARAM** value is a pointer to the **STOREFOLDERID** of the folder.                                                                                                    |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IStoreFolder**](oe-istorefolder.md)
</dt> <dt>

[**IStoreFolder::UnregisterNotification**](oe-istorefolder-unregisternotification.md)
</dt> </dl>

 

 





