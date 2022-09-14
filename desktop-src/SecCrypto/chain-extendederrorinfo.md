---
description: Returns a string that contains additional error information about the indexed entry.
ms.assetid: 4f0d5289-c414-4e2b-b612-be8ce1d98b12
title: IChain2::ExtendedErrorInfo method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Chain.ExtendedErrorInfo
- IChain2.ExtendedErrorInfo
api_type:
- COM
api_location:
- Capicom.dll
---

# IChain2::ExtendedErrorInfo method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Chain Class**](/dotnet/api/system.security.cryptography.x509certificates.x509chain) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor) namespace.\]

The **ExtendedErrorInfo** method returns a string that contains additional error information about the indexed entry.

This method is introduced in CAPICOM 2.0.

## Syntax


```VB
Chain.ExtendedErrorInfo( _
  [ ByVal Index ] _
)
```



## Parameters

<dl> <dt>

*Index* \[in, optional\]
</dt> <dd>

A **Long** representing the index of the entry. The default value is 1, which returns error information for the end certificate in the chain. **Certificates.Count** returns information about the root certificate of the chain. 0 returns extended error information for the entire chain.

</dd> </dl>

## Return value

A string that contains the extended error information.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Chain**](chain.md)
</dt> </dl>

 

 
