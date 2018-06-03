---
title: SMB Management API
description: The SMB Management API provides WMI classes and methods to manage shares and share access.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9cd0ed3c-ef1c-4a06-bfdc-786dbee09115
ms.prod: windows-server-dev
ms.technology:
- server-message-block-(smb)
- windows-management-instrumentation
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SMB Management API

## Purpose

The SMB Management API provides WMI classes and methods to manage shares and share access.

## In this section

<dl> <dt>

[**MSFT\_SmbBandwidthLimit**](msft-smbbandwidthlimit.md)
</dt> <dd>

Represents an SMB bandwidth limit, which is used to throttle SMB traffic.

</dd> <dt>

[**MSFT\_SmbClientConfiguration**](msft-smbclientconfiguration.md)
</dt> <dd>

Represents the configuration settings for an SMB client.

</dd> <dt>

[**MSFT\_SmbClientNetworkInterface**](msft-smbclientnetworkinterface.md)
</dt> <dd>

Represents a network interface used by SMB client.

</dd> <dt>

[**MSFT\_SmbConnection**](msft-smbconnection.md)
</dt> <dd>

Represents a connection established from an SMB client to an SMB server from the client's perspective.

</dd> <dt>

[**MSFT\_SmbMapping**](msft-smbmapping.md)
</dt> <dd>

Represents an SMB mapping.

</dd> <dt>

[**MSFT\_SmbMultichannelConnection**](msft-smbmultichannelconnection.md)
</dt> <dd>

Represents an SMB connection network interface.

</dd> <dt>

[**MSFT\_SmbMultichannelConstraint**](msft-smbmultichannelconstraint.md)
</dt> <dd>

Represents a network interface that SMB can use to connect to a server.

</dd> <dt>

[**MSFT\_SmbOpenFile**](msft-smbopenfile.md)
</dt> <dd>

Represents a file that is opened on an SMB server from the server's perspective.

</dd> <dt>

[**MSFT\_SmbServerConfiguration**](msft-smbserverconfiguration.md)
</dt> <dd>

Represents the configuration of an SMB server.

</dd> <dt>

[**MSFT\_SmbServerNetworkInterface**](msft-smbservernetworkinterface.md)
</dt> <dd>

Represents an SMB server network interface.

</dd> <dt>

[**MSFT\_SmbSession**](msft-smbsession.md)
</dt> <dd>

Represents a session on an SMB server from the server's perspective.

</dd> <dt>

[**MSFT\_SmbShare**](msft-smbshare.md)
</dt> <dd>

Represents an SMB share.

</dd> <dt>

[**MSFT\_SmbShareAccessControlEntry**](msft-smbshareaccesscontrolentry.md)
</dt> <dd>

Represents the access permissions that have been granted to a share's users.

</dd> <dt>

[**MSFT\_SmbShareChangeEvent**](msft-smbsharechangeevent.md)
</dt> <dd>

This is an indication class. Any subscriber to it will receive an indication whenever a share is created, deleted, or modified.

</dd> <dt>

[**MSFT\_SmbWitnessClient**](msft-smbwitnessclient-.md)
</dt> <dd>

Represents an SMB witness client.

</dd> </dl>

## Developer audience

SMB Management API is designed for use by WMI developers who use C/C++, the Microsoft Visual Basic application, or a scripting language that has an engine on Windows and handles Microsoft ActiveX objects. Familiarity with COM programming is helpful but not required. For more information about WMI, see [Windows Management Instrumentation](https://msdn.microsoft.com/library/aa394582).

## Run-time requirements

The SMB Management API is supported on Windows-based operating systems beginning with Windows 8 and Windows Server 2012.

## Related topics

<dl> <dt>

[Network Share Management](https://msdn.microsoft.com/library/windows/desktop/bb525392)
</dt> </dl>

 

 




