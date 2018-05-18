---
title: Cluster.Open method
description: Opens a connection to a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '1f5d9f49-1169-45f2-9f3d-11ce9d8db5ef'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Open method Failover Cluster", "Open method Failover Cluster , Cluster object", "Cluster object Failover Cluster , Open method"]
topic_type:
- apiref
api_name:
- Cluster.Open
api_location:
- MsClus.dll
api_type:
- COM
---

# Cluster.Open method

\[The **Open** method is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Opens a connection to a [*cluster*](c-gly.md#-wolf-cluster-gly).

## Syntax


```VB
Cluster.Open( _
  ByVal strClusterName _
)
```



## Parameters

<dl> <dt>

*strClusterName* 
</dt> <dd>

String specifying the name of the cluster to open. If set to a zero-length string (""), the method connects to the local machine's cluster.

</dd> </dl>

## Return value

This method does not return a value.

## Examples

The following example illustrates the Open method. For more examples see [Using Cluster Automation Server](using-cluster-automation-server.md).


```VB
'''''''''''''''''''''''''''''''''''
'  opendemo.vbs  (use with cscript.exe)
'  Run from the command line using the following syntax:
'        opendemo [clustername]
'''''''''''''''''''''''''''''''''''
Option Explicit
Dim objArgs, objCluster
Set objArgs = WScript.Arguments
Set objCluster = CreateObject("MSCluster.Cluster")
If objArgs.Count > 0 Then
    objCluster.Open objArgs(0)
Else
    objCluster.Open ""
End If
WScript.Echo "Successfully opened " & objCluster.Name
Set objCluster = Nothing
Set objArgs = Nothing
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISCluster is defined as F2E606E4-2631-11D1-89F1-00A0C90D061E<br/>          |



## See also

<dl> <dt>

[**Cluster**](cluster-object.md)
</dt> </dl>

 

 





