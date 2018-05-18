---
title: NetworkControllerNodeClusterInfo class
description: Contains information on a network controller node cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0e2e1edd-bb8f-4d9f-b81d-d7e7b428c0e7'
ms.prod: 'windows-server-dev'
ms.technology: 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["NetworkControllerNodeClusterInfo class", "NetworkControllerNodeClusterInfo class, described"]
topic_type:
- apiref
api_name:
- NetworkControllerNodeClusterInfo
- NetworkControllerNodeClusterInfo.Name
- NetworkControllerNodeClusterInfo.Server
- NetworkControllerNodeClusterInfo.samAccountName
- NetworkControllerNodeClusterInfo.FaultDomain
- NetworkControllerNodeClusterInfo.IsSeedNode
- NetworkControllerNodeClusterInfo.CertificateRawData
- NetworkControllerNodeClusterInfo.Status
api_location:
- NCServerPSProvider.dll
api_type:
- DllExport
---

# NetworkControllerNodeClusterInfo class

Contains information on a network controller node cluster.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("NcServerPSProvider"), AMENDMENT]
class NetworkControllerNodeClusterInfo
{
  string  Name;
  string  Server;
  string  samAccountName;
  string  FaultDomain;
  boolean IsSeedNode;
  uint8   CertificateRawData[];
  string  Status;
};
```

## Members

The **NetworkControllerNodeClusterInfo** class has these types of members:

-   [Properties](#properties)

### Properties

The **NetworkControllerNodeClusterInfo** class has these properties.

<dl> <dt>

**CertificateRawData**
</dt> <dd> <dl> <dt>

Data type: **uint8** array
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Octetstring**
</dt> </dl>

Gets the cluster certificate.

</dd> <dt>

**FaultDomain**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the fault domain of the node.

</dd> <dt>

**IsSeedNode**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Returns **true** if the current instance this a seed node; otherwise, **false**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the name of the node.

</dd> <dt>

**samAccountName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the node name in "domain\\hostname$" format, used in Windows Authentication.

</dd> <dt>

**Server**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the IP address or FQDN of the node.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

Gets the node status.

The possible values are.

<dt>

<span id="Invalid"></span><span id="invalid"></span><span id="INVALID"></span>

**Invalid** ("Invalid")


</dt> <dd></dd> <dt>

<span id="Up"></span><span id="up"></span><span id="UP"></span>

**Up** ("Up")


</dt> <dd></dd> <dt>

<span id="Down"></span><span id="down"></span><span id="DOWN"></span>

**Down** ("Down")


</dt> <dd></dd> <dt>

<span id="Enabling"></span><span id="enabling"></span><span id="ENABLING"></span>

**Enabling** ("Enabling")


</dt> <dd></dd> <dt>

<span id="Disabling"></span><span id="disabling"></span><span id="DISABLING"></span>

**Disabling** ("Disabling")


</dt> <dd></dd> <dt>

<span id="Disabled"></span><span id="disabled"></span><span id="DISABLED"></span>

**Disabled** ("Disabled")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                   |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                    |
| Namespace<br/>                | Root\\Microsoft\\Windows\\NetworkController\\Server<br/>                                    |
| MOF<br/>                      | <dl> <dt>NCServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>NCServerPSProvider.dll</dt> </dl> |



 

 





