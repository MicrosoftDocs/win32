---
title: DtcInstance class
description: Represents a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: bb50e45d-505f-4d97-b894-5234f9c83515
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DtcInstance class
- DtcInstance class, described
topic_type:
- apiref
api_name:
- DtcInstance
- DtcInstance.DtcName
- DtcInstance.VirtualServerName
- DtcInstance.Status
- DtcInstance.OleTxEndpointCid
- DtcInstance.XAEndpointCid
- DtcInstance.UisEndpointCid
- DtcInstance.KtmRmEndpointCid
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DtcInstance class

Represents a DTC instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class DtcInstance
{
  string DtcName;
  string VirtualServerName;
  string Status;
  string OleTxEndpointCid;
  string XAEndpointCid;
  string UisEndpointCid;
  string KtmRmEndpointCid;
};
```

## Members

The **DtcInstance** class has these types of members:

-   [Properties](#properties)

### Properties

The **DtcInstance** class has these properties.

<dl> <dt>

**DtcName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the DTC instance.

</dd> <dt>

**KtmRmEndpointCid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The contact ID that is used by the KtmRm service.

</dd> <dt>

**OleTxEndpointCid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The contact ID used for the OleTx protocol.

</dd> <dt>

**Status**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The status of the instance.

</dd> <dt>

**UisEndpointCid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The contact ID used by the management endpoint of the instance.

</dd> <dt>

**VirtualServerName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the virtual server that is used by the instance.

</dd> <dt>

**XAEndpointCid**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The contact ID that is used for the XA protocol.

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

 

 





