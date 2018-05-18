---
Description: 'Gets the values of all of the properties for the specified node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2F5098A3-3D94-4C27-8AC0-2F67FC603B5E'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Get Node
---

# Get Node

Gets the values of all of the properties for the specified node.

## Request

You can specify the Get Node request as follows.



| Method                     | Request URI                                                                         |
|----------------------------|-------------------------------------------------------------------------------------|
| GET (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Node/*node\_name* |
| GET (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/Node/*node\_name*                      |



 

For instances of the REST web service that are hosted in Azure, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for the HPC cluster, use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version | Required if the request does not contain the api-version header. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/> |



 

### Request Headers

The following table describes required and optional request headers.



| Request Header | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| api-version    | Required if the request does not include the api-version URI parameter. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with SP3, use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value specified in this header overrides the value specified in the api-version URI parameter if both are specified.<br/> |



 

### Request Body

None.

## Response

The response includes an HTTP status code, a set of response headers, and a response body in XML format.

### Status Code

A successful operation returns status code 200 (OK).

If the request includes neither the api-version URI parameter nor the api-version header, the operation returns status code 400 (Bad Request).

For more information about status codes, see [HttpStatusCode](https://msdn.microsoft.com/library/system.net.httpstatuscode.aspx).

The error response will be contained in a descriptive XML response (Note: Values will vary based on the error):


```XML
<HpcWebServiceFault xmlns="http://schemas.microsoft.com/HPCS2008R2/common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
  <Code>267386880</Code>
  <Message>Error message text.</Message>
  <Values i:nil="true" xmlns:a="http://schemas.datacontract.org/2004/07/System.Collections.Generic"/>
</HpcWebServiceFault>
```



### Response Headers

The response for this operation includes the following headers.



| Response Header         | Description                                                                                                                                                                                                                                                                                                                                                                               |
|-------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| x-ms-hpc-authoritychain | A comma-separated list of RFC 1918 IP addresses that indicate the sequence of instances of the REST web service that the operation called in order from to right.<br/> Only responses from instances of the REST web service that are hosted on Azure contain this header. Responses from instances of the REST web service that are hosted on premise omit this header.<br/> |



 

The response for this operation also includes standard HTTP headers. All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

The format of the response body is as follows.


```XML
<ArrayOfProperty xmlns="http://schemas.microsoft.com/HPCS2008R2/common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
    <Property>
        <Name>node_property1_name</Name>
        <Value>node_property1_value</Value>
    </Property>
    <Property>
        <Name>node_property2_name</Name>
        <Value>node_property2_value</Value>
    </Property>
    ...
</ArrayOfProperty>
```



The following table describes each of the elements in the response XML.



| Element         | Description                                               |
|-----------------|-----------------------------------------------------------|
| ArrayOfProperty | Represents the set of properties for the node.<br/> |
| Property        | Represents a single property for the node.<br/>     |
| Name            | Contains the name of the property.<br/>             |
| Value           | Contains the value of the property.<br/>            |



 

## Remarks

The following table shows the node properties for which this operation gets the values. For information about the property, see the corresponding property of the ISchedulerNode interface in the managed API for Windows HPC Server.



| Property         | Corresponding ISchedulerNode Property                                                                                              |
|------------------|------------------------------------------------------------------------------------------------------------------------------------|
| Availability     | [ISchedulerNode.Availability](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.availability.aspx)         |
| AzureServiceName | [ISchedulerNode.AzureServiceName](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.azureservicename.aspx) |
| CpuSpeed         | [ISchedulerNode.CpuSpeed](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.cpuspeed.aspx)                 |
| DnsSuffix        | [ISchedulerNode.DnsSuffix](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.dnssuffix.aspx)               |
| Guid             | [ISchedulerNode.Guid](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.guid.aspx)                         |
| Id               | [ISchedulerNode.Id](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.id.aspx)                             |
| JobType          | [ISchedulerNode.JobType](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.jobtype.aspx)                   |
| Location         | [ISchedulerNode.Location](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.location.aspx)                 |
| MemorySize       | [ISchedulerNode.MemorySize](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.memorysize.aspx)             |
| MoveToOffline    | [ISchedulerNode.MoveToOffline](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.movetooffline.aspx)       |
| Name             | [ISchedulerNode.Name](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.name.aspx)                         |
| NodeGroups       | [ISchedulerNode.NodeGroups](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.nodegroups.aspx)             |
| NumCores         | [ISchedulerNode.NumberOfCores](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.numberofcores.aspx)       |
| NumSockets       | [ISchedulerNode.NumberOfSockets](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.numberofsockets.aspx)   |
| OfflineTime      | [ISchedulerNode.OfflineTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.offlinetime.aspx)           |
| OnlineTime       | [ISchedulerNode.OnlineTime](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.onlinetime.aspx)             |
| Reachable        | [ISchedulerNode.Reachable](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.reachable.aspx)               |
| State            | [ISchedulerNode.State](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.ischedulernode.state.aspx)                       |



 

## Requirements



|                    |                                                                                |
|--------------------|--------------------------------------------------------------------------------|
| Product<br/> | HPC Pack 2008 R2 with at least SP3, or a later version of HPC Pack.<br/> |



 

 




