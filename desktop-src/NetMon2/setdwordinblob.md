---
description: The SetDwordInBlob function sets the named DWORD value of a BLOB.
ms.assetid: 9174cd5c-4442-4fbe-8dc7-f8a74e1cc85d
title: SetDwordInBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetDwordInBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# SetDwordInBlob function

The **SetDwordInBlob** function sets the named **DWORD** value of a BLOB.

## Syntax


```C++
DWORD SetDwordInBlob(
  _In_       HBLOB hBlob,
  _In_ const char  *pOwnerName,
  _In_ const char  *pCategoryName,
  _In_ const char  *pTagName,
  _In_       DWORD Dword
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to a BLOB being set.

</dd> <dt>

*pOwnerName* \[in\]
</dt> <dd>

Pointer to the BLOB **Owner** name being set.

</dd> <dt>

*pCategoryName* \[in\]
</dt> <dd>

Pointer to the BLOB **Category** name being set.

</dd> <dt>

*pTagName* \[in\]
</dt> <dd>

Pointer to the BLOB **Tag** name being set.

</dd> <dt>

*Dword* \[in\]
</dt> <dd>

**DWORD** value of the BLOB being set.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that indicates the error.

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

[GetDwordFromBlob](getdwordfromblob.md)
</dt> <dt>

[SetBoolInBlob](setboolinblob.md)
</dt> <dt>

[SetClassIDInBlob](setclassidinblob.md)
</dt> <dt>

[SetMacAddressInBlob](setmacaddressinblob.md)
</dt> <dt>

[SetNetworkInfoInBlob](setnetworkinfoinblob.md)
</dt> <dt>

[SetNPPAddressFilterInBlob](setnppaddressfilterinblob.md)
</dt> <dt>

[SetNPPPatternFilterInBlob](setnpppatternfilterinblob.md)
</dt> <dt>

[SetNPPTriggerInBlob](setnpptriggerinblob.md)
</dt> <dt>

[SetStringInBlob](setstringinblob.md)
</dt> </dl>

 

 




