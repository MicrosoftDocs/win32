---
description: The SetClassIDInBlob function sets the named class identifier value of a BLOB.
ms.assetid: d17dd48b-2e35-4c57-ba33-688180910b63
title: SetClassIDInBlob function (Netmon.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SetClassIDInBlob
api_type: 
- DllExport
api_location: 
- Npptools.dll
---

# SetClassIDInBlob function

The **SetClassIDInBlob** function sets the named class identifier value of a BLOB.

## Syntax


```C++
DWORD SetClassIDInBlob(
  _In_       HBLOB hBlob,
  _In_ const char  *pOwnerName,
  _In_ const char  *pCategoryName,
  _In_ const char  *pTagName,
  _In_ const CLSID *pClsID
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

Pointer to the BLOB **Owner** name that is set.

</dd> <dt>

*pCategoryName* \[in\]
</dt> <dd>

Pointer to the BLOB **Category** name that is set.

</dd> <dt>

*pTagName* \[in\]
</dt> <dd>

Pointer to the BLOB **Tag** name that is set.

</dd> <dt>

*pClsID* \[in\]
</dt> <dd>

Pointer to the class identifier of the BLOB that is set.

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

[GetClassIDFromBlob](getclassidfromblob.md)
</dt> <dt>

[SetBoolInBlob](setboolinblob.md)
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

 

 




