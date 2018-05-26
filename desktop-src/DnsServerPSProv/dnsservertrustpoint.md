---
title: DnsServerTrustPoint class
description: Retrieves settings for a trust point on a DNS server.
audience: developer
ms.assetid: 317aa5f3-41f4-4037-8b86-a47f61b96c91
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerTrustPoint class
- DnsServerTrustPoint class, described
topic_type:
- apiref
api_name:
- DnsServerTrustPoint
- DnsServerTrustPoint.TrustPointName
- DnsServerTrustPoint.TrustPointState
- DnsServerTrustPoint.LastActiveRefreshTime
- DnsServerTrustPoint.NextActiveRefreshTime
- DnsServerTrustPoint.LastSuccessfulActiveRefreshTime
- DnsServerTrustPoint.LastActiveRefreshResult
- DnsServerTrustPoint.LastActiveRefreshResultDescription
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DnsServerTrustPoint class

Retrieves settings for a trust point on a DNS server.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerTrustPoint
{
  string   TrustPointName;
  string   TrustPointState;
  datetime LastActiveRefreshTime;
  datetime NextActiveRefreshTime;
  datetime LastSuccessfulActiveRefreshTime;
  uint32   LastActiveRefreshResult;
  string   LastActiveRefreshResultDescription;
};
```

## Members

The **DnsServerTrustPoint** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerTrustPoint** class has these properties.

<dl> <dt>

**LastActiveRefreshResult**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The error code for the last active refresh attempt for the trust point. This property is returns "0" for a success and an error code for a failure.

</dd> <dt>

**LastActiveRefreshResultDescription**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

A user friendly description for **LastActiveRefreshResult**.

</dd> <dt>

**LastActiveRefreshTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when active refresh was attempted for the trust point.

</dd> <dt>

**LastSuccessfulActiveRefreshTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when active refresh was successful for the trust point.

</dd> <dt>

**NextActiveRefreshTime**
</dt> <dd> <dl> <dt>

Data type: **datetime**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The time when active refresh is scheduled to happen for the trust point.

</dd> <dt>

**TrustPointName**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The name of the trust point.

</dd> <dt>

**TrustPointState**
</dt> <dd> <dl> <dt>

Data type: **string**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The state of the trust point.

The possible values are.

<dt>

<span id="Initialized"></span><span id="initialized"></span><span id="INITIALIZED"></span>

**Initialized** ("Initialized")


</dt> <dd></dd> <dt>

<span id="DSPending"></span><span id="dspending"></span><span id="DSPENDING"></span>

**DSPending** ("DSPending")


</dt> <dd></dd> <dt>

<span id="DSInvalid"></span><span id="dsinvalid"></span><span id="DSINVALID"></span>

**DSInvalid** ("DSInvalid")


</dt> <dd></dd> <dt>

<span id="AddPending"></span><span id="addpending"></span><span id="ADDPENDING"></span>

**AddPending** ("AddPending")


</dt> <dd></dd> <dt>

<span id="Valid"></span><span id="valid"></span><span id="VALID"></span>

**Valid** ("Valid")


</dt> <dd></dd> <dt>

<span id="Missing"></span><span id="missing"></span><span id="MISSING"></span>

**Missing** ("Missing")


</dt> <dd></dd> <dt>

<span id="Revoked"></span><span id="revoked"></span><span id="REVOKED"></span>

**Revoked** ("Revoked")


</dt> <dd></dd> <dt>

<span id="Deleted"></span><span id="deleted"></span><span id="DELETED"></span>

**Deleted** ("Deleted")


</dt> <dd></dd> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                                    |
|-------------------------------------|----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                     |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Dns<br/>                                                           |
| MOF<br/>                      | <dl> <dt>DnsServerPSProvider.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>DnsServerPSProvider.dll</dt> </dl> |



## See also

<dl> <dt>

[DnsServerPSProvider Provider](dns-server-classes.md)
</dt> </dl>

 

 





