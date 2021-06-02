---
description: Creates a hash of the specified string.
ms.assetid: 8d3e16e7-7b93-410c-b771-7684d1bf2160
title: HashedData.Hash method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- HashedData.Hash
api_type:
- COM
api_location:
- Capicom.dll
---

# HashedData.Hash method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**HashAlgorithm Class**](/previous-versions/windows/) in the [**System.Security.Cryptography**](/dotnet/api/system.security.cryptography?view=dotnet-plat-ext-3.1&preserve-view=true) namespace.\]

The **Hash** method creates a hash of the specified string.

## Syntax


```VB
HashedData.Hash( _
  ByVal newVal _
)
```



## Parameters

<dl> <dt>

*newVal* 
</dt> <dd>

String that contains the value to hash.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

To create the hash of a large amount of data, call the **Hash** method for each piece of data. The hash of each piece of data is concatenated to the [**Value**](hasheddata-value.md) property until the property is read. The contents of the **Value** property are reset when the property is read.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
