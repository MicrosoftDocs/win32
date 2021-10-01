---
title: Installing the Provider
description: The procedure for installing the DNS WMI Provider differs based on the version of Windows on which it is installed.
ms.assetid: 5f2bd11a-bc1d-4a43-92d4-26392d2504e7
keywords:
- Domain Name System, WMI provider, installing
ms.topic: article
ms.date: 05/31/2018
---

# Installing the Provider

The procedure for installing the DNS WMI Provider differs based on the version of Windows on which it is installed. The following procedure describes how to install and set up the DNS WMI Provider on Windows 2000. To obtain the DNS WMI Provider for Windows 2000, download the following file:

**WARNING:** DNS WMI Provider files are not interchangeable. Windows 2000 DNS Servers require different files and a different procedure than Windows Server 2003 DNS Servers. The procedure for each is provided.

**To install the DNS WMI Provider on Windows 2000 Server**

1.  Obtain the DNS WMI Provider for Windows 2000 from the Windows 2000 Server Resource Kit, or download the file, Dnsprov.zip, from: ftp://ftp.microsoft.com/reskit/win2000/
2.  Copy the DNS WMI Provider (Dnsprov.dll) and Dnsschema.mof files to the &lt;winntdir&gt;\\system32\\wbem directory.
3.  Compile the MOF file. Doing so customizes the schema to match the server.

    **mofcomp dnsschema.mof**

4.  Register the DLL on the DNS Server.

    **regsvr32 dnsprov.dll**

5.  Scripts or programs that use the DNS WMI Provider to manage DNS Servers can then be used. The scripts or programs can be run from either the DNS Server, or from a client computer.
    > [!Note]  
    > The WMI SDK is not required to run the DNS WMI Provider, but it contains many useful tools.

     

The DNS WMI Provider must be installed on any DNS Server to be managed; the DNS scripts, however, can be run on the DNS Server or on a remote host.

**To install the DNS WMI Provider on Windows Server 2003**

-   For Windows Server 2003 operating systems, the DNS WMI Provider is automatically installed and registered, and its MOF file is compiled when the DNS Server service is installed.

 

 




