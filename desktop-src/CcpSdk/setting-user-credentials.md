---
Description: 'To run a task that is part of a job or that is executed as a command, you must specify the user credentials under which the task will run. You can specify the credentials when you submit the job or execute the command, or you can cache the credentials.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fea7fb4f-5204-4c4e-9fad-448073833e5e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Setting User Credentials
---

# Setting User Credentials

To run a task that is part of a job or that is executed as a command, you must specify the user credentials under which the task will run. You can specify the credentials when you submit the job or execute the command, or you can cache the credentials.

The following [**ICluster**](icluster.md) methods require user credentials:

-   [**ExecuteCommand**](icluster-executecommand.md)
-   [**ExecuteCommandWithPaging**](icluster-executecommandwithpaging.md)
-   [**QueueJob**](icluster-queuejob.md)
-   [**QueueJobs**](icluster-queuejobs.md)
-   [**SubmitJob**](icluster-submitjob.md)
-   [**SubmitJobs**](icluster-submitjobs.md)

You can specify credentials in one of the following ways:

-   Set the *userName* and *password* parameters to a valid user and password.
-   Set the *userName* parameter to a valid user and the *password* parameter to **NULL**. If the user's credentials are cached, the cached credentials are used; otherwise, the user is prompted for the password.
-   Set the *userName* and *password* parameters to **NULL**. If the cache contains the credentials for a single user, the cached credentials are used; otherwise, the user is prompted for the credentials to use.

For a job that has already been submitted, you can also call the [**ICluster::SetJobCredentials**](icluster-setjobcredentials.md) or [**ICluster::SetJobCredentialsFromCache**](icluster-setjobcredentialsfromcache.md) method to change the credentials that are used.

To cache credentials, call the [**ICluster::SetCachedCredentials**](icluster-setcachedcredentials.md) method. Each cluster manages its own credentials cache (if you specify credentials on cluster A, the credentials are not available to cluster B). The cluster creates a cache for each user that calls the **SetCachedCredentials** method. A user's cache can contain one or more valid credentials. If the credential already exists in the cache, the credential is overwritten.

If the cache contains credentials for a single user, you can set the *userName* and *password* parameters to **NULL** for [**SubmitJob**](icluster-submitjob.md) (or any method that asks for credentials) and the cluster will use the credentials from the cache by default. If the cache contains credentials for multiple users, the user is prompted for the credentials to use. If you specify the *userName* parameter and the user is found in the cache, the credentials are used; otherwise, the user is prompted for the credentials to use.

To remove credentials from the calling user's cache, call the [**ICluster::DeleteCachedCredentials**](icluster-deletecachedcredentials.md) method. Only the user that added the credentials to the cache can remove them.

For more information about how CCP handles credentials, see [Credential Handling](credential-handling.md).

## Related topics

<dl> <dt>

[Using CCP](using-ccp.md)
</dt> </dl>

 

 



