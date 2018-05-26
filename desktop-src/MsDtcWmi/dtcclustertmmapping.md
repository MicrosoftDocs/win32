---
title: DtcClusterTMMapping class
description: Represents a cluster DTC mapping of a cluster resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 62504688-e009-41e3-aba0-1da8a3a76b22
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DtcClusterTMMapping class
- DtcClusterTMMapping class, described
topic_type:
- apiref
api_name:
- DtcClusterTMMapping
- DtcClusterTMMapping.Name
- DtcClusterTMMapping.ApplicationType
- DtcClusterTMMapping.Application
- DtcClusterTMMapping.Local
- DtcClusterTMMapping.ClusterResourceName
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DtcClusterTMMapping class

Represents a cluster DTC mapping of a cluster resource.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class DtcClusterTMMapping
{
  string  Name;
  string  ApplicationType;
  string  Application;
  boolean Local;
  string  ClusterResourceName;
};
```

## Members

The **DtcClusterTMMapping** class has these types of members:

-   [Properties](#properties)

### Properties

The **DtcClusterTMMapping** class has these properties.

<dl> <dt>

**Application**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the application that is associated with the mapping.

</dd> <dt>

**ApplicationType**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The application type that is associated with the mapping.

</dd> <dt>

**ClusterResourceName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the cluster DTC resource that is associated with the mapping.

</dd> <dt>

**Local**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if the application type is local; otherwise, **false**.

</dd> <dt>

**Name**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the DTC mapping.

</dd> </dl>

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                    |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                          |
| Namespace<br/>                | Root\\MsDTC<br/>                                                                  |
| MOF<br/>                      | <dl> <dt>Msdtcwmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsDtcWmi.dll</dt> </dl> |



## See also

<dl> <dt>

[Distributed Transaction Coordinator WMI Provider](distributed-transaction-coordinator-wmi-provider-portal.md)
</dt> </dl>

 

 





