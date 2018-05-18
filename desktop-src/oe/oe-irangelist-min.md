---
title: IRangeList Min method
description: Returns the minimum value in the message range list.
ms.assetid: '8eb985d3-9cdd-4d84-87fe-826c9b05e719'
keywords: ["Min method Windows Mail (formerly Outlook Express)", "Min method Windows Mail (formerly Outlook Express) , IRangeList interface", "IRangeList interface Windows Mail (formerly Outlook Express) , Min method"]
topic_type:
- apiref
api_name:
- IRangeList.Min
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IRangeList::Min method

\[**IRangeList::Min** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the minimum value in the message range list.

## Syntax


```C++
HRESULT Min(
  [out] ULONG *pulMin
);
```



## Parameters

<dl> <dt>

*pulMin* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the minimum value in the range list.



| Value                                                                                                                                                                                                                              | Meaning                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="RL_RANGE_ERROR"></span><span id="rl_range_error"></span><dl> <dt>**RL\_RANGE\_ERROR**</dt> <dt>((ULONG)-1)</dt> </dl> | Indicates that the range list is empty. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example, for the range list "10–20,31,44,50–65", **Min**() returns 10.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





