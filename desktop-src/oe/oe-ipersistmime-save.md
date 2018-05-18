---
title: IPersistMime Save method
description: Persists an IMimeMessage object.
ms.assetid: '57f0b1c8-1a13-4cb2-8b7b-36c0da8cd48a'
keywords: ["Save method Windows Mail (formerly Outlook Express)", "Save method Windows Mail (formerly Outlook Express) , IPersistMime interface", "IPersistMime interface Windows Mail (formerly Outlook Express) , Save method"]
topic_type:
- apiref
api_name:
- IPersistMime.Save
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IPersistMime::Save method

\[**IPersistMime::Save** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Persists an [**IMimeMessage**](oe-imimemessage.md) object.

## Syntax


```C++
HRESULT Save(
  [in] IMimeMessage *pMsg,
  [in] DWORD        dwFlags
);
```



## Parameters

<dl> <dt>

*pMsg* \[in\]
</dt> <dd>

Type: **[**IMimeMessage**](oe-imimemessage.md)\***

Specifies the message to save.

</dd> <dt>

*dwFlags* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies the format.

<dl> <dt>

<span id="PMS_HTML"></span><span id="pms_html"></span>**PMS\_HTML** (0x00000001)
</dt> <dt>

<span id="PMS_TEXT"></span><span id="pms_text"></span>**PMS\_TEXT** (0x00000002)
</dt> </dl> </dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                          | Description                     |
|------------------------------------------------------------------------------------------------------|---------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                 | Indicates success. <br/>  |
| <dl> <dt>**MAPI\_E\_USER\_CANCEL**</dt> </dl> | Indicates canceled. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Mimeole.h</dt> </dl>                           |
| IDL<br/>                      | <dl> <dt>Mimeole.idl</dt> </dl>                         |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





