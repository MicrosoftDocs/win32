---
description: Represents a team in the IM Platform.
ms.assetid: 1740eadb-e00b-4526-be64-a6395aaf2bcd
title: MSFT\_NetImPlatTeam class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetImPlatTeam
- MSFT_NetImPlatTeam.InstanceID
- MSFT_NetImPlatTeam.Name
api_type: 
- DllExport
api_location: 
- NdisIMPlatCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetImPlatTeam class

Represents a team in the IM Platform.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Abstract, ClassVersion("10")]
class MSFT_NetImPlatTeam : CIM_ManagedElement
{
  string InstanceID;
  string Name;
};
```

## Members

The **MSFT\_NetImPlatTeam** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetImPlatTeam** class has these properties.

<dl> <dt>

**InstanceID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**, **Override**
</dt> </dl>

The team GUID associated with this team.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the team.

</dd> </dl>

## Requirements



|                                     |                                                                                                |
|-------------------------------------|------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                 |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                 |
| MOF<br/>                      | <dl> <dt>MsNetImPlatform.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NdisIMPlatCim.dll</dt> </dl>   |



 

 




