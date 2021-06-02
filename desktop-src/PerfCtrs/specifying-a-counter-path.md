---
description: The system uses counters to collect performance data.
ms.assetid: d1f1a90c-425a-4606-b86d-2948305ea84a
title: Specifying a Counter Path
ms.topic: article
ms.date: 05/31/2018
---

# Specifying a Counter Path

The system uses counters to collect performance data. Each counter is uniquely identified through its name and its path, or location. The syntax of a counter path is:

``` syntax
\\Computer\PerfObject(ParentInstance/ObjectInstance#InstanceIndex)\Counter
```

The Computer element specifies the name or IP address of the computer from which you want to query performance data. The computer name is optional if the counter is located on the local computer.

The PerfObject element specifies the performance object to query. A performance object can be a physical component, such as processors, disks, and memory, or a system object, such as processes and threads. Each system object is related to a functional element within the computer and has a set of standard counters assigned to it. Each computer may have a different set of performance objects and counters installed on it because applications can install their own performance objects and counters. For a list of the performance objects and counters installed on your computer, see the **Add Counters** dialog box in the Performance tool on your computer. These objects are also listed in the PDH browse dialog box (see [Browsing Counters](browsing-counters.md)). For a list of system performance objects and counters, see [Counters by Object](/previous-versions/windows/it-pro/windows-server-2003/cc783073(v=ws.10)).

The ParentInstance, ObjectInstance, and InstanceIndex are included in the path if multiple instances of the object can exist. For example, processes and threads are multiple instance objects because more than one process or thread can run at the same time. If an object can have more than one instance, the counter path must specify an object instance.

The format of the instance related elements depends on the object type. If the object has simple instances, then the format is only the instance name enclosed in parentheses. For example:

``` syntax
(Explorer)
```

If the instance of this object also requires a parent instance name, the parent instance name must come before the object instance and be separated by a forward slash character. For example, threads belong to processes. If you query a thread object, you must also specify the process to which it belongs as shown in the following example:

``` syntax
(Explorer/0)
```

If the object has multiple instances that have the same name string, they can be indexed sequentially by specifying the instance index prefixed by a pound sign. Instance indexes are 0-based. If you want to query the first instance, do not include \#0—just specify the instance name. To specify the second instance, use \#1; to specify the third instance, use \#2; and so on. For example:

``` syntax
(Explorer/0#1)
```

The Counter element specifies the performance counter that you want to query for the given the performance object.

PDH uses the following special characters in a counter path. Providers should not use these characters in their names. If a provider uses these special characters, PDH cannot parse the full counter path to obtain the counter and instances names.



| Character | Description                                                |
|-----------|------------------------------------------------------------|
| \\        | Generic separator for computer, object, and counter.       |
| (         | Beginning of instance name.                                |
| )         | Ending of instance name.                                   |
| /         | Separates instance and parent instance.                    |
| \#n       | Identifies a specific occurrence of a same-named instance. |
| \*        | Wildcard character.                                        |



 

The following examples show the possible formats for counter paths:

-   \\\\computer\\object(parent/instance\#index)\\counter
-   \\\\computer\\object(parent/instance)\\counter
-   \\\\computer\\object(instance\#index)\\counter
-   \\\\computer\\object(instance)\\counter
-   \\\\computer\\object\\counter
-   \\object(parent/instance\#index)\\counter
-   \\object(parent/instance)\\counter
-   \\object(instance\#index)\\counter
-   \\object(instance)\\counter
-   \\object\\counter

## Using wildcard characters

Counter paths may contain a wildcard character only for the instance name as shown in the following example.

``` syntax
\Process(*)\% Processor Time
```

To expand the wildcard into a list of counter paths that contain instances found on the computer or in the log file, call [**PdhExpandWildCardPath**](/windows/desktop/api/Pdh/nf-pdh-pdhexpandwildcardpatha).

 

 
