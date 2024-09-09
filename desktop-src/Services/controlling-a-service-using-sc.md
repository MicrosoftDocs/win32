---
description: The Windows SDK contains a command-line utility, Sc.exe, that can be used to control a service. Its commands correspond to the functions provided by the SCM. The syntax is as follows.
ms.assetid: 7c3e5c39-ec0f-4174-9ecf-239927de3d39
title: Controlling a Service Using SC
ms.topic: article
ms.date: 05/31/2018
---

# Controlling a Service Using SC

The Windows SDK contains a command-line utility, Sc.exe, that can be used to control a service. Its commands correspond to the functions provided by the SCM. The syntax is as follows.

## Syntax

```
sc.exe [<servername>] [<command>] [<servicename>] [<option1>] [<option2>] ...
```

To see the available commands, type:

```
sc
```

To see the syntax for a specific command, include a command. Here's an example:

```
sc start
```

## Parameters

|Parameter|Description|
|---------|-----------|
| `<servername>` | Specifies the name of the remote server on which the service is located. The name must use the Universal Naming Convention (UNC) format (for example, \\myserver). To run SC.exe locally, don't use this parameter. |
| `<command>` | One of the following commands: <dl> <dd>continue</dd> <dd>control</dd> <dd>interrogate</dd> <dd>pause</dd> <dd>start</dd> <dd>stop</dd> </dl> |
| `<servicename>` | The name of the service, as specified when it was installed. |
| `<option1>` | An optional parameter. |
| `<option2>` | An optional parameter. |

## Related topics

* [Service control requests](service-control-requests.md)
* [Service startup](service-startup.md)
