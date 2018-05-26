---
title: IRangeList MaxOfRange method
description: Finds the range in the message range list that the specified value belongs to and returns the maximum value of that range.
ms.assetid: 77f600ca-5970-45cb-8e93-98067b785060
keywords:
- MaxOfRange method Windows Mail (formerly Outlook Express)
- MaxOfRange method Windows Mail (formerly Outlook Express) , IRangeList interface
- IRangeList interface Windows Mail (formerly Outlook Express) , MaxOfRange method
topic_type:
- apiref
api_name:
- IRangeList.MaxOfRange
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

# IRangeList::MaxOfRange method

\[**IRangeList::MaxOfRange** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Finds the range in the message range list that the specified value belongs to and returns the maximum value of that range.

## Syntax


```C++
HRESULT MaxOfRange(
  [in]  const ULONG value,
  [out]       ULONG *pulMaxOfRange
);
```



## Parameters

<dl> <dt>

*value* \[in\]
</dt> <dd>

Type: **const ULONG**

Specifies a **ULONG** that contains a value within the range whose maximum value is returned.



| Value                                                                                                                                                                                                                                 | Meaning                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="RL_LAST_MESSAGE"></span><span id="rl_last_message"></span><dl> <dt>**RL\_LAST\_MESSAGE**</dt> <dt>((ULONG)-1)</dt> </dl> | Equivalent to "\*" in an IMAP range list. <br/> |



 

</dd> <dt>

*pulMaxOfRange* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the maximum value in the range that includes *value*.



| Value                                                                                                                                                                                                                              | Meaning                                                                  |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|
| <span id="RL_RANGE_ERROR"></span><span id="rl_range_error"></span><dl> <dt>**RL\_RANGE\_ERROR**</dt> <dt>((ULONG)-1)</dt> </dl> | Indicates that *value* could not be found in the range list. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example, for the range list "10 20,30,40 50", **MaxOfRange**(15) returns 20.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





