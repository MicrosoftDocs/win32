---
title: IStoreNamespace RegisterNotification method
description: Registers a window to receive a WM\_FOLDERNOTIFY message whenever a folder operation is performed.
ms.assetid: 6783f856-2686-43de-b991-39b88125f7a1
keywords:
- RegisterNotification method Windows Mail (formerly Outlook Express)
- RegisterNotification method Windows Mail (formerly Outlook Express) , IStoreNamespace interface
- IStoreNamespace interface Windows Mail (formerly Outlook Express) , RegisterNotification method
topic_type:
- apiref
api_name:
- IStoreNamespace.RegisterNotification
api_location:
- Inetcomm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IStoreNamespace::RegisterNotification method

Registers a window to receive a **WM\_FOLDERNOTIFY** message whenever a folder operation is performed.

## Syntax


```C++
HRESULT RegisterNotification(
  [in] DWORD dwReserved,
  [in] HWND  hwnd
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



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *hwnd* is **NULL** or specifies an invalid window, or *dwReserved* is not 0.<br/>                                                       |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

## Remarks

The window specified by *hwnd* will receive **WM\_FOLDERNOTIFY** messages. The **LPARAM** of these messages is a pointer to a [**FOLDERNOTIFYEX**](oe-foldernotifyex.md) structure that contains information about the message. This pointer has memory associated with it, and must be freed after use by calling [CoTaskMemFree](http://msdn.microsoft.com/library/com/htm/cmf_a2c_63l1.asp) and passing the **LPARAM** value as the first parameter.

The window specified by *hwnd* will receive notifications for all folder operations. To register for folder-specific notifications, use [**IStoreFolder::RegisterNotification**](oe-istorefolder-registernotification.md).

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



## See also

<dl> <dt>

[**IStoreNamespace**](oe-istorenamespace.md)
</dt> <dt>

[**IStoreNamespace::UnregisterNotification**](oe-istorenamespace-unregisternotification.md)
</dt> </dl>

 

 





