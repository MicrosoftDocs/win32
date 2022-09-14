---
description: The GetClassIDFromBlob function retrieves a named class identifier value from a BLOB.
ms.assetid: fef29a42-ccd3-4655-958c-d150e5bcd0d7
title: GetClassIDFromBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetClassIDFromBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# GetClassIDFromBlob function

The **GetClassIDFromBlob** function retrieves a named class identifier value from a BLOB.

## Syntax


```C++
DWORD GetClassIDFromBlob(
  _In_        HBLOB hBlob,
  _In_  const char  *pOwnerName,
  _In_  const char  *pCategoryName,
  _In_  const char  *pTagName,
  _Out_       CLSID *pClsID
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

Pointer to the BLOB owner name.

</dd> <dt>

*pCategoryName* \[in\]
</dt> <dd>

Pointer to the BLOB category name.

</dd> <dt>

*pTagName* \[in\]
</dt> <dd>

Pointer to the BLOB tag name.

</dd> <dt>

*pClsID* \[out\]
</dt> <dd>

Pointer to the BLOB class identifier.

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

[SetClassIDInBlob](setclassidinblob.md)
</dt> <dt>

[GetBoolFromBlob](getboolfromblob.md)
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

 

 




