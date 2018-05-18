---
title: IStoreNamespace UnregisterNotification method
description: Unregisters a window from receiving WM\_FOLDERNOTIFY messages whenever folder operations are performed.
ms.assetid: 'c77b7de3-b668-4526-a588-8da85805bf48'
keywords: ["UnregisterNotification method Windows Mail (formerly Outlook Express)", "UnregisterNotification method Windows Mail (formerly Outlook Express) , IStoreNamespace interface", "IStoreNamespace interface Windows Mail (formerly Outlook Express) , UnregisterNotification method"]
topic_type:
- apiref
api_name:
- IStoreNamespace.UnregisterNotification
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreNamespace::UnregisterNotification method

Unregisters a window from receiving **WM\_FOLDERNOTIFY** messages whenever folder operations are performed.

## Syntax


```C++
HRESULT UnregisterNotification(
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

Handle to a window to unregister.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                                  | Description                                                                                                                                                |
|--------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>                 | The value of *hwnd* is **NULL** or specifies an invalid window, or *dwReserved* is not 0.<br/>                                                       |
| <dl> <dt>**MSOEAPI\_E\_STORE\_INITIALIZE**</dt> </dl> | The namespace has not been initialized. To initialize the namespace, call [**IStoreNamespace::Initialize**](oe-istorenamespace-initialize.md).<br/> |



 

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

[**IStoreNamespace**](oe-istorenamespace.md)
</dt> <dt>

[**IStoreNamespace::RegisterNotification**](oe-istorenamespace-registernotification.md)
</dt> </dl>

 

 





