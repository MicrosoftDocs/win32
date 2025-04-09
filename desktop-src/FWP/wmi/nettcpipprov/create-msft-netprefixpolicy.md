---
description: Creates a prefix policy.
ms.assetid: a6205f16-a30b-43ee-9587-e7d721f04e44
title: Create method of the MSFT\_NetPrefixPolicy class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- kbSyntax
api_name: 
api_type: 
api_location: 
---

# Create method of the MSFT\_NetPrefixPolicy class

Creates a prefix policy.

## Syntax


```mof
uint32 Create(
  [in]  string               Prefix,
  [in]  uint32               Precedence,
  [in]  uint32               Label,
  [in]  string               PolicyStore,
  [in]  boolean              PassThru,
  [out] MSFT_NetPrefixPolicy CmdletOutput[]
);
```



## Parameters

<dl> <dt>

*Prefix* \[in\]
</dt> <dd>

Specifies the prefix of the policy.

</dd> <dt>

*Precedence* \[in\]
</dt> <dd>

Specifies the precedence value in the policy table, which is used for sorting destination addresses.

</dd> <dt>

*Label* \[in\]
</dt> <dd>

Specifies a label value that allows for policies that prefer a particular source address prefix for use with a destination address prefix.

</dd> <dt>

*PolicyStore* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*PassThru* \[in\]
</dt> <dd>

Specifies whether the method should output an object that represents the newly created prefix policy in the *CmdletOutput* parameter.

</dd> <dt>

*CmdletOutput* \[out\]
</dt> <dd>

Receives a [**MSFT\_NetPrefixPolicy**](msft-netprefixpolicy.md) object that represents the new prefix policy.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                          |
| MOF<br/>                      | <dl> <dt>NetTCPIP.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetTCPIP.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_NetPrefixPolicy**](msft-netprefixpolicy.md)
</dt> </dl>

 

 




