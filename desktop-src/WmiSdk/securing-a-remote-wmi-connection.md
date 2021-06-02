---
description: To connect to a remote computer using WMI, ensure that the correct DCOM settings and WMI namespace security settings are enabled for the connection.
ms.assetid: 96ebaa9b-a062-4300-a637-8eb71cb80d1c
ms.tgt_platform: multiple
title: Securing a Remote WMI Connection
ms.topic: article
ms.date: 05/31/2018
---

# Securing a Remote WMI Connection

To connect to a remote computer using WMI, ensure that the correct DCOM settings and WMI namespace security settings are enabled for the connection.

WMI has default impersonation, authentication, and authentication service (NTLM or Kerberos) settings that the target computer in a remote connection requires. Your local machine may use different defaults that the target system does not accept. You can change these settings in the connection call.

The following sections are discussed in this topic:

-   [DCOM Impersonation and Authentication Settings for WMI](#dcom-impersonation-and-authentication-settings-for-wmi)
-   [Setting DCOM Security to Allow a User to Access a Computer Remotely](#setting-dcom-security-to-allow-a-user-to-access-a-computer-remotely)
-   [Allowing Users Access to a Specific WMI Namespace](#allowing-users-access-to-a-specific-wmi-namespace)
-   [Setting Namespace Security to Require Data Encryption for Remote Connections](#setting-namespace-security-to-require-data-encryption-for-remote-connections)
-   [Related topics](#related-topics)

## DCOM Impersonation and Authentication Settings for WMI

WMI has default DCOM impersonation, authentication, and authentication service (NTLM or Kerberos) settings that the a remote system requires. Your local system may use different defaults that the target remote system does not accept. You can change these settings in the connection call. For more information, see [Setting Client Application Process Security](setting-client-application-process-security.md). However, for the authentication service, it is recommended that you specify **RPC\_C\_AUTHN\_DEFAULT** and allow DCOM to choose the appropriate service for the target computer.

You can supply settings in parameters for the calls to [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) or [**CoSetProxyBlanket**](/windows/win32/api/combaseapi/nf-combaseapi-cosetproxyblanket) in C++. In scripts, you can establish security settings in calls to [**SWbemLocator.ConnectServer**](swbemlocator-connectserver.md), in an [**SWbemSecurity**](swbemsecurity.md) object, or in the scripting [moniker](constructing-a-moniker-string.md) string.

For a list of all the C++ impersonation constants, see [Setting the Default Process Security Level Using C++](setting-the-default-process-security-level-using-c-.md). For the Visual Basic constants and scripting strings for using the moniker connection, see [Setting the Default Process Security Level Using VBScript](setting-the-default-process-security-level-using-vbscript.md).

The following table lists the default DCOM impersonation, authentication, and authentication service settings required by the target computer (Computer B) in a remote connection. For more information, see Securing a Remote WMI Connection.



| Computer B operating system | Impersonation level scripting string | Authentication level scripting string | Authentication service |
|-----------------------------|--------------------------------------|---------------------------------------|------------------------|
| Windows Vista or later      | Impersonate                          | Pkt                                   | Kerberos               |



 

WMI remote connections are affected by [User Account Control (UAC)](/previous-versions/aa905108(v=msdn.10)) and [Windows Firewall](https://www.microsoft.com/technet/itsolutions/network/wf/default.mspx). For more information, see [Connecting to WMI Remotely Starting with Vista](connecting-to-wmi-remotely-starting-with-vista.md) and [Connecting Through Windows Firewall](/windows/desktop/WmiSdk/connecting-to-wmi-remotely-starting-with-vista).

Be aware that connecting to WMI on the local computer has a default authentication level of **PktPrivacy**.

## Setting DCOM Security to Allow a User to Access a Computer Remotely

Security in WMI is related to connecting to a WMI namespace. WMI uses DCOM to handle remote calls. One reason for failure to connect to a remote computer is due to a DCOM failure (error "DCOM Access Denied" decimal -2147024891 or hex 0x80070005). For more information about DCOM security in WMI for C++ applications, see [Setting Client Application Process Security](setting-client-application-process-security.md).

You can configure DCOM settings for WMI using the DCOM Config utility (**DCOMCnfg.exe**) found in **Administrative Tools** in **Control Panel**. This utility exposes the settings that enable certain users to connect to the computer remotely through DCOM. Members of the Administrators group are allowed to remotely connect to the computer by default. With this utility you can set the security to start, access, and configure the WMI service.

The following procedure describes how to grant DCOM remote startup and activation permissions for certain users and groups. If Computer A is connecting remotely to Computer B, you can set these permissions on Computer B to allow a user or group that is not part of the Administrators group on Computer B to execute DCOM startup and activation calls on Computer B.

**To grant DCOM remote launch and activation permissions for a user or group**

1.  Click **Start**, click **Run**, type **DCOMCNFG**, and then click **OK**.
2.  In the **Component Services** dialog box, expand **Component Services**, expand **Computers**, and then right-click **My Computer** and click **Properties**.
3.  In the **My Computer Properties** dialog box, click the **COM Security** tab.
4.  Under **Launch and Activation Permissions**, click **Edit Limits**.
5.  In the **Launch Permission** dialog box, follow these steps if your name or your group does not appear in the **Groups or user names list**:

    1.  In the **Launch Permission** dialog box, click **Add**.
    2.  In the **Select Users, Computers, or Groups** dialog box, add your name and the group in the **Enter the object names to select** box, and then click **OK**.

6.  In the **Launch Permission** dialog box, select your user and group in the **Group or user names** box. In the **Allow** column under **Permissions for User**, select **Remote Launch** and select **Remote Activation**, and then click **OK**.

The following procedure describes how to grant DCOM remote access permissions for certain users and groups. If Computer A is connecting remotely to Computer B, you can set these permissions on Computer B to allow a user or group that is not part of the Administrators group on Computer B to connect to Computer B.

**To grant DCOM remote access permissions**

1.  Click **Start**, click **Run**, type **DCOMCNFG**, and then click **OK**.
2.  In the **Component Services** dialog box, expand **Component Services**, expand **Computers**, and then right-click **My Computer** and click **Properties**.
3.  In the **My Computer Properties** dialog box, click the **COM Security** tab.
4.  Under **Access Permissions**, click **Edit Limits**.
5.  In the **Access Permission** dialog box, select **ANONYMOUS LOGON** name in the **Group or user names** box. In the **Allow** column under **Permissions for User**, select **Remote Access**, and then click **OK**.

## Allowing Users Access to a Specific WMI Namespace

You can allow or disallow users access to a specific WMI namespace by setting the "Remote Enable" permission in the WMI Control for a namespace. If a user tries to connect to a namespace they are not allowed access to, they will receive error 0x80041003. By default, this permission is enabled only for administrators. An administrator can enable remote access to specific WMI namespaces for a nonadministrator user.

The following procedure sets remote enable permissions for a non-administrator user.

**To set remote enable permissions**

1.  Connect to the remote computer using the WMI Control.

    For more information about the WMI Control, see [Setting Namespace Security with the WMI Control](setting-namespace-security-with-the-wmi-control.md).

2.  In the **Security** tab, select the namespace and click **Security**.
3.  Locate the appropriate account and check **Remote Enable** in the **Permissions** list.

## Setting Namespace Security to Require Data Encryption for Remote Connections

An administrator or a MOF file can configure a WMI namespace so that no data is returned unless you use packet privacy (**RPC\_C\_AUTHN\_LEVEL\_PKT\_PRIVACY** or **PktPrivacy** as a moniker in a script) in a connection to that namespace. This ensures that data is encrypted as it crosses the network. If you try to set a lower authentication level, you will get an access denied message. For more information, see [Requiring an Encrypted Connection to a Namespace](requiring-an-encrypted-connection-to-a-namespace.md).

The following VBScript code example shows how to connect to an encrypted namespace using "pktPrivacy".


```VB
strComputer = "RemoteComputer"
Set objWMIService = GetObject("winmgmts:{impersonationLevel=impersonate,authenticationLevel=pktPrivacy}!\\" _
                              & strComputer & "\root\EncryptedNamespace")
```



## Related topics

<dl> <dt>

[Delegating with WMI](connecting-to-a-3rd-computer-delegation.md)
</dt> <dt>

[Creating Processes Remotely with WMI](creating-processes-remotely.md)
</dt> <dt>

[Securing C++ Clients and Providers](securing-c---clients-and-providers.md)
</dt> <dt>

[Securing Scripting Clients](securing-scripting-clients.md)
</dt> </dl>

 

 
