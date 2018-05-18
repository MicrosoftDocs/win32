---
Description: 'Adds one or more jobs to the cluster and scheduling queue.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd9c66c22-0ad4-47f9-82b7-49f9e0b51004'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::QueueJobs method'
---

# ICluster::QueueJobs method

Adds one or more jobs to the cluster and scheduling queue.

## Syntax


```C++
HRESULT QueueJobs(
  [in]           IClusterEnumerable *jobs,
  [in]           BSTR               userName,
  [in]           BSTR               password,
  [in]           VARIANT_BOOL       isConsole,
  [in, optional] long               hwndParent,
  [out]          IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*jobs* \[in\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains one or more jobs that you want to add to the queue. For each item in the collection, set the variant type to VT\_DISPATCH. Query the [**IJob**](ijob.md) interface for the **IDispatch** interface and set the **pdispVal** member of the variant to the **IDispatch** interface.

</dd> <dt>

*userName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*user*, under which the job will run. The user name is limited to 80 Unicode characters.

If *userName* is **NULL**, empty, or not valid, the cluster searches the calling user's credential cache for the credentials to use. If the cache contains only one credential, that credential is used. If the cache does not exist or contains multiple credentials, the user is prompted for the credentials.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The RunAs user's password. The password is limited to 127 Unicode characters. If this parameter is **NULL** or empty, the method uses the cached credentials. See [**ICluster::SetCachedCredentials**](icluster-setcachedcredentials.md). If the credentials are not cached, the current user is prompted for the credentials. If the *isConsole* parameter is VARIANT\_TRUE, the user is prompted in the console window, otherwise, the standard credentials dialog box is used.

</dd> <dt>

*isConsole* \[in\]
</dt> <dd>

Set the value to VARIANT\_TRUE if the application is a console-mode application. Set the value to VARIANT\_FALSE if the application is a GUI application.

</dd> <dt>

*hwndParent* \[in, optional\]
</dt> <dd>

The handle to use as the parent window for the modal credentials dialog box. If 0, HWND\_DESKTOP is used. The handle is ignored if *isConsole* is VARIANT\_TRUE.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface than contains one or more job identifiers. The identifiers in this collection correspond directly to the jobs collection passed in the *jobs* parameter. When you enumerate the identifiers in this collection, the identifiers are returned as variants. The variant type is VT\_I4. The **lVal** member of the variant contains the identifier.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

If you need to add multiple jobs to the queue, calling this method provides better performance than calling the [**ICluster::QueueJob**](icluster-queuejob.md) method in a loop.

If the method fails to add one of the jobs to the scheduling queue, none of the jobs are added to the queue.

Calling this method is the same as calling both the [**ICluster::AddJobs**](icluster-addjobs.md) and [**ICluster::SubmitJobs**](icluster-submitjobs.md) methods.

## Examples

For an example that calls this method, see [Submitting a Job to the Scheduling Queue](submitting-a-job-to-the-scheduling-queue.md).

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddJobs**](icluster-addjobs.md)
</dt> <dt>

[**ICluster::QueueJob**](icluster-queuejob.md)
</dt> <dt>

[**ICluster::RequeueJobs**](icluster-requeuejobs.md)
</dt> <dt>

[**ICluster::SubmitJobs**](icluster-submitjobs.md)
</dt> </dl>

 

 




