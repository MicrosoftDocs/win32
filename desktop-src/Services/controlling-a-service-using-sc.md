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

**sc** \[*ServerName*\] *Command* \[*ServiceName*\]\[*option1*\]\[*option2*\]...

<dl> <dt>

<span id="ServerName"></span><span id="servername"></span><span id="SERVERNAME"></span>*ServerName*
</dt> <dd>

Optional server name. Use the form \\\\*ServerName*.

</dd> <dt>

<span id="Command"></span><span id="command"></span><span id="COMMAND"></span>*Command*
</dt> <dd>

One of the following commands:

<dl> <dd>continue</dd> <dd>control</dd> <dd>interrogate</dd> <dd>pause</dd> <dd>start</dd> <dd>stop</dd> </dl> </dd> <dt>

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

[Service Control Requests](service-control-requests.md)
</dt> <dt>

[Service Startup](service-startup.md)
</dt> </dl>

 

 



