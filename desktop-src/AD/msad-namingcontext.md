---
title: MSAD_NamingContext class
description: Represents a particular naming context (NC) on the domain controller.
ms.assetid: 67dd6c68-6c67-40b4-a20a-c6c312d23441
ms.tgt_platform: multiple
keywords:
- MSAD_NamingContext class Active Directory
- MSAD_NamingContext class Active Directory , described
topic_type:
- apiref
api_name:
- MSAD_NamingContext
- MSAD_NamingContext.DistinguishedName
- MSAD_NamingContext.IsFullReplica
api_location:
- replprov.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# MSAD\_NamingContext class

Represents a particular naming context (NC) on the domain controller.

## Syntax

``` syntax
[dynamic, provider("ReplProv1")]
class MSAD_NamingContext
{
  String  DistinguishedName;
  boolean IsFullReplica = FALSE;
};
```

## Members

The **MSAD\_NamingContext** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSAD\_NamingContext** class has these properties.

<dl> <dt>

**DistinguishedName**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier)
</dt> </dl>

Gets the X.500 path of the NC.

</dd> <dt>

**IsFullReplica**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the value that indicates whether the NC is read/write. **TRUE** if the NC is read/write; **FALSE** if the NC is read-only.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftActiveDirectory<br/>                                               |
| MOF<br/>                      | <dl> <dt>Replprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Replprov.dll</dt> </dl> |



 

