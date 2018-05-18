---
Description: 'Represents an optional companion for a server component.'
audience: developer
ms.assetid: '1f5ad17f-fa0e-42f9-b451-6269f728da29'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: 'MSFT\_OptionalCompanion class'
---

# MSFT\_OptionalCompanion class

Represents an optional companion for a server component.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("deploymentprovider")]
class MSFT_OptionalCompanion
{
  string  CompanionComponentName;
  uint8   CompanionType;
  Boolean PrerequisiteEnabled;
};
```

## Members

The **MSFT\_OptionalCompanion** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_OptionalCompanion** class has these properties.

<dl> <dt>

**CompanionComponentName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the component.

</dd> <dt>

**CompanionType**
</dt> <dd> <dl> <dt>

Data type: **uint8**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the type of the companion.

This property contains the following value:

<dt>

<span id="RSAT"></span><span id="rsat"></span>

**RSAT** (0)


</dt> <dd></dd> </dl>

</dd> <dt>

**PrerequisiteEnabled**
</dt> <dd> <dl> <dt>

Data type: **Boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Indicates whether the prerequisites for the companion are enabled. True if the prerequisites are enabled; otherwise false.

</dd> </dl>

## Requirements



|                                     |                                                                                                                 |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                                       |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                  |
| Namespace<br/>                | Root\\StandardCimv2<br/>                                                                                  |
| MOF<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ServerManager.DeploymentProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[ServerManager Deploymentprovider Provider Classes](server-manager-deployment.md)
</dt> </dl>

 

 




