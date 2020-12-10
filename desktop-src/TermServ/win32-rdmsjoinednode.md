---
title: Win32_RDMSJoinedNode class
description: Represents a server node that is managed by Remote Desktop Management Services (RDMS).
ms.assetid: 8751f3f7-dfb5-45bd-a6b1-758aa22a3569
ms.tgt_platform: multiple
keywords:
- Win32_RDMSJoinedNode class Remote Desktop Services
- Win32_RDMSJoinedNode class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- Win32_RDMSJoinedNode
- Win32_RDMSJoinedNode.FQDN
- Win32_RDMSJoinedNode.SID
- Win32_RDMSJoinedNode.OSVersion
- Win32_RDMSJoinedNode.IsRdcb
- Win32_RDMSJoinedNode.IsRdg
- Win32_RDMSJoinedNode.IsRdls
- Win32_RDMSJoinedNode.IsRdvh
- Win32_RDMSJoinedNode.IsRdwa
- Win32_RDMSJoinedNode.IsRdsh
- Win32_RDMSJoinedNode.IsWebAccessCertificateInstalled
- Win32_RDMSJoinedNode.IsGatewayCertificateInstalled
- Win32_RDMSJoinedNode.IsRedirectorCertificateInstalled
- Win32_RDMSJoinedNode.IsPublishingCertificateInstalled
api_location:
- RDMS.dll
api_type:
- DllExport
ms.topic: reference
ms.date: 05/31/2018
---

# Win32\_RDMSJoinedNode class

Represents a server node that is managed by Remote Desktop Management Services (RDMS).

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[dynamic, provider("Win32_RDManagement_Prov"), AMENDMENT]
class Win32_RDMSJoinedNode
{
  string  FQDN;
  string  SID;
  String  OSVersion;
  boolean IsRdcb;
  boolean IsRdg;
  boolean IsRdls;
  boolean IsRdvh;
  boolean IsRdwa;
  boolean IsRdsh;
  boolean IsWebAccessCertificateInstalled;
  boolean IsGatewayCertificateInstalled;
  boolean IsRedirectorCertificateInstalled;
  boolean IsPublishingCertificateInstalled;
};
```

## Members

The **Win32\_RDMSJoinedNode** class has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Win32\_RDMSJoinedNode** class has these methods.



| Method                                                                | Description                                                                                                                                                                                           |
|:----------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**GetJoinedNodeCount**](win32-rdmsjoinednode-getjoinednodecount.md) | **Windows Server 2012 R2 and Windows Server 2012:** This method is unavailable prior to Windows Server 2016.<br/> Gets the number of servers that have the specified role installed.<br/> |
| [**Join**](join-win32-rdmsjoinednode.md)                             | Adds a node to RDMS.<br/>                                                                                                                                                                       |
| [**Unjoin**](unjoin-win32-rdmsjoinednode.md)                         | Removes a node from RDMS.<br/>                                                                                                                                                                  |



 

### Properties

The **Win32\_RDMSJoinedNode** class has these properties.

<dl> <dt>

**FQDN**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**key**](/windows/desktop/WmiSdk/key-qualifier), [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Gets the fully qualified domain name of the node.

</dd> <dt>

**IsGatewayCertificateInstalled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server has a certificate to perform authentication for Remote Desktop gateway connections. **TRUE** if the certificate is installed; otherwise, **FALSE**.

</dd> <dt>

**IsPublishingCertificateInstalled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server has a certificate to sign Remote Desktop Protocol publishing files. **TRUE** if the certificate is installed; otherwise, **FALSE**.

</dd> <dt>

**IsRdcb**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server is Remote Desktop Connection Broker. **TRUE** if the server is a Remote Desktop Connection Broker; otherwise, **FALSE**.

</dd> <dt>

**IsRdg**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server is Remote Desktop gateway server. **TRUE** if the server is a Remote Desktop gateway server; otherwise, **FALSE**.

</dd> <dt>

**IsRdls**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server is Remote Desktop license server. **TRUE** if the server is a Remote Desktop license server; otherwise, **FALSE**.

</dd> <dt>

**IsRdsh**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server is Remote Desktop session host server. **TRUE** if the server is a Remote Desktop session host server; otherwise, **FALSE**.

</dd> <dt>

**IsRdvh**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server is Remote Desktop virtualization host. **TRUE** if the server is a Remote Desktop virtualization host; otherwise, **FALSE**.

</dd> <dt>

**IsRdwa**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server is Remote Desktop web access server. **TRUE** if the server is a Remote Desktop Web Access server; otherwise, **FALSE**.

</dd> <dt>

**IsRedirectorCertificateInstalled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server has a certificate to perform authentication for Remote Desktop Services deployment. **TRUE** if the certificate is installed; otherwise, **FALSE**.

</dd> <dt>

**IsWebAccessCertificateInstalled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read/write
</dt> </dl>

Gets and sets a value that indicates whether the server has a certificate to perform authentication for Remote Desktop Web Access. **TRUE** if the certificate is installed; otherwise, **FALSE**.

</dd> <dt>

**OSVersion**
</dt> <dd> <dl> <dt>

Data type: **String**
</dt> <dt>

Access type: Read/write
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (64)
</dt> </dl>

Gets and sets the version of the operating systems on the node.

</dd> <dt>

**SID**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**MaxLen**](/windows/desktop/WmiSdk/standard-qualifiers) (256)
</dt> </dl>

Gets the security identifier (SID) of the node.

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                              |
| Namespace<br/>                | Root\\cimv2\\rdms<br/>                                                                |
| MOF<br/>                      | <dl> <dt>RDManagement.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RDMS.dll</dt> </dl>         |



## See also

<dl> <dt>

[Remote Desktop Management Services Provider](rdms-api-reference.md)
</dt> </dl>

 

