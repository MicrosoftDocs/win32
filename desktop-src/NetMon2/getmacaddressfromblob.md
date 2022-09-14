---
description: The GetMacAddressFromBlob function retrieves the named MAC address from a BLOB.
ms.assetid: 1769c92c-0946-447c-885a-fcf175fa1bf3
title: GetMacAddressFromBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetMacAddressFromBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# GetMacAddressFromBlob function

The **GetMacAddressFromBlob** function retrieves the named MAC address from a BLOB.

## Syntax


```C++
DWORD GetMacAddressFromBlob(
  _In_        HBLOB hBlob,
  _In_  const char  *pOwnerName,
  _In_  const char  *pCategoryName,
  _In_  const char  *pTagName,
  _Out_       BYTE  *pMacAddress
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

*pMacAddress* \[out\]
</dt> <dd>

Pointer to the MAC address of the BLOB.

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

[SetMacAddressInBlob](setmacaddressinblob.md)
</dt> <dt>

[GetBoolFromBlob](getboolfromblob.md)
</dt> <dt>

[GetClassIDFromBlob](getclassidfromblob.md)
</dt> <dt>

[GetDwordFromBlob](getdwordfromblob.md)
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

 

 




