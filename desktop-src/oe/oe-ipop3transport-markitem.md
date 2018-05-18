---
title: IPOP3Transport MarkItem method
description: Marks a message with the intended action.
ms.assetid: '28c007d7-db8e-47ec-9a2f-5d4d84d6320a'
keywords: ["MarkItem method Windows Mail (formerly Outlook Express)", "MarkItem method Windows Mail (formerly Outlook Express) , IPOP3Transport interface", "IPOP3Transport interface Windows Mail (formerly Outlook Express) , MarkItem method"]
topic_type:
- apiref
api_name:
- IPOP3Transport.MarkItem
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IPOP3Transport::MarkItem method

\[**IPOP3Transport::MarkItem** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Marks a message with the intended action.

## Syntax


```C++
HRESULT MarkItem(
  [in] POP3MARKTYPE marktype,
  [in] DWORD        dwPopId,
  [in] boolean      fMarked
);
```



## Parameters

<dl> <dt>

*marktype* \[in\]
</dt> <dd>

Type: **[**POP3MARKTYPE**](oe-pop3marktype.md)**

Specifies a [**POP3MARKTYPE**](oe-pop3marktype.md) value that indicates the command to use for the message.

</dd> <dt>

*dwPopId* \[in\]
</dt> <dd>

Type: **DWORD**

Specifies a **DWORD** that contains the ID of the message.

</dd> <dt>

*fMarked* \[in\]
</dt> <dd>

Type: **boolean**

Specifies whether the message should be marked with the specified *marktype* or the mark should be cleared.



| Value                                                                                                                                | Meaning                                                         |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <span id="FALSE"></span><span id="false"></span><dl> <dt>**FALSE**</dt> </dl> | Removes the specified *marktype* from the bitfield. <br/> |
| <span id="TRUE"></span><span id="true"></span><dl> <dt>**TRUE**</dt> </dl>    | Sets the specified *marktype* in the bitfield. <br/>      |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                               | Description                                                                                   |
|-----------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>                      | Indicates success. <br/>                                                                |
| <dl> <dt>**IXP\_E\_POP3\_NEED\_STAT**</dt> </dl>   | Indicates that status has not been requested from the server during this session. <br/> |
| <dl> <dt>**IXP\_E\_POP3\_NO\_MESSAGES**</dt> </dl> | Indicates that there are no messages. <br/>                                             |
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>              | Indicates that *marktype* or *dwPopId* is invalid. <br/>                                |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





