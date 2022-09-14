---
description: The SetBoolInBlob function sets a Boolean value at a given location within a BLOB.
ms.assetid: 354d22be-b8c4-4068-8356-19b30ac188d0
title: SetBoolInBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetBoolInBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# SetBoolInBlob function

The **SetBoolInBlob** function sets a Boolean value at a given location within a BLOB.

## Syntax


```C++
DWORD SetBoolInBlob(
  _In_       HBLOB hBlob,
  _In_ const char  *pOwnerName,
  _In_ const char  *pCategoryName,
  _In_ const char  *pTagName,
  _In_       BOOL  Bool
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to a BLOB.

</dd> <dt>

*pOwnerName* \[in\]
</dt> <dd>

Pointer to the BLOB **Owner** name.

</dd> <dt>

*pCategoryName* \[in\]
</dt> <dd>

Pointer to the BLOB **Category** name.

</dd> <dt>

*pTagName* \[in\]
</dt> <dd>

Pointer to the BLOB **Tag** name.

</dd> <dt>

*Bool* \[in\]
</dt> <dd>

Boolean value that is set at the given location.

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

[GetBoolFromBlob](getboolfromblob.md)
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

[SetNPPPatternFilterInBlob](setnpppatternfilterinblob.md)
</dt> <dt>

[SetNPPTriggerInBlob](setnpptriggerinblob.md)
</dt> <dt>

[SetStringInBlob](setstringinblob.md)
</dt> </dl>

 

 




