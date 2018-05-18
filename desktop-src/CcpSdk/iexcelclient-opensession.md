---
Description: 'Starts a new SOA session that uses the specified resource settings to perform calculations from the specified Excel workbook on the HPC cluster with the specified head node.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5025AFF5-5485-435F-B8B1-F0357FA2FC49'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'IExcelClient::OpenSession method'
---

# IExcelClient::OpenSession method

Starts a new SOA session that uses the specified resource settings to perform calculations from the specified Excel workbook on the HPC cluster with the specified head node.

## Syntax


```C++
HRESULT OpenSession(
  [in]           BSTR    headNode,
                 String  headNode,
  [in]           BSTR    remoteWorkbookPath,
  [in]           String  remoteWorkbookPath,
  [in, optional] VARIANT minResources,
  [in, optional] Variant minResources,
  [in, optional] VARIANT maxResources,
  [in, optional] Variant maxResources,
  [in, optional] VARIANT resourceType,
  [in, optional] Variant resourceType,
  [in, optional] BSTR    jobTemplate,
  [in, optional] String  jobTemplate,
  [in, optional] BSTR    serviceName,
  [in, optional] String  serviceName,
  [out, retval]  long    *pRetVal,
  [retval]       Long    pRetVal
);
```

<span codelanguage="VisualBasic"></span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th>VB</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><pre><code>pRetValpRetVal = .OpenSession( _
  ByVal headNode As BSTR, _
  ByVal headNode As String, _
  ByVal remoteWorkbookPath As BSTR, _
  ByVal remoteWorkbookPath As String, _
  [ ByVal minResources As VARIANT ], _
  [ ByVal minResources As Variant ], _
  [ ByVal maxResources As VARIANT ], _
  [ ByVal maxResources As Variant ], _
  [ ByVal resourceType As VARIANT ], _
  [ ByVal resourceType As Variant ], _
  [ ByVal jobTemplate As BSTR ], _
  [ ByVal jobTemplate As String ], _
  [ ByVal serviceName As BSTR ], _
  [ ByVal serviceName As String ] _
) As HRESULT</code></pre></td>
</tr>
</tbody>
</table>



## Parameters

<dl> <dt>*headNode* \[in\]</dt> <dd> 

|         |                                                                                                  |
|---------|--------------------------------------------------------------------------------------------------|
| **C++** | The name of the head node of the cluster on which you want to create the SOA session.<br/> |
| **VB**  | The name of the head node of the cluster on which you want to create the SOA session.<br/> |

 </dd> <dt>*remoteWorkbookPath* \[in\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                 |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | The path to the Excel workbook for which the session should perform calculations. This path is relative to the compute nodes of the HPC cluster, and the path can refer to a shared folder. This location must be accessible from the compute nodes.<br/> |
| **VB**  | The path to the Excel workbook for which the session should perform calculations. This path is relative to the compute nodes of the HPC cluster, and the path can refer to a shared folder. This location must be accessible from the compute nodes.<br/> |

 </dd> <dt>*minResources* \[in, optional\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | **VARIANT** that specifies an integer that indicates the minimum number of resource units that are specified in the *resourceType* parameter that the HPC Job Scheduler Service should allocate to the service job for the SOA session. This value should be greater than 0, but less than or equal to the value of the *maxResources* parameter and less than or equal to the number of resources of the specified type that are available in the HPC cluster.<br/> |
| **VB**  | **Variant** that specifies an integer that indicates the minimum number of resource units that are specified in the *resourceType* parameter that the HPC Job Scheduler Service should allocate to the service job for the SOA session. This value should be greater than 0, but less than or equal to the value of the *maxResources* parameter and less than or equal to the number of resources of the specified type that are available in the HPC cluster.<br/> |

 </dd> <dt>*maxResources* \[in, optional\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                                                                                                                |
|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | **VARIANT** that specifies an integer that indicates the maximum number of resource units that are specified in the *resourceType* parameter that the HPC Job Scheduler Service should allocate to the service job for the SOA session. This value should be greater than 0 and greater than or equal to the value of the *minResources* parameter.<br/> |
| **VB**  | **Variant** that specifies an integer that indicates the maximum number of resource units that are specified in the *resourceType* parameter that the HPC Job Scheduler Service should allocate to the service job for the SOA session. This value should be greater than 0 and greater than or equal to the value of the *minResources* parameter.<br/> |

 </dd> <dt>*resourceType* \[in, optional\]</dt> <dd> 

|         |                                                                                                                                                                                                                                                                    |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **C++** | **VARIANT** that specifies an integer value from the [**SessionUnitType**](sessionunittype.md) enumeration that indicates the type of resource that the HPC Job Scheduler Service should use to allocate resources to the service job for the session.<br/> |
| **VB**  | **Variant** that specifies an integer value from the [**SessionUnitType**](sessionunittype.md) enumeration that indicates the type of resource that the HPC Job Scheduler Service should use to allocate resources to the service job for the session.<br/> |

 </dd> <dt>*jobTemplate* \[in, optional\]</dt> <dd> 

|         |                                                      |
|---------|------------------------------------------------------|
| **C++** | The template to use for the service job. <br/> |
| **VB**  | The template to use for the service job. <br/> |

 </dd> <dt>*serviceName* \[in, optional\]</dt> <dd> 

|         |                                                                        |
|---------|------------------------------------------------------------------------|
| **C++** | The name of the service to run on the nodes of the cluster.<br/> |
| **VB**  | The name of the service to run on the nodes of the cluster.<br/> |

 </dd> <dt>*pRetVal* \[out, retval\]</dt> <dd> 

|         |                                                                       |
|---------|-----------------------------------------------------------------------|
| **C++** | The identifier of the SOA session that the method created.<br/> |
| **VB**  | The identifier of the SOA session that the method created.<br/> |

 </dd> </dl>

## Return value

### C++

Returns **S\_OK** unless an exception occurs.

### VB

The identifier of the SOA session that the method created.

## Remarks

You must call the [**IExcelClient::Initialize**](iexcelclient-initialize.md) method before you call the **IExcelClient::OpenSession** method.

## Requirements



|                         |                                                                                                    |
|-------------------------|----------------------------------------------------------------------------------------------------|
| Product<br/>      | HPC Pack 2008 R2 Client Utilities<br/>                                                       |
| Type library<br/> | <dl> <dt>Microsoft.Hpc.Excel.tlb</dt> </dl> |



## See also

<dl> <dt>

[**IExcelClient**](iexcelclient.md)
</dt> <dt>

[**IExcelClient::Initialize**](iexcelclient-initialize.md)
</dt> <dt>

[**IExcelClient::CloseSession**](iexcelclient-closesession.md)
</dt> </dl>

 

 




