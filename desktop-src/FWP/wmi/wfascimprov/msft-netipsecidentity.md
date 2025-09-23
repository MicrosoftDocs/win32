---
description: An identity used by IPsec.
ms.assetid: 64ba4a6f-abc8-4cc7-912d-730f80b8c7b4
title: MSFT\_NetIPsecIdentity class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetIPsecIdentity
- MSFT_NetIPsecIdentity.ImpersonationType
- MSFT_NetIPsecIdentity.AuthenticationMethod
- MSFT_NetIPsecIdentity.Flags
- MSFT_NetIPsecIdentity.Identity
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetIPsecIdentity class

An identity used by IPsec

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetIPsecIdentity
{
  uint32 ImpersonationType;
  uint32 AuthenticationMethod;
  uint32 Flags;
  string Identity;
};
```

## Members

The **MSFT\_NetIPsecIdentity** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetIPsecIdentity** class has these properties.

<dl> <dt>

**AuthenticationMethod**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Authentication method used by this identity

</dd> <dt>

**Flags**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identity flags

</dd> <dt>

**Identity**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Identity

</dd> <dt>

**ImpersonationType**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

ImpersonationType

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




