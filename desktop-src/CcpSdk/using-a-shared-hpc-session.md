---
Description: 'By default, each client application initiates a new HPC session. Having separate sessions for applications that require dedicated compute resources for mission-critical, deadline-sensitive workloads, is appropriate.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '091ac9f6-c84a-46eb-90cd-100c865e0a33'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Using a Shared HPC Session
---

# Using a Shared HPC Session

By default, each client application initiates a new HPC session. Having separate sessions for applications that require dedicated compute resources for mission-critical, deadline-sensitive workloads, is appropriate.

However, you should consider sharing the session for cases where it costs more to load the service than to process the request. For example, it makes sense for a simple service that creates yield curves or cash flow curves to share the startup costs because it may take one minute to load all the data but only three seconds to complete the computation.

The following procedure describes how to share a session.

**To share a session**

1.  The client that starts the session must set the [SessionStartInfo.ShareSession](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.sessionstartinfo.sharesession.aspx) property to true.
2.  The clients that want to join the session must get the broker job associated with the session, or the client that starts the session must share the endpoint references that the scheduler returns when it creates the session (see [Session.NetTcpEndpointReference](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.session.nettcpendpointreference.aspx) and [Session.HtppEndpointReference](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.session.session.httpendpointreference.aspx)).

    The client that creates the session can share the broker's job identifier, or you can use the name of the service to look up the job (the scheduler uses the name of the service as part of the name of the job).

    To use the name to lookup the broker job, call the [**IScheduler::GetJobList**](frlrfMicrosoftHpcSchedulerISchedulerClassGetJobListTopic) method. You must use the [JobPropertyIds.State](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.state.aspx) and [JobPropertyIds.JobType](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.jobtype.aspx) filters when calling **GetJobList**. Set the [State](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.state.aspx) filter value to Running and the [JobType](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobpropertyids.jobtype.aspx) filter value to [JobType.Broker](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.jobtype.broker.aspx).

    Enumerate the jobs in the collection and search for a job name that contains the service's name (the service name will be a substring within the job name).

3.  Access the [ISchedulerJob::EndpointAddresses](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulerjob.endpointaddresses.aspx) property of the broker's job that you found.

    Typically, the session specifies only one binding type so you would use the first address in the collection. However, if the session contains multiple bindings, the client must disambiguate the endpoint addresses.

4.  Use the endpoint address when constructing a new proxy object (see EchoServiceClient in the [Creating a SOA Client](creating-a-soa-client.md) example) to bind your client to the session.

Note that services that use static data should load the data into memory at startup to help ensure a fast response time.

 

 



