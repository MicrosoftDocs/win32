---
description: The SetMacAddressInBlob function sets the requested MAC address of a BLOB.
ms.assetid: f44d0cec-ced7-4d2a-a58e-aeb476bfe800
title: SetMacAddressInBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetMacAddressInBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# SetMacAddressInBlob function

The **SetMacAddressInBlob** function sets the requested MAC address of a BLOB.

## Syntax


```C++
DWORD SetMacAddressInBlob(
  _In_       HBLOB hBlob,
  _In_ const char  *pOwnerName,
  _In_ const char  *pCategoryName,
  _In_ const char  *pTagName,
  _In_ const BYTE  *pMacAddress
);
```



## Parameters

<dl> <dt>

*hBlob* \[in\]
</dt> <dd>

Handle to the BLOB being set.

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

*pMacAddress* \[in\]
</dt> <dd>

Pointer to the MAC address of the BLOB being set.

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

[GetMacAddressFromBlob](getmacaddressfromblob.md)
</dt> <dt>

[SetBoolInBlob](setboolinblob.md)
</dt> <dt>

[SetClassIDInBlob](setclassidinblob.md)
</dt> <dt>

[SetDwordInBlob](setdwordinblob.md)
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

 

 




