---
title: CIM\_ElementCapabilities class
description: Represents an association between a managed element and its capabilities.
ms.assetid: 'edbb2f6a-467b-4689-b2dc-e5f90a8b5f48'
keywords: ["CIM_ElementCapabilities class Hyper-V", "CIM_ElementCapabilities class Hyper-V , described"]
topic_type:
- apiref
api_name:
- CIM_ElementCapabilities
- CIM_ElementCapabilities.ManagedElement
- CIM_ElementCapabilities.Capabilities
api_location:
- Root\virtualization
api_type:
- Schema
---

# CIM\_ElementCapabilities class

Represents an association between a managed element and its capabilities.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, Association, Version("2.12.0"), AMENDMENT]
class CIM_ElementCapabilities
{
  CIM_ManagedElement REF ManagedElement;
  CIM_Capabilities   REF Capabilities;
};
```

## Members

The **CIM\_ElementCapabilities** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ElementCapabilities** class has these properties.

<dl> <dt>

**Capabilities**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_Capabilities**](cim-capabilities.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157)
</dt> </dl>

The capabilities associated with the managed element.

</dd> <dt>

**ManagedElement**
</dt> <dd> <dl> <dt>

Data type: **[**CIM\_ManagedElement**](cim-managedelement.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa392157), [**Min**](https://msdn.microsoft.com/library/aa393650) (1)
</dt> </dl>

The managed element.

</dd> </dl>

## Requirements



|                                     |                                                                                                      |
|-------------------------------------|------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                       |
| End of client support<br/>    | None supported<br/>                                                                            |
| End of server support<br/>    | Windows Server 2012 R2<br/>                                                                    |
| Namespace<br/>                | Root\\virtualization<br/>                                                                      |
| MOF<br/>                      | <dl> <dt>WindowsVirtualization.mof</dt> </dl> |



 

 





