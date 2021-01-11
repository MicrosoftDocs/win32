---
description: You can use the COM+ Compensating Resource Manager (CRM) to easily and quickly integrate application resources with Microsoft Distributed Transaction Coordinator (DTC) transactions.
ms.assetid: 8d1d034f-8a09-40ae-842a-5251135bd3c8
title: COM+ Compensating Resource Manager Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Compensating Resource Manager Concepts

You can use the COM+ Compensating Resource Manager (CRM) to easily and quickly integrate application resources with Microsoft Distributed Transaction Coordinator (DTC) transactions. Your application resources can vote on the outcome of a transaction and can receive final notification of its outcome. A durable log is generated so that your application resources can write records that survive failures, and the CRM recovers this log file when the application restarts.

A CRM consists of the following two components:

-   CRM Worker. This component performs the main work of the specific CRM and implements an interface specific to the task it needs to perform. The CRM infrastructure provides an interface to the CRM Worker through which the CRM Worker can write records to a durable log file on disk. The CRM Worker must write records to the log and make them durable before it performs its work so that, if a crash occurs, recovery can occur correctly. The CRM Worker always requires a transaction.
-   CRM Compensator. This component is created by the CRM infrastructure at the completion of the transaction. It implements a defined interface by which the CRM infrastructure can pass on notifications of transaction completion and the log records that were previously written by the CRM Worker.

A COM+ CRM provides atomicity with transactional notifications, and durability with the CRM log, but does not provide isolation of resources. In a multithreaded environment, it is the responsibility of the CRM developer to ensure that access to resources, either by multiple CRM Workers or external applications, is serialized while in a transaction.

After the transaction has passed the prepare phase, the CRM Compensator and CRM Workers can be running concurrently. It is possible for the CRM Worker component of a new transaction to become active while the CRM Compensator of a previous transaction is still processing the previous transaction.

During failures prior to recovery of the CRM server application, an interrupted transaction should be considered active and not complete. It should not be possible for external processes to access the resources that were being changed by this particular transaction prior to recovery of the CRM server process.

The CRM defines three interface types for the basic CRM functions:

-   [**ICrmLogControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmlogcontrol) is implemented on the CRM clerk and is used by the CRM Worker to write log records to the log. It can also used by the CRM Compensator.
-   [**ICrmCompensator**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmcompensator) and [**ICrmCompensatorVariants**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmcompensatorvariants) are implemented on the CRM Compensator. These interfaces are used to deliver transaction outcome notifications and their associated log records to the CRM Compensator. Normally, the CRM Compensator would implement only one of these interfaces, depending on whether it required unstructured or structured log records. *Structured log records* are those that are built up as a collection of Variants and are typically for use by Microsoft Visual Basic. *Unstructured log records* are just a buffer of bytes and are typically for use by Microsoft Visual C++. A CRM Compensator can implement both of the compensator interfaces; however, only one at a time is used to deliver log records.
-   The COM+ CRM monitoring interfaces are used for monitoring the CRMs within a particular server application. For detailed information about the monitoring interfaces, see [COM+ CRM Monitoring Interfaces](com--crm-monitoring-interfaces.md).

The following topics in this section provide more detail about the COM+ CRM service:

-   [COM+ CRM Security Considerations](com--crm-security-considerations.md)
-   [COM+ CRM Operating Process](com--crm-operating-process.md)
-   [COM+ CRM Startup and Recovery](com--crm-startup-and-recovery.md)
-   [Using the COM+ CRM in a Cluster Environment](using-the-com--crm-in-a-cluster-environment.md)
-   [Error Handling in the COM+ CRM](error-handling-in-the-com--crm.md)
-   [COM+ CRM Registry Settings](com--crm-registry-settings.md)
-   [Troubleshooting the COM+ CRM](troubleshooting-the-com--crm.md)
-   [Design Suggestions for Developing a COM+ CRM](design-suggestions-for-developing-a-com--crm.md)
-   [COM+ CRM Monitoring Interfaces](com--crm-monitoring-interfaces.md)
-   [COM+ CRM Interfaces](com--crm-interfaces.md)

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Tasks](com--compensating-resource-manager-tasks.md)
</dt> </dl>

 

 



