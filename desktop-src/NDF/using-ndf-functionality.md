---
title: Using NDF Functionality
description: Microsoft provides access to NDF functionality through a public API. When a problem occurs, the application can use this API to leverage this functionality within the context of a specific application.
ms.assetid: db06b9a9-a64a-43ff-9b77-95230208cfd6
ms.topic: article
ms.date: 05/31/2018
---

# Using NDF Functionality

Microsoft provides access to NDF functionality through a public API. When a problem occurs, the application can use this API to leverage this functionality within the context of a specific application.

There are three stages of performing diagnosis with NDF: creating an incident, running diagnosis and repairs, and closing the incident. This overview indicates which NDF functions may be relevant for a specific scenario. Detailed information on each function can be found in the [NDF Reference](ndf-reference.md) section.

## Creating an Incident

An NDF diagnostics session requires a specific incident to diagnose. There are several functions which can be used to create an incident. Choose the function which most closely matches what the application was trying to do when the failure occurred.

-   [**NdfCreateConnectivityIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcreateconnectivityincident): General Internet connectivity problems which do not need additional information.
-   [**NdfCreateWebIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcreatewebincident)/[**NdfCreateWebIncidentEx**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcreatewebincidentex): Connecting to an HTTP or HTTPS URL.
-   [**NdfCreateSharingIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcreatesharingincident): Accessing a UNC path or file share.
-   [**NdfCreateDNSIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcreatednsincident): Resolving a DNS host name.
-   [**NdfCreatePnrpIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcreatepnrpincident): Resolving a PNRP peer name.
-   [**NdfCreateGroupingIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcreategroupingincident): Joining a peer-to-peer group.
-   [**NdfCreateWinSockIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcreatewinsockincident): Connecting to a destination by using a socket (when none of the other functions specifically apply).
-   [**NdfCreateIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcreateincident): Used when no other scenario is appropriate and the specific NDF helper class to be invoked is known (along with the arguments it requires). Primarily used for testing purposes by application developers who have written their own helper class.

## Running Diagnosis and Repairs

There are two ways to launch the diagnosis and repair functionality.

-   Using the Windows User Interface (Recommended)

    When running in the standard Windows user interface, you can simply call the [**NdfExecuteDiagnosis**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfexecutediagnosis) function. The NDF Wizard will launch and assist the user in identifying (and if possible, and resolving) the problem. The function will return after this process has finished. The user interface is optionally modal to your application.

-   Using a Custom User Interface (Windows 7 and later only)

    Different functions are available to use in scenarios where no user interface is being shown, or where the standard Windows experience is not being used (such as Media Center, embedded applications, and the command prompt). This option bypasses the user experience functionality provided in the NDF Wizard, which includes limiting the results to fully-supported root causes, as well as heuristics to present repairs to the user in recommended order. When using these functions, you must provide any such functionality yourself. You must also make sure to free memory used by the diagnosis results.

    To begin diagnosis, call the [**NdfDiagnoseIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfdiagnoseincident) function. Any problems found will be returned to the application as a collection of [**RootCauseInfo**](/windows/win32/api/ndattrib/ns-ndattrib-rootcauseinfo) structures describing identified root causes and possible repairs.

    After selecting a repair (or asking the user to select a repair), [**NdfRepairIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfrepairincident) should be called to attempt the repair and determine whether the problem was resolved.

    In some cases, a repair may be successfully performed but will not resolve the problem. In such cases, closing the existing incident and then opening a new one is recommended. This will ensure that any new problems unmasked by the initial repair are identified. For example, suppose that no wireless networks had been visible. After resetting the adapter, wireless networks are visible, but none of them are on the preferred list. This is a new problem that would require a new diagnosis to identify. If such a second diagnosis attempt does not identify additional problems, a different repair can be attempted to resolve the original issue, or the user can be informed that the problem could not be resolved.

    [**NdfDiagnoseIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfdiagnoseincident) and [**NdfRepairIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfrepairincident) are synchronous APIs. If you wish to cancel activity initiated by these functions, call [**NdfCancelIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcancelincident) from another thread. The function will return at the next available stopping point in the diagnosis or repair process.

    At any point, you may optionally call [**NdfGetTraceFile**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfgettracefile) to retrieve a copy of the NDF log for the current diagnosis session and include it with your application logs. The log is flushed once retrieved, and subsequent calls will only retrieve events which occurred after the last call to this function.

## Closing an Incident

When you are finished diagnosing an incident, call [**NdfCloseIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfcloseincident) to free system resources associated with performing diagnostics on that incident. (Note that this does not free objects created by [**NdfDiagnoseIncident**](/windows/desktop/api/Ndfapi/nf-ndfapi-ndfdiagnoseincident).
