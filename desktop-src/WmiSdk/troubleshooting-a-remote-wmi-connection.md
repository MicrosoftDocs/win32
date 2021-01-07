---
description: The following sections describe common issues developers may have with creating a remote WMI connection.
ms.assetid: 328e420b-a859-4ce9-8a31-67150eb0a78f
ms.tgt_platform: multiple
title: Troubleshooting a Remote WMI Connection
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting a Remote WMI Connection

The following sections describe common issues developers may have with creating a remote WMI connection.

The following sections are discussed in this topic:

-   [DCOM Access Denied](#dcom-access-denied)
-   [Failure to Connect](#failure-to-connect)
-   [WMI Connection Timed Out](#wmi-connection-timed-out)
-   [Related topics](#related-topics)

## DCOM Access Denied

<dl> <dt>

<span id="Symptom"></span><span id="symptom"></span><span id="SYMPTOM"></span>Symptom
</dt> <dd>

your connection failed with the error "DCOM Access Denied", along with the decimal value -2147024891 or hex value0x80070005.

</dd> <dt>

<span id="Issue"></span><span id="issue"></span><span id="ISSUE"></span>Issue
</dt> <dd>

DCOM may not be configured to allow a WMI connection.

</dd> <dt>

<span id="Resolution"></span><span id="resolution"></span><span id="RESOLUTION"></span>Resolution
</dt> <dd>

You can configure DCOM settings for WMI using the DCOM Config utility (**DCOMCnfg.exe**) found in **Administrative Tools** in **Control Panel**. This utility exposes the settings that enable certain users to connect to the computer remotely through DCOM. Members of the Administrators group are allowed to remotely connect to the computer by default. With this utility you can set the security to start, access, and configure the WMI service.

For more information, see [Securing a Remote WMI Connection](securing-a-remote-wmi-connection.md).

</dd> </dl>

## Failure to Connect

<dl> <dt>

<span id="Symptom"></span><span id="symptom"></span><span id="SYMPTOM"></span>Symptom
</dt> <dd>

You cannot connect to WMI on a remote system.

</dd> <dt>

<span id="Issue"></span><span id="issue"></span><span id="ISSUE"></span>Issue
</dt> <dd>

You may be trying to connect to a system that does not support WMI. The following connections between operating system versions are not supported:

-   You cannot connect to a computer that is running a Starter, Basic, or Home edition.

Alternately, you may be trying to connect to a namespace which requires an encrypted connection, one that requires an authentication level of `pktPrivacy`, **WbemAuthenticationLevelPktPrivacy**, or **RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY**.

</dd> <dt>

<span id="Resolution"></span><span id="resolution"></span><span id="RESOLUTION"></span>Resolution
</dt> <dd>

For more information, see [Securing WMI Namespaces](securing-wmi-namespaces.md), [Securing C++ Clients and Providers](securing-c---clients-and-providers.md), or [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

</dd> </dl>

## WMI Connection Timed Out

<dl> <dt>

<span id="Symptom"></span><span id="symptom"></span><span id="SYMPTOM"></span>Symptom
</dt> <dd>

Your WMI connection times out.

</dd> <dt>

<span id="Issue"></span><span id="issue"></span><span id="ISSUE"></span>Issue
</dt> <dd>

Due to network lag issues, the computer is simply not able to respond in time.

</dd> <dt>

<span id="Resolution"></span><span id="resolution"></span><span id="RESOLUTION"></span>Resolution
</dt> <dd>

When connecting to WMI through a call to [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md) or [**IWbemLocator::ConnectServer**](/windows/desktop/api/Wbemcli/nf-wbemcli-iwbemlocator-connectserver), you can set the **wbemConnectFlagUseMaxWait** flag (scripting) or the **WBEM\_FLAG\_CONNECT\_USE\_MAX\_WAIT**in C++ value to 128 (0x80) to impose a two (2) minute time-out on the call.

</dd> </dl>

## Related topics

<dl> <dt>

[Connecting to WMI on a Remote Computer](connecting-to-wmi-on-a-remote-computer.md)
</dt> </dl>

 

 



