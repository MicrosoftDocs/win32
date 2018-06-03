---
title: DnsServerRecursionStatistics class
description: DNS server's statistics related to recursive resource record lookups.
audience: developer
ms.assetid: c88de9b4-72cf-499d-b45f-28dfc02ee005
ms.prod: windows-server-dev
ms.technology:
- dns-server
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- DnsServerRecursionStatistics class
- DnsServerRecursionStatistics class, described
topic_type:
- apiref
api_name:
- DnsServerRecursionStatistics
- DnsServerRecursionStatistics.ReferalPasses
- DnsServerRecursionStatistics.QueriesRecursed
- DnsServerRecursionStatistics.OriginalQuestionRecursed
- DnsServerRecursionStatistics.AdditionalRecursed
- DnsServerRecursionStatistics.TotalQuestionsRecursed
- DnsServerRecursionStatistics.Retries
- DnsServerRecursionStatistics.LookupPasses
- DnsServerRecursionStatistics.Forwards
- DnsServerRecursionStatistics.Sends
- DnsServerRecursionStatistics.Responses
- DnsServerRecursionStatistics.ResponsesUnmatched
- DnsServerRecursionStatistics.ResponsesMismatched
- DnsServerRecursionStatistics.ResponseFromForwarder
- DnsServerRecursionStatistics.ResponseAuthoritative
- DnsServerRecursionStatistics.ResponseNotAuthoritative
- DnsServerRecursionStatistics.ResponseAnswer
- DnsServerRecursionStatistics.ResponseNameError
- DnsServerRecursionStatistics.ResponseRCode
- DnsServerRecursionStatistics.ResponseEmpty
- DnsServerRecursionStatistics.ResponseDelegation
- DnsServerRecursionStatistics.ResponseNonZoneData
- DnsServerRecursionStatistics.ResponseUnsecure
- DnsServerRecursionStatistics.ResponseBadPacket
- DnsServerRecursionStatistics.SendResponseDirect
- DnsServerRecursionStatistics.ContinueCurrentRecursion
- DnsServerRecursionStatistics.ContinueCurrentLookup
- DnsServerRecursionStatistics.ContinueNextLookup
- DnsServerRecursionStatistics.RootNsQuery
- DnsServerRecursionStatistics.RootNsResponse
- DnsServerRecursionStatistics.CacheUpdateAlloc
- DnsServerRecursionStatistics.CacheUpdateResponse
- DnsServerRecursionStatistics.CacheUpdateFree
- DnsServerRecursionStatistics.CacheUpdateRetry
- DnsServerRecursionStatistics.SuspendedQuery
- DnsServerRecursionStatistics.ResumeSuspendedQuery
- DnsServerRecursionStatistics.TimedoutQueries
- DnsServerRecursionStatistics.FinalTimeoutQueued
- DnsServerRecursionStatistics.FinalTimeoutExpired
- DnsServerRecursionStatistics.RecursionFailure
- DnsServerRecursionStatistics.ServerFailure
- DnsServerRecursionStatistics.PartialFailure
- DnsServerRecursionStatistics.CacheUpdateFailure
- DnsServerRecursionStatistics.RecursePassFailure
- DnsServerRecursionStatistics.FailureReachAuthority
- DnsServerRecursionStatistics.FailureReachPreviousResponse
- DnsServerRecursionStatistics.TcpTry
- DnsServerRecursionStatistics.TcpConnect
- DnsServerRecursionStatistics.TcpQuery
- DnsServerRecursionStatistics.TcpResponse
- DnsServerRecursionStatistics.TcpDisconnect
- DnsServerRecursionStatistics.DiscardedDuplicateQueries
- DnsServerRecursionStatistics.DuplicateCoalesedQueries
- DnsServerRecursionStatistics.GnzLocalQuery
- DnsServerRecursionStatistics.GnzRemoteQuery
- DnsServerRecursionStatistics.GnzRemoteResponse
- DnsServerRecursionStatistics.GnzRemoteResponseCacheSuccess
- DnsServerRecursionStatistics.GnzRemoteResponseCacheFailure
- DnsServerRecursionStatistics.CacheLockingDiscards
api_location:
- DnsServerPSProvider.dll
api_type:
- DllExport
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsServerRecursionStatistics class

DNS server's statistics related to recursive resource record lookups.

The following syntax is simplified from Managed Object Format (MOF) code and includes all of the inherited properties.

## Syntax

``` syntax
[ClassVersion("1.0.0"), dynamic, provider("DnsServerPSProvider"), AMENDMENT]
class DnsServerRecursionStatistics
{
  uint32 ReferalPasses;
  uint32 QueriesRecursed;
  uint32 OriginalQuestionRecursed;
  uint32 AdditionalRecursed;
  uint32 TotalQuestionsRecursed;
  uint32 Retries;
  uint32 LookupPasses;
  uint32 Forwards;
  uint32 Sends;
  uint32 Responses;
  uint32 ResponsesUnmatched;
  uint32 ResponsesMismatched;
  uint32 ResponseFromForwarder;
  uint32 ResponseAuthoritative;
  uint32 ResponseNotAuthoritative;
  uint32 ResponseAnswer;
  uint32 ResponseNameError;
  uint32 ResponseRCode;
  uint32 ResponseEmpty;
  uint32 ResponseDelegation;
  uint32 ResponseNonZoneData;
  uint32 ResponseUnsecure;
  uint32 ResponseBadPacket;
  uint32 SendResponseDirect;
  uint32 ContinueCurrentRecursion;
  uint32 ContinueCurrentLookup;
  uint32 ContinueNextLookup;
  uint32 RootNsQuery;
  uint32 RootNsResponse;
  uint32 CacheUpdateAlloc;
  uint32 CacheUpdateResponse;
  uint32 CacheUpdateFree;
  uint32 CacheUpdateRetry;
  uint32 SuspendedQuery;
  uint32 ResumeSuspendedQuery;
  uint32 TimedoutQueries;
  uint32 FinalTimeoutQueued;
  uint32 FinalTimeoutExpired;
  uint32 RecursionFailure;
  uint32 ServerFailure;
  uint32 PartialFailure;
  uint32 CacheUpdateFailure;
  uint32 RecursePassFailure;
  uint32 FailureReachAuthority;
  uint32 FailureReachPreviousResponse;
  uint32 TcpTry;
  uint32 TcpConnect;
  uint32 TcpQuery;
  uint32 TcpResponse;
  uint32 TcpDisconnect;
  uint32 DiscardedDuplicateQueries;
  uint32 DuplicateCoalesedQueries;
  uint32 GnzLocalQuery;
  uint32 GnzRemoteQuery;
  uint32 GnzRemoteResponse;
  uint32 GnzRemoteResponseCacheSuccess;
  uint32 GnzRemoteResponseCacheFailure;
  uint32 CacheLockingDiscards;
};
```

## Members

The **DnsServerRecursionStatistics** class has these types of members:

-   [Properties](#properties)

### Properties

The **DnsServerRecursionStatistics** class has these properties.

<dl> <dt>

**AdditionalRecursed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of recursions performed to return additional data or CNAME.

</dd> <dt>

**CacheLockingDiscards**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server discarded a cache update due to cache record locking.

</dd> <dt>

**CacheUpdateAlloc**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server allocated a query to be sent to update a cache entry.

</dd> <dt>

**CacheUpdateFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received failure for self-generated cache update recursion queries to remote servers.

</dd> <dt>

**CacheUpdateFree**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server released a query request or response packet sent to update a cache entry.

</dd> <dt>

**CacheUpdateResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received responses for a query sent to update a cache entry.

</dd> <dt>

**CacheUpdateRetry**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server reattempted a query to update cache entry information.

</dd> <dt>

**ContinueCurrentLookup**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received a response from a remote DNS server while processing a client query and restarted recursion.

</dd> <dt>

**ContinueCurrentRecursion**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of additional remote queries generated by the DNS server during normal query processing.

</dd> <dt>

**ContinueNextLookup**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server started a lookup with the next query.

</dd> <dt>

**DiscardedDuplicateQueries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server discarded a query that was received from the same client with the same transaction ID when there was already a query with the same query name, type ID, and transaction ID outstanding.

</dd> <dt>

**DuplicateCoalesedQueries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server coalesced a query that was received from a client while another query with the same query name and type ID was outstanding at the server for processing.

</dd> <dt>

**FailureReachAuthority**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server failed to perform recursive lookups on queries, because it failed to reach an authoritative server.

</dd> <dt>

**FailureReachPreviousResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received failure while performing recursive lookup on queries, because the query recursed back to the domain from which a name server had already responded.

</dd> <dt>

**FinalTimeoutExpired**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of recursive queries expired without the server receiving any response.

</dd> <dt>

**FinalTimeoutQueued**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of recursive queries enlisted to wait for final time-out before they expire.

</dd> <dt>

**Forwards**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of recursive queries sent to forwarding servers.

</dd> <dt>

**GnzLocalQuery**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times a GNZ lookup query was answered locally.

</dd> <dt>

**GnzRemoteQuery**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times a GNZ lookup query was sent to a remote server.

</dd> <dt>

**GnzRemoteResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times a GNZ lookup query response was received from a remote server.

</dd> <dt>

**GnzRemoteResponseCacheFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received failure for GNZ cache update query requests sent to a remote server.

</dd> <dt>

**GnzRemoteResponseCacheSuccess**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times a GNZ cache update query response was successfully received from a remote server.

</dd> <dt>

**LookupPasses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of recursive lookups performed.

</dd> <dt>

**OriginalQuestionRecursed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of new recursive queries initiated

</dd> <dt>

**PartialFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received failures for recursion queries to remote servers, when it had already received an answer but was looking up additional records.

</dd> <dt>

**QueriesRecursed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of queries received that required recursive lookups.

</dd> <dt>

**RecursePassFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server failed to perform recursive lookups on queries.

</dd> <dt>

**RecursionFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received failures for recursion queries to remote servers.

</dd> <dt>

**ReferalPasses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server returned a referral value.

</dd> <dt>

**ResponseAnswer**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of responses received from other servers for recursive queries.

</dd> <dt>

**ResponseAuthoritative**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of responses received from the server authoritative for the zone.

</dd> <dt>

**ResponseBadPacket**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of bad response packets received.

</dd> <dt>

**ResponseDelegation**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of delegation responses received by the server.

</dd> <dt>

**ResponseEmpty**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of empty responses received from other servers.

</dd> <dt>

**ResponseFromForwarder**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of responses received from forwarders.

</dd> <dt>

**ResponseNameError**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of name errors received by the server.

</dd> <dt>

**ResponseNonZoneData**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of error responses when a name is not found in the zone.

</dd> <dt>

**ResponseNotAuthoritative**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of responses received from a server not authoritative for the zone.

</dd> <dt>

**ResponseRCode**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of errors other than name errors received by the server.

</dd> <dt>

**Responses**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of query responses received by the server.

</dd> <dt>

**ResponsesMismatched**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of responses received for which an outstanding query with a matching transaction-id was located but response was invalid for the query.

</dd> <dt>

**ResponsesUnmatched**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of responses received for which an outstanding query with a matching transaction-id could not be located.

</dd> <dt>

**ResponseUnsecure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of unsecure responses received when the server is configured to receive secure responses.

</dd> <dt>

**ResumeSuspendedQuery**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server resumed a suspended query that was needed to update cache entry information

</dd> <dt>

**Retries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of retries performed for recursive queries sent by the server.

</dd> <dt>

**RootNsQuery**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server sent a query for a root name server.

</dd> <dt>

**RootNsResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server processed a response from one of its root servers.

</dd> <dt>

**SendResponseDirect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of responses that the DNS server received from remote servers and sent directly to clients.

</dd> <dt>

**Sends**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The total number of recursive queries sent by the server.

</dd> <dt>

**ServerFailure**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server sent failures to the client.

</dd> <dt>

**SuspendedQuery**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server suspended sending a query needed to update cache entry information.

</dd> <dt>

**TcpConnect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server successfully established a TCP connection to send a recursive query.

</dd> <dt>

**TcpDisconnect**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server disconnected a connection that was established to send a recursive query over TCP to a remote server.

</dd> <dt>

**TcpQuery**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server sent a recursive query over TCP.

</dd> <dt>

**TcpResponse**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server received a recursive query response over TCP.

</dd> <dt>

**TcpTry**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of times the server started a recursive query over TCP.

</dd> <dt>

**TimedoutQueries**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of timed-out recursive queries.

</dd> <dt>

**TotalQuestionsRecursed**
</dt> <dd> <dl> <dt>

Data type: **uint32**
</dt> <dt>

Access type: Read-only
</dt> </dl>

The number of total recursions including original and additional.

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

 

 





