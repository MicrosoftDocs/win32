---
description: Retrieves a specified number of random bytes from the system random number generator.
ms.assetid: 04746229-9dc1-4748-80c1-f1960bd1b768
title: SystemPrng function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- SystemPrng
api_type: 
- DllExport
api_location: 
- Ksecdd.sys
- Cng.sys
---

# SystemPrng function

\[**SystemPrng** is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions. Instead, use [**BCryptGenRandom**](/windows/desktop/api/Bcrypt/nf-bcrypt-bcryptgenrandom).\]

The **SystemPrng** function retrieves a specified number of random bytes from the system random number generator.

> [!Note]  
> This function has no associated header file or import library. To call this function, you must create a user-defined header file.

 

## Syntax


```C++
BOOL SystemPrng(
  _Out_ unsigned char pbRandomData,
  _In_  size_t        cbRandomData
);
```



## Parameters

<dl> <dt>

*pbRandomData* \[out\]
</dt> <dd>

A pointer to a buffer that receives the retrieved bytes.

</dd> <dt>

*cbRandomData* \[in\]
</dt> <dd>

The number of bytes to retrieve.

</dd> </dl>

## Return value

Always returns **TRUE**.

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1 \[desktop apps only\]<br/>                                                                                                                                                                                        |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                                                                                                                                                                           |
| DLL<br/>                      | <dl> <dt>Ksecdd.sys on Windows Server 2008 and Windows Vista with SP1; </dt> <dt>Cng.sys on Windows 7 and Windows Server 2008 R2</dt> </dl> |



 

 




