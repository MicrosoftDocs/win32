---
description: Sets a string at a given location within a BLOB.
ms.assetid: 645e6b8b-aaaf-429f-ad2f-bf4364ef4e80
title: SetStringInBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetStringInBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# SetStringInBlob function

The **SetStringInBlob** function sets a string at a given location within a BLOB.

## Syntax


```C++
DWORD SetStringInBlob(
  _In_       HBLOB hBlob,
  _In_ const char  *pOwnerName,
  _In_ const char  *pCategoryName,
  _In_ const char  *pTagName,
  _In_ const char  *pString
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

A handle to the BLOB.

</dd> <dt>

*pOwnerName* \[in\]
</dt> <dd>

A pointer to the **Owner** section of the BLOB, where the string is set.

</dd> <dt>

*pCategoryName* \[in\]
</dt> <dd>

A pointer to the **Category** section of the BLOB, where the string is set.

</dd> <dt>

*pTagName* \[in\]
</dt> <dd>

A pointer to the **Tag** of the requested string.

</dd> <dt>

*pString* \[in\]
</dt> <dd>

A pointer to the variable where a pointer to the string will be returned.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that indicates the problem.

If the specified **Owner**, **Category**, or **Tag** information does not exist, the return value is NMERR\_BLOB\_ENTRY\_DOES\_NOT\_EXIST.

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

[GetStringFromBlob](getstringfromblob.md)
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

[SetNPPPatternFilterInBlob](setnpppatternfilterinblob.md)
</dt> <dt>

[SetNPPTriggerInBlob](setnpptriggerinblob.md)
</dt> </dl>

 

 




