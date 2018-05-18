---
Description: 'This section provides reference information for the Physical Computer System View Provider.'
audience: developer
author: 'REDMOND\\markl'
manager: 'REDMOND\\markl'
ms.assetid: 'a4cabe88-2319-469c-9024-5772c8a90bfa'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
title: Physical Computer System View Provider
---

# Physical Computer System View Provider

This section provides reference information for the Physical Computer System View Provider.

## In this section

<dl> <dt>

[**CIM\_ConcreteJob**](cim-concretejob.md)
</dt> <dd>

A concrete version of Job. This class represents a generic and instantiable unit of work, such as a batch or a print job.

</dd> <dt>

[**CIM\_Error**](cim-error.md)
</dt> <dd>

CIM\_Error is a specialized class that contains information about the severity, cause, recommended actions and other data related to the failure of a CIM Operation. Instances of this type MAY be included as part of the response to a CIM Operation.

</dd> <dt>

[**CIM\_Job**](cim-job.md)
</dt> <dd>

A Job is a LogicalElement that represents an executing unit of work, such as a script or a print job. A Job is distinct from a Process in that a Job can be scheduled or queued, and its execution is not limited to a single system.

</dd> <dt>

[**CIM\_RecordForLog**](cim-recordforlog.md)
</dt> <dd>

The RecordForLog class is used to instantiate records to be aggregated to a Log.

</dd> <dt>

[**CIM\_LogicalElement**](cim-logicalelement.md)
</dt> <dd>

CIM\_LogicalElement is a base class for all the components of a System that represent abstract system components, such as Files, Processes, or LogicalDevices.

</dd> <dt>

[**CIM\_LogRecord**](cim-logrecord.md)
</dt> <dd>

The LogRecord object can describe the definitional format for entries in a MessageLog, or can be used to instantiate the actual records in the Log. The latter approach provides a great deal more semantic definition and management control over the individual entries in a MessageLog, than do the record manipulation methods of the Log class. It is recommended that the data in individual Log entries be modeled using subclasses of LogRecord, to avoid the creation of LogRecords with one property (such as RecordData) without semantics. Definitional formats for LogRecords could be specified by establishing a naming convention for the RecordID and Message Timestamp key properties.

</dd> <dt>

[**CIM\_ManagedSystemElement**](cim-managedsystemelement.md)
</dt> <dd>

CIM\_ManagedSystemElement is the base class for the System Element hierarchy. Any distinguishable component of a System is a candidate for inclusion in this class. Examples of system components include: - software components such as application servers, databases, and applications - operating system components such as files, processes, and threads - device components such as disk drives, controllers, processors, and printers - physical components such as chips and cards.

</dd> <dt>

[**CIM\_ManagedElement**](cim-managedelement.md)
</dt> <dd>

ManagedElement is an abstract class that provides a common superclass (or top of the inheritance tree) for the non-association classes in the CIM Schema.

</dd> <dt>

[**CIM\_RecordForLog**](cim-recordforlog.md)
</dt> <dd>

The RecordForLog class is used to instantiate records to be aggregated to a Log.

</dd> <dt>

[**CIM\_View**](cim-view.md)
</dt> <dd>

View is an abstract class that provides a common superclass for classes providing de-normalized, aggregate representations of managed resources. The definition of each sub-class will include properties propagated from the graph of classes that are used to model the resource in the normalized view. The classes may be resource classes or associations. The definition of how a value is propagated (i.e. source class and value transformations) is required to be specified. Sub-classes may be explicitly constrained to be read only. If a sub-class is not constrained as read only, the designers are strongly encouraged to carefully consider the data synchronization and consistencies issues that may result. The ElementView association may be used to find the instances that form the normalized view of the managed resource.

</dd> <dt>

[**CIM\_PhysicalComputerSystemView**](cim-physicalcomputersystemview.md)
</dt> <dd>

This class defines a view class for a physical computer system.

</dd> <dt>

[**MSFT\_PCSVDevice**](msft-pcsvdevice.md)
</dt> <dd>

Defines a view class for a physical computer system.

</dd> <dt>

[**MSFT\_PCSVLogRecord**](msft-pcsvlogrecord.md)
</dt> <dd>

The LogRecord object can describe the definitional format for entries in a MessageLog, or can be used to instantiate the actual records in the Log. The latter approach provides a great deal more semantic definition and management control over the individual entries in a MessageLog, than do the record manipulation methods of the Log class. It is recommended that the data in individual Log entries be modeled using subclasses of LogRecord, to avoid the creation of LogRecords with one property (such as RecordData) without semantics. Definitional formats for LogRecords could be specified by establishing a naming convention for the RecordID and Message Timestamp key properties.

</dd> </dl>

 

 



