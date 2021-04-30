---
description: The CommandLineEventConsumer class runs a specified executable program from a command line when a specified event occurs. This class is a standard event consumer that WMI provides.
ms.assetid: b912a4a1-7b1c-43a9-b098-fcfd62a2c2db
ms.tgt_platform: multiple
title: Running a Program from the Command Line Based on an Event
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Running a Program from the Command Line Based on an Event

The [**CommandLineEventConsumer**](commandlineeventconsumer.md) class runs a specified executable program from a command line when a specified event occurs. This class is a standard event consumer that WMI provides.

When you use [**CommandLineEventConsumer**](commandlineeventconsumer.md), you should secure the executable that you want to start. If the executable is not in a secure location or not secured with a strong access control list (ACL), a user without access privileges can replace your executable with a different executable. You can use the [**Win32\_LogicalFileSecuritySetting**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalfilesecuritysetting) or [**Win32\_LogicalShareSecuritySetting**](/previous-versions/windows/desktop/secrcw32prov/win32-logicalsharesecuritysetting) classes to change programmatically the security of a file or share. For more information, see [Creating a Security Descriptor for a New Object in C++](/windows/desktop/SecAuthZ/creating-a-security-descriptor-for-a-new-object-in-c--).

The basic procedure to use standard consumers is always the same, and is located in [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md). The following procedure adds to the basic procedure, is specific to the [**CommandLineEventConsumer**](commandlineeventconsumer.md) class, and describes how to create an event consumer that runs a program.

> [!Caution]
>
> The [**CommandLineEventConsumer**](commandlineeventconsumer.md) class has special security constraints. This standard consumer must be configured by a local member of the Administrators group on the local computer. If you use a domain account to create the subscription, the LocalSystem account must have the necessary permissions on the domain to verify that the creator is a member of the local Administrators group.
>
> [**CommandLineEventConsumer**](commandlineeventconsumer.md) cannot be used to start a process that runs interactively.

 

The following procedure describes how to create an event consumer that runs a process from a command line.

**To create an event consumer that runs a process from a command line**

1.  In the Managed Object Format (MOF) file, create an instance of [**CommandLineEventConsumer**](commandlineeventconsumer.md) to receive the events you request in the query. For more information, see [Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md).
2.  Create an instance of [**\_\_EventFilter**](--eventfilter.md) and give it a name.
3.  Create a query to specify the type of event. For more information, see [Querying with WQL](querying-with-wql.md).
4.  Create an instance of [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) to associate the filter with the instance of [**CommandLineEventConsumer**](commandlineeventconsumer.md).
5.  Compile your MOF file by using [**Mofcomp.exe**](mofcomp.md).

## Example

The following code example creates a new class called "MyCmdLineConsumer" to generate events when an instance of the new class is created at the end of a MOF. The example is in MOF code, but you can create the instances programmatically by using the [Scripting API for WMI](scripting-api-for-wmi.md) or the [COM API for WMI](com-api-for-wmi.md).

The following procedure describes how to create a new class called MyCmdLineConsumer.

**To create a new class called MyCmdLineConsumer**

1.  Create the c:\\cmdline\_test.bat file with a command that executes a visible program, such as "calc.exe" .
2.  Copy the MOF to a text file and save it with a .mof extension.
3.  In a Command window, compile the MOF file by using the following command: **Mofcomp filename.mof**.

> [!Note]  
> The program specified in cmdline\_test.bat should execute.

 

``` syntax
// Set the namespace as root\subscription.
// The CommandLineEventConsumer is already compiled
// in the root\subscription namespace. 
#pragma namespace ("\\\\.\\Root\\subscription")

class MyCmdLineConsumer
{
 [key]string Name;
};

// Create an instance of the command line consumer
// and give it the alias $CMDLINECONSUMER

instance of CommandLineEventConsumer as $CMDLINECONSUMER
{
 Name = "CmdLineConsumer_Example";
 CommandLineTemplate = "c:\\cmdline_test.bat";
 RunInteractively = True;
 WorkingDirectory = "c:\\";
};    

// Create an instance of the event filter
// and give it the alias $CMDLINEFILTER
// The filter queries for instance creation event
// for instances of the MyCmdLineConsumer class

instance of __EventFilter as $CMDLINEFILTER
{
    Name = "CmdLineFilter";
    Query = "SELECT * FROM __InstanceCreationEvent"
        " WHERE TargetInstance.__class = \"MyCmdLineConsumer\"";
    QueryLanguage = "WQL";
};

// Create an instance of the binding
// between filter and consumer instances.

instance of __FilterToConsumerBinding
{
     Consumer = $CMDLINECONSUMER;
     Filter = $CMDLINEFILTER;
};

// Create an instance of this class right now. 
// The commands in c:\\cmdline_test.bat execute
// as the result of creating the instance
// of MyCmdLineConsumer.
 
instance of MyCmdLineConsumer
{
     Name = "CmdLineEventConsumer test";
};
```

## Related topics

<dl> <dt>

[Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md)
</dt> </dl>

 

 
