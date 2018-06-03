---
title: How-to install, configure and test with an RMS server
description: This topic covers the steps to connect to an RMS Sever for testing your rights-enabled application.
audience: developer
author: REDMOND\\bruceper
manager: REDMOND\\mbaldwin
ms.assetid: 32C7F387-CF7E-4CE0-AFC9-4C63FE1E134A
ms.prod: windows-server-dev
ms.technology: active-directory-rights-management
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# How-to: install, configure and test with an RMS server

This topic covers the steps to connect to an RMS Sever for testing your rights-enabled application.

## Instructions

### Step 1: Install

-   Beginning with Windows Server 2008, both the client and the server components are included in the operating system. You can download the server components for prior operating systems from [RMS Server v1.0 SP2](http://go.microsoft.com/fwlink/p/?linkid=73722).

    To configure the server component on Windows Server 2008, you must install the AD RMS role.

### Step 2: Enroll

The RMS server can be self-enrolled or via an on-line process.

-   **Self-enrollment** - Beginning with Windows Server 2008, you can enroll an RMS server without sending information to Microsoft. When you install the RMS role, a self-enrollment certificate and private key are also installed. These are used to automatically create the server licensor certificate. No information is exchanged with Microsoft.

    **Online enrollment** - If you are using AD RMS v1.0 SP2, you can enroll the server online. Enrollment takes place behind the scenes during the provisioning process, but you must have an internet connection.

    **HKEY\_LOCAL\_MACHINE**\\**Software**\\**Microsoft**\\**DRMS**\\**1.0**\\**UddiProvider** = 0e3d9bb8-b765-4a68-a329-51548685fed3

### Step 3: Connect

Configure either server-side discovery or client-side discovery to enable the Rights Management Service Client 2.1 to discover and establish connection with your RMS server.

-   In *server-side discovery*, an administrator registers a Service Connection Point (SCP) for the RMS root cluster with Active Directory, and the client queries Active Directory to discover the SCP and establish a connection with the server.

    In *client-side discovery*, you configure RMS Service Discovery settings in the registry on the computer where the RMS Client 2.1 is running. These settings point the RMS Client 2.1 to the RMS server to use. When they are present, server-side discovery is not performed.

    To configure client-side discovery, you can set the following registry keys to point to your RMS server. For information about how to configure service-side discovery, see [RMS Client 2.0 Deployment Notes](https://TechNet.Microsoft.Com/library/jj159267(WS.10).aspx).

    

    <table>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th>Key</th>
    <th>Value</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td><pre data-space="preserve"><code>HKEY_LOCAL_MACHINE
       SOFTWARE
          Microsoft
             MSIPC
                ServiceLocation
                   EnterpriseCertification</code></pre>
    <br/></td>
    <td>(Default):<br/> [<strong>http</strong>|<strong>https</strong>]<strong>://</strong><em>RMSClusterName</em><strong>/_wmcs/Certification</strong><br/></td>
    </tr>
    <tr class="even">
    <td><pre data-space="preserve"><code>HKEY_LOCAL_MACHINE
       SOFTWARE
          Microsoft
             MSIPC
                ServiceLocation
                   EnterprisePublishing</code></pre>
    <br/></td>
    <td>(Default):<br/> [<strong>http</strong>|<strong>https</strong>]<strong>://</strong><em>RMSClusterName</em><strong>/_wmcs/Licensing</strong><br/></td>
    </tr>
    </tbody>
    </table>

    

     

    > [!Note]  
    > By default, these keys do not exist in the registry and must be created.

     

    > \[!Important\]
    >
    > If you are running a 32-bit application on a 64-bit version of Windows, you must set these keys in the following key location:
    >
    > ```
    > HKEY_LOCAL_MACHINE
    >    SOFTWARE
    >       Wow6432Node
    >          Microsoft
    >             MSIPC
    > ```

     

## Remarks

## Related topics

<dl> <dt>

[RMS Server v1.0 SP2](http://go.microsoft.com/fwlink/p/?linkid=73722)
</dt> <dt>

[RMS Client 2.0 Deployment Notes](https://TechNet.Microsoft.Com/library/jj159267(WS.10).aspx)
</dt> </dl>

 

 





