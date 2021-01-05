---
description: COM+ CRM Startup and Recovery
ms.assetid: dee1f2df-dfe0-44c3-830b-871690e513e9
title: COM+ CRM Startup and Recovery
ms.topic: article
ms.date: 05/31/2018
---

# COM+ CRM Startup and Recovery

If a server application has the **Enable compensating resource managers** checkbox selected (using the Component Services administrative tool, on the **Advanced** tab of the COM+ application's property page), the first time it starts up it creates a CRM log file to be used by all CRMs in that server application process. (For detailed instructions about configuring the CRM, see [Configuring COM+ CRM Components](configuring-com--crm-components.md).)

The name of the CRM log file created for the server application is based on the AppId (a GUID) of the server application, and the CRM log file is placed in the same directory as the DTC log file (normally your %SystemRoot%\\winnt\\system32\\DtcLog directory). CRM log files have the extension .crmlog.

> [!Note]  
> It may be necessary to change the default location of a CRM log file due to performance reasons (to have the DTC log file on a different disk than the CRM log file) or perhaps due to use of the CRM in a cluster environment. The location of the CRM log files can be changed using the COM+ administration SDK. The property name is CRMLogFile, and it exists on the [**Applications**](applications.md) collection object.

 

When a server application (that is CRM-enabled) starts up and finds that a CRM log file already exists for that server application, it performs recovery on that CRM log file. *Recovery* is the process of completing any transactions that were interrupted by a failure and involves the CRM infrastructure reading the CRM log file for any transactions that were not fully completed. If it finds any, it contacts the DTC to determine the transaction outcome. It then creates the CRM Compensator and passes on the commit or abort notifications as required, together with the associated log records.

Prepare notifications are not received by the CRM Compensator during recovery. The CRM Compensator has a flag to distinguish whether it is being called during normal operation or during recovery.

Recovery will normally find uncompleted transactions only if the server application has been shutdown abnormally, due to either a server application process crash or a computer crash. If the server application is allowed to shut down normally, due either to the idle time-out or to manual shutdown via the Component Services administrative tool, the log file will be clean.

Starting of a CRM server application for recovery is not automatically initiated. Some external action must be taken to start the CRM server application where recovery is required. Typically this would be creating a component in that server application.

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> <dt>

[COM+ CRM Operating Process](com--crm-operating-process.md)
</dt> </dl>

 

 



