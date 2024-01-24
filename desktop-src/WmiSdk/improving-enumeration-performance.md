---
description: Enumerations tend to use a significant amount of system resources.
ms.assetid: 4163e6c2-4ee3-4906-b297-618509666c90
ms.tgt_platform: multiple
title: Improving Enumeration Performance
ms.topic: article
ms.date: 05/31/2018
---

# Improving Enumeration Performance

Enumerations tend to use a significant amount of system resources. Therefore, you should try to optimize the WMI enumeration process if you plan on performing enumerations on a large group. Scripts can also use a query to avoid performance degradation in "For each….Next" operations with a large set. For more information, see [Querying WMI](querying-wmi.md).

The following procedure describes how to improve enumeration performance.

**To improve enumeration performance**

1.  Set the *lFlags* parameter to allow semisynchronous return of the data with an enumerator that discards each item from WMI as it is delivered. For more information, see [Calling a Method](calling-a-method.md).

    The following C++ code example shows how to use the **WBEM\_FLAG\_RETURN\_IMMEDIATE** and **WBEM\_FLAG\_FORWARD\_ONLY** flags.

    `WBEM_FLAG_RETURN_IMMEDIATE | WBEM_FLAG_FORWARD_ONLY`

    In VBScript or Visual Basic, use the scripting flags **WbemFlagReturnImmediately** and **WbemFlagForwardOnly** from [WbemFlagEnum](/windows/desktop/api/Wbemdisp/ne-wbemdisp-wbemflagenum). The combined value of these flags is decimal 48.

    The scripting and parameter flags cause the following behavior:

    -   The **WBEM\_FLAG\_RETURN\_IMMEDIATE** or **wbemFlagReturnImmediately** flag requests semisynchronous behavior. The call to create the enumerator returns immediately. You can then begin to traverse the object set that you receive.
    -   The **WBEM\_FLAG\_FORWARD\_ONLY** flag or **wbemFlagForwardOnly** flag requests an enumerator that you cannot rewind. That is, WMI can release an object after you view the object.

    In situations where the enumeration is large and the application is very fast, using forward-only enumerators with semisynchronous processing allows WMI to hold on to far fewer objects, thereby increasing response time and memory performance significantly.

    The following VBScript code example shows how to make a call using the combined **wbemFlagReturnImmediately** and **wbemFlagForwardOnly** flags to obtain a collection of events from an event log.

    ```VB
    Set Events = GetObject("winmgmts:").ExecQuery _
         ("SELECT * FROM Win32_NTLogEvent " _
          & "WHERE Logfile = 'System'",,48)
    ```

    

2.  Whenever possible, avoid using [**CreateInstanceEnum**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createinstanceenum) in C++ or [**SWbemServices.InstancesOf**](swbemservices-instancesof.md), and instead use **ExecQuery**.

    The **ExecQuery** method queries WMI using database technologies, while [**CreateInstanceEnum**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-createinstanceenum) or [**SWbemServices.InstancesOf**](swbemservices-instancesof.md) enumerates WMI objects. Specifically, **ExecQuery** can request specific subsets of data that the enumerating methods cannot.

    Because some providers do not have querying capabilities, WMI provides a "post filter" feature that allows WMI to discard instances that do not fulfill a query's specifications. Whether a particular provider takes advantage of this feature is up to the provider author.

3.  Experiment with different queries to determine what gives you the best performance.

    For example, WMI seldom efficiently processes queries with **WHERE** clauses of the form Prop1 < "x". In contrast, WMI normally processes queries of the form KeyProp1 = "x" efficiently.

For more information, see [Enumerating WMI](enumerating-wmi.md).

 

 



