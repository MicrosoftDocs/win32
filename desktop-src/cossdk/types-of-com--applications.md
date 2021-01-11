---
description: Types of COM+ Applications
ms.assetid: 4b731f22-6837-4c03-9c8c-a76451369cf1
title: Types of COM+ Applications
ms.topic: article
ms.date: 05/31/2018
---

# Types of COM+ Applications

Following are the four basic types of COM+ applications:

-   **Server applications.** A COM+ *server application* runs in its own process. Server applications can support all COM+ services.
-   **Library applications.** A COM+ *library application* runs in the process of the client that creates it. More specifically, the components in a library application are always loaded into the process of the creator. Library applications are not explicitly associated with a server process. They can use role-based security but do not support remote access or queued components.
-   **Application proxies.** An *application proxy* is a set of files containing registration information that allows a client to remotely access a server application. When run on a client computer, an application proxy file writes information about the COM+ server application, including CLSIDs, ProgIDs, RemoteServerName, and marshaling information, to the client computer. The server application can then be accessed remotely from the client computer.
-   **COM+ preinstalled applications**. COM+ includes a set of preinstalled applications that handle internal functions. The preinstalled applications are listed in the COM+ Applications folder in the Component Services administrative tool, but they cannot be modified or deleted. These applications include the following:
    -   .NET Utilities
    -   Analyzer Control Publisher Application
    -   COM+ Explorer
    -   COM+ QC Dead Letter Queue Listener
    -   COM+ Utilities
    -   IIS In-Process Applications
    -   IIS Out-Of-Process Pooled Applications
    -   System Application

## Notes

As of Windows Server 2003, it is possible to run COM+ applications even if the System Application is disabled. The COM+ applications will run, though without the services usually provided by the System Application. These services include use of the Component Services administrative tool and system event tracking.

Also as of Windows Server 2003, the authentication capability for the COM+ System Application includes the value EOAC\_DISABLE\_AAA. This value, which disables activate-as-activator (AAA) activations, is used with the [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity) function when launching the System Application. Setting the authentication capability to EOAC\_DISABLE\_AAA allows an application that runs under a privileged account (such as LocalSystem) to help prevent its identity from being used to launch untrusted components.

 

 
