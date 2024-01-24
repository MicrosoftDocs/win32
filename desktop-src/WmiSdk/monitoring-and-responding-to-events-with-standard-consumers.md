---
description: You can use the installed standard consumer classes to perform actions based on events in an operating system.
ms.assetid: 1979dc55-a440-4c31-832b-36fa84def4c9
ms.tgt_platform: multiple
title: Monitoring and Responding to Events with Standard Consumers
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Monitoring and Responding to Events with Standard Consumers

You can use the installed [standard consumer classes](standard-consumer-classes.md) to perform actions based on events in an operating system. Standard consumers are simple classes that are already registered, and they define permanent consumer classes. Each standard consumer takes a specific action after it receives an event notification. For example, you can define an instance of [**ActiveScriptEventConsumer**](activescripteventconsumer.md) to execute a script when free disk space on a computer is different from a specified size.

WMI compiles the standard consumers into default namespaces that depend on the operating system, for example:

-   In Windows Server 2003, all of the standard consumers are compiled by default into the "Root\\Subscription" namespace.

> [!Note]  
> For the default namespaces and operating systems that are specific for each WMI class, see the Remarks and Requirements sections of each class topic.

 

The following table lists and describes the WMI standard consumers.



| Standard consumer                                              | Description                                                                                                                                                                                                                                                                                                                                                                                                             |
|----------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ActiveScriptEventConsumer**](activescripteventconsumer.md) | Executes a script when it receives an event notification. For more information, see [Running a Script Based on an Event](running-a-script-based-on-an-event.md).                                                                                                                                                                                                                                                       |
| [**LogFileEventConsumer**](logfileeventconsumer.md)           | Writes customized strings to a text log file when it receives an event notification. For more information, see [Writing to a Log File Based on an Event](writing-to-a-log-file-based-on-an-event.md).                                                                                                                                                                                                                  |
| [**NTEventLogEventConsumer**](nteventlogeventconsumer.md)     | Logs a specific message to the Application event log. For more information, see [Logging to NT Event Log Based on an Event](logging-to-nt-event-log-based-on-an-event.md).                                                                                                                                                                                                                                             |
| [**SMTPEventConsumer**](smtpeventconsumer.md)                 | Sends an email message by using SMTP each time an event is delivered to it. For more information, see [Sending Email Based on an Event](sending-e-mail-based-on-an-event.md).                                                                                                                                                                                                                                          |
| [**CommandLineEventConsumer**](commandlineeventconsumer.md)   | Launches a process when an event is delivered to a local system. The executable file must be in a secure location, or secured with a strong access control list (ACL) to prevent an unauthorized user from replacing your executable with a different executable. For more information, see [Running a Program from the Command Line Based on an Event](running-a-program-from-the-command-line-based-on-an-event.md). |



 

The following procedure describes how to monitor and respond to events by using a standard consumer. Note that the procedure is the same for a Managed Object Format (MOF) file, script, or application.

**To monitor and respond to events with a standard consumer**

1.  Specify the namespace in a MOF file by using the MOF preprocessor command [\#pragma namespace](pragma-namespace.md). In a script or application, specify the namespace in the code that connects to WMI.

    The following MOF code example shows how to specify the root\\subscription namespace.

    ```syntax
    #pragma namespace ("\\\\.\\root\\subscription")
    ```

    Most [*intrinsic events*](gloss-i.md) are associated with changes to class instances in the root\\cimv2 namespace. However, registry events such as [**RegistryKeyChangeEvent**](/previous-versions/windows/desktop/regprov/registrykeychangeevent) are fired in the root\\default namespace by the [System Registry Provider](/previous-versions/windows/desktop/regprov/system-registry-provider).

    A consumer can include event classes located in other namespaces by specifying the namespace in the **EventNamespace** property in the [**\_\_EventFilter**](--eventfilter.md) query for events. The [*intrinsic events*](gloss-i.md) classes, such as [**\_\_InstanceOperationEvent**](--instanceoperationevent.md) are available in every namespace.

2.  Create and populate an instance of a standard consumer class.

    This instance may have a unique value in the **Name** property. You can update an existing consumer by reusing the same name.

    **InsertionStringTemplates** contains the text to insert in an event that you specify in **EventType**. You can use literal strings or refer directly to a property. For more information, see [Using Standard String Templates](using-standard-string-templates.md) and [SELECT Statement for Event Queries](select-statement-for-event-queries.md).

    Use an existing source for the event log that supports an insertion string without associated text.

    The following MOF code example shows how to use an existing source of WSH and an **EventID** value of 8.

    ```syntax
    instance of NTEventLogEventConsumer as $Consumer
    {
        Name = "RunKeyEventlogConsumer";
        SourceName = "WSH";               
        EventID = 8;
        // Warning                              
        EventType = 2;
        // One string supplies the entire message          
        NumberOfInsertionStrings = 1;             
        // the %Hive% and %KeyPath% are properties of
        // the RegistryKeyChangeEvent instance 
        InsertionStringTemplates = 
            {"The key %Hive%\\%RootPath% has been modified."
            "Check if the change is intentional"};
    };
    ```

3.  Create an instance of [**\_\_EventFilter**](--eventfilter.md) and define a query for events.

    In the following example, the filter monitors the registry key where startup programs are registered. Monitoring this registry key may be important because an unauthorized program can register itself under the key, which causes it to be launched when the computer boots.

    ```syntax
    instance of __EventFilter as $Filter
    {
    Name = "RunKeyFilter";
    QueryLanguage = "WQL"; 
    Query = "Select * from RegistryTreeChangeEvent"
        " where (Hive = \"HKEY_LOCAL_MACHINE\" and "
        "RootPath = \"Software\\\\Microsoft\\\\Windows"
        "\\\\CurrentVersion\\\\Run\")";

    // RegistryTreeChangeEvents only fire in root\default namespace
    EventNamespace = "root\\default";                       
    };
    ```

4.  Identify an event to monitor and create an event query.

    You can check to see if there is an intrinsic or extrinsic event that use. For example, use the [**RegistryTreeChangeEvent**](/previous-versions/windows/desktop/regprov/registrytreechangeevent) class of the Registry provider to monitor changes to the system registry.

    If a class does not exist that describes an event you need to monitor, you must create your own event provider, and define new extrinsic event classes. For more information, see [Writing an Event Provider](writing-an-event-provider.md).

    In a MOF file, you can define an [*alias*](gloss-a.md) for the filter and consumer, which provides an easy way to describe the instance paths.

    The following example shows how to define an [*alias*](gloss-a.md) for the filter and consumer.

    ```syntax
    instance of __EventFilter as $FILTER
    instance of LogFileEventConsumer as $CONSUMER
    ```

5.  Create an instance of [**\_\_FilterToConsumerBinding**](--filtertoconsumerbinding.md) to associate the filter and the consumer classes. This instance determines that when an event occurs that matches the specified filter, the action specified by the consumer must occur. [**\_\_EventFilter**](--eventfilter.md), [**\_\_EventConsumer**](--eventconsumer.md), and **\_\_FilterToConsumerBinding** must have the same individual security identifier (SID) in the **CreatorSID** property. For more information, see [Binding an Event Filter with a Logical Consumer](binding-an-event-filter-with-a-logical-consumer.md).

    The following example shows how to identify an instance by the object path, or use an alias as a shorthand expression for the object path.

    ```syntax
    instance of __EventFilter as $FILTER
    instance of NTEventLogEventConsumer as $CONSUMER
    ```

    The following example binds the filter to the consumer by using aliases.

    ```syntax
    instance of __FilterToConsumerBinding
    {
        Filter = $FILTER;
        Consumer = $CONSUMER;
        
    };
    ```

    You can bind one filter to several consumers, which indicates that when matching events occur, several actions must be taken; or you can bind one consumer to several filters, which indicates that the action must be taken when events that match one of the filters occur.

    The following actions are taken based on the condition of consumers and events:

    -   If one of the permanent consumers fails, other consumers that request the event receive notification.
    -   If an event is dropped, WMI fires [**\_\_EventDroppedEvent**](--eventdroppedevent.md).
    -   If you subscribe to this event, it returns the event that is dropped, and a reference to the [**\_\_EventConsumer**](--eventconsumer.md) represents the failed consumer.
    -   If a consumer fails, WMI fires [**\_\_ConsumerFailureEvent**](--consumerfailureevent.md), which may contain more information in the **ErrorCode**, **ErrorDescription** and **ErrorObject** properties.

    For more information, see [Binding an Event Filter with a Logical Consumer](binding-an-event-filter-with-a-logical-consumer.md).

## Example

The following example shows the MOF for an instance of [**NTEventLogEventConsumer**](nteventlogeventconsumer.md). After you compile this MOF, any attempt to create, delete, or modify a value in the Registry path **HKEY\_LOCAL\_MACHINE\\ Software\\Microsoft\\Windows\\CurrentVersion\\Run** logs an entry in the Application eventlog, under the source "WSH".


```mof
#pragma namespace ("\\\\.\\root\\subscription")
 
instance of __EventFilter as $Filter
{
    Name = "RunKeyFilter";
    QueryLanguage = "WQL";
    Query = "Select * from RegistryTreeChangeEvent"
            " where (Hive = \"HKEY_LOCAL_MACHINE\" and "
            "KeyPath = \"Software\\\\Microsoft\\\\Windows"
            "\\\\CurrentVersion\\\\Run\")";

    // RegistryTreeChangeEvents only fire
    // in root\default namespace
    EventNamespace = "root\\default";   
};
 
instance of NTEventLogEventConsumer as $Consumer
{
    Name = "RunKeyEventlogConsumer";
    SourceName = "WSH";               
    EventID = 8;
    EventType = 2;                            // Warning
    Category = 0;
    NumberOfInsertionStrings = 1;

    // the %Hive% and %KeyPath% are properties
    // of the RegistryKeyChangeEvent instance 
    InsertionStringTemplates = {"The key %Hive%\\%RootPath% "
        "has been modified. Check if the change is intentional"};
};
 

// Bind the filter to the consumer
instance of __FilterToConsumerBinding
{
    Filter = $Filter;
    Consumer = $Consumer;
};
```



## Related topics

<dl> <dt>

[Receiving Events Securely](receiving-events-securely.md)
</dt> </dl>

 

 
