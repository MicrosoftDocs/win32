---
description: The WMI Query Language (WQL) is a subset of standard American National Standards Institute Structured Query Language (ANSI SQL) with minor semantic changes to support WMI.
ms.assetid: 7e04ba37-c0e0-4304-b162-8b911f233f38
ms.tgt_platform: multiple
title: Querying with WQL
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Querying with WQL

The WMI Query Language (WQL) is a subset of standard American National Standards Institute Structured Query Language (ANSI SQL) with minor semantic changes to support WMI.

For a complete list of supported WQL keywords, see [WQL (SQL for WMI)](wql-sql-for-wmi.md). Using SQL keywords for object or property names may restrict a query from being parsed. The following SQL keywords are restricted: **NULL**, **TRUE**, and **FALSE**.

> [!Note]  
> There are limits to the number of AND and OR keywords that can be used in WQL queries. Large numbers of WQL keywords used in a complex query can cause WMI to return the **WBEM\_E\_QUOTA\_VIOLATION** error code as an **HRESULT** value. The limit of WQL keywords depends on how complex the query is.

 

Queries can use the **WHERE** clause for extension and customization, although it is not required. The **WHERE** clause is made up of a property or keyword, an operator, and a constant. All **WHERE** clauses must specify one of the predefined operators that are included in WQL. For more information about syntax, see [WHERE Clause](where-clause.md). For more information about valid WQL operators, see [WQL Operators](wql-operators.md).

As with other SQL query strings, you can escape your queries.

> [!Note]  
> WQL does not support cross-namespace queries or associations. You cannot query for all instances of a specified class residing in all of the namespaces on the target computer.

 

WQL supports the following types of queries:

-   Data queries

    Data queries are used to retrieve class instances and data associations. They are the most commonly used type of query in WMI scripts and applications. For more information about the syntax of data queries, see [Requesting Class Instance Data](requesting-class-instance-data.md). For more information about associations, see [Declaring an Association Class](declaring-an-association-class.md).

    > [!Note]  
    > WQL does not support queries of array datatypes.

     

    The following data query example requests the event log file named "Application" from all instances of [**Win32\_NTLogEvent**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogevent).

    ```VB
    strComputer = "." 
    Set objWMIService = GetObject("winmgmts:\\" _
        & strComputer & "\root\CIMV2") 
    Set colItems = objWMIService.ExecQuery( _
        "SELECT * FROM Win32_NTLogEvent " _
        & "WHERE Logfile = 'Application'",,48)
    ```

    

-   Event queries

    Consumers use event queries to register to receive notification of events. Event providers use event queries to register to support one or more events. For more information about event queries, see [Receiving Event Notifications](receiving-event-notifications.md).

    The following example event query by a temporary event consumer requests notification when a new instance of a class derived from [**Win32\_NTLogEvent**](/previous-versions/windows/desktop/eventlogprov/win32-ntlogevent) is created.

    ```VB
    strComputer = "." 
    Set objWMIService = GetObject("winmgmts:\\" _
        & strComputer & "\root\CIMV2") 
    Set objEvents = objWMIService.ExecNotificationQuery _
    ("SELECT * FROM __InstanceModificationEvent WITHIN 10 WHERE " & _
        "TargetInstance ISA 'Win32_Service'" & _
        " AND TargetInstance._Class = 'win32_TerminalService'")

    i = TRUE
    Do While i = TRUE
        Set strReceivedEvent = objEvents.NextEvent

        'report an event
        Wscript.Echo "An event has occurred."
    Loop
    ```

    

-   Schema queries

    Schema queries are used to retrieve class definitions (rather than class instances) and schema associations. Class providers use schema queries to specify the classes that they support when they register. For more information about schema queries, see [Retrieving Class Definitions](retrieving-class-definitions.md).

    The following example schema query shows the special syntax.

    ```sql
    SELECT * FROM meta_class WHERE __this ISA "Win32_BaseService"
    ```

    

## Related topics

<dl> <dt>

[WMI Date and Time Format](date-and-time-format.md)
</dt> </dl>

 

 
