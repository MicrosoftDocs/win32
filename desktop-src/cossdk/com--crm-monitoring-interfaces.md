---
Description: 'The CRM infrastructure provides a set of interfaces that can be used for monitoring the CRMs within a particular server application.'
ms.assetid: 'b8f40c91-001b-4003-b377-57a918988100'
title: COM+ CRM Monitoring Interfaces
---

# COM+ CRM Monitoring Interfaces

The CRM infrastructure provides a set of interfaces that can be used for monitoring the CRMs within a particular server application. To access the monitoring interfaces, a component running within the server application must first create a specialized CRM clerk called the CRM recovery clerk.

In normal use of CRMs, transactions are expected to be short-lived, and hence CRM Workers and CRM Compensators exist for a brief period of time, typically only a few seconds at most. The monitoring interfaces are therefore designed to give a snapshot of the state of the executing CRMs at a particular point in time. If any of the CRMs are having problems, the monitoring interfaces can be used to zero in on the troublesome CRM, to inspect its log records and to abort its transaction if required.

Following are the three CRM monitoring interfaces and descriptions of how they work.



| Interface                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|-------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ICrmMonitor**](icrmmonitor.md)<br/>                     | Using [**ICrmMonitor::GetClerks**](icrmmonitor-getclerks.md), a snapshot can be obtained of the current set of active CRM clerks within the server application. From this, a particular CRM clerk collection object of interest can be located and queried, including the current state of its transaction and the log records written by the CRM.<br/> When the monitoring tool has determined which clerk is of interest, it calls [**ICrmMonitor::HoldClerk**](icrmmonitor-holdclerk.md) to get an [**ICrmMonitorLogRecords**](icrmmonitorlogrecords.md) interface on that particular clerk. At this point, the monitoring tool is holding a reference to that clerk, and if the transaction completes, the clerk is held in memory and is not released until the monitoring tool is done.<br/>                                                                                                                                                                                                    |
| [**ICrmMonitorClerks**](icrmmonitorclerks.md)<br/>         | Using this interface, the clerk collection object can be browsed for information about the state of the clerk collection at the moment it was obtained. This information includes the number of clerks, the ProgID of the CRM Compensator used by the clerk, the description provided at the time the CRM Compensator was registered (using [**ICrmLogControl::RegisterCompensator**](icrmlogcontrol-registercompensator.md)), the transaction unit-of-work ID, and the activity ID. Individual clerks are also uniquely identified by a "clerk instance CLSID," which is not a COM CLSID in the usual sense of the term but simply a unique GUID that identifies this particular clerk for its lifetime.<br/>                                                                                                                                                                                                                                                                                                |
| [**ICrmMonitorLogRecords**](icrmmonitorlogrecords.md)<br/> | This interface can be used to query the current state of the transaction, to find out how many log records this CRM clerk has written, and to get the actual log record data. The log records are provided from the [**ICrmMonitorLogRecords**](icrmmonitorlogrecords.md) interface in the same format that they were originally written (using [**ICrmLogControl**](icrmlogcontrol.md)). In addition, **ICrmMonitorLogRecords** can be optionally implemented to convert the log records to viewable format so they can be presented using a generic monitoring tool.<br/> Because [**ICrmMonitorLogRecords**](icrmmonitorlogrecords.md) is implemented directly on the CRM clerk, you can [**QueryInterface**](https://msdn.microsoft.com/library/windows/desktop/ms682521) for [**ICrmLogControl**](icrmlogcontrol.md) (also implemented on the CRM clerk). This can then be used to directly abort the transaction if required ([**ICrmLogControl::ForceTransactionToAbort**](icrmlogcontrol-forcetransactiontoabort.md)).<br/> |



 

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> </dl>

 

 




