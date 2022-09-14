---
description: The GetNetworkInfoFromBlob function retrieves network information from a given BLOB.
ms.assetid: 217c33f4-e548-4072-9edd-ded61e6cd743
title: GetNetworkInfoFromBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- GetNetworkInfoFromBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# GetNetworkInfoFromBlob function

The **GetNetworkInfoFromBlob** function retrieves network information from a given BLOB.

## Syntax


```C++
DWORD GetNetworkInfoFromBlob(
  _In_    HBLOB         hBlob,
  _Inout_ LPNETWORKINFO lpNetworkInfo
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to a BLOB.

</dd> <dt>

*lpNetworkInfo* \[in, out\]
</dt> <dd>

A pointer to the user-allocated [NETWORKINFO](networkinfo.md) structure that is filled in.

</dd> </dl>

## Return value

If the **GetNetworkInfoFromBlob** function is successful, the return value is NMERR\_SUCCESS.

If the function is unsuccessful, the return value is a NMERR value that describes the error.

## Remarks

The network information is stored in the BLOB **NetworkInfo** section of the BLOB NPP **Owner** category.

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

[SetNetworkInfoInBlob](setnetworkinfoinblob.md)
</dt> <dt>

[GetBoolFromBlob](getboolfromblob.md)
</dt> <dt>

[GetClassIDFromBlob](getclassidfromblob.md)
</dt> <dt>

[GetDwordFromBlob](getdwordfromblob.md)
</dt> <dt>

[GetMacAddressFromBlob](getmacaddressfromblob.md)
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

 

 




