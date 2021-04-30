---
description: COM+ Service Application Concepts
ms.assetid: d6b1cf4a-ca39-4d50-a33d-aa639937ef9e
title: COM+ Service Application Concepts
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Service Application Concepts

You can use the Component Services administrative tool to configure a COM+ server application as a service application. Running a COM+ server application as a service offers the following advantages:

-   If your application always needs to be running, Component Services can optionally have the server started automatically and can also restart the server if it times out. For example, if a computer running Queued Components listener components is rebooted, the Queued Components listeners can be started automatically if they are configured as a service.
-   If your application needs to perform privileged operations, the application can run as the local system account. Only NT services are allowed to run with this level of security. The application will be compatible with the Windows Cluster service, which manages services during system failover.
-   If other services need to be marked as dependent, Component Services provides that option. For example, if your application makes use of functionality provided by another service, the service marked as dependent will be started before your application starts.

## Starting an Application Automatically

When the COM+ server application is started automatically, it acts like a service, requiring the developer to manage the server using the Services administrative tool.

> [!Note]  
> The Services administrative tool can be accessed by launching the Component Services administrative tool and then clicking **Services (Local)**.

 

## Starting an Application Manually

When the COM+ server application is started manually, it acts like a DLL host with the security settings of a service. The service will be started up manually when activated and shut down automatically when it times out.

## Service Configurations

Regardless of the startup type, the application can be configured to run as a local system account or assigned to a user account. The local system and user account can be configured at the time of creating the service. To configure the security settings, the Services administrative tool will have to be used. Dependencies can also be set for the service.

The application can also be started in any particular order by selecting dependencies from a list of other system services. For example, the system services can be marked as dependent and will not start the application until the system services have been started in the specified order. This will properly initialize the service application before it is used.

For a step-by-step instruction on how to configure a COM+ application to run as a service, see [Configuring a COM+ Server Application as a Service Application](configuring-a-com--server-application-as-a-service-application.md).

## Related topics

<dl> <dt>

[COM+ Service Application Tasks](com--service-application-tasks.md)
</dt> </dl>

 

 



