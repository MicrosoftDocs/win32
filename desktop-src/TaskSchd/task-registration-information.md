---
title: Task Registration Information
description: Registration information provides a way to identify a task in several different ways. For example, a task can be identified by the author, how it was authored (referred to as the task source), and date of registration.
ms.assetid: 45c9fa99-2718-4202-8987-4b506bd677e9
keywords:
- registration information Task Scheduler
ms.topic: article
ms.date: 05/31/2018
---

# Task Registration Information

Registration information provides a way to identify a task in several different ways. For example, a task can be identified by the author, how it was authored (referred to as the task source), and date of registration.

## Using Registration Information

Registration information is typically specified when the task is created and then used in the following ways:

-   Displayed by the Task Scheduler user interface.
-   Get or set by C++ applications or scripts.
-   In an enterprise environment, used as a search criteria when enumerating over all registered tasks.

## Types of Registration Information

Task registration information is defined by the properties of the [**RegistrationInfo**](registrationinfo.md) object for scripting applications, the properties of the [**IRegistrationInfo**](/windows/desktop/api/taskschd/nn-taskschd-iregistrationinfo) interface for C++ applications, and the child elements of the [**RegistrationInfo (taskType) element**](taskschedulerschema-registrationinfo-tasktype-element.md) for reading or writing XML.

These properties allow access to the following types of registration information:

-   Task Author

    Task Scheduler sets the author of the task when it is created.

-   Task Registration Date

    Task Scheduler sets this date when the task is registered.

-   Task Description

    A user-defined description that may include what triggers are used to start the task or what actions the task performs.

-   Task Documentation

    User-supplied documentation that is needed by the task.

-   Task Security Descriptor

    A user-supplied security descriptor.

-   Task Source

    User-supplied information that describes where the task originated from. For example, a task may originate from a component, service, application, or user.

-   Task URI

    A uniform resource identifier (URI) for the task.

-   Task Version

    User-supplied information that is used when multiple versions of a task exist.

-   XML Text

    An XML-formatted version of the registration information. Note that you can set or modify the registration information directly through this XML and the appropriate object and interface properties will be updated accordingly.

## Registering Tasks

A task can be registered after the task definitions are created and registration information and setting values are supplied by the user. A task is registered using the [**TaskFolder.RegisterTaskDefinition**](taskfolder-registertaskdefinition.md) method for scripting applications or the [**ITaskFolder::RegisterTaskDefinition**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertaskdefinition) method for C++ applications. If you want to register a task using XML to define the task, you use the [**TaskFolder.RegisterTask**](taskfolder-registertask.md) method for scripting applications and the [**ITaskFolder::RegisterTask**](/windows/desktop/api/taskschd/nf-taskschd-itaskfolder-registertask) method for C++ applications.

In the methods mentioned above, you can specify the security context to run the task. You have to be an administrator on the system to schedule jobs to run under contexts other than your own. For more information on the security contexts to run tasks, see [Security Contexts for Running Tasks](security-contexts-for-running-tasks.md).

## Related topics

<dl> <dt>

[About The Task Scheduler](about-the-task-scheduler.md)
</dt> <dt>

[Task Scheduler](task-scheduler-start-page.md)
</dt> </dl>

 

 




