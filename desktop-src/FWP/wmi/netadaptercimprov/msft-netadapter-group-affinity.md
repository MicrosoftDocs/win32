---
description: This class represents a processor affinity mask.
ms.assetid: 81ceffaf-8491-4249-be33-50b7385988a9
title: MSFT\_NetAdapter\_Group\_Affinity class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetAdapter_Group_Affinity
- MSFT_NetAdapter_Group_Affinity.ProcessorAffinityMask
- MSFT_NetAdapter_Group_Affinity.ProcessorGroup
api_type: 
- DllExport
api_location: 
- NetAdapterCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetAdapter\_Group\_Affinity class

This class represents a processor affinity mask.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Dynamic, Provider("NetAdapterCim")]
class MSFT_NetAdapter_Group_Affinity
{
  uint64 ProcessorAffinityMask;
  uint16 ProcessorGroup;
};
```

## Members

The **MSFT\_NetAdapter\_Group\_Affinity** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetAdapter\_Group\_Affinity** class has these properties.

<dl> <dt>

**ProcessorAffinityMask**
</dt> <dd> <dl> <dt>

Data type: **uint64**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The bitmask for a set of logical processors in a group.

</dd> <dt>

**ProcessorGroup**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The group number for a set of logical processors.

</dd> </dl>

## Requirements



|                                     |                                                                                              |
|-------------------------------------|----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                               |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                               |
| MOF<br/>                      | <dl> <dt>NetAdapterCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NetAdapterCim.dll</dt> </dl> |



 

 




