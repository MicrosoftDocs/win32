---
description: The Windows SDK contains a command-line utility, Sc.exe, that can be used to query or modify the database of installed services. Its commands correspond to the functions provided by the SCM. The syntax is as follows.
ms.assetid: d304922c-86fb-4c62-9bfa-c827df4aecd8
title: Configuring a Service Using SC
ms.topic: article
ms.date: 05/31/2018
---

# Configuring a Service Using SC

The Windows SDK contains a command-line utility, Sc.exe, that can be used to query or modify the database of installed services. Its commands correspond to the functions provided by the SCM. The syntax is as follows.

## Syntax

```
sc.exe [<servername>] [<command>] [<servicename>] [<option1>] [<option2>] ...
```

To see the available commands, type:

```
sc
```

To see the syntax for a specific command, include a command, e.g. 

```
sc pause
```

## Parameters


|Parameter|Description|
|---------|-----------|
| `<servername>` | Specifies the name of the remote server on which the service is located. The name must use the Universal Naming Convention (UNC) format (for example, \\myserver). To run SC.exe locally, don't use this parameter. |
| `<command>` | One of the following commands: <dl> <dd>boot</dd> <dd>config</dd> <dd>create</dd> <dd>delete</dd> <dd>description</dd> <dd>EnumDepend</dd> <dd>failure</dd> <dd>failureflag</dd> <dd>GetDisplayName</dd> <dd>GetKeyName</dd> <dd>Lock</dd> <dd>qc</dd> <dd>qdescription</dd> <dd>qfailure</dd> <dd>qfailureflag</dd> <dd>qprivs</dd> <dd>qsidtype</dd> <dd>query</dd> <dd>queryex</dd> <dd>privs</dd> <dd>QueryLock</dd> <dd>sdset</dd> <dd>sdshow</dd> <dd>showsid</dd> <dd>sidtype</dd> </dl> |
| `<servicename>` | The name of the service, as specified when it was installed. |
| `<option1>` | An optional parameter. |
| `<option2>` | An optional parameter. |

## Related topics

<dl> <dt>

[Service Configuration](service-configuration.md)
</dt> <dt>

[Service Installation, Removal, and Enumeration](service-installation-removal-and-enumeration.md)
</dt> </dl>
