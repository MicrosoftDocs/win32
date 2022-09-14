---
description: By using the SMTPEventConsumer class, you can send email to a designated user when a specified event occurs. This class is a standard event consumer that WMI provides.
ms.assetid: ed10e6f7-8e18-4cde-bd46-a7791547c7da
ms.tgt_platform: multiple
title: Sending Email Based on an Event
ms.topic: article
ms.date: 05/31/2018
---

# Sending Email Based on an Event

By using the [SMTPEventConsumer](smtpeventconsumer.md) class, you can send email to a designated user when a specified event occurs. This class is a [standard event consumer](standard-consumer-classes.md) that WMI provides.

The [SMTPEventConsumer](smtpeventconsumer.md) class requires the following conditions to send an email message in response to an event:

-   The [SMTPEventConsumer](smtpeventconsumer.md) class must be compiled into the correct namespace. For more information, see [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md).
-   An SMTP server must exist on the network.
-   The email message cannot have an attachment.
-   The email message must be encoded in US-ASCII.

The basic procedure for using standard consumers is always the same, and is located in [Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md). The following procedure adds to the basic procedure; is specific to the [SMTPEventConsumer](smtpeventconsumer.md) class; and describes how to create an event consumer that sends email.

The following procedure describes how to create an event consumer that sends email.

**To create an event consumer that sends email**

1.  Install and register the [SMTPEventConsumer](smtpeventconsumer.md) class, if necessary.

    The [SMTPEventConsumer](smtpeventconsumer.md) class is compiled into the root\\subscription namespace by the WMI setup program.

2.  Identify the event that you want to monitor and create the event query.

    There might be an existing intrinsic event that use to monitor your event. Most intrinsic events are associated with changes to class instances in the "root\\cimv2" namespace. By analyzing the classes in the [WMI Classes](wmi-classes.md) reference, you can probably find a class that identifies the event you want to monitor. For example, use the [**Win32\_LogicalDisk**](/windows/desktop/CIMWin32Prov/win32-logicaldisk) class to monitor changes to a hard disk drive.

    If there are no existing intrinsic events that use, there might be an extrinsic event provider that can work. For example, use the [**RegistryTreeChangeEvent**](/previous-versions/windows/desktop/regprov/registrytreechangeevent) class of the Registry provider to monitor changes to the system registry.

    If a class does not exist that identifies the event you want to monitor, you must create your own event provider and define new extrinsic event classes. For more information, see [Writing an Event Provider](writing-an-event-provider.md).

3.  In the Managed Object Format (MOF) file, create an instance of the [SMTPEventConsumer](smtpeventconsumer.md) to receive events.

    Use the properties of the instance to define the email message to send when an event occurs. For example, the **ToLine** property defines the email address, and the **Message** property defines the text of the email message. You must define the email address, subject, and text of a message, but an email message cannot have an attachment. For more information, see [Designing Managed Object Format (MOF) Classes](designing-managed-object-format--mof--classes.md).

4.  Create an event query that specifies the events you want to monitor.

    For more information, see [Querying with WQL](querying-with-wql.md).

5.  Create an instance of [**\_\_EventFilter**](--eventfilter.md) and store your query in the **Query** property.

    For more information see, [Querying with WQL](querying-with-wql.md).

6.  Create an instance of [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) to associate the filter and the consumer.
7.  Compile the MOF file by using [**Mofcomp.exe**](mofcomp.md).


## Example

The example in this section is in MOF code, but you can create the instances programmatically by using the [Scripting API for WMI](scripting-api-for-wmi.md) or the [COM API for WMI](com-api-for-wmi.md).

The following procedure describes how to use the example.

**To use the example**

1.  Copy the following MOF to a text file and save it with a .mof extension.
2.  In a command prompt window, compile the MOF file by using the following command:

    **Mofcomp** *filename***.mof**

> [!Note]  
> When MOF code is compiled into the root\\subscription namespace, the [SMTPEventConsumer](smtpeventconsumer.md) is compiled into the same namespace.

 

``` syntax
#pragma namespace ("\\\\.\\root\\subscription")

instance of __EventFilter as $FILTER
{
    Name = "LowDiskspaceFilter";
    
    EventNamespace = "\\\\.\\root\\cimv2";  

    Query = "SELECT * FROM __InstanceModificationEvent WITHIN 10 "
            "WHERE TargetInstance ISA \"Win32_LogicalDisk\" "
            "AND TargetInstance.FreeSpace < 846000000 "
            "AND PreviousInstance.FreeSpace >= 846000000 "
            "AND (TargetInstance.DeviceID = \"C:\" "
            "OR TargetInstance.DeviceID = \"D:\")";
    QueryLanguage = "WQL";
};


instance of SMTPEventConsumer as $CONSUMER
{
    Name = "LowDisk";
    ToLine = "SysAd@MyCompany.com, MyAlias@MyCompany.com";
    CcLine = "MyHome@MyISP.com";
    ReplyToLine = "MyAlias@MyCompany.com";
    SMTPServer = "SmartHost";
    Subject = "WARNING: Low disk space";
    Message = "WARNING: Your %TargetInstance.DeviceID% is"
        " getting dangerously low.";
};

instance of __FilterToConsumerBinding
{
    Consumer = $CONSUMER ;
    Filter = $FILTER ;
};
```

## Related topics

<dl> <dt>

[Monitoring and Responding to Events with Standard Consumers](monitoring-and-responding-to-events-with-standard-consumers.md)
</dt> </dl>

 

 
