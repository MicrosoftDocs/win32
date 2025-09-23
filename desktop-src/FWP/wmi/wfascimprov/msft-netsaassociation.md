---
description: A MainMode SA.
ms.assetid: 064fcd6b-3bf9-4a41-bd01-221aa5a15772
title: MSFT\_NetSAAssociation class


ms.author: windowssdkdev
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- MSFT_NetSAAssociation
- MSFT_NetSAAssociation.Antecedent
- MSFT_NetSAAssociation.Dependent
api_type: 
- DllExport
api_location: 
- WFasCim.dll
ROBOTS: INDEX,FOLLOW
---

# MSFT\_NetSAAssociation class

A MainMode SA.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
class MSFT_NetSAAssociation : CIM_Phase1SAUsedForPhase2
{
  CIM_SecurityAssociationEndpoint REF Antecedent;
  CIM_IPsecSAEndpoint             REF Dependent;
};
```

## Members

The **MSFT\_NetSAAssociation** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_NetSAAssociation** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_SecurityAssociationEndpoint**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_IPsecSAEndpoint**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Reserved for internal use by the WMI provider only.

</dd> </dl>

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                         |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                         |
| MOF<br/>                      | <dl> <dt>WFasCim.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WFasCim.dll</dt> </dl> |



 

 




