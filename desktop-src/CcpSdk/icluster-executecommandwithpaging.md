---
Description: 'Executes a task on a specified group of nodes in the cluster. The output is returned in the requested page size.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '1076ac45-d552-40a0-86e0-b3c5ea60cbbc'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ICluster::ExecuteCommandWithPaging method'
---

# ICluster::ExecuteCommandWithPaging method

Executes a task on a specified group of nodes in the cluster. The output is returned in the requested page size.

## Syntax


```C++
HRESULT ExecuteCommandWithPaging(
  [in]           long               Id,
  [in]           ITask              *Task,
  [in]           BSTR               userName,
  [in]           BSTR               password,
  [in]           VARIANT_BOOL       isConsole,
  [in, optional] long               hwndParent,
  [in]           long               pageSize,
  [out]          IClusterEnumerable **pRetVal
);
```



## Parameters

<dl> <dt>

*Id* \[in\]
</dt> <dd>

The command identifier. To obtain this value, call the [**ICluster::GetNewCommandId**](icluster-getnewcommandid.md) method.

</dd> <dt>

*Task* \[in\]
</dt> <dd>

An [**ITask**](itask.md) interface of the task to execute. To create the task, call the [**ICluster::CreateTask**](icluster-createtask.md) method.

</dd> <dt>

*userName* \[in\]
</dt> <dd>

The name of the RunAs user, in the form *domain*\\*user*. The user name is limited to 80 Unicode characters.

If *userName* is **NULL**, empty, or not valid, the cluster searches the calling user's credential cache for the credentials to use. If the cache contains only one credential, it is used. If the cache does not exist or contains multiple credentials, the user is prompted for the credentials.

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

The handle to use as the parent window for the modal credentials dialog box. If 0, HWND\_DESKTOP is used. The handle is ignored if the *isConsole* parameter is VARIANT\_TRUE.

</dd> <dt>

*pageSize* \[in\]
</dt> <dd>

The number of Unicode characters to return in each page of the output. The minimum size is 2,048 Unicode characters and the maximum size is 20,480. If the value is outside this range, the method determines the page size.

</dd> <dt>

*pRetVal* \[out\]
</dt> <dd>

An [**IClusterEnumerable**](iclusterenumerable.md) interface that contains an [**IExecutionResult**](iexecutionresult.md) interface for each instance of the task (one result for each node on which the task ran). When you enumerate the items in this collection, the items are returned as variants. The variant type is VT\_DISPATCH. Query the **pdispVal** member for the **IExecutionResult** interface.

</dd> </dl>

## Return value

If the method succeeds, the return value is S\_OK. Otherwise, the return value is an error code. To get a description of the error, call the [**ICluster::get\_ErrorMessage**](icluster-get-errormessage.md) method.

## Remarks

This method can be called only by a cluster administrator.

An instance of the task runs on the nodes specified in the [**ITask::put\_RequiredNodes**](itask-put-requirednodes.md) method. If no nodes are specified, the command runs on each node in the cluster. The task does not wait in the queue to be scheduled. Standard output and standard error are captured in the result. To get the output in the specified page size, call the [**ICluster::ReadExecutionResult**](icluster-readexecutionresult.md) method in a loop until the output string is empty.

To cancel all instances, call the [**ICluster::EndCommand**](icluster-endcommand.md) method.

## Requirements



|                         |                                                                                       |
|-------------------------|---------------------------------------------------------------------------------------|
| Product<br/>      | Compute Cluster Pack Client Utilities<br/>                                      |
| Type library<br/> | <dl> <dt>Ccpapi.tlb</dt> </dl> |



## See also

<dl> <dt>

[**ICluster**](icluster.md)
</dt> <dt>

[**ICluster::EndCommand**](icluster-endcommand.md)
</dt> <dt>

[**ICluster::ExecuteCommand**](icluster-executecommand.md)
</dt> <dt>

[**ICluster::GetNewCommandId**](icluster-getnewcommandid.md)
</dt> </dl>

 

 




