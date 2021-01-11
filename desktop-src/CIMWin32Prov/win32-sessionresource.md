---
description: The Win32\_SessionResource association represents the relationship between a session and the resources that the session provides access to.
ms.assetid: 39c195cf-e70b-4e93-b46b-61ed4f08f57e
ms.tgt_platform: multiple
title: Win32_SessionResource class
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Win32_SessionResource
- Win32_SessionResource.Antecedent
- Win32_SessionResource.Dependent
api_type: 
- DllExport
api_location: 
- cimwin32.dll
---

# Win32\_SessionResource class

The Win32\_SessionResource association represents the relationship between a session and the resources that the session provides access to.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, AMENDMENT]
class Win32_SessionResource : CIM_Dependency
{
  Win32_LogicalElement REF Antecedent;
  Win32_Session        REF Dependent;
};
```

## Members

The **Win32\_SessionResource** class has these types of members:

-   [Properties](#properties)

### Properties

The **Win32\_SessionResource** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_LogicalElement**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Antecedent")
</dt> </dl>

The Antecedent reference represents resources used by this session.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **Win32\_Session**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](../wmisdk/standard-qualifiers.md) ("Dependent")
</dt> </dl>

The Dependent reference represents the session using the resource.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\CIMV2<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>CimWin32.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Cimwin32.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 
