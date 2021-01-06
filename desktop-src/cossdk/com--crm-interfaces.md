---
description: The CRM interfaces are required to provide support for CRM Workers and CRM Compensators developed using Visual Basic and Visual C++.
ms.assetid: 68a75da7-1f35-41a4-8872-e3f4ad1fc30d
title: COM+ CRM Interfaces
ms.topic: article
ms.date: 05/31/2018
---

# COM+ CRM Interfaces

The CRM interfaces are required to provide support for CRM Workers and CRM Compensators developed using Visual Basic and Visual C++.

You can use the COM+ Compensating Resource Manager (CRM) to quickly and easily integrate application resources with Microsoft Distributed Transaction Coordinator (DTC) transactions.

It is easier for components written with Visual Basic to build up a log record as a collection of Variants. Also, Visual Basic components are apartment threaded, which implies that it must be possible to marshal the interfaces from the multithreaded apartment to a single-threaded apartment. CRM components developed with Visual C++ could also use the Apartment threading model, although it is recommended that these use the Both threading model instead.

The interfaces described in the following table provide detailed reference information for developers of COM+ CRMs.



| CRM interfaces                                             | Description                                                                                                               |
|------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [**ICrmCompensator**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmcompensator)                 | This interface delivers unstructured log records in Visual C++.                                                           |
| [**ICrmCompensatorVariants**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmcompensatorvariants) | This interface delivers structured log records to the CRM Compensator when using Visual Basic.                            |
| [**ICrmFormatLogRecords**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmformatlogrecords)       | This interface converts the log records to viewable format so that they can be presented using a generic monitoring tool. |
| [**ICrmLogControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmlogcontrol)                   | This interface is used by the CRM Worker and CRM Compensator to write records to the log and make them durable.           |
| [**ICrmMonitor**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmmonitor)                         | This interface captures a snapshot of the current state of a CRM and holds a specific CRM clerk.                          |
| [**ICrmMonitorClerks**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmmonitorclerks)             | This interface obtains information about the state of clerks.                                                             |
| [**ICrmMonitorLogRecords**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmmonitorlogrecords)     | This interface monitors the individual log records maintained by a specific CRM clerk for a given transaction.            |



 

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> </dl>

 

 



