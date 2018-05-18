---
title: CIM\_ServiceServiceDependency class
description: CIM\_ServiceServiceDependency is an association between a service and another service, indicating that the latter is required to be present, required to have completed, or must be absent for the former service to provide its functionality.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '21e87d85-fc3c-4655-a986-0663e80f202c'
ms.prod: 'windows-server-dev'
ms.technology:
- 'network-load-balancing'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CIM_ServiceServiceDependency class", "CIM_ServiceServiceDependency class, described"]
topic_type:
- apiref
api_name:
- CIM_ServiceServiceDependency
- CIM_ServiceServiceDependency.Antecedent
- CIM_ServiceServiceDependency.Dependent
- CIM_ServiceServiceDependency.TypeOfDependency
api_location:
- WlbsProv.dll
api_type:
- DllExport
---

# CIM\_ServiceServiceDependency class

**CIM\_ServiceServiceDependency** is an association between a service and another service, indicating that the latter is required to be present, required to have completed, or must be absent for the former service to provide its functionality. For example, boot services may be dependent upon underlying BIOS Disk and initialization services. In the case of the initialization services, the boot service is simply dependent on the init services completing. For the disk services, boot services may actually utilize the SAPs of this service.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Association, AMENDMENT]
class CIM_ServiceServiceDependency : CIM_Dependency
{
  CIM_Service REF Antecedent;
  CIM_Service REF Dependent;
  uint16          TypeOfDependency;
};
```

## Members

The **CIM\_ServiceServiceDependency** class has these types of members:

-   [Properties](#properties)

### Properties

The **CIM\_ServiceServiceDependency** class has these properties.

<dl> <dt>

**Antecedent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Antecedent")
</dt> </dl>

The required service.

</dd> <dt>

**Dependent**
</dt> <dd> <dl> <dt>

Data type: **CIM\_Service**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Override**](https://msdn.microsoft.com/library/aa393650) ("Dependent")
</dt> </dl>

The service that is dependent on an underlying service.

</dd> <dt>

**TypeOfDependency**
</dt> <dd> <dl> <dt>

Data type: **uint16**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The nature of the service to service dependency. This property describes that the associated service must have completed (value=2), must be started (3) or must not be started (4) in order for the service to function.

<dt>

<span id="Unknown"></span><span id="unknown"></span><span id="UNKNOWN"></span>

**Unknown** (0)


</dt> <dd></dd> <dt>

<span id="Other"></span><span id="other"></span><span id="OTHER"></span>

**Other** (1)


</dt> <dd></dd> <dt>

<span id="Service_Must_Have_Completed"></span><span id="service_must_have_completed"></span><span id="SERVICE_MUST_HAVE_COMPLETED"></span>

**Service Must Have Completed** (2)


</dt> <dd></dd> <dt>

<span id="Service_Must_Be_Started"></span><span id="service_must_be_started"></span><span id="SERVICE_MUST_BE_STARTED"></span>

**Service Must Be Started** (3)


</dt> <dd></dd> <dt>

<span id="Service_Must_Not_Be_Started"></span><span id="service_must_not_be_started"></span><span id="SERVICE_MUST_NOT_BE_STARTED"></span>

**Service Must Not Be Started** (4)


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Namespace<br/>                | Root\\MicrosoftNLB<br/>                                                           |
| MOF<br/>                      | <dl> <dt>WlbsProv.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WlbsProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**CIM\_Dependency**](cim-dependency.md)
</dt> </dl>

 

 





