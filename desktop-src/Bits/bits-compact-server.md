---
title: BITS Compact Server
description: The Background Intelligent Transfer Service (BITS) Compact Server is a stand-alone HTTP/HTTPS file server that provides the ability to transfer a limited number of large files asynchronously between computers.
ms.assetid: ab4cf901-6d93-433c-b1b2-ffa54d10725c
ms.topic: article
ms.date: 05/31/2018
---

# BITS Compact Server

The Background Intelligent Transfer Service (BITS) Compact Server is a stand-alone HTTP/HTTPS file server that provides the ability to transfer a limited number of large files asynchronously between computers. The Compact Server is built as an NT Service and uses HTTP.SYS.

The BITS Compact Server is intended for use by enterprise and small business customers under the following conditions:

-   The anticipated usage is a maximum of 25 URL groups, and each URL group supports 3 simultaneous file transfers.
-   File transfers occur between computers in the same domain or mutually trusted domains.
-   File transfers are not intended for Internet-facing clients.

## Installing the BITS Compact Server

The BITS Compact Server is an optional server component. You can use one of the following options to install the BITS Compact Server:

-   Server Manager

-   Windows PowerShell

-   Package Manager

**To install the BITS Compact Server by using Server Manager**

1.  In the **Features Summary** section of the **Server Manager**, click **Add Features**.
2.  In the Add Features Wizard, select **Background Intelligent Transfer Service (BITS)** and **Compact Server**.
3.  Follow the wizard instructions, including installing the required software if indicated.

For more information, see the **Server Manager** online help.

**To install the BITS Compact Server by using Windows PowerShell**

1.  In a Windows PowerShell command prompt, type the following command: **Import-Module ServerManager**. Then press Enter.
2.  Type the following command: **Add-WindowsFeature BITS-Compact-Server**. Then press Enter.

The following text-based example demonstrates installing the BITS Compact Server using Windows PowerShell cmdlets.

``` syntax
PS C:\> Import-Module ServerManager
PS C:\> Add-WindowsFeature BITS-Compact-Server

Success Restart Needed Exit Code Feature Result
------- -------------- --------- --------------
True    No             Success   {Compact Server}


PS C:\>
```

For information about using cmdlets, see the [Windows PowerShell](https://msdn.microsoft.com/library/dd835506(v=vs.85).aspx) documentation.

For more information about the Import-Module cmdlet, see [Import-Module](/previous-versions//dd347701(v=technet.10)) in the Microsoft TechNet Library. For help at the command line, type **get-help import-module**.

For more information about the Add-WindowsFeature cmdlet, see [Add-WindowsFeature](/previous-versions//dd347701(v=technet.10)) in the Microsoft TechNet Library. For help at the command line, type **get-help Add-WindowsFeature**.

**To install the BITS Compact Server by using Package Manager**

-   Enter the following command: **PkgMgr.exe /iu:LightweightServer**.

> [!Note]  
> The settings are lost if the Compact Server service is restarted or if the computer is rebooted.

 

## BITS Compact Server Remote Management

The BITS Compact Server with BITS Remote Management enables more secure remote file transfers. BITS Remote Management uses a Windows Management Instrumentation (WMI) provider to let a system administrator or a controller application remotely create BITS transfer jobs on the clients and to publish files for hosting on the BITS Compact Server. The BITS provider can also be used to enable an application to remotely use the BITS client in conjunction with the BITS Compact Server to transfer files from one remote computer to another remote computer.

For more information, see the [BITS provider](/previous-versions/windows/desktop/bitsprov/bits-provider) documentation.

## Related topics

<dl> <dt>

[BITS provider](/previous-versions/windows/desktop/bitsprov/bits-provider)
</dt> </dl>

 

 