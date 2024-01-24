---
description: Adds data to a specified hash object.
ms.assetid: 8E32BBC4-C2DD-4174-9FF1-9001E4A7D87B
title: A_SHAUpdate function (Sha.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- A_SHAUpdate
api_type: 
- DllExport
api_location: 
- ntdll.dll
---

# A\_SHAUpdate function

Adds data to a specified hash object.

## Syntax


```C++
void RSA32API A_SHAUpdate(
  _Inout_ A_SHA_CTX     *Context,
  _In_    UNSIGNED CHAR *Buffer,
          UNSIGNED INT  BufferSize
);
```



## Parameters

<dl> <dt>

*Context* \[in, out\]
</dt> <dd>

The SHA context.

</dd> <dt>

*Buffer* \[in\]
</dt> <dd>

A pointer to a buffer that contains the data to be added to the hash object.

</dd> <dt>

*BufferSize* 
</dt> <dd>

The size of the buffer.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function can be called multiple times to compute the hash on long data streams or discontinuous data streams. The [**A\_SHAFinal**](a-shafinal.md) function must be called before retrieving the hash value.

This function is very similar to SHAUpdate, but is called directly from the library, rather than being routed through the cryptography infrastructure. For more information, see [Windows NTCryptographic Providers](/previous-versions/tn-archive/cc723484(v=technet.10)).

## Requirements



| Requirement | Value |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Sha.h</dt> </dl>     |
| Library<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |
| DLL<br/>     | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 
