---
description: When developing COM+ applications, the principal tasks include designing COM components to encapsulate application logic and integrating these components into a COM+ application, creating the COM+ application, and administering the application through deployment and maintenance.
ms.assetid: 8c6ec901-1eeb-46b0-8a3a-26d8eff99f6d
title: Developing COM+ Applications
ms.topic: article
ms.date: 05/31/2018
---

# Developing COM+ Applications

When developing COM+ applications, the principal tasks include designing COM components to encapsulate application logic and integrating these components into a COM+ application, creating the COM+ application, and administering the application through deployment and maintenance.

## Designing COM Components

The following steps describe a general procedure for good component design:

1.  Define the COM classes and implementation classes.
2.  Group the classes into components.
3.  Select the set of COM+ services for your component, even if you do not specify all of them when developing the component. These services can later be specified using the Component Services administrative tool or the COM+ administration object model (See [Automating COM+ Administration](automating-com--administration.md) for more information about the COM+ administration object model.)

## Creating the COM+ Application

After designing the COM components, the developer integrates the components into a COM+ application and configures the application. The following steps describe the process:

1.  Integrate the components into a COM+ application. You can integrate the components into an existing COM+ application or create a new (empty) application for the components. (See [Creating COM+ Applications](creating-com--applications.md).)
2.  Specify the correct set of attributes for each of the classes (if any, and if not specified in the development tool). These attributes express the components dependencies on any COM+ services its implementation might rely on (for example, transactions, Queued Components, Security, Object Pooling, and Just-in-Time Activation).
3.  Set up the security framework (roles and assignment of roles to classes, interfaces, and methods).
4.  Configure environment-specific attributes on classes and applications (the default object pool size, for example). These environment-specific attributes can later be set (or modified) by the system administrator.
5.  Export the application for redistribution and deployment.

For more detailed information on the steps in designing distributed applications, see [Designing COM+ Applications](designing-com--applications.md).

## Administering COM+ Applications

Typically, a developer delivers a partially configured COM+ application to the system administrator. The administrator can then customize the application for one or more specific environments (for example, by adding user accounts in roles and server names in an application cluster). The administrator's tasks include the following:

-   Installing the partially configured COM+ application on an administrative computer.
-   Providing environment-specific attributes, such as role members and object pool size.
-   Re-exporting the fully configured COM+ application.
-   Creating an application proxy (if the application is to be accessed remotely).

After an application is fully configured for a specific environment, the administrator can then deploy it on test or production machines. This involves installing the fully configured COM+ application on one or more computers.

For detailed information on COM+ administration procedures, see the Component Services administrative tool.

 

 



