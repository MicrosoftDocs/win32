---
description: COM+ CRM Operating Process
ms.assetid: be50912e-b9fd-4ef7-b81a-e37617a96955
title: COM+ CRM Operating Process
ms.topic: article
ms.date: 05/31/2018
---

# COM+ CRM Operating Process

In normal operation, an application component running in a server application process would use a COM+ CRM by creating a CRM worker. The CRM worker implements a COM interface specific to the task it is designed to perform. The application component must be running under a transaction so that the CRM worker inherits the transaction of the application component. CRM workers always require a transaction.

To access the COM+ CRM, the CRM worker first obtains the [**ICrmLogControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmlogcontrol) interface, which allows the CRM worker to write records to the durable log. The CRM worker obtains this interface by creating a CRM clerk component.

Next the CRM worker must tell the CRM clerk the name of the CRM Compensator it wants to use. It does this by calling the [**ICrmLogControl::RegisterCompensator**](/windows/desktop/api/ComSvcs/nf-comsvcs-icrmlogcontrol-registercompensator) method. After this method is called, the CRM Compensator is created by the CRM infrastructure when the transaction completes.

After the CRM worker has registered its CRM Compensator, it can write records to the CRM log using [**ICrmLogControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmlogcontrol). The CRM worker must *write ahead*; that is, it must write a record to the log describing an action before it actually performs the action, in case a crash occurs immediately after completing the action. Without these write-ahead log records, there is no way to correct for the action.

Also, write ahead means that the CRM Compensator, which is the component that receives the log records on recovery, must deal with the case where the log records were written but the action did not in fact occur. Actions by the CRM Compensator must be *idempotent*; that is, they should be capable of being performed more than once but should lead to the same outcome. For example, setting an account balance to the value of $100 is an idempotent action; adding $100 to the account balance is not.

The [**ICrmLogControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmlogcontrol) interface provides the following two methods for writing log records:

-   [**WriteLogRecordVariants**](/windows/desktop/api/ComSvcs/nf-comsvcs-icrmlogcontrol-writelogrecordvariants) is used for writing a structured log record that is built up as a collection of Variants. It is primarily for use when developing CRMs in Microsoft Visual Basic.
-   [**WriteLogRecord**](/windows/desktop/api/ComSvcs/nf-comsvcs-icrmlogcontrol-writelogrecord) is used for writing an unstructured log record as BLOBs of bytes. It is primarily for use when developing CRMs in Microsoft Visual C++. Because record structures in C are often made up of a set of headers and fields that may be scattered in memory, the **WriteLogRecord** method implements a gather capability that reduces the copying of data.

> [!Note]  
> You should not user pointer types within data structures in a log record. Pointers are no longer valid during recovery phase because the CRM Compensator runs in a different process than that of the CRM worker that wrote the log record. Including pointer types in a log record might cause an application to crash or corrupt itself during recovery.

 

Both of these write methods write a log record to disk but do not guarantee the record's durability. While allowing lazy writes to accumulate before forcing to disk can improve performance, you can use the [**ICrmLogControl::ForceLog**](/windows/desktop/api/ComSvcs/nf-comsvcs-icrmlogcontrol-forcelog) method instead to guarantee that all writes done by the CRM are durable on disk, which is important for failure recovery.

When the CRM worker is done with its actions and has finished writing and forcing records to the log, it must release [**ICrmLogControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmlogcontrol). When the transaction completes (typically due to the application component calling [**SetComplete**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setcomplete) or [**SetAbort**](/windows/desktop/api/ComSvcs/nf-comsvcs-iobjectcontext-setabort)), the CRM infrastructure creates the CRM Compensator component, which implements either the [**ICrmCompensator**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmcompensator) interface or the [**ICrmCompensatorVariants**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmcompensatorvariants) interface. These interfaces are used to pass the unstructured (Visual C++) or structured (Visual Basic) records to the CRM Compensator along with the transaction outcome notifications.

The CRM Compensator is first notified of the prepare phase of the transaction completion and can vote either yes or no to the prepare request. If the CRM Compensator votes no, it does not receive any further abort notifications. If it votes yes to the prepare request, it receives either the commit or abort notifications. In the case of a client abort, no prepare notifications are received, only abort notifications. The CRM Compensator must be prepared to handle all these cases, and it also must handle the case where no log records were successfully written by the CRM worker. The CRM Compensator must not assume that the same CRM Compensator instance will receive both the phase 1 (prepare) and the phase 2 (commit or abort) notifications, as these could be interrupted by recovery.

Typically, a CRM Compensator uses the abort notification to reverse the action that was performed by the CRM worker. The CRM worker might leave some state available in case it needs to reverse its action. That state might be fully contained in the log records, and if not, the CRM Compensator needs to clean up that state if the transaction commits. This is the reason why the CRM Compensator receives the commit notification. The CRM Compensator does not run under a DTC transaction.

The CRM Compensator can log new records if required by using [**ICrmLogControl**](/windows/desktop/api/ComSvcs/nn-comsvcs-icrmlogcontrol), which it receives as it is created. Both the CRM worker and CRM Compensator can also forget the last log record they wrote, which might be required to avoid unnecessary recovery.

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> <dt>

[COM+ CRM Startup and Recovery](com--crm-startup-and-recovery.md)
</dt> </dl>

 

 



