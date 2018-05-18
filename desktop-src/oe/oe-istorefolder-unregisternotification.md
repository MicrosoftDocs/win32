---
title: IStoreFolder UnregisterNotification method
description: Unregisters a window from receiving notification messages whenever message operations are performed in this folder.
ms.assetid: '296de1d5-a1a0-491e-829a-6babe808231d'
keywords: ["UnregisterNotification method Windows Mail (formerly Outlook Express)", "UnregisterNotification method Windows Mail (formerly Outlook Express) , IStoreFolder interface", "IStoreFolder interface Windows Mail (formerly Outlook Express) , UnregisterNotification method"]
topic_type:
- apiref
api_name:
- IStoreFolder.UnregisterNotification
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreFolder::UnregisterNotification method

Unregisters a window from receiving notification messages whenever message operations are performed in this folder.

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



| Return code                                                                                  | Description                                                                                                                                                          |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *dwReserved* parameter is not 0, or the *hwnd* value is **NULL** or does not specify a valid window.<br/>                                                  |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | No notification has been registered. To register a notification, call [**IStoreFolder::RegisterNotification**](oe-istorefolder-registernotification.md).<br/> |



 

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

[**IStoreFolder::RegisterNotification**](oe-istorefolder-registernotification.md)
</dt> </dl>

 

 





