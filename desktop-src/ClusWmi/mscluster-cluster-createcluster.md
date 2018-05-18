---
title: CreateCluster method of the MSCluster\_Cluster class
description: Creates a cluster.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0b4aee95-1752-43bf-9038-0d7e2cdba7e7'
ms.prod: 'windows-server-dev'
ms.technology:
- 'failover-cluster-management'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["CreateCluster method", "CreateCluster method, MSCluster_Cluster class", "MSCluster_Cluster class, CreateCluster method"]
topic_type:
- apiref
api_name:
- MSCluster_Cluster.CreateCluster
api_location:
- ClusWMI.dll
api_type:
- COM
---

# CreateCluster method of the MSCluster\_Cluster class

Creates a cluster.

## Syntax


```mof
void CreateCluster(
  [in] string ClusterName,
  [in] string NodeNames[],
  [in] string IPAddresses[],
  [in] string SubnetMasks[],
  [in] uint32 AdministrativeAccessPoint
);
```



## Parameters

<dl> <dt>

*ClusterName* \[in\]
</dt> <dd>

Cluster name.

</dd> <dt>

*NodeNames* \[in\]
</dt> <dd>

Node names that will form the cluster.

</dd> <dt>

*IPAddresses* \[in\]
</dt> <dd>

IP addresses that the cluster will use.

</dd> <dt>

*SubnetMasks* \[in\]
</dt> <dd>

IP address subnet masks or prefix lengths that the cluster will use.

</dd> <dt>

*AdministrativeAccessPoint* \[in\]
</dt> <dd>

The type of the cluster management point.

**Windows Server 2012 R2, Windows Server 2012, Windows Server 2008 R2 and Windows Server 2008:  **

This parameter is not supported before Windows Server 2016.

<dt>

<span id="None"></span><span id="none"></span><span id="NONE"></span>

**None** (0)


</dt> <dd></dd> <dt>

<span id="ActiveDirectoryAndDns"></span><span id="activedirectoryanddns"></span><span id="ACTIVEDIRECTORYANDDNS"></span>

**ActiveDirectoryAndDns** (1)


</dt> <dd></dd> <dt>

<span id="Dns"></span><span id="dns"></span><span id="DNS"></span>

**Dns** (2)


</dt> <dd></dd> <dt>

<span id="ActiveDirectory"></span><span id="activedirectory"></span><span id="ACTIVEDIRECTORY"></span>

**ActiveDirectory** (3)


</dt> <dd></dd> </dl> </dd> </dl>

## Return value

This method does not return a value.

## Remarks

Due to delegation issues, by default a multinode cluster cannot be created with one call. To create a multinode cluster, first create the cluster using **CreateCluster**, wait 30 seconds, and then connect to each of the additional nodes and add them to the cluster using the [**AddNode**](mscluster-cluster-addnode.md) method of the [**MSCluster\_Cluster**](mscluster-cluster.md) class.

To enable delegation, enable **Trusted for delegation** for the computer nodes in the directory and enable Kerberos authentication and impersonation level as **Delegate** when connecting to WMI (this has serious security implications). For more information, see [Connecting to a 3rd Computer-Delegation](https://msdn.microsoft.com/library/aa389288).

## Examples


```VB
' @Description: Creates a cluster that has static IP address using WMI Interface
' @Comments: No input from command line
' @Usage: Modify the parameters and run at CScript Prompt.

Option Explicit

' Global Vars

Dim szServerName
Dim szClusterName
Dim szUserName
Dim szPassword
Dim szArrIPAddrs
Dim szArrSubNetMasks
Dim szArrNodeNames
Dim szQuorum
Dim objSWbemServices


Main(WScript.Arguments)
Wscript.Quit

Function Main(WscriptArgs)
  ' Change the server name, user name, and password.

  szServerName     = "ClusterTest1"
  szClusterName    = "ClusterTest"
  szUserName       = NULL
  szPassword       = NULL
  szArrIPAddrs     = Array("10.10.0.1")
  szArrSubNetMasks = Array("255.255.255.0")
  szArrNodeNames   = Array("ClusterTest1")
  szQuorum         = NULL

  Set objSWbemServices = ClusWMI_ConnectServer()
  Call ClusWMI_CreateCluster(objSWbemServices)


End Function

Function ClusWMI_ConnectServer()

  Dim objSWbemLocator
  Dim objSWbemServices

  WScript.Echo "Connecting to WMI Namespace of " & szServerName

  Set objSWbemLocator = CreateObject("WbemScripting.SWbemLocator")
  Set objSWbemServices = objSWbemLocator.ConnectServer(szServerName,     _
                                                       "Root\MSCluster", _
                                                       szUserName,       _
                                                       szPassWord)
  'objSWbemServices.Security_.ImpersonationLevel = 4
  Set ClusWMI_ConnectServer = objSWbemServices

  WScript.Echo "Leaving ClusWMI_ConnectServer Method ..."

End Function

Function ClusWMI_CreateCluster(objSWbemServices_In)

  Dim objMSCluster
  Dim objInParams
  Dim objOutParams

  Set objMSCluster = objSWbemServices_In.Get("MSCluster_Cluster")
  Set objInParams = objMSCluster.Methods_("CreateCluster").InParameters.SpawnInstance_()

  objInParams.Properties_.Item("ClusterName") = szClusterName
  objInParams.Properties_.Item("IPAddresses") = szArrIPAddrs
  objInParams.Properties_.Item("SubnetMasks") = szArrSubNetMasks
  objInParams.Properties_.Item("NodeNames")   = szArrNodeNames
  objInParams.Properties_.Item("UserName")    = szUserName
  objInParams.Properties_.Item("Password")    = szPassword
  objInParams.Properties_.Item("Quorum")      = szQuorum

  Set objOutParams = objSWbemServices_In.ExecMethod("MSCluster_Cluster", _
                                                    "CreateCluster",     _
                                                    objInParams )



  WScript.Echo" Leaving CreateCluster Method..."

End Function
```



## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                              |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Namespace<br/>                | Root\\MSCluster<br/>                                                             |
| Header<br/>                   | <dl> <dt>Clusapi.h</dt> </dl>   |
| MOF<br/>                      | <dl> <dt>ClusWmi.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>ClusWMI.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSCluster\_Cluster**](mscluster-cluster.md)
</dt> </dl>

 

 





