---
description: Sets the BLOB pattern match filter.
ms.assetid: 44e7c67a-f430-4d68-bc7f-f6bbd5b9e5a9
title: SetNPPPatternFilterInBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetNPPPatternFilterInBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# SetNPPPatternFilterInBlob function

The **SetNPPPatternFilterInBlob** function sets the BLOB pattern match filter.

## Syntax


```C++
DWORD SetNPPPatternFilterInBlob(
  _In_  HBLOB        hBlob,
  _In_  LPEXPRESSION pExpression,
  _Out_ HBLOB        hErrorBlob
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

The handle to the BLOB.

</dd> <dt>

*pExpression* \[in\]
</dt> <dd>

A pointer to an [EXPRESSION](expression.md) structure that defines the filter expression being set.

</dd> <dt>

*hErrorBlob* \[out\]
</dt> <dd>

The handle to an error BLOB that specifies where in the original BLOB the error (if any) occurred.

</dd> </dl>

## Return value

If the **SetNPPPatternFilterInBlob** function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that indicates the error.

## Remarks

The pattern match filter data stored in the **Config** category of the BLOB.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                              |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                    |
| Header<br/>                   | <dl> <dt>Netmon.h</dt> </dl>     |
| Library<br/>                  | <dl> <dt>Npptools.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Npptools.dll</dt> </dl> |



## See also

<dl> <dt>

[GetNPPAddressFilterFromBlob](getnppaddressfilterfromblob.md)
</dt> <dt>

[SetBoolInBlob](setboolinblob.md)
</dt> <dt>

[SetClassIDInBlob](setclassidinblob.md)
</dt> <dt>

[SetDwordInBlob](setdwordinblob.md)
</dt> <dt>

[SetMacAddressInBlob](setmacaddressinblob.md)
</dt> <dt>

[SetNetworkInfoInBlob](setnetworkinfoinblob.md)
</dt> <dt>

[SetNPPAddressFilterInBlob](setnppaddressfilterinblob.md)
</dt> <dt>

[SetNPPTriggerInBlob](setnpptriggerinblob.md)
</dt> <dt>

[SetStringInBlob](setstringinblob.md)
</dt> </dl>

 

 




