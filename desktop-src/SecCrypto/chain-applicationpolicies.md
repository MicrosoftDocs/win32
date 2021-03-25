---
description: Returns an OIDs collection that represents the application policy OIDs valid for the chain.
ms.assetid: 4e4a7dce-5004-4b80-b132-3cdc0c048cde
title: IChain2::ApplicationPolicies method
ms.topic: reference
ms.date: 05/31/2018
topic_type:
- APIRef
- kbSyntax
api_name:
- Chain.ApplicationPolicies
- IChain2.ApplicationPolicies
api_type:
- COM
api_location:
- Capicom.dll
---

# IChain2::ApplicationPolicies method

\[CAPICOM is a 32-bit only component that is available for use in the following operating systems: Windows Server 2008, Windows Vista, and Windows XP. Instead, use the [**X509Chain Class**](/dotnet/api/system.security.cryptography.x509certificates.x509chain?view=netcore-3.1) in the [**System.Security.Cryptography.X509Certificates**](/dotnet/api/system.security.cryptography.x509certificates.publickey.-ctor?view=netcore-3.1) namespace.\]

The **ApplicationPolicies** method returns an [**OIDs**](oids.md) collection that represents the application policy OIDs valid for the chain.

This method is introduced in CAPICOM 2.0.

## Syntax


```VB
Chain.ApplicationPolicies()
```



## Parameters

This method has no parameters.

## Requirements



| Requirement | Value |
|----------------------------------|----------------------------------------------------------------------------------------|
| End of client support<br/> | Windows Vista<br/>                                                               |
| End of server support<br/> | Windows Server 2008<br/>                                                         |
| Redistributable<br/>       | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>                   | <dl> <dt>Capicom.dll</dt> </dl> |



 

 
