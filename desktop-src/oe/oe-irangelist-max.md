---
title: IRangeList Max method
description: Returns the maximum value in the message range list.
ms.assetid: '18a8937f-cf74-4d46-9fbf-475953caef3d'
keywords: ["Max method Windows Mail (formerly Outlook Express)", "Max method Windows Mail (formerly Outlook Express) , IRangeList interface", "IRangeList interface Windows Mail (formerly Outlook Express) , Max method"]
topic_type:
- apiref
api_name:
- IRangeList.Max
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IRangeList::Max method

\[**IRangeList::Max** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Returns the maximum value in the message range list.

## Syntax


```C++
HRESULT Max(
  [out] ULONG *pulMax
);
```



## Parameters

<dl> <dt>

*pulMax* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the maximum value in the range list.



| Value                                                                                                                                                                                                                              | Meaning                                             |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| <span id="RL_RANGE_ERROR"></span><span id="rl_range_error"></span><dl> <dt>**RL\_RANGE\_ERROR**</dt> <dt>((ULONG)-1)</dt> </dl> | Indicates that the range list is empty. <br/> |



 

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example, for the range list "10–20,31,44,50–65", **Max**() returns 65.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





