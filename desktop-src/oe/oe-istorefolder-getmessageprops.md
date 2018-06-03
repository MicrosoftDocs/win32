---
title: IStoreFolder GetMessageProps method
description: Gets properties of a specified message.
ms.assetid: 6a63da65-6fd5-4571-ac92-4d33b80cae82
keywords:
- GetMessageProps method Windows Mail (formerly Outlook Express)
- GetMessageProps method Windows Mail (formerly Outlook Express) , IStoreFolder interface
- IStoreFolder interface Windows Mail (formerly Outlook Express) , GetMessageProps method
topic_type:
- apiref
api_name:
- IStoreFolder.GetMessageProps
api_location:
- Inetcomm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IStoreFolder::GetMessageProps method

Gets properties of a specified message.

## Syntax


```C++
HRESULT GetMessageProps(
  [in]      MESSAGEID      dwMessageId,
  [in]      DWORD          dwFlags,
  [in, out] LPMESSAGEPROPS pProps
);
```



## Parameters

<dl> <dt>

*dwMessageId* \[in\]
</dt> <dd>

Type: **MESSAGEID**

Specifies the message for which properties will be retrieved.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Flags that determine how the operation will be performed. Set to 0 to retrieve all properties of the specified message. Set to MSGPROPS\_FAST to expedite retrieval and return a limited set of message information.

</dd> <dt>

*pProps* \[in, out\]
</dt> <dd>

Type: **LPMESSAGEPROPS**

Pointer to a [**MESSAGEPROPS**](oe-messageprops.md) structure that receives the properties for the specified message.

</dd> </dl>

## Return value

Type: **HRESULT**

Returns S\_OK if successful, or one of the following error values.



| Return code                                                                                  | Description                                                                              |
|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The value of *dwMessageId* is invalid, or the *pProps* parameter is **NULL**.<br/> |
| <dl> <dt>**E\_FAIL**</dt> </dl>       | The message referenced by *dwMessageId* was not found.<br/>                        |



 

## Remarks

If *dwFlags* is set to MSGPROPS\_FAST, only the following members of the structure referenced by the *pProps* structure will be valid.

-   cbSize
-   dwReserved
-   dwMessageId
-   dwLanguage
-   dwState

The [**MESSAGEPROPS**](oe-messageprops.md) structure that is received by the *pProps* parameter must be freed after use using the [**IStoreFolder::FreeMessageProps**](oe-istorefolder-freemessageprops.md) method.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Msoeapi.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Msoeapi.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





