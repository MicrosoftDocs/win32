---
title: IRangeList Next method
description: Returns the next value in the message range list by determining the smallest value in the list that is greater than the specified value.
ms.assetid: 5e069546-72c8-47ab-9c4a-9cae43a6eec2
keywords:
- Next method Windows Mail (formerly Outlook Express)
- Next method Windows Mail (formerly Outlook Express) , IRangeList interface
- IRangeList interface Windows Mail (formerly Outlook Express) , Next method
topic_type:
- apiref
api_name:
- IRangeList.Next
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

# IRangeList::Next method

\[**IRangeList::Next** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the next value in the message range list by determining the smallest value in the list that is greater than the specified value.

## Syntax


```C++
HRESULT Next(
  [in]  const ULONG current,
  [out]       ULONG *pulNext
);
```



## Parameters

<dl> <dt>

*current* \[in\]
</dt> <dd>

Type: **const ULONG**

Specifies a **ULONG** that contains the value to use as the basis for finding the next value.

</dd> <dt>

*pulNext* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the next number in the range list.



| Value                                                                                                                                                                                                                              | Meaning                                                                                      |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| <span id="RL_RANGE_ERROR"></span><span id="rl_range_error"></span><dl> <dt>**RL\_RANGE\_ERROR**</dt> <dt>((ULONG)-1)</dt> </dl> | Indicates that the range list is empty or that the next number is out of bounds. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example, for the range list "10 20,31,44,50 65", **Next**(31) returns 44.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





