---
Description: 'Adds the specified job to the cluster and scheduling queue.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '70cafe48-3226-43cf-bcc2-6c533d291810'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::QueueJob method'
---

# ICluster::QueueJob method

Adds the specified job to the cluster and scheduling queue.

## Syntax


```C++
HRESULT QueueJob(
  [in]           IJob         *Job,
  [in]           BSTR         userName,
  [in]           BSTR         password,
  [in]           VARIANT_BOOL isConsole,
  [in, optional] long         hwndParent,
  [out]          long         *pRetVal
);
```



## Parameters

<dl> <dt>

*Job* \[in\]
</dt> <dd>

An [**IJob**](ijob.md) interface. To get the interface pointer, call the [**ICluster::CreateJob**](icluster-createjob.md) method.

</dd> <dt>

*userName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*user*, under which the job will run. The user name is limited to 80 Unicode characters.

If *userName* is **NULL**, empty, or not valid, the cluster searches the calling user's credential cache for the credentials to use. If the cache contains only one credential, that credential is used. If the cache does not exist or contains multiple credentials, the user is prompted for the credentials.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The RunAs user's password. The password is limited to 127 Unicode characters. If this parameter is **NULL** or empty, the method uses the cached credentials. See [**ICluster::SetCachedCredentials**](icluster-setcachedcredentials.md). If the credentials are not cached, the current user is prompted for the credentials. If the *isConsole* parameter is VARIANT\_TRUE, the user is prompted in the console window; otherwise, the standard credentials dialog box is used.

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

The job identifier. The identifier is unique within the cluster.

Note that identifiers for jobs that are no longer in the cluster are reused.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Calling this method is the same as calling both the [**ICluster::AddJob**](icluster-addjob.md) and [**ICluster::SubmitJob**](icluster-submitjob.md) methods.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::AddJob**](icluster-addjob.md)
</dt> <dt>

[**ICluster::QueueJobs**](icluster-queuejobs.md)
</dt> <dt>

[**ICluster::RequeueJob**](icluster-requeuejob.md)
</dt> <dt>

[**ICluster::SubmitJob**](icluster-submitjob.md)
</dt> </dl>

 

 




