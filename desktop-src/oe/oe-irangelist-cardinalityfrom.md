---
title: IRangeList CardinalityFrom method
description: Counts the members in the message range list that are larger than the specified starting point.
ms.assetid: '8d7a7ba0-49b7-40c3-8bcb-96a5f67192d7'
keywords: ["CardinalityFrom method Windows Mail (formerly Outlook Express)", "CardinalityFrom method Windows Mail (formerly Outlook Express) , IRangeList interface", "IRangeList interface Windows Mail (formerly Outlook Express) , CardinalityFrom method"]
topic_type:
- apiref
api_name:
- IRangeList.CardinalityFrom
api_location:
- Inetcomm.dll
api_type:
- COM
---

# IRangeList::CardinalityFrom method

\[**IRangeList::CardinalityFrom** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Counts the members in the message range list that are larger than the specified starting point.

## Syntax


```C++
HRESULT CardinalityFrom(
  [in]  const ULONG ulStartPoint,
  [out]       ULONG *pulCardinalityFrom
);
```



## Parameters

<dl> <dt>

*ulStartPoint* \[in\]
</dt> <dd>

Type: **const ULONG**

Specifies a **ULONG** that contains a starting point value. The starting point should be one less than the lowest number to be counted.

</dd> <dt>

*pulCardinalityFrom* \[out\]
</dt> <dd>

Type: **ULONG\***

Receives a pointer to a **ULONG** that contains the number of members in the range list which are larger than the starting point specified by *ulStartPoint*. A value of zero indicates that the sum of *ulStartPoint* + 1 is not in the range list.

</dd> </dl>

## Return value

Type: **HRESULT**

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

For example, for the range list "10–20,31,44,50–65", **CardinalityFrom**(43) returns 17. To include 44 in the count, a starting point number one less than 44 (that is, 43) is passed to the method.

## Requirements



|                                     |                                                                                                                |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                                           |
| Product<br/>                  | Outlook Express 6.0<br/>                                                                                 |
| Header<br/>                   | <dl> <dt>Imnxport.h</dt> </dl>                          |
| IDL<br/>                      | <dl> <dt>Imnxport.idl</dt> </dl>                        |
| DLL<br/>                      | <dl> <dt>Inetcomm.dll (version 6.0 or later)</dt> </dl> |



 

 





