---
title: DtcNetworkSettings class
description: Represents network and security configuration settings for a DTC instance.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f9f04679-e4cd-4c6e-83d5-1ef1d837aeb2
ms.prod: windows-server-dev
ms.technology:
- distributed-transaction-coordinator
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DtcNetworkSettings class
- DtcNetworkSettings class, described
topic_type:
- apiref
api_name:
- DtcNetworkSettings
- DtcNetworkSettings.InboundTransactionsEnabled
- DtcNetworkSettings.OutboundTransactionsEnabled
- DtcNetworkSettings.RemoteClientAccessEnabled
- DtcNetworkSettings.RemoteAdministrationAccessEnabled
- DtcNetworkSettings.XATransactionsEnabled
- DtcNetworkSettings.LUTransactionsEnabled
- DtcNetworkSettings.AuthenticationLevel
api_location:
- MsDtcWmi.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DtcNetworkSettings class

Represents network and security configuration settings for a DTC instance.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[Version("1.0"), AMENDMENT]
class DtcNetworkSettings
{
  boolean InboundTransactionsEnabled;
  boolean OutboundTransactionsEnabled;
  boolean RemoteClientAccessEnabled;
  boolean RemoteAdministrationAccessEnabled;
  boolean XATransactionsEnabled;
  boolean LUTransactionsEnabled;
  string  AuthenticationLevel;
};
```

## Members

The **DtcNetworkSettings** class has these types of members:

-   [Properties](#properties)

### Properties

The **DtcNetworkSettings** class has these properties.

<dl> <dt>

**AuthenticationLevel**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The authentication level of the security settings.

</dd> <dt>

**InboundTransactionsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if inbound transactions are enabled; otherwise, **false**.

</dd> <dt>

**LUTransactionsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if LU transactions are enabled; otherwise, **false**.

</dd> <dt>

**OutboundTransactionsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if outbound transactions are enabled; otherwise, **false**.

</dd> <dt>

**RemoteAdministrationAccessEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if remote administration access is enabled; otherwise, **false**.

</dd> <dt>

**RemoteClientAccessEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if remote client access is enabled; otherwise, **false**.

</dd> <dt>

**XATransactionsEnabled**
</dt> <dd> <dl> <dt>

Data type: **boolean**
</dt> <dt>

Access type: Read-only
</dt> </dl>

**true** if XA transactions are enabled; otherwise, **false**.

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

 

 





