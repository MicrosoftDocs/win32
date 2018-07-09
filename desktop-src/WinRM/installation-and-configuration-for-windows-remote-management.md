---
title: Installation and Configuration for Windows Remote Management
description: If Windows Remote Management (WinRM) is not installed and configured, WinRM scripts do not run and the Winrm command-line tool cannot perform data operations.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 81c40456-0003-46d0-8695-83bf77432056
ms.prod: windows-server-dev
ms.technology: windows-remote-management
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
topic_type: 
- kbArticle
api_name: 
api_type: 
api_location: 
---

# Installation and Configuration for Windows Remote Management

If Windows Remote Management (WinRM) is not installed and configured, WinRM scripts do not run and the **Winrm** command-line tool cannot perform data operations. The [*Windows Remote Shell*](windows-remote-management-glossary.md) command-line tool, Winrs, [*event forwarding*](windows-remote-management-glossary.md), and Windows PowerShell 2.0 remoting also depend on WinRM configuration.

## Installing WinRM

WinRM is automatically installed with all currently-supported versions of the Windows operating system.

## Configuration of WinRM and IPMI

The following WinRM and [*Intelligent Platform Management Interface (IPMI)*](windows-remote-management-glossary.md) [WMI provider](https://msdn.microsoft.com/library/aa391402) components are installed with the operating system:

-   The WinRM service starts automatically on Windows Server 2008. On Windows Vista, the service must be started manually.
-   By default, no WinRM [*listener*](windows-remote-management-glossary.md) is configured. Even if the WinRM service is running, WS-Management protocol [*messages*](windows-remote-management-glossary.md) that request data cannot be received or sent.
-   Internet Connection Firewall (ICF) blocks access to ports.

Use the **Winrm** command to locate listeners and the addresses by typing the following command at a command prompt: **winrm e winrm/config/listener**. To check the state of configuration settings, type **winrm get winrm/config**.

## Quick Default Configuration

You can enable the WS-Management protocol on the local computer and set up the default configuration for remote management with the following command: **Winrm quickconfig**.

The **winrm quickconfig** command (or the abbreviated version **winrm qc**) performs the following operations:

-   Starts the WinRM service, and sets the service startup type to auto-start.
-   Configures a listener for the ports that send and receive WS-Management protocol [*messages*](windows-remote-management-glossary.md) using either HTTP or HTTPS on any IP address.
-   Defines ICF exceptions for the WinRM service, and opens the ports for HTTP and HTTPS.

**Note**  The **winrm quickconfig** command creates a firewall exception only for the current user profile. If the firewall profile is changed for any reason, **winrm quickconfig** should be run to enable the firewall exception for the new profile; otherwise, the exception might not be enabled.

To retrieve information about customizing a configuration, type **winrm help config** at a command prompt.

**To configure WinRM with default settings**

1.  Type the following command at a command prompt: **Winrm quickconfig**.

    If you are not running under the local computer Administrator account, you must either select **Run as Administrator** from the **Start** menu or use the **Runas** command at a command prompt.

2.  When the tool displays **Make these changes \[y/n\]?**, type **y**.

    If configuration is successful, the following output is displayed:

    ``` syntax
    WinRM has been updated for remote management.

    WinRM service type changed to delayed auto start.
    WinRM service started.
    Created a WinRM listener on HTTP://* to accept WS-Man requests to any IP on this
     machine.
    ```

3.  Keep the default settings for client and server components of WinRM, or customize them. For example, you might need to add certain remote computers to the client configuration TrustedHosts list.

    A trusted hosts list should be set up when mutual authentication cannot be established. Kerberos allows mutual authentication, but it cannot be used in workgroups, only domains. A best practice when setting up trusted hosts for a workgroup is to make the list should be as restricted as possible.

4.  Create an HTTPS listener by typing the following command: **winrm quickconfig -transport:https**. Be aware that you must open port 5986 for HTTPS transport to work.

## Listener and WS-Management protocol Default Settings

To get the listener configuration, type **winrm enumerate winrm/config/listener** at a command prompt. Listeners are defined by a transport (HTTP or HTTPS) and an IPv4 or IPv6 address.

**Winrm quickconfig** creates the following default settings for a listener. You can create more than one listener. For more information, type **winrm help config** at a command prompt.

<dl> <dt>

<span id="Address"></span><span id="address"></span><span id="ADDRESS"></span>Address
</dt> <dd>

Specifies the address for which this listener was created.

</dd> <dt>

<span id="Transport"></span><span id="transport"></span><span id="TRANSPORT"></span>Transport
</dt> <dd>

Specifies the transport to use to send and receive WS-Management protocol requests and responses. The value must be either HTTP or HTTPS. The default is HTTP.

</dd> <dt>

<span id="Port"></span><span id="port"></span><span id="PORT"></span>Port
</dt> <dd>

Specifies the TCP port for which this listener is created.

**WinRM 2.0:** The default HTTP port is 5985.

</dd> <dt>

<span id="Hostname"></span><span id="hostname"></span><span id="HOSTNAME"></span>Hostname
</dt> <dd>

Specifies the host name of the computer on which the WinRM service is running. The value must be a fully qualified domain name, an IPv4 or IPv6 literal string, or a wildcard character.

</dd> <dt>

<span id="Enabled"></span><span id="enabled"></span><span id="ENABLED"></span>Enabled
</dt> <dd>

Specifies whether the listener is enabled or disabled. The default is **True**.

</dd> <dt>

<span id="URLPrefix"></span><span id="urlprefix"></span><span id="URLPREFIX"></span>URLPrefix
</dt> <dd>

Specifies a URL prefix on which to accept HTTP or HTTPS requests. This is a string containing only the characters a-z, A-Z, 9-0, underscore (\_), and slash (/). The string must not start with or end with a slash (/). For example, if the computer name is SampleMachine, the WinRM client would specify http://SampleMachine/&lt;*URLPrefix*&gt; in the destination address. The default URL prefix is "wsman".

</dd> <dt>

<span id="CertificateThumbprint"></span><span id="certificatethumbprint"></span><span id="CERTIFICATETHUMBPRINT"></span>CertificateThumbprint
</dt> <dd>

Specifies the thumbprint of the service certificate. This value represents a string of two-digit hexadecimal values found in the Thumbprint field of the certificate. This string contains the SHA-1 hash of the certificate. Certificates are used in client certificate-based authentication. Certificates can be mapped only to local user accounts, and they do not work with domain accounts.

</dd> <dt>

<span id="ListeningOn"></span><span id="listeningon"></span><span id="LISTENINGON"></span>ListeningOn
</dt> <dd>

Specifies the IPv4 and IPv6 addresses that the listener uses. For example: "111.0.0.1, 111.222.333.444, ::1, 1000:2000:2c:3:c19:9ec8:a715:5e24, 3ffe:8311:ffff:f70f:0:5efe:111.222.333.444, fe80::5efe:111.222.333.444%8, fe80::c19:9ec8:a715:5e24%6".

</dd> </dl>

## Protocol Default Settings

Many of the configuration settings, such as MaxEnvelopeSizekb or SoapTraceEnabled, determine how the WinRM client and server components interact with the WS-Management protocol. The following list describes the available configuration settings.

<dl> <dt>

<span id="MaxEnvelopeSizekb"></span><span id="maxenvelopesizekb"></span><span id="MAXENVELOPESIZEKB"></span>MaxEnvelopeSizekb
</dt> <dd>

Specifies the maximum Simple Object Access Protocol (SOAP) data in kilobytes. The default is 150 kilobytes.

> [!Note]  
> The behavior is unsupported if MaxEnvelopeSizekb is set to a value greater than 1039440.

 

</dd> <dt>

<span id="MaxTimeoutms"></span><span id="maxtimeoutms"></span><span id="MAXTIMEOUTMS"></span>MaxTimeoutms
</dt> <dd>

Specifies the maximum time-out, in milliseconds, that can be used for any request other than Pull requests. The default is 60000.

</dd> <dt>

<span id="MaxBatchItems"></span><span id="maxbatchitems"></span><span id="MAXBATCHITEMS"></span>MaxBatchItems
</dt> <dd>

Specifies the maximum number of elements that can be used in a Pull response. The default is 32000.

</dd> <dt>

<span id="MaxProviderRequests"></span><span id="maxproviderrequests"></span><span id="MAXPROVIDERREQUESTS"></span>MaxProviderRequests
</dt> <dd>

Specifies the maximum number of concurrent requests that are allowed by the service. The default is 25.

**WinRM 2.0:** This setting is deprecated and set to read-only.

</dd> </dl>

## WinRM Client Default Configuration Settings

The client version of WinRM has the following default configuration settings.

<dl> <dt>

<span id="NetworkDelayms"></span><span id="networkdelayms"></span><span id="NETWORKDELAYMS"></span>NetworkDelayms
</dt> <dd>

Specifies the extra time in milliseconds that the client computer waits to accommodate for network delay time. The default is 5000 milliseconds.

</dd> <dt>

<span id="URLPrefix"></span><span id="urlprefix"></span><span id="URLPREFIX"></span>URLPrefix
</dt> <dd>

Specifies a URL prefix on which to accept HTTP or HTTPS requests. The default URL prefix is wsman.

</dd> <dt>

<span id="AllowUnencrypted"></span><span id="allowunencrypted"></span><span id="ALLOWUNENCRYPTED"></span>AllowUnencrypted
</dt> <dd>

Allows the client computer to request unencrypted traffic. By default, the client computer requires encrypted network traffic and this setting is **False**.

</dd> <dt>

<span id="Basic"></span><span id="basic"></span><span id="BASIC"></span>Basic
</dt> <dd>

Allows the client computer to use Basic authentication. Basic authentication is a scheme in which the user name and password are sent in clear text to the server or proxy. This method is the least secure method of authentication. The default is **True**.

</dd> <dt>

<span id="Digest"></span><span id="digest"></span><span id="DIGEST"></span>Digest
</dt> <dd>

Allows the client to use Digest authentication. Digest authentication is a challenge-response scheme that uses a server-specified data string for the challenge. Only the client computer can initiate a Digest authentication request. The client computer sends a request to the server to authenticate and receives a token string from the server. Then the client computer sends the resource request, including the user name and a cryptographic hash of the password combined with the token string. Digest authentication is supported for HTTP and for HTTPS. WinRM Shell client scripts and applications can specify Digest authentication, but the WinRM service does not accept Digest authentication. The default is **True**.

> [!Note]  
> Digest authentication over HTTP is not considered secure.

 

</dd> <dt>

<span id="Certificate"></span><span id="certificate"></span><span id="CERTIFICATE"></span>Certificate
</dt> <dd>

Allows the client to use client certificate-based authentication. Certificate-based authentication is a scheme in which the server authenticates a client identified by an X509 certificate. The default is **True**.

</dd> <dt>

<span id="Kerberos"></span><span id="kerberos"></span><span id="KERBEROS"></span>Kerberos
</dt> <dd>

Allows the client to use Kerberos authentication. Kerberos authentication is a scheme in which the client and server mutually authenticate by using Kerberos certificates. The default is **True**.

</dd> <dt>

<span id="Negotiate"></span><span id="negotiate"></span><span id="NEGOTIATE"></span>Negotiate
</dt> <dd>

Allows the client to use Negotiate authentication. Negotiate authentication is a scheme in which the client sends a request to the server to authenticate. The server determines whether to use the Kerberos protocol or NTLM. The Kerberos protocol is selected to authenticate a domain account, and NTLM is selected for local computer accounts. The user name must be specified in domain\\user\_name format for a domain user. The user name must be specified in "server\_name\\user\_name" format for a local user on a server computer. The default is **True**.

</dd> <dt>

<span id="CredSSP"></span><span id="credssp"></span><span id="CREDSSP"></span>CredSSP
</dt> <dd>

Allows the client to use Credential Security Support Provider (CredSSP) authentication. CredSSP enables an application to delegate the user's credentials from the client computer to the target server. The default is **False**.

</dd> <dt>

<span id="DefaultPorts"></span><span id="defaultports"></span><span id="DEFAULTPORTS"></span>DefaultPorts
</dt> <dd>

Specifies the ports that the client will use for either HTTP or HTTPS.

**WinRM 2.0:** The default HTTP port is 5985, and the default HTTPS port is 5986.

</dd> <dt>

<span id="TrustedHosts"></span><span id="trustedhosts"></span><span id="TRUSTEDHOSTS"></span>TrustedHosts
</dt> <dd>

Specifies the list of remote computers that are trusted. Other computers in a workgroup or computers in a different domain should be added to this list.

> [!Note]  
> The computers in the TrustedHosts list are not authenticated. The client may send credential information to these computers.

 

If an IPv6 address is specified for a TrustedHost, the address must be enclosed in square brackets as demonstrated by the following winrm utility command: **winrm set winrm/config/client '@{TrustedHosts ="\[0:0:0:0:0:0:0:0\]"}'**.

For more information about how to add computers to the TrustedHosts list, type **winrm help config**.

</dd> </dl>

## WinRM Service Default Configuration Settings

The service version of WinRM has the following default configuration settings.

<dl> <dt>

<span id="RootSDDL"></span><span id="rootsddl"></span><span id="ROOTSDDL"></span>RootSDDL
</dt> <dd>

Specifies the security descriptor that controls remote access to the listener. The default is "O:NSG:BAD:P(A;;GA;;;BA)(A;;GR;;;ER)S:P(AU;FA;GA;;;WD)(AU;SA;GWGX;;;WD)".

</dd> <dt>

<span id="MaxConcurrentOperations"></span><span id="maxconcurrentoperations"></span><span id="MAXCONCURRENTOPERATIONS"></span>MaxConcurrentOperations
</dt> <dd>

The maximum number of concurrent operations. The default is 100.

**WinRM 2.0:** The MaxConcurrentOperations setting is deprecated and set to read-only. This setting has been replaced by MaxConcurrentOperationsPerUser.

</dd> <dt>

<span id="MaxConcurrentOperationsPerUser"></span><span id="maxconcurrentoperationsperuser"></span><span id="MAXCONCURRENTOPERATIONSPERUSER"></span>MaxConcurrentOperationsPerUser
</dt> <dd>

Specifies the maximum number of concurrent operations that any user can remotely open on the same system. The default is 1500.

</dd> <dt>

<span id="EnumerationTimeoutms"></span><span id="enumerationtimeoutms"></span><span id="ENUMERATIONTIMEOUTMS"></span>EnumerationTimeoutms
</dt> <dd>

Specifies the idle time-out in milliseconds between Pull messages. The default is 60000.

</dd> <dt>

<span id="MaxConnections"></span><span id="maxconnections"></span><span id="MAXCONNECTIONS"></span>MaxConnections
</dt> <dd>

Specifies the maximum number of active requests that the service can process simultaneously. The default is 300.

**WinRM 2.0:** The default is 25.

</dd> <dt>

<span id="MaxPacketRetrievalTimeSeconds"></span><span id="maxpacketretrievaltimeseconds"></span><span id="MAXPACKETRETRIEVALTIMESECONDS"></span>MaxPacketRetrievalTimeSeconds
</dt> <dd>

Specifies the maximum length of time, in seconds, the WinRM service takes to retrieve a packet. The default is 120 seconds.

</dd> <dt>

<span id="AllowUnencrypted"></span><span id="allowunencrypted"></span><span id="ALLOWUNENCRYPTED"></span>AllowUnencrypted
</dt> <dd>

Allows the client computer to request unencrypted traffic. The default is **False**.

</dd> <dt>

<span id="Basic"></span><span id="basic"></span><span id="BASIC"></span>Basic
</dt> <dd>

Allows the WinRM service to use Basic authentication. The default is **False**.

</dd> <dt>

<span id="Certificate"></span><span id="certificate"></span><span id="CERTIFICATE"></span>Certificate
</dt> <dd>

Allows the WinRM service to use client certificate-based authentication. The default is **False**.

</dd> <dt>

<span id="Kerberos"></span><span id="kerberos"></span><span id="KERBEROS"></span>Kerberos
</dt> <dd>

Allows the WinRM service to use Kerberos authentication. The default is **True**.

</dd> <dt>

<span id="Negotiate"></span><span id="negotiate"></span><span id="NEGOTIATE"></span>Negotiate
</dt> <dd>

Allows the WinRM service to use Negotiate authentication. The default is **True**.

</dd> <dt>

<span id="CredSSP"></span><span id="credssp"></span><span id="CREDSSP"></span>CredSSP
</dt> <dd>

Allows the WinRM service to use Credential Security Support Provider (CredSSP) authentication. The default is **False**.

</dd> <dt>

<span id="CbtHardeningLevel"></span><span id="cbthardeninglevel"></span><span id="CBTHARDENINGLEVEL"></span>CbtHardeningLevel
</dt> <dd>

Sets the policy for channel-binding token requirements in authentication requests. The default is **Relaxed**.

</dd> <dt>

<span id="DefaultPorts"></span><span id="defaultports"></span><span id="DEFAULTPORTS"></span>DefaultPorts
</dt> <dd>

Specifies the ports that the WinRM service will use for either HTTP or HTTPS.

**WinRM 2.0:** The default HTTP port is 5985, and the default HTTPS port is 5986.

</dd> <dt>

<span id="IPv4Filter_and_________IPv6Filter"></span><span id="ipv4filter_and_________ipv6filter"></span><span id="IPV4FILTER_AND_________IPV6FILTER"></span>IPv4Filter and IPv6Filter
</dt> <dd>

Specifies the IPv4 or IPv6 addresses that listeners can use. The defaults are IPv4Filter = \* and IPv6Filter = \*.

**IPv4:** An IPv4 literal string consists of four dotted decimal numbers, each in the range 0 through 255. For example: 192.168.0.0.

**IPv6:** An IPv6 literal string is enclosed in brackets and contains hexadecimal numbers that are separated by colons. For example: \[::1\] or \[3ffe:ffff::6ECB:0101\].

</dd> <dt>

<span id="EnableCompatibilityHttpListener"></span><span id="enablecompatibilityhttplistener"></span><span id="ENABLECOMPATIBILITYHTTPLISTENER"></span>EnableCompatibilityHttpListener
</dt> <dd>

Specifies whether the compatibility HTTP listener is enabled. If this setting is **True**, the listener will listen on port 80 in addition to port 5985. The default is **False**.

</dd> <dt>

<span id="EnableCompatibilityHttpsListener"></span><span id="enablecompatibilityhttpslistener"></span><span id="ENABLECOMPATIBILITYHTTPSLISTENER"></span>EnableCompatibilityHttpsListener
</dt> <dd>

Specifies whether the compatibility HTTPS listener is enabled. If this setting is **True**, the listener will listen on port 443 in addition to port 5986. The default is **False**.

</dd> </dl>

## Winrs Default Configuration Settings

**Winrm quickconfig** also configures **Winrs** default settings.

<dl> <dt>

<span id="AllowRemoteShellAccess"></span><span id="allowremoteshellaccess"></span><span id="ALLOWREMOTESHELLACCESS"></span>AllowRemoteShellAccess
</dt> <dd>

Enables access to remote shells. If you set this parameter to **False**, new remote shell connections will be rejected by the server. The default is **True**.

</dd> <dt>

<span id="IdleTimeout"></span><span id="idletimeout"></span><span id="IDLETIMEOUT"></span>IdleTimeout
</dt> <dd>

Specifies the maximum time, in milliseconds, that the remote shell will remain open when there is no user activity in the remote shell. The remote shell is automatically deleted after the time that is specified.

**WinRM 2.0:** The default is 180000. The minimum value is 60000. Setting this value lower than 60000 will have no effect on the time-out.

</dd> <dt>

<span id="MaxConcurrentUsers"></span><span id="maxconcurrentusers"></span><span id="MAXCONCURRENTUSERS"></span>MaxConcurrentUsers
</dt> <dd>

Specifies the maximum number of users who can concurrently perform remote operations on the same computer through a remote shell. New remote shell connections will be rejected if they exceed the specified limit. The default is 5.

</dd> <dt>

<span id="MaxShellRunTime"></span><span id="maxshellruntime"></span><span id="MAXSHELLRUNTIME"></span>MaxShellRunTime
</dt> <dd>

Specifies the maximum time, in milliseconds, that the remote command or script is allowed to execute. The default is 28800000.

**WinRM 2.0:** The MaxShellRunTime setting is set to read-only. Changing the value for MaxShellRunTime will have no effect on the remote shells.

</dd> <dt>

<span id="MaxProcessesPerShell"></span><span id="maxprocessespershell"></span><span id="MAXPROCESSESPERSHELL"></span>MaxProcessesPerShell
</dt> <dd>

Specifies the maximum number of processes that any shell operation is allowed to start. A value of 0 allows for an unlimited number of processes. The default is 15.

</dd> <dt>

<span id="MaxMemoryPerShellMB"></span><span id="maxmemorypershellmb"></span><span id="MAXMEMORYPERSHELLMB"></span>MaxMemoryPerShellMB
</dt> <dd>

Specifies the maximum amount of memory allocated per shell, including the shell's child processes. The default is 150 MB.

</dd> <dt>

<span id="MaxShellsPerUser"></span><span id="maxshellsperuser"></span><span id="MAXSHELLSPERUSER"></span>MaxShellsPerUser
</dt> <dd>

Specifies the maximum number of concurrent shells that any user can remotely open on the same computer. If this policy setting is enabled, the user will not be able to open new remote shells if the count exceeds the specified limit. If this policy setting is disabled or is not configured, the limit will be set to 5 remote shells per user by default.

</dd> </dl>

## Configuring WinRM with Group Policy

Use the Group Policy editor to configure Windows Remote Shell and WinRM for computers in your enterprise.

**To configure with Group Policy**

1.  Open a Command Prompt window as an administrator.
2.  At the Command Prompt, type **gpedit.msc**. The **Group Policy Object Editor** window opens.
3.  Find the **Windows Remote Management** and **Windows Remote Shell** Group Policy Objects (GPO) under **Computer Configuration\\Administrative Templates\\Windows Components**.
4.  On the **Extended** tab, select a setting to see a description. Double click a setting to edit it.

## Windows Firewall and WinRM 2.0 Ports

Starting in WinRM 2.0, the default listener ports configured by **Winrm quickconfig** are port 5985 for HTTP transport and port 5986 for HTTPS. WinRM listeners can be configured on any arbitrary port.

If a computer is upgraded to WinRM 2.0, the previously configured listeners are migrated and still receive traffic.

## WinRM Installation and Configuration Notes

WinRM is not dependent on any other service except WinHttp. If the IIS Admin Service is installed on the same computer, you might see messages that indicate WinRM cannot be loaded before Internet Information Services (IIS). However, WinRM does not actually depend on IIS: these messages occur because the load order ensures that the IIS service starts before the HTTP service. WinRM does require that WinHTTP.dll be registered.

If the ISA2004 firewall client is installed on the computer, it can cause a Web Services for Management (WS-Management) client to stop responding. To avoid this issue, install ISA2004 Firewall SP1.

If two listener services with different IP addresses are configured with the same port number and computer name, WinRM listens or receives messages on only one address. This is because the URL prefixes used by the WS-Management protocol are the same.

## IPMI Driver and Provider Installation Notes

The driver might not detect the existence of IPMI drivers that are not from Microsoft. If the driver fails to start, you might need to disable it.

If the [*baseboard management controller (BMC)*](windows-remote-management-glossary.md) resources appear in the system BIOS, ACPI (Plug and Play) detects the BMC hardware and automatically installs the IPMI driver. Plug and Play support might not be present in all BMCs. If the BMC is detected by Plug and Play, an Unknown Device appears in Device Manager before the Hardware Management component is installed. When the driver is installed, a new component, the Microsoft ACPI Generic IPMI Compliant Device, appears in Device Manager.

If your system does not automatically detect the BMC and install the driver, but a BMC was detected during the setup process, the BMC device must be manually created. To do this, type the following command at a command prompt: **Rundll32 ipmisetp.dll, AddTheDevice**. After this command is executed, the IPMI device is created and appears in Device Manager. If you uninstall the Hardware Management component, the device is removed.

For more information, see [Hardware Management Introduction](http://go.microsoft.com/fwlink/p/?linkid=45204).

The IPMI provider places the hardware classes in the **root\\hardware** [*namespace*](https://msdn.microsoft.com/library/aa390820#wmi-gloss-namespace) of WMI. For more information about the hardware classes, see [IPMI Provider](https://msdn.microsoft.com/library/aa391402). For more information about WMI *namespaces*, see [WMI Architecture](https://msdn.microsoft.com/library/aa394553).

## WMI Plug-in Configuration Notes

Beginning with Windows 8 and Windows Server 2012, [*WMI plug-ins*](windows-remote-management-glossary.md) have their own security configurations. For a normal or power (non-administrator) user to be able to use the *WMI plug-in*, you need to enable access for that user after the [*listener*](windows-remote-management-glossary.md) has been configured. First, you must set up the user for remote access to [*WMI*](windows-remote-management-glossary.md) through one of these steps:

-   run **lusrmgr.msc** to add the user to the **WinRMRemoteWMIUsers\_\_** group in the **Local Users and Groups** window, or

-   use the **winrm** command-line tool to configure the security descriptor for the [*namespace*](windows-remote-management-glossary.md) of the [*WMI plug-in*](windows-remote-management-glossary.md), as follows: **winrm configSDDL http://schemas.microsoft.com/wbem/wsman/1/wmi/***WmiNamespace*.

    When the user interface appears, add the user.

After setting up the user for remote access to [*WMI*](windows-remote-management-glossary.md), you must set up *WMI* to allow the user to access the plug-in. To do this, run **wmimgmt.msc** to modify the *WMI* security for the [*namespace*](windows-remote-management-glossary.md) to be accessed in the **WMI Control** window.

The majority of the WMI classes for management are in the **root\\cimv2** namespace.

 

 




