---
title: IRangeList DeleteRange method
description: Removes a range of values from the message range list.
ms.assetid: 59c80236-7ce5-4e1d-baf7-8abf099e9bfb
keywords:
- DeleteRange method Windows Mail (formerly Outlook Express)
- DeleteRange method Windows Mail (formerly Outlook Express) , IRangeList interface
- IRangeList interface Windows Mail (formerly Outlook Express) , DeleteRange method
topic_type:
- apiref
api_name:
- IRangeList.DeleteRange
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

# IRangeList::DeleteRange method

\[**IRangeList::DeleteRange** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Removes a range of values from the message range list.

## Syntax


```C++
HRESULT DeleteRange(
  [in] const ULONG low,
  [in] const ULONG high
);
```



## Parameters

<dl> <dt>

*low* \[in\]
</dt> <dd>

Type: **const ULONG**

Specifies a **ULONG** that contains the low number of the range to delete from the range list.

</dd> <dt>

*high* \[in\]
</dt> <dd>

Type: **const ULONG**

Specifies a **ULONG** that contains the high number of the range to delete from the range list.



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
| <dl> <dt>**E\_INVALIDARG**</dt> </dl>  | Indicates that the range list is empty. <br/>             |
| <dl> <dt>**E\_OUTOFMEMORY**</dt> </dl> | Indicates that an attempt to allocate memory failed.<br/> |



 

## Remarks

For example, **DeleteRange**(7,11) removes the values 7 through 11 from the range list.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





