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

**sc** \[*ServerName*\] *Command* \[*ServiceName*\]\[*option1*\]\[*option2*\]...

<dl> <dt>

<span id="ServerName"></span><span id="servername"></span><span id="SERVERNAME"></span>*ServerName*
</dt> <dd>

Optional server name. Use the form \\\\*ServerName*.

</dd> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>*Command*
</dt> <dd>

One of the following commands:

<dl> <dd>boot</dd> <dd>config</dd> <dd>create</dd> <dd>delete</dd> <dd>description</dd> <dd>EnumDepend</dd> <dd>failure</dd> <dd>failureflag</dd> <dd>GetDisplayName</dd> <dd>GetKeyName</dd> <dd>Lock</dd> <dd>qc</dd> <dd>qdescription</dd> <dd>qfailure</dd> <dd>qfailureflag</dd> <dd>qprivs</dd> <dd>qsidtype</dd> <dd>query</dd> <dd>queryex</dd> <dd>privs</dd> <dd>QueryLock</dd> <dd>sdset</dd> <dd>sdshow</dd> <dd>showsid</dd> <dd>sidtype</dd> </dl> </dd> <dt>

<span id="ServiceName"></span><span id="servicename"></span><span id="SERVICENAME"></span>*ServiceName*
</dt> <dd>

The name of the service, as specified when it was installed.

</dd> <dt>

<span id="option1"></span><span id="OPTION1"></span>*option1*
</dt> <dd>

An optional parameter.

</dd> <dt>

<span id="option2"></span><span id="OPTION2"></span>*option2*
</dt> <dd>

An optional parameter.

</dd> </dl>

## Remarks

To see complete syntax for a command, use the following command:

**sc** *Command*

## Related topics

<dl> <dt>

[Service Configuration](service-configuration.md)
</dt> <dt>

[Service Installation, Removal, and Enumeration](service-installation-removal-and-enumeration.md)
</dt> </dl>

 

 



