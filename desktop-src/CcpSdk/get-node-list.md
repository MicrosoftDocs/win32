---
Description: 'Gets the values of the specified properties for all of the nodes in an HPC cluster.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'F89AF3E0-1814-4708-A127-CBA0604375C9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Get Node List
---

# Get Node List

Gets the values of the specified properties for all of the nodes in an HPC cluster.

## Request

You can specify the Get Node List request as follows.



| Method                     | Request URI                                                             |
|----------------------------|-------------------------------------------------------------------------|
| GET (before HPC Pack 2016) | https://*head\_node\_name*:*port*/WindowsHPC/*HPC\_cluster\_name*/Nodes |
| GET (HPC Pack 2016)        | https://*head\_node\_name*:*port*/WindowsHPC/Nodes                      |



 

For instances of the REST web service that are hosted in Azure, the head node name should have a format of *Windows\_Azure\_service\_name*.cloudapp.net.

To get the name to use for the HPC cluster, use the [**Get Clusters**](get-clusters.md) operation.

### URI Parameters

You can specify the following additional parameters on the request URI.



| Parameter    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *Properties* | Optional. A comma-separated list of the names for the properties of the nodes for which you want to get values. For a list of properties for which you can get values, see the Remarks section.<br/> If you do not specify the *Properties* parameter, the response contains values for all of the available properties of the nodes.<br/> If a property with a specified name does not exist for a node, an error occurs.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| api-version  | Required if the request does not contain the api-version header. Specifies the version of the operation to use for this request. To specify Microsoft HPC Pack 2008 R2 with Service Pack 3 (SP3), use a value of 2011-11-01. The minimum version that supports this operation is Microsoft HPC Pack 2008 R2 with SP3.<br/> The value of this URI parameter is ignored if the request also contains the api-version header.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| *QueryId*    | Specifies internal data from the x-ms-continuation-QueryId header from the response in the previous Get Node List operation in a continuation sequence of Get Node List operations. For more information, see the Response Headers section later in this topic.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| $filter      | Optional. Specifies OData filters to use for this request in the following format "$filter=&lt;filter1&gt;%20and%20&lt;filter2&gt;…". <br/> To filter the nodes by a valid node state, use the filter "NodeState%20eq%20&lt;NodeState&gt;". To retrieve nodes whose state changed after a certain date and time, use the filter "ChangeTimeFrom%20eq%20&lt;DateTime&gt;". <br/> A null value is ignored. <br/> The minimum version that supports this URI parameter is Microsoft HPC Pack 2012. To use this parameter, also specify the Render URI parameter set to RestPropRender and a minimum api-version value of 2012-11-01.<br/> Example: "$filter=NodeState%20eq%20draining%20and%20ChangeTimeFrom%20eq%202015-10-16&Render=RestPropRender&api-version=2012-11-01". For information about node states, see [NodeState](https://msdn.microsoft.com/library/microsoft.hpc.scheduler.properties.nodestate.aspx). |
| Render       | Required if the $filter URI parameter is specified. Set the value to RestPropRender to specify that the response body is formatted in XML compatible with Microsoft HPC Pack 2008 R2 with Service Pack 2 (SP2). The minimum version that supports this URI parameter is Microsoft HPC Pack 2012.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| SortNodesBy  | Optional. A node property by which nodes will be sorted. If this parameter is not specified or a property with a specified name does not exist for a node, the result will be sorted by node Id.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| RowsPerRead  | Optional. Specifies how many lines of data to retrieve each time. The default is set to 10. At least one record will be retrieved.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |



 

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



| Response Header           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|---------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| x-ms-hpc-authoritychain   | A comma-separated list of RFC 1918 IP addresses that indicate the sequence of instances of the REST web service that the operation called in order from to right.<br/> Only responses from instances of the REST web service that are hosted on Azure contain this header. Responses from instances of the REST web service that are hosted on premise omit this header.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| x-ms-continuation-QueryId | Enables large sets of data to be returned in smaller responses across a continuation sequence of several requests. The value of this header is to be assigned to the queryId query string parameter in the next call in the sequence of calls to the Get Node List operation. The response to the Get Node List operation contains this header as long as additional data remains to be processed. You use the values of this header for one operation in the queryId URI parameter for the next operation.<br/> The format of these data in this header is not guaranteed to remain unchanged. You should only copy the data in this header from one operation in a set of multiple operations to the queryId URI parameter for the next operation. You should not use the data in this header or depend on the format of the data in this header in any other way.<br/> For an example of how to use this header and URI parameter in a way that potential changes will not impact, see the code for the sample client applications for REST API. For information about how to get these sample client applications, see [Getting Sample Programs that use the REST API](creating-and-managing-jobs-with-the-web-service-interface.md#getting-sample-programs-that-use-the-rest-api).<br/> |



 

The response for this operation also includes standard HTTP headers. All standard headers conform to the [HTTP/1.1 protocol specification](http://www.w3.org/Protocols/rfc2616/rfc2616.mdl).

### Response Body

The format of the response body is as follows.


```XML
<ArrayOfObject xmlns="http://schemas.microsoft.com/HPCS2008R2/common" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
    <Object>
        <Properties>
            <Property>
                <Name>node1_property1_name</Name>
                <Value>node1_property1_value</Value>
           </Property>
           <Property>
               <Name>node1_property2_name</Name>
               <Value>node1_property2_value</Value>
           </Property>
           ...
        </Properties>
    </Object>    
    <Object>
        <Properties>
            <Property>
                <Name>node2_property1_name</Name>
                <Value>node2_property1_value</Value>
           </Property>
           <Property>
               <Name>node2_property2_name</Name>
               <Value>node2_property2_value</Value>
           </Property>
           ...
        </Properties>
    </Object>
    ...
</ArrayOfObject>
```



The following table describes each of the elements in the response XML.



| Element       | Description                                                |
|---------------|------------------------------------------------------------|
| ArrayOfObject | Represents the set of nodes in the HPC cluster.<br/> |
| Object        | Represents a single node.<br/>                       |
| Properties    | Represents the set of properties for the node.<br/>  |
| Property      | Represents a single property for the node.<br/>      |
| Name          | Contains the name of the property.<br/>              |
| Value         | Contains the value of the property.<br/>             |



 

## Remarks

The following table shows the node properties for which you can get the values or by which you can sort results. For information about the property, see the corresponding property of the ISchedulerNode interface in the managed API for Microsoft HPC Pack.



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



 

 




