---
title: IRangeList IsInRange method
description: Determines whether the specified value is in the message range list.
ms.assetid: 7cd3c11e-9009-4317-bb67-944db77a948e
keywords:
- IsInRange method Windows Mail (formerly Outlook Express)
- IsInRange method Windows Mail (formerly Outlook Express) , IRangeList interface
- IRangeList interface Windows Mail (formerly Outlook Express) , IsInRange method
topic_type:
- apiref
api_name:
- IRangeList.IsInRange
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

# IRangeList::IsInRange method

\[**IRangeList::IsInRange** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Determines whether the specified value is in the message range list.

## Syntax


```C++
HRESULT IsInRange(
  [in] const ULONG value
);
```



## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

Type: **const ULONG**

Specifies the value to test against the range list.



| Value                                                                                                                                                                                                                                 | Meaning                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="RL_LAST_MESSAGE"></span><span id="rl_last_message"></span><dl> <dt>**RL\_LAST\_MESSAGE**</dt> <dt>((ULONG)-1)</dt> </dl> | Equivalent to "\*" in an IMAP range list. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

Returns one of the following values.



| Return code                                                                             | Description                                                               |
|-----------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| <dl> <dt>**S\_OK**</dt> </dl>    | Indicates that the specified value is in the range list. <br/>      |
| <dl> <dt>**S\_FALSE**</dt> </dl> | Indicates that the specified value is outside the range list. <br/> |



 

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





