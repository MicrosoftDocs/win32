---
title: Shielded VM Provisioning Service WMI Provider
description: Shielded VM Provisioning Service WMI Provider enables developers to start the provisioning process for a shielded virtual machine.In this sectionCIM\_ConcreteJobA concrete version of Job.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 704e38f1-ef69-467f-879f-9a75785946be
ms.prod: windows-server-dev
ms.technology:
- shielded-vm-provisioning
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Shielded VM Provisioning Service WMI Provider

## Purpose

Shielded VM Provisioning Service WMI Provider enables developers to start the provisioning process for a shielded virtual machine.

## In this section

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> <dd>

A concrete version of Job. This class represents a generic and instantiable unit of work, such as a batch or a print job.

</dd> <dt>

[**CIM\_Error**](cim-error.md)
</dt> <dd>

A specialized class that contains information about the severity, cause, recommended actions and other data related to the failure of a CIM Operation. Instances of this type MAY be included as part of the response to a CIM Operation.

</dd> <dt>

[**CIM\_Job**](cim-job.md)
</dt> <dd>

A Job is a LogicalElement that represents an executing unit of work, such as a script or a print job. A Job is distinct from a Process in that a Job can be scheduled or queued, and its execution is not limited to a single system.

</dd> <dt>

[**CIM\_LogicalElement**](cim-logicalelement.md)
</dt> <dd>

A base class for all the components of a System that represent abstract system components, such as Files, Processes, or Logical Devices.

</dd> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dd>

An abstract class that provides a common superclass (or top of the inheritance tree) for the non-association classes in the CIM Schema.

</dd> <dt>

[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)
</dt> <dd>

CIM\_ManagedSystemElement is the base class for the System Element hierarchy. Any distinguishable component of a System is a candidate for inclusion in this class. Examples of system components include:

</dd> <dt>

[**Msps\_ProvisioningJob**](msps-provisioningjob.md)
</dt> <dd>

Represents an active provisioning job for a specific machine. The class provides access to job status, errors, and the fabric policy associated with the machine.

</dd> <dt>

[**Msps\_ProvisioningService**](msps-provisioningservice.md)
</dt> <dd>

Represents the Shielded VM Provisioning Service.

</dd> </dl>

## Developer audience

The primary audience of the Shielded VM Provisioning Service WMI Provider are developers who need a standard way for a Fabric Controller to begin provisioning a shielded virtual machine (VSM). The provider also exposes a standard process for other components in the provisioning work flow to obtain secrets from the VSM. This is so multiple components do not have to interact with the VSM, or that multiple components do not have to change when the VSM changes.

 

 




