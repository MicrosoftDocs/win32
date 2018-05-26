---
title: IRangeList AddSingleValue method
description: Adds a single value to the message range list.
ms.assetid: 5d0a14c4-5f81-4f1e-b08f-f69b46e8852c
keywords:
- AddSingleValue method Windows Mail (formerly Outlook Express)
- AddSingleValue method Windows Mail (formerly Outlook Express) , IRangeList interface
- IRangeList interface Windows Mail (formerly Outlook Express) , AddSingleValue method
topic_type:
- apiref
api_name:
- IRangeList.AddSingleValue
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

# IRangeList::AddSingleValue method

\[**IRangeList::AddSingleValue** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds a single value to the message range list.

## Syntax


```C++
HRESULT AddSingleValue(
  [in] const ULONG value
);
```



## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

Type: **const ULONG**

Specifies the single value to add to the range list.



| Value                                                                                                                                                                                                                                 | Meaning                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="RL_LAST_MESSAGE"></span><span id="rl_last_message"></span><dl> <dt>**RL\_LAST\_MESSAGE**</dt> <dt>((ULONG)-1)</dt> </dl> | Equivalent to "\*" in an IMAP range list. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                                   | Description                                                     |
|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>          | Indicates success.<br/>                                   |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

For example, **AddSingleValue**(69) adds 69 to the range list.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





