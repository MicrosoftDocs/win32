---
Description: 'Sets the credentials for the specified job using credentials from the credential cache.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b3f6d5a8-de69-407f-a0bb-8d5fce4a647f'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::SetJobCredentialsFromCache method'
---

# ICluster::SetJobCredentialsFromCache method

Sets the credentials for the specified job using credentials from the credential cache.

## Syntax


```C++
HRESULT SetJobCredentialsFromCache(
  [in] long         jobId,
  [in] BSTR         userName,
  [in] VARIANT_BOOL isConsole,
  [in] long         hwndParent
);
```



## Parameters

<dl> <dt>

*jobId* \[in\]
</dt> <dd>

The job identifier. The [**ICluster::AddJob**](icluster-addjob.md) method returns this value. If you have an instance of the job that has already been added to the cluster, you can call the [**IJob::get\_Id**](ijob-get-id.md) method to get the identifier.

</dd> <dt>

*userName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*user*. The user name is limited to 80 Unicode characters.

If *userName* is **NULL**, empty, or not valid, the service searches the credential cache for the credentials to use. If the cache contains only one credential, that credential is used. However, if multiple credentials exist in the cache, the user is prompted for the credentials.

</dd> <dt>

*isConsole* \[in\]
</dt> <dd>

Set the value to VARIANT\_TRUE if the application is a console-mode application. Set the value to VARIANT\_FALSE if the application is a GUI application.

If the credentials are not cached, the user is prompted for the credentials. If the *isConsole* parameter is VARIANT\_TRUE, the user is prompted in the console window; otherwise, the standard credentials dialog box is used.

</dd> <dt>

*hwndParent* \[in\]
</dt> <dd>

The handle to use as the parent window for the modal credentials dialog box. If 0, HWND\_DESKTOP is used. The handle is ignored if *isConsole* is VARIANT\_TRUE.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

You would call this method after submitting a job to change the credentials that the job uses.

To add credentials to the cache, use the [**ICluster::SetCachedCredentials**](icluster-setcachedcredentials.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::SetCachedCredentials**](icluster-setcachedcredentials.md)
</dt> <dt>

[**ICluster::SetJobCredentials**](icluster-setjobcredentials.md)
</dt> </dl>

 

 




