---
description: An application running as a standard user communicates with a service running as SYSTEM by using Remote Procedure Call (RPC).
ms.assetid: c0bcebe3-f7eb-471f-a21d-5840d2e26729
title: Operating System Service Model
ms.topic: article
ms.date: 05/31/2018
---

# Operating System Service Model

In the operating system service model, an application running as a standard user communicates with a service running as **SYSTEM** by using [Remote Procedure Call](/windows/desktop/Rpc/rpc-start-page) (RPC).

The standard user application is marked in the application manifest with a **requestedExecutionLevel** of **asInvoker**. To perform an operation that requires administrator privilege, the standard user application makes a request to the service.

One use for the operating system service model is to manage applications that could impact the system, such as antivirus or other unwanted software and spyware. The standard user application allows the logged on user to control some aspects of the service. The service is responsible for determining which operations it performs for a standard user application. For example, an antivirus service might allow a standard user to start a scan of the system, but it might not allow a standard user to disable real-time virus checking.

A major benefit of using the operating system service model is that no elevation prompting is required.

One drawback of using the operating system service model is that a service running on the system uses more resources than a task, and a service cannot be stopped by a standard user. Consider using the [Elevated Task Model](elevated-task-model.md) if it suffices.

To implement the operating system service model, create a standard user client application and an operating system service. Install the service in the operating system during product installation time.

## Related topics

<dl> <dt>

[Developing Applications that Require Administrator Privilege](developing-applications-that-require-administrator-privilege.md)
</dt> <dt>

[Administrator Broker Model](administrator-broker-model.md)
</dt> <dt>

[Administrator COM Object Model](administrator-com-object-model.md)
</dt> <dt>

[Elevated Task Model](elevated-task-model.md)
</dt> </dl>

 

 
