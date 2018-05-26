---
Description: Initiates the hashing of a stream of data.
ms.assetid: 0EA7C98E-777C-4B2A-AF35-04F90BA3D024
title: A\_SHAInit function
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# A\_SHAInit function

Initiates the hashing of a stream of data.

## Syntax


```C++
void RSA32API A_SHAInit(
  _Inout_ A_SHA_CTX *Context
);
```



## Parameters

<dl> <dt>

*Context* \[in, out\]
</dt> <dd>

The SHA context.

</dd> </dl>

## Return value

This function does not return a value.

## Remarks

This function is very similar to SHAInit, but is called directly from the library, rather than being routed through the cryptography infrastructure. For more information, see [Windows NTCryptographic Providers](https://msdn.microsoft.com/en-us/library/cc723484.aspx).

## Requirements



|                    |                                                                                      |
|--------------------|--------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>Sha.h</dt> </dl>     |
| Library<br/> | <dl> <dt>Ntdll.dll</dt> </dl> |
| DLL<br/>     | <dl> <dt>Ntdll.dll</dt> </dl> |



 

 




