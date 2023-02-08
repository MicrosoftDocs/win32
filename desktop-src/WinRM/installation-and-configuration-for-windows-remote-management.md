---
title: Installation and configuration for Windows Remote Management
description: Learn how to install and configure Windows Remote Management in order to run Windows Remote Management scripts and for the Winrm tool to perform data operations.
ms.date: 02/08/2023
ms.assetid: 81c40456-0003-46d0-8695-83bf77432056
ms.topic: conceptual
ms.custom: contperf-fy21q1
---

# Installation and configuration for Windows Remote Management

For Windows Remote Management (WinRM) scripts to run, and for the *Winrm* command-line tool to perform data operations, WinRM has to be both installed and configured.

These elements also depend on WinRM configuration.

- The [Windows Remote Shell](./windows-remote-management-glossary.md#w) command-line tool, *Winrs*.
- [Event forwarding](./windows-remote-management-glossary.md#e).
- Windows PowerShell 2.0 remoting.

## The install location of WinRM

WinRM is automatically installed with all currently-supported versions of the Windows operating system.

## Configuration of WinRM and IPMI

These WinRM and [Intelligent Platform Management Interface (IPMI)](./windows-remote-management-glossary.md#i) [WMI provider](/previous-versions/windows/desktop/ipmiprv/ipmi-provider) components are installed with the operating system.

- The WinRM service starts automatically on Windows Server 2008 and later. On earlier versions of Windows (client or server), you need to start the service manually.
- By default, no WinRM [listener](./windows-remote-management-glossary.md#l) is configured. Even if the WinRM service is running, WS-Management protocol [messages](./windows-remote-management-glossary.md#m) that request data can't be received or sent.
- Internet Connection Firewall (ICF) blocks access to ports.

Use the `winrm` command to locate listeners and the addresses by typing the following command at a command prompt.

```console
winrm enumerate winrm/config/listener
```

To check the state of configuration settings, type the following command.

```console
winrm get winrm/config
```

## Quick default configuration

Enable the WS-Management protocol on the local computer, and set up the default configuration for remote management with the command `winrm quickconfig`.

The `winrm quickconfig` command (which can be abbreviated to `winrm qc`) performs these operations:

- Starts the WinRM service, and sets the service startup type to *auto-start*.
- Configures a listener for the ports that send and receive WS-Management protocol [messages](./windows-remote-management-glossary.md#m) using either HTTP or HTTPS on any IP address.
- Defines ICF exceptions for the WinRM service, and opens the ports for HTTP and HTTPS.

> [!NOTE]
> The `winrm quickconfig` command creates a firewall exception only for the current user profile. If the firewall profile is changed for any reason, then run `winrm quickconfig` to enable the firewall exception for the new profile (otherwise the exception might not be enabled).

To retrieve information about customizing a configuration, type the following command at a command prompt.

```console
winrm help config
```

### To configure WinRM with default settings

1. At a command prompt running as the local computer Administrator account, run this command:

   ```console
   winrm quickconfig
   ```

   If you're not running as the local computer Administrator, either select **Run as Administrator** from the **Start** menu, or use the `Runas` command at a command prompt.

2. When the tool displays **Make these changes \[y/n\]?**, type **y**.

   If configuration is successful, the following output is displayed.

   ```output
   WinRM has been updated for remote management.

   WinRM service type changed to delayed auto start.
   WinRM service started.
   Created a WinRM listener on https://* to accept WS-Man requests to any IP on this machine.
   ```

3. Keep the default settings for client and server components of WinRM, or customize them. For example, you might need to add certain remote computers to the client configuration `TrustedHosts` list.

   Set up a trusted hosts list when mutual authentication can't be established. Kerberos allows mutual authentication, but it can't be used in workgroups; only domains. A best practice when setting up trusted hosts for a workgroup is to make the list as restricted as possible.

4. Create an HTTPS listener by typing the following command:

   ```console
   winrm quickconfig -transport:https
   ```

   > [!NOTE]
   > Open port 5986 for HTTPS transport to work.

## Listener and WS-Management protocol default settings

To get the listener configuration, type `winrm enumerate winrm/config/listener` at a command prompt. Listeners are defined by a transport (HTTP or HTTPS) and an IPv4 or IPv6 address.

The `winrm quickconfig` command creates the following default settings for a listener. You can create more than one listener. For more information, type `winrm help config` at a command prompt.

### Address

Specifies the address for which this listener is being created.

### Transport

Specifies the transport to use to send and receive WS-Management protocol requests and responses. The value must be either *HTTP* or *HTTPS*. The default is *HTTP*.

### Port

Specifies the TCP port for which this listener is created.

**WinRM 2.0**: The default HTTP port is 5985.

### Hostname

Specifies the host name of the computer on which the WinRM service is running. The value must be: a fully-qualified domain name; an IPv4 or IPv6 literal string; or a wildcard character.

### Enabled

Specifies whether the listener is enabled or disabled. The default value is *True*.

### URLPrefix

Specifies a URL prefix on which to accept HTTP or HTTPS requests. This string contains only the characters a-z, A-Z, 9-0, underscore (\_), and slash (/). The string must not start with or end with a slash (/). For example, if the computer name is *SampleMachine*, then the WinRM client would specify `https://SampleMachine/<URLPrefix>` in the destination address. The default URL prefix is `wsman`.

### CertificateThumbprint

Specifies the thumbprint of the service certificate. This value represents a string of two-digit hexadecimal values found in the *Thumbprint* field of the certificate. This string contains the SHA-1 hash of the certificate. Certificates are used in client certificate-based authentication. Certificates can be mapped only to local user accounts. They don't work with domain accounts.

### ListeningOn

Specifies the IPv4 and IPv6 addresses that the listener uses. For example: `111.0.0.1, 111.222.333.444, ::1, 1000:2000:2c:3:c19:9ec8:a715:5e24, 3ffe:8311:ffff:f70f:0:5efe:111.222.333.444, fe80::5efe:111.222.333.444%8, fe80::c19:9ec8:a715:5e24%6`.

## Protocol default settings

Many of the configuration settings, such as *MaxEnvelopeSizekb* or *SoapTraceEnabled*, determine how the WinRM client and server components interact with the WS-Management protocol. The following sections describe the available configuration settings.

### MaxEnvelopeSizekb

Specifies the maximum Simple Object Access Protocol (SOAP) data in kilobytes. The default is 150 kilobytes.

> [!NOTE]  
> The behavior is unsupported if *MaxEnvelopeSizekb* is set to a value greater than 1039440.

### MaxTimeoutms

Specifies the maximum time-out in milliseconds that can be used for any request other than `Pull` requests. The default is 60000.

### MaxBatchItems

Specifies the maximum number of elements that can be used in a `Pull` response. The default is 32000.

### MaxProviderRequests

Specifies the maximum number of concurrent requests that are allowed by the service. The default is 25.

**WinRM 2.0**: This setting is deprecated, and is set to read-only.

## WinRM client default configuration settings

The client version of WinRM has the following default configuration settings.

### NetworkDelayms

Specifies the extra time in milliseconds that the client computer waits to accommodate for network delay time. The default is 5000 milliseconds.

### URLPrefix

Specifies a URL prefix on which to accept HTTP or HTTPS requests. The default URL prefix is *wsman*.

### AllowUnencrypted

Allows the client computer to request unencrypted traffic. By default, the client computer requires encrypted network traffic and this setting is *False*.

### Basic

Allows the client computer to use Basic authentication. Basic authentication is a scheme in which the user name and password are sent in clear text to the server or proxy. This method is the least secure method of authentication. The default is *True*.

### Digest

Allows the client to use Digest authentication. Digest authentication is a challenge-response scheme that uses a server-specified data string for the challenge. Only the client computer can initiate a Digest authentication request.

The client computer sends a request to the server to authenticate, and receives a token string from the server. Then the client computer sends the resource request, including the user name and a cryptographic hash of the password combined with the token string.

Digest authentication is supported for HTTP and for HTTPS. WinRM Shell client scripts and applications can specify Digest authentication, but the WinRM service doesn't accept Digest authentication. The default is `True`.

> [!NOTE]
> Digest authentication over HTTP isn't considered secure.

### Certificate

Allows the client to use client certificate-based authentication. Certificate-based authentication is a scheme in which the server authenticates a client identified by an X509 certificate. The default is *True*.

### Kerberos

Allows the client to use Kerberos authentication. Kerberos authentication is a scheme in which the client and server mutually authenticate by using Kerberos certificates. The default is *True*.

### Negotiate

Allows the client to use *Negotiate* authentication. Negotiate authentication is a scheme in which the client sends a request to the server to authenticate.

The server determines whether to use the Kerberos protocol or NT LAN Manager (NTLM). The Kerberos protocol is selected to authenticate a domain account. NTLM is selected for local computer accounts. The user name must be specified in *domain\\user\_name* format for a domain user. The user name must be specified in *server\_name\\user\_name* format for a local user on a server computer. The default is `True`.

### CredSSP

Allows the client to use Credential Security Support Provider (CredSSP) authentication. CredSSP enables an application to delegate the user's credentials from the client computer to the target server. The default is `False`.

### DefaultPorts

Specifies the ports that the client uses for either HTTP or HTTPS.

WinRM 2.0: The default HTTP port is 5985, and the default HTTPS port is 5986.

### TrustedHosts

Specifies the list of remote computers that are trusted. Other computers in a workgroup or computers in a different domain should be added to this list.

> [!NOTE]
> The computers in the trusted hosts list aren't authenticated. The client might send credential information to these computers.

If an IPv6 address is specified for a trusted host, the address must be enclosed in square brackets as demonstrated by the following `Winrm` utility command:

```console
winrm set winrm/config/client '@{TrustedHosts ="[0:0:0:0:0:0:0:0]"}'
```

For more information about how to add computers to the `TrustedHosts` list, type `winrm help config`.

## WinRM service default configuration settings

The service version of WinRM has the following default configuration settings.

### RootSDDL

Specifies the security descriptor that controls remote access to the listener. The default is `O:NSG:BAD:P(A;;GA;;;BA)(A;;GR;;;ER)S:P(AU;FA;GA;;;WD)(AU;SA;GWGX;;;WD)`.

### MaxConcurrentOperations

The maximum number of concurrent operations. The default is 100.

**WinRM 2.0**: The `MaxConcurrentOperations` setting is deprecated, and is set to read-only. This setting has been replaced by `MaxConcurrentOperationsPerUser`.

### MaxConcurrentOperationsPerUser

Specifies the maximum number of concurrent operations that any user can remotely open on the same system. The default is 1500.

### EnumerationTimeoutms

Specifies the idle time-out in milliseconds between `Pull` messages. The default is 60000.

### MaxConnections

Specifies the maximum number of active requests that the service can process simultaneously. The default is 300.

WinRM 2.0: The default is 25.

### MaxPacketRetrievalTimeSeconds

Specifies the maximum length of time in seconds that the WinRM service takes to retrieve a packet. The default is 120 seconds.

### AllowUnencrypted

Allows the client computer to request unencrypted traffic. The default is `False`.

### Basic

Allows the WinRM service to use Basic authentication. The default is `False`.

### Certificate

Allows the WinRM service to use client certificate-based authentication. The default is `False`.

### Kerberos

Allows the WinRM service to use Kerberos authentication. The default is `True`.

### Negotiate

Allows the WinRM service to use Negotiate authentication. The default is `True`.

### CredSSP

Allows the WinRM service to use Credential Security Support Provider (CredSSP) authentication. The default is `False`.

### CbtHardeningLevel

Sets the policy for channel-binding token requirements in authentication requests. The default is *Relaxed*.

### DefaultPorts

Specifies the ports that the WinRM service uses for either HTTP or HTTPS.

WinRM 2.0: The default HTTP port is 5985. The default HTTPS port is 5986.

### IPv4Filter and IPv6Filter

Specifies the IPv4 or IPv6 addresses that listeners can use. The defaults are `IPv4Filter = *` and `IPv6Filter = *`.

- IPv4: An IPv4 literal string consists of four dotted decimal numbers, each in the range 0 through 255. For example: 192.168.0.0.
- IPv6: An IPv6 literal string is enclosed in brackets and contains hexadecimal numbers that are separated by colons. For example: \[::1\] or \[3ffe:ffff::6ECB:0101\].

### EnableCompatibilityHttpListener

Specifies whether the compatibility HTTP listener is enabled. If this setting is `True`, the listener listens on port 80 in addition to port 5985. The default is `False`.

### EnableCompatibilityHttpsListener

Specifies whether the compatibility HTTPS listener is enabled. If this setting is `True`, the listener listens on port 443 in addition to port 5986. The default is `False`.

## Winrs default configuration settings

The `winrm quickconfig` command also configures Winrs default settings.

### AllowRemoteShellAccess

Enables access to remote shells. If you set this parameter to `False`, the server rejects new remote shell connections  by the server. The default is `True`.

### IdleTimeout

Specifies the maximum time in milliseconds that the remote shell remains open when there's no user activity in the remote shell. The remote shell is deleted after that time.

WinRM 2.0: The default is 180000. The minimum value is 60000. Setting this value lower than 60000 have no effect on the time-out behavior.

### MaxConcurrentUsers

Specifies the maximum number of users who can concurrently perform remote operations on the same computer through a remote shell. If new remote shell connections exceed the limit, the computer rejects them. The default is 5.

### MaxShellRunTime

Specifies the maximum time in milliseconds that the remote command or script is allowed to run. The default is 28800000.

WinRM 2.0: The `MaxShellRunTime` setting is set to read-only. Changing the value for `MaxShellRunTime` has no effect on the remote shells.

### MaxProcessesPerShell

Specifies the maximum number of processes that any shell operation is allowed to start. A value of 0 allows for an unlimited number of processes. The default is 15.

### MaxMemoryPerShellMB

Specifies the maximum amount of memory allocated per shell, including the shell's child processes. The default is 150 MB.

### MaxShellsPerUser

Specifies the maximum number of concurrent shells that any user can remotely open on the same computer. If this policy setting is enabled, the user won't be able to open new remote shells if the count exceeds the specified limit. If this policy setting is disabled or isn't configured, the limit is set to five remote shells per user by default.

## Configuring WinRM with Group Policy

Use the Group Policy editor to configure Windows Remote Shell and WinRM for computers in your enterprise.

To configure with Group Policy:

1. Open a Command Prompt window as an administrator.
2. At the command prompt, type `gpedit.msc`. The **Group Policy Object Editor** window opens.
3. Find the **Windows Remote Management** and **Windows Remote Shell** Group Policy Objects (GPO) under **Computer Configuration\\Administrative Templates\\Windows Components**.
4. On the **Extended** tab, select a setting to see a description. Double-click a setting to edit it.

## Windows Firewall and WinRM 2.0 ports

Starting in WinRM 2.0, the default listener ports configured by `Winrm quickconfig` are port 5985 for HTTP transport, and port 5986 for HTTPS. WinRM listeners can be configured on any arbitrary port.

If you upgrade a computer to WinRM 2.0, the previously configured listeners are migrated, and still receive traffic.

## WinRM installation and configuration notes

WinRM isn't dependent on any other service except `WinHttp`. If the IIS Admin Service is installed on the same computer, then you might see messages that indicate that WinRM can't be loaded before Internet Information Services (IIS). However, WinRM doesn't actually depend on IIS. Those messages occur because the load order ensures that the IIS service starts before the HTTP service. WinRM requires that `WinHTTP.dll` is registered.

If the ISA2004 firewall client is installed on the computer, it can cause a Web Services for Management (WS-Management) client to stop responding. To avoid this issue, install ISA2004 Firewall SP1.

If two listener services with different IP addresses are configured with the same port number and computer name, then WinRM listens or receives messages on only one address. This approach used is because the URL prefixes used by the WS-Management protocol are the same.

## IPMI driver and provider installation notes

The driver might not detect the existence of IPMI drivers that aren't from Microsoft. If the driver fails to start, then you might need to disable it.

If the [baseboard management controller (BMC)](./windows-remote-management-glossary.md#b) resources appear in the system BIOS, then ACPI (Plug and Play) detects the BMC hardware, and automatically installs the IPMI driver. Plug and Play support might not be present in all BMCs. If the BMC is detected by Plug and Play, then an **Unknown Device** appears in Device Manager before the Hardware Management component is installed. When the driver is installed, a new component, the **Microsoft ACPI Generic IPMI Compliant Device**, appears in Device Manager.

If your system doesn't automatically detect the BMC and install the driver, but a BMC was detected during the setup process, create the BMC device. To create the device, type the following command at a command prompt:

```console
Rundll32 ipmisetp.dll, AddTheDevice
```

After this command runs, the IPMI device is created, and it appears in Device Manager. If you uninstall the Hardware Management component, the device is removed.

For more information, see [Hardware management introduction](/previous-versions/windows/it-pro/windows-server-2003/cc785056(v=ws.10)).

The IPMI provider places the hardware classes in the *root\\hardware* [namespace](/windows/desktop/WmiSdk/gloss-n) of WMI. For more information about the hardware classes, see [IPMI Provider](/previous-versions/windows/desktop/ipmiprv/ipmi-provider). For more information about WMI namespaces, see [WMI architecture](/windows/desktop/WmiSdk/wmi-architecture).

## WMI plug-in configuration notes

Beginning with Windows 8 and Windows Server 2012, [WMI plug-ins](./windows-remote-management-glossary.md#w) have their own security configurations. For a normal or power user, not an administrator, to be able to use the WMI plug-in, enable access for that user after the [listener](./windows-remote-management-glossary.md#l) has been configured. Set up the user for remote access to [WMI](./windows-remote-management-glossary.md#w) through one of these steps.

- Run `lusrmgr.msc` to add the user to the **WinRMRemoteWMIUsers\_\_** group in the **Local Users and Groups** window.
- Use the Winrm command-line tool to configure the security descriptor for the [namespace](./windows-remote-management-glossary.md#n) of the [WMI plug-in](./windows-remote-management-glossary.md#w):

  ```console
  winrm configSDDL http://schemas.microsoft.com/wbem/wsman/1/wmi/ WmiNamespace
  ```

When the user interface appears, add the user.

After setting up the user for remote access to [WMI](./windows-remote-management-glossary.md#w), you must set up *WMI* to allow the user to access the plug-in. To allow access, run *wmimgmt.msc* to modify the WMI security for the [namespace](./windows-remote-management-glossary.md#n) to be accessed in the **WMI Control** window.

Most of the WMI classes for management are in the *root\\cimv2* namespace.
