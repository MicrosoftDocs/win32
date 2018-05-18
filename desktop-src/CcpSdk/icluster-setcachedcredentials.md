---
Description: 'Sets credentials for the specified user in the credential cache.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'ff215125-28bb-44bc-ba22-168ad7330852'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::SetCachedCredentials method'
---

# ICluster::SetCachedCredentials method

Sets credentials for the specified user in the credential cache.

## Syntax


```C++
HRESULT SetCachedCredentials(
  [in]           BSTR         userName,
  [in]           BSTR         password,
  [in]           VARIANT_BOOL isConsole,
  [in, optional] long         hwndParent
);
```



## Parameters

<dl> <dt>

*userName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*user*, under which the job will run. If **NULL**, the method adds the calling user's credential to the cache. The user name is limited to 80 Unicode characters.

</dd> <dt>

*password* \[in\]
</dt> <dd>

The RunAs user's password. The password is limited to 127 Unicode characters. If this parameter is **NULL** or empty, the current user is prompted for the credentials. If the *isConsole* parameter is VARIANT\_TRUE, the user is prompted in the console window; otherwise, the standard credentials dialog box is used.

</dd> <dt>

*isConsole* \[in\]
</dt> <dd>

Set the value to VARIANT\_TRUE if the application is a console-mode application. Set the value to VARIANT\_FALSE if the application is a GUI application.

</dd> <dt>

*hwndParent* \[in, optional\]
</dt> <dd>

The handle to use as the parent window for the modal credentials dialog box. If 0, HWND\_DESKTOP is used. The handle is ignored if *isConsole* is VARIANT\_TRUE.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

Each cluster manages its own credentials cache. (If you specify credentials on cluster A, the credentials are not available to cluster B.) The cluster creates a cache for each user that calls this method. A user's cache can contain one or more valid credentials. If the credential already exists in the cache, the credential is overwritten.

If you call the [**ICluster::SubmitJob**](icluster-submitjob.md) method (or any method that asks for credentials) and set the *userName* parameter to **NULL**, the cluster searches the calling user's credential cache for the credentials to use. If the cache contains only one credential, that credential is used. If the cache does not exist or contains multiple credentials, the user is prompted for the credentials.

To specify cached credentials for a job after the job has been queued, call the [**ICluster::SetJobCredentialsFromCache**](icluster-setjobcredentialsfromcache.md) method.

To delete cached credentials, use the [**ICluster::DeleteCachedCredentials**](icluster-deletecachedcredentials.md) method. Only the user that cached the credentials can delete the credentials.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::DeleteCachedCredentials**](icluster-deletecachedcredentials.md)
</dt> <dt>

[**ICluster::SetJobCredentials**](icluster-setjobcredentials.md)
</dt> <dt>

[**ICluster::SetJobCredentialsFromCache**](icluster-setjobcredentialsfromcache.md)
</dt> </dl>

 

 




