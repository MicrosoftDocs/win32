---
title: ClusResDependencies.AddItem method
description: Adds an existing cluster resource to the dependency collection.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f8462df8-dece-423f-a585-5774411401c8
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- AddItem method Failover Cluster
- AddItem method Failover Cluster , ClusResDependencies class
- ClusResDependencies class Failover Cluster , AddItem method
topic_type:
- apiref
api_name:
- ClusResDependencies.AddItem
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ClusResDependencies.AddItem method

\[The **AddItem** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Adds an existing cluster [resource](resources.md) to the [*dependency*](d-gly.md#-wolf-dependency-gly) collection.

## Syntax


```VB
ClusResDependencies.AddItem( _
  ByVal objResource _
)
```



## Parameters

<dl> <dt>

*objResource* 
</dt> <dd>

The [**ClusResource**](clusresource-object.md) object to add to the collection.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Resources added to a [**ClusResDependencies**](clusresdependencies-collection.md) collection become [dependencies](resource-dependencies.md) of the resource from which the collection was obtained

## Examples

The following script uses the **AddItem** method to add a dependency to a resource.


```VB
'''''''''''''''''''''''''''''''''''
' adddependency.vbs
' Adds a dependency to a resource. Both resources must already exist
' and be able to form a dependency relationship. Run the script on 
' the command line using the following syntax:
'     AddDependency Resourcename Dependencyname
' The resource identified by Resourcename will depend on the resource
' identified by Dependencyname.
''''''''''''''''''''''''''''''''''' 
Option Explicit
Dim objArgs, objCluster, objResource, objDependency
Set objArgs = WScript.Arguments
If objArgs.Count <> 2 Then
    WScript.Echo "Syntax:   AddDependency Resourcename Dependencyname"
    WScript.Quit
End If
Set objCluster = CreateObject("MSCluster.Cluster")
objClus.Open ""
Set objResource = objCluster.Resources.Item(objArgs(0))
Set objDependency = objCluster.Resources.Item(objArgs(1))
If objResource.CanResourceBeDependent(objDependency) Then
    objResource.Dependencies.AddItem(objDependency)
Else
    WScript.Echo objResource.Name & " cannot depend on " & objDependency.Name
End If
Set objResource = Nothing
Set objDependency = Nothing
Set objCluster = Nothing
```



## Requirements



|                                     |                                                                                          |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>                |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>      |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>    |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>    |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>    |
| IID<br/>                      | IID\_ISClusResDependencies is defined as F2E60704-2631-11D1-89F1-00A0C90D061E<br/> |



## See also

<dl> <dt>

[**ClusResDependencies**](clusresdependencies-collection.md)
</dt> <dt>

[**ClusResource**](clusresource-object.md)
</dt> </dl>

 

 





