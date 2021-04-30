---
description: A COM+ application is essentially a declarative construct that enables you to configure any number of components in common. For example, you can configure the components in an application with a common security policy.
ms.assetid: 50039b30-1c91-4e93-9f23-873accb651cf
title: Configuring COM+ Applications
ms.topic: article
ms.date: 05/31/2018
---

# Configuring COM+ Applications

A COM+ application is essentially a declarative construct that enables you to configure any number of components in common. For example, you can configure the components in an application with a common security policy.

Configuration is an essential part of the development process for COM+ applications. How you configure an application will determine how COM+ will provide services for it and how it behaves when running.

You can configure COM+ applications using either the Component Services administration tool or the scriptable administration objects and interfaces that provide the underlying functionality of the administration tool. For details on performing scripted administration, see [Automating COM+ Administration](automating-com--administration.md).

You can configure elements at the following levels within COM+ applications:

-   [Application-Level Settings](#application-level-settings)
-   [Component-Level (Class-Level) Settings](#component-level-class-level-settings)
-   [Interface-Level Setting](#interface-level-setting)
-   [Method-Level Setting](#method-level-setting)
-   [Related topics](#related-topics)

How you install components into an application can affect how you can configure them. You should always install components into COM+ applications (as opposed to importing them). Installing components will fully register them, along with interfaces and type libraries, in the COM+ class registration database (RegDB) so that you can configure them.

## Application-Level Settings



| Attribute                                                                                        | Description                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Activation](context-activation.md)<br/>                                                  | Specifies application type: either server application or library application.<br/>                                                                                                            |
| [Enabling access checks](enabling-access-checks-for-an-application.md)<br/>               | Turns security checking on and off.<br/>                                                                                                                                                      |
| [Security level](setting-a-security-level-for-access-checks.md)<br/>                      | Specifies that access checks will be performed at the process level (access-checking levels generated from roles) or both at process and at component levels (full role-based security).<br/> |
| [Authentication level](setting-an-authentication-level-for-a-server-application.md)<br/>  | Sets the authentication level used on calls into the application.<br/>                                                                                                                        |
| [Impersonation level](setting-an-impersonation-level.md)<br/>                             | Sets the impersonation level used on calls to other applications.<br/>                                                                                                                        |
| [Queuing](creating-queuable-components.md)<br/>                                           | Specifies that application components will use queuing services.<br/>                                                                                                                         |
| [Enable CRM](configuring-com--crm-components.md)<br/>                                     | Enables use of Compensating Resource Managers.<br/>                                                                                                                                           |
| [Run application as a service](com--applications-running-as-service-applications.md)<br/> | Configures and implements a COM+ server application as an NT service.<br/>                                                                                                                    |
| [COM+ SOAP service](com--soap-service.md)<br/>                                            | Exposes a COM+ application as an XML web service.<br/>                                                                                                                                        |
| [Application pooling](com--application-pooling.md)<br/>                                   | Adds scalability for single-threaded processes and integrates with the COM+ Application Recycling service.<br/>                                                                               |
| [Application recycling](com--application-recycling.md)<br/>                               | Increases application stability by gracefully shutting down a process associated with an application and restarting it.<br/>                                                                  |
| [Process dumping](what-s-new-in-com--1-5.md)<br/>                                         | Dumps the entire state of a process without terminating it, for debugging purposes.<br/>                                                                                                      |
| Server process shutdown<br/>                                                               | Shuts down a process after a specified idle period.<br/>                                                                                                                                      |
| Permissions<br/>                                                                           | Disables changes to configuration settings, including deletion.<br/>                                                                                                                          |
| Security identity<br/>                                                                     | Specifies the identity under which the application runs.<br/>                                                                                                                                 |
| Launch in debugger<br/>                                                                    | Specifies that the application will be launched in a debugger, with user-specified command-line settings.<br/>                                                                                |
| Enable 3GB support<br/>                                                                    | Enables use of extended process memory address space.<br/>                                                                                                                                    |



 

## Component-Level (Class-Level) Settings



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="configuring-transactions.md">Transactions</a><br/></td>
<td>Sets automatic transaction requirements Disabled, Not Supported, Supported, Required, or Requires New.<br/></td>
</tr>
<tr class="even">
<td><a href="setting-the-synchronization-attribute.md">Synchronization</a><br/></td>
<td>Sets synchronization requirements Disabled, Not Supported, Supported, Required, or Requires New.<br/></td>
</tr>
<tr class="odd">
<td><a href="enabling-jit-activation-for-a-component.md">JIT Activation</a><br/></td>
<td>Enables just-in-time activation.<br/></td>
</tr>
<tr class="even">
<td><a href="configuring-a-component-to-be-pooled.md">Object pooling</a><br/></td>
<td>Enables object pooling. Minimum and maximum pool size and object time-out values are configurable.<br/></td>
</tr>
<tr class="odd">
<td><a href="specifying-an-object-constructor-string-for-a-component.md">Object construction</a><br/></td>
<td>Enables parameterized object construction with an administratively specified constructor string. <br/>
<blockquote>
[!Note]<br />
The constructor string should not be used to store security-sensitive information.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td><a href="enabling-access-checks-at-the-component-level.md">Component-level access checks</a><br/></td>
<td>Turns on or off component-level role-based security checking.<br/></td>
</tr>
<tr class="odd">
<td><a href="assigning-roles-to-components--interfaces--or-methods.md">Declarative role assignment</a><br/></td>
<td>Enables explicit assignment of roles to the component.<br/></td>
</tr>
<tr class="even">
<td><a href="persistent-client-side-failures.md">Queuing exception class</a><br/></td>
<td>Indicates an exception class for handling client-side failures.<br/></td>
</tr>
<tr class="odd">
<td><a href="com--instrumentation-concepts.md">Instrumentation events and statistics</a><br/></td>
<td>Enables detailed system event and object statistics reporting.<br/></td>
</tr>
<tr class="even">
<td><a href="context-activation.md">Activation context</a><br/></td>
<td>Enables forced activation of an object in the caller's context or default context.<br/></td>
</tr>
<tr class="odd">
<td><a href="what-s-new-in-com--1-5.md">Creating private components</a><br/></td>
<td>Marks component as private to the application. A private component can be seen and activated only by other components in the same application.<br/></td>
</tr>
</tbody>
</table>



 

## Interface-Level Setting



| Attribute                                                                                           | Description                                                                                                                      |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|
| [Queued](creating-queuable-components.md)<br/>                                               | Indicates a queuable interface, defined in IDL.<br/>                                                                       |
| [Declarative role assignment](assigning-roles-to-components--interfaces--or-methods.md)<br/> | Enables explicit assignment of roles to the interface as well as implicitly inherited roles from the component level.<br/> |



 

## Method-Level Setting



| Attribute                                                                                           | Description                                                                                                                                  |
|-----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| [Auto-done](enabling-auto-done-for-a-method.md)<br/>                                         | Automatically deactivates object on method return and votes in transaction.<br/>                                                       |
| [Declarative role assignment](assigning-roles-to-components--interfaces--or-methods.md)<br/> | Enables explicit assignment of roles to the method as well as implicitly inherited roles from the interface and component levels.<br/> |



 

## Related topics

<dl> <dt>

[Automating COM+ Administration](automating-com--administration.md)
</dt> <dt>

[Creating COM+ Applications](creating-com--applications.md)
</dt> <dt>

[Deploying COM+ Applications](deploying-com--applications.md)
</dt> </dl>

 

 




