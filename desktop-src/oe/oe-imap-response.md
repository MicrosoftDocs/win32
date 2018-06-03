---
title: IMAP\_RESPONSE structure
description: Holds responses from the Internet Message Access Protocol (IMAP) server.
ms.assetid: e62265c9-3627-4f3d-9b45-9a3c22d5af05
keywords:
- IMAP_RESPONSE structure Windows Mail (formerly Outlook Express)
- IMAPADDR structure Windows Mail (formerly Outlook Express)
topic_type:
- apiref
api_name:
- IMAPADDR
api_location:
- Imnxport.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: structure
ms.date: 05/31/2018
---

# IMAP\_RESPONSE structure

\[**IMAP\_RESPONSE** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Holds responses from the Internet Message Access Protocol (IMAP) server.

## Syntax


```C++
typedef struct tagIMAP_RESPONSE {
  WPARAM             wParam;
  LPARAM             lParam;
  HRESULT            hrResult;
  LPSTR              lpszResponseText;
  IMAP_RESPONSE_TYPE irtResponseType;
  IMAP_RESPONSE_DATA irdResponseData;
} IMAPADDR;
```



## Members

<dl> <dt>

**wParam**
</dt> <dd>

Type: **WPARAM**

</dd> <dd>

Contains a **WPARAM** that together with **lParam** forms a unique transaction ID. The value is zero for unsolicited or unresolvable responses.

</dd> <dt>

**lParam**
</dt> <dd>

Type: **LPARAM**

</dd> <dd>

Contains an **LPARAM** that together with **wParam** forms a unique transaction ID. The value is zero for unsolicited or unresolvable responses.

</dd> <dt>

**hrResult**
</dt> <dd>

Type: **HRESULT**

</dd> <dd>

Contains any error code encountered while processing the server response.

</dd> <dt>

**lpszResponseText**
</dt> <dd>

Type: **LPSTR**

</dd> <dd>

Contains a **LPSTR** that contains the text of the server response. This parameter is **NULL** when **irtResponseType** is [**irtAPPEND\_PROGRESS**](oe-imap-response-type.md), **irtAPPLICABLE\_FLAGS**, **irtDELETED\_MSG**, **irtFETCH\_BODY**, **irtMAILBOX\_LISTING**, **irtMAILBOX\_STATUS**, **irtMAILBOX\_UPDATE**, **irtSEARCH**, **irtUPDATE\_MSG**, or **irtUPDATE\_MSG\_EX**.

</dd> <dt>

**irtResponseType**
</dt> <dd>

Type: **[**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md)**

</dd> <dd>

Contains an [**IMAP\_RESPONSE\_TYPE**](oe-imap-response-type.md) value that categorizes the response.

</dd> <dt>

**irdResponseData**
</dt> <dd>

Type: **[**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md)**

</dd> <dd>

Contains an [**IMAP\_RESPONSE\_DATA**](oe-imap-response-data.md) structure that contains various information dependent on the specific **irtResponseType**.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                             |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                    |
| Product<br/>                  | Outlook Express 6.0<br/>                                                          |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl> |



 

 





