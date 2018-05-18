---
title: IStoreFolder GetNextMessage method
description: Continues enumeration of messages using a provided handle and retrieves properties about the next result.
ms.assetid: '08f179ab-6849-4aa8-ab83-7996c801483a'
keywords: ["GetNextMessage method Windows Mail (formerly Outlook Express)", "GetNextMessage method Windows Mail (formerly Outlook Express) , IStoreFolder interface", "IStoreFolder interface Windows Mail (formerly Outlook Express) , GetNextMessage method"]
topic_type:
- apiref
api_name:
- IStoreFolder.GetNextMessage
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IStoreFolder::GetNextMessage method

Continues enumeration of messages using a provided handle and retrieves properties about the next result.

## Syntax


```C++
HRESULT GetNextMessage(
  [in]      HENUMSTORE     hEnum,
  [in]      DWORD          dwFlags,
  [in, out] LPMESSAGEPROPS pProps
);
```



## Parameters

<dl> <dt>

*hEnum* \[in\]
</dt> <dd>

Type: **HENUMSTORE**

Handle that specifies an existing enumeration to continue.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Flags that determine how the operation will be performed. Set to 0 to retrieve all properties of the message. Set to MSGPROPS\_FAST to expedite retrieval and return a limited set of message information.

</dd> <dt>

*pProps* \[in, out\]
</dt> <dd>

Type: **LPMESSAGEPROPS**

Pointer to a [**MESSAGEPROPS**](oe-messageprops.md) structure that receives the properties for the retrieved message.

</dd> </dl>

## Return value

Type: **HRESULT**

The function will return S\_OK if there are more folders to enumerate. If there are no more folders, the function will return S\_FALSE. If an error occurs, the following error code will be returned.



| Return code                                                                                  | Description                                                                     |
|----------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| <dl> <dt>**E\_INVALIDARG**</dt> </dl> | The *hEnum* parameter is invalid, or the *pProps* value is **NULL**.<br/> |



 

## Remarks

The first parameter to this method is the handle to an existing enumeration. To get a handle, you must first call [**IStoreFolder::GetFirstMessage**](oe-istorefolder-getfirstmessage.md).

If *dwFlags* is set to MSGPROPS\_FAST, only the following members of the structure referenced by the *pProps* structure will be valid.

-   cbSize
-   dwReserved
-   dwMessageId
-   dwLanguage
-   dwState

The [**MESSAGEPROPS**](oe-messageprops.md) structure that is received by the *pProps* parameter must be freed after use using the [**IStoreFolder::FreeMessageProps**](oe-istorefolder-freemessageprops.md) method.

When you have completed enumerating messages, call [**IStoreFolder::GetMessageClose**](oe-istorefolder-getmessageclose.md) to free memory associated with the enumeration.

The enumeration is not recursive.

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

**Reference**
</dt> <dt>

[**GetFirstMessage**](oe-istorefolder-getfirstmessage.md)
</dt> <dt>

[**GetMessageClose**](oe-istorefolder-getmessageclose.md)
</dt> </dl>

 

 





