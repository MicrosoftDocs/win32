---
description: Retrieves a named Boolean value from a BLOB.
ms.assetid: 26acfd2a-5b17-47ad-8f7b-7793174a13c3
title: GetBoolFromBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetBoolFromBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# GetBoolFromBlob function

The **GetBoolFromBlob** function retrieves a named Boolean value from a BLOB.

## Syntax


```C++
DWORD GetBoolFromBlob(
  _In_        HBLOB hBlob,
  _In_  const char  *pOwnerName,
  _In_  const char  *pCategoryName,
  _In_  const char  *pTagName,
  _Out_       BOOL  *pBool
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

A handle to a BLOB.

</dd> <dt>

*pOwnerName* \[in\]
</dt> <dd>

A pointer to the BLOB owner name.

</dd> <dt>

*pCategoryName* \[in\]
</dt> <dd>

A pointer to the BLOB category name.

</dd> <dt>

*pTagName* \[in\]
</dt> <dd>

A pointer to the BLOB tag name.

</dd> <dt>

*pBool* \[out\]
</dt> <dd>

Pointer to the Boolean value of the BLOB.

</dd> </dl>

## Return value

If the function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that describes the error.

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

[SetBoolInBlob](setboolinblob.md)
</dt> <dt>

[GetClassIDFromBlob](getclassidfromblob.md)
</dt> <dt>

[GetDwordFromBlob](getdwordfromblob.md)
</dt> <dt>

[GetMacAddressFromBlob](getmacaddressfromblob.md)
</dt> <dt>

[GetNetworkInfoFromBlob](getnetworkinfofromblob.md)
</dt> <dt>

[GetNPPAddressFilterFromBlob](getnppaddressfilterfromblob.md)
</dt> <dt>

[GetNPPPatternFilterFromBlob](getnpppatternfilterfromblob.md)
</dt> <dt>

[GetNPPTriggerFromBlob](getnpptriggerfromblob.md)
</dt> <dt>

[GetStringFromBlob](getstringfromblob.md)
</dt> <dt>

[GetStringsFromBlob](getstringsfromblob.md)
</dt> </dl>

 

 




