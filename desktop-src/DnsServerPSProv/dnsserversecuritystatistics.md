---
title: DnsServerSecurityStatistics class
description: Represents DNS server statistics for security context processing.
audience: developer
ms.assetid: 3b3f607a-946b-417c-8a2b-483a3c408778
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerSecurityStatistics class
- DnsServerSecurityStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerSecurityStatistics
- DnsServerSecurityStatistics.SecurityContextCreate
- DnsServerSecurityStatistics.SecurityContextFree
- DnsServerSecurityStatistics.SecurityContextQueue
- DnsServerSecurityStatistics.SecurityContextQueueInNego
- DnsServerSecurityStatistics.SecurityContextQueueInNegoComplete
- DnsServerSecurityStatistics.SecurityContextQueueLength
- DnsServerSecurityStatistics.SecurityContextDequeue
- DnsServerSecurityStatistics.SecurityContextTimeout
- DnsServerSecurityStatistics.SecurityPackAlloc
- DnsServerSecurityStatistics.SecurityPackFree
- DnsServerSecurityStatistics.SecurityTKeyInvalid
- DnsServerSecurityStatistics.SecurityTKeyBadTime
- DnsServerSecurityStatistics.SecurityTSigFormError
- DnsServerSecurityStatistics.SecurityTSigEcho
- DnsServerSecurityStatistics.SecurityTSigBadKey
- DnsServerSecurityStatistics.SecurityTSigVerifySuccess
- DnsServerSecurityStatistics.SecurityTSigVerifyFailed
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerSecurityStatistics class

Represents DNS server statistics for security context processing.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerSecurityStatistics
{
  uint32 SecurityContextCreate;
  uint32 SecurityContextFree;
  uint32 SecurityContextQueue;
  uint32 SecurityContextQueueInNego;
  uint32 SecurityContextQueueInNegoComplete;
  uint32 SecurityContextQueueLength;
  uint32 SecurityContextDequeue;
  uint32 SecurityContextTimeout;
  uint32 SecurityPackAlloc;
  uint32 SecurityPackFree;
  uint32 SecurityTKeyInvalid;
  uint32 SecurityTKeyBadTime;
  uint32 SecurityTSigFormError;
  uint32 SecurityTSigEcho;
  uint32 SecurityTSigBadKey;
  uint32 SecurityTSigVerifySuccess;
  uint32 SecurityTSigVerifyFailed;
};
```

## Members

The **DnsServerSecurityStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerSecurityStatistics** class has these properties.

<dl> <dt>

**SecurityContextCreate**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of security contexts created by the server since the server was started.

</dd> <dt>

**SecurityContextDequeue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of security contexts removed from the queue for negotiation since the server was started.

</dd> <dt>

**SecurityContextFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of security contexts released by the server since the server was started.

</dd> <dt>

**SecurityContextQueue**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of security contexts queued in the queue for negotiation on the server since the server was started.

</dd> <dt>

**SecurityContextQueueInNego**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of security contexts entered in negotiation. since the server was started.

</dd> <dt>

**SecurityContextQueueInNegoComplete**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of security contexts that have completed negotiation since the server was started.

</dd> <dt>

**SecurityContextQueueLength**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of security contexts currently queued.

</dd> <dt>

**SecurityContextTimeout**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of security contexts in the negotiation list that timed out since the server was started.

</dd> <dt>

**SecurityPackAlloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of buffers allocated by the server for use with GSS-API signature validation.

</dd> <dt>

**SecurityPackFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of buffers for use with GSS-API signature validation released by the server.

</dd> <dt>

**SecurityTKeyBadTime**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of secure DNS update messages that had TKEY with a skewed time stamp.

</dd> <dt>

**SecurityTKeyInvalid**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of secure DNS update messages from which TKEY was successfully retrieved.

</dd> <dt>

**SecurityTSigBadKey**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of TSIG records received for which the cached security context could not be found.

</dd> <dt>

**SecurityTSigEcho**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of echo TSIG records received by the server, indicating that the remote server is not security aware.

</dd> <dt>

**SecurityTSigFormError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of TSIG records from which signature extraction failed.

</dd> <dt>

**SecurityTSigVerifyFailed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of TSIG records received for which signature verification failed.

</dd> <dt>

**SecurityTSigVerifySuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of TSIG records received for which the signature was successfully verified.

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

 

 





