---
title: Scripting Entry Points
description: A control script consists of a set of entry point functions (for example, IsAlive) for the Generic Script resource DLL.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4793f054-acbb-4f6c-bb30-d00a0082dbc8'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["entry point functions Failover Cluster , scripting"]
---

# Scripting Entry Points

A control script consists of a set of entry point functions (for example, [**IsAlive**](isalive.md)) for the Generic Script resource DLL. The Resource Monitor calls these scripted entry point functions during cluster operation. Except for the [**Open**](open.md) function, the scripted entry point functions serve the same purpose as the same-named resource DLL entry point functions implemented using the Failover Cluster API. For more information, see [Implementing Resource DLLs](implementing-resource-dlls.md).

A control script must implement the [**LooksAlive**](looksalive.md) and [**IsAlive**](isalive.md) functions and can also implement the functions [**Open**](open.md), [**Online**](online.md), [**Offline**](offline.md), [**Close**](close.md), and [**Terminate**](terminate.md).

> [!Note]  
> You should not store control script files on cluster disks. Although these drives may seem to be the ideal location because all nodes in the [*cluster*](c-gly.md#-wolf-cluster-gly) can access them, storing control script files there causes problems when you upgrade either the Cluster service or the application software, especially if the cluster is in a production environment. Such upgrades require the cluster to be shut down completely. If you choose instead to install control script files on all nodes in the cluster, you can use a rolling upgrade approach—upgrading each node individually—without affecting the operation of the cluster.

 

### Script Execution

A Resource Monitor call to either of the time-critical entry point functions [**LooksAlive**](looksalive.md) or [**IsAlive**](isalive.md) executes directly, without calling other entry point functions and without loading or unloading the script. A Resource Monitor call to any other entry point function (for example, [**Online**](online.md)) generates associated Resource Monitor entry point function calls (for example, to [**Open**](open.md)) and may cause the script to load or unload. For more information on the Resource Monitor actions for each entry point function call, see the following table.

In a control script, code within the script body, outside any of the entry point functions, is executed when the script is loaded. Code within an entry point function is executed whenever that function is called. For example, code within the [**Open**](open.md) function is executed not only when the script is opened, but also when **Open** is called prior to [**Online**](online.md) or [**Close**](close.md).



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Function name</th>
<th>Resource monitor actions</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>[<strong>Open</strong>](open.md)</td>
<td>Perform when the script is opened. Resource Monitor will:<br/>
<ul>
<li>load the script</li>
<li>call [<strong>Open</strong>](open.md)</li>
<li>call [<strong>Close</strong>](close.md)</li>
<li>unload the script</li>
</ul></td>
</tr>
<tr class="even">
<td>[<strong>Online</strong>](online.md)</td>
<td>Perform when the resource is placed online. Resource Monitor will:<br/>
<ul>
<li>load the script</li>
<li>call [<strong>Open</strong>](open.md)</li>
<li>call [<strong>Online</strong>](online.md)</li>
</ul></td>
</tr>
<tr class="odd">
<td>[<strong>LooksAlive</strong>](looksalive.md)</td>
<td>Perform one or more very fast, cursory checks of the specified instance with the emphasis on detecting potential problems rather than verifying operational status. [<strong>IsAlive</strong>](isalive.md) will determine whether the instance is really operational. Take no more than 300 milliseconds to return a value. Resource Monitor calls [<strong>LooksAlive</strong>](looksalive.md) repeatedly at a specified time interval (for example, once every five seconds).</td>
</tr>
<tr class="even">
<td>[<strong>IsAlive</strong>](isalive.md)</td>
<td>Perform a complete check of the resource to see if it is functioning properly. The set of procedures you need to use depends on your resource. For example, a database resource should check to see that the database can write to the disk and perform queries and updates to the disk. If the resource has definitely failed, return <strong>FALSE</strong>. The Resource Monitor immediately sets the status of the resource to &quot;ClusterResourceFailed&quot; and calls the [<strong>Terminate</strong>](terminate.md) entry point function. Resource Monitor calls [<strong>IsAlive</strong>](isalive.md) repeatedly at a specified time interval (for example, once every sixty seconds).</td>
</tr>
<tr class="odd">
<td>[<strong>Offline</strong>](offline.md)</td>
<td>Perform when the resource is placed offline. Resource Monitor will:<br/>
<ul>
<li>call [<strong>Offline</strong>](offline.md)</li>
<li>call [<strong>Close</strong>](close.md)</li>
<li>unload the script</li>
</ul></td>
</tr>
<tr class="even">
<td>[<strong>Close</strong>](close.md)</td>
<td>Perform when the script is closed. Resource Monitor will:<br/>
<ul>
<li>load the script</li>
<li>call [<strong>Open</strong>](open.md)</li>
<li>call [<strong>Close</strong>](close.md)</li>
<li>unload the script</li>
</ul></td>
</tr>
<tr class="odd">
<td>[<strong>Terminate</strong>](terminate.md)</td>
<td>Perform when terminating the script. Resource Monitor will:<br/>
<ul>
<li>load the script (if not already loaded)</li>
<li>call [<strong>Open</strong>](open.md)</li>
<li>call [<strong>Terminate</strong>](terminate.md)</li>
<li>call [<strong>Close</strong>](close.md)</li>
<li>unload the script</li>
</ul></td>
</tr>
</tbody>
</table>



 

### Parameters and Return Values

Parameters are not passed in a call to an entry point function in a script.

An entry point function can optionally set a return value. A return value of zero (or "true") indicates success and does not appear in the cluster log. The functions [**LooksAlive**](looksalive.md) and [**IsAlive**](isalive.md) should return the Boolean "true" rather than a numeric zero. Success is assumed if the return value is not set explicitly in the function.

A nonzero return value (or false) indicates failure and appears in the cluster log.

## Accessing Resources

The Generic Script resource DLL creates a [**Resource**](resource-object.md) object for each scripted resource instance. The **Resource** object enables a control script to log information, manipulate properties, and access the resource name. For more information, see **Resource Object**.

> [!Note]  
> To avoid deadlocks, do not use the [Cluster Automation Server](https://msdn.microsoft.com/library/aa372940), the [Failover Cluster WMI Provider](https://msdn.microsoft.com/library/aa372876), or otherwise make any calls to the [Cluster API](cluster-api.md) from your control script. All interaction with the [*cluster*](c-gly.md#-wolf-cluster-gly) should be done through the [**Resource**](resource-object.md) object.

 

## Instance Management

For each instance of a scripted resource, the Generic Script resource DLL runs an instance of a control script in a separate thread. Thus there is no need to implement instance management in a control script; as far as a control script is concerned, there is one and only one resource instance.

## Control Script Layout

The following example illustrates the layout of a control script in VBScript that implements all the supported entry point functions. For executable script resource examples, see [Scripted Resource Example](scripted-resource-example.md).


```VB
'   ... Insert your script-level global variables and definitions here
'   ... e.g. Resource.LogInformation("ScriptWide Global Stuff is Run")
'   ... Code placed here is outside any entry point function.
'   ... It is run once when the script is created
'   ... and once when the script is placed online.

Function Open( )
'   ... Insert your Open code here.
End Function

Function Online( )
'   ... Insert your Online code here.
'   ... Online is executed once when the resource is placed online.
End Function

Function LooksAlive( )
'   ... Insert your LooksAlive code here.
'   ... LooksALive is executed at specified intervals.
End Function

Function IsAlive( )
'   ... Insert your IsAlive code here.
'   ... IsAlive is executed at specified intervals
'   ... or when a LooksAlive call fails.
End Function

Function Offline( )
'   ... Insert your Offline code here.
'   ... Offline is executed once when the resource is placed offline.
End Function

Function Close( )
'   ... Insert your Close code here.
End Function

Function Terminate( )
'   ... Insert your Terminate code here.
'   ... Terminate is executed once when the script terminates.
End Function
```



## Related topics

<dl> <dt>

[Using the Generic Script Resource Type](using-the-generic-script-resource-type.md)
</dt> </dl>

 

 





