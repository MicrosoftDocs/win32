---
title: ClusVersion object
description: Provides version information about the operating system and the Cluster service. For more information on cluster versions and version numbers, see Version Compatibility.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2215335a-1858-437f-8654-2e9d601fe061
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ClusVersion object Failover Cluster
- ClusVersion object Failover Cluster , described
topic_type:
- apiref
api_name:
- ClusVersion
- ISClusVersion
api_location:
- MsClus.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
---

# ClusVersion object

\[The **ClusVersion** object is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Provides version information about the operating system and the [*Cluster service*](c-gly.md#-wolf-cluster-service-gly). For more information on [*cluster versions*](c-gly.md#-wolf-cluster-version-gly) and [*version numbers*](v-gly.md#-wolf-version-number-gly), see [Version Compatibility](version-compatibility.md).

## Members

The **ClusVersion** object has these types of members:

-   [Properties](#properties)

### Properties

The **ClusVersion** object has these properties.



| Property                                                                      | Description                                                                                                          |
|:------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------|
| [**BuildNumber**](clusversion-buildnumber.md)<br/>                     | Returns the build number of the operating system installed on the local [node](nodes.md).<br/>                |
| [**ClusterHighestVersion**](clusversion-clusterhighestversion.md)<br/> | Returns the current value of ClusterHighestVersion.<br/>                                                       |
| [**ClusterLowestVersion**](clusversion-clusterlowestversion.md)<br/>   | Returns the current value of ClusterLowestVersion<br/>                                                         |
| [**CSDVersion**](clusversion-csdversion.md)<br/>                       | Returns the number of the latest Service Pack installed on the local node.<br/>                                |
| [**Flags**](clusversion-flags.md)<br/>                                 | Returns any cluster version flags set in the [*cluster*](c-gly.md#-wolf-cluster-gly).<br/>                    |
| [**MajorVersion**](clusversion-majorversion.md)<br/>                   | Returns the major version number of the operating system installed on the local node.<br/>                     |
| [**MinorVersion**](clusversion-minorversion.md)<br/>                   | Returns the major version number of the operating system installed on the local node.<br/>                     |
| [**MixedVersion**](clusversion-mixedversion.md)<br/>                   | Indicates whether different versions of the Cluster service are present in the cluster.<br/>                   |
| [**Name**](clusversion-name.md)<br/>                                   | Returns the name of the cluster.<br/>                                                                          |
| [**VendorId**](clusversion-vendorid.md)<br/>                           | Returns vendor identification information for the version of Cluster service installed on the local node.<br/> |



 

## Remarks

A **ClusVersion** collection:

-   Is obtained from [**Cluster.Version**](cluster-version.md).

Some of the **ClusVersion** properties correspond to dynamic values maintained internally by the cluster. A **ClusVersion** object is instantiated with a snapshot of those values and stores them statically. Therefore, the **ClusVersion** property values represent the state of the cluster when the object was first created. To obtain the latest version information from the cluster, create a new **ClusVersion** object.

For more information about the versioning process see [Version Compatibility](version-compatibility.md).

## Examples

The following script instantiates and uses a **ClusVersion** object.


```VB
'---------------------------------------------------------------------
' ClusVersion.vbs
' Uses the ClusVersion object to display version information about
' the local cluster.
'---------------------------------------------------------------------
Option Explicit
Const LOW16 = 65535
Dim objClus, objVers
Dim strVersion, strOSVersion, strHighest, strLowest

' Connect to the local cluster and get a ClusVersion object.
Set objClus = CreateObject("MSCluster.Cluster")
objClus.Open ""
Set objVers = objClus.Version

' Format a string describing the current version
strOSVersion = CStr(objVers.MajorVersion) & "." & _
               CStr(objVers.MinorVersion) & "." & _
               CStr(objVers.BuildNumber)

' Format a string describing the highest compatible version.
' We must extract the upper and lower 16 bits of the 32-bit value.
strHighest = CStr(CLng(objVers.ClusterHighestVersion / (2 ^ 15))) & _
             ".0." & _
             CStr(CLng(objVers.ClusterHighestVersion And LOW16))

' Format a string describing the lowest compatible version.
' We must extract the upper and lower 16 bits of the 32-bit value.
strLowest = CStr(CLng(objVers.ClusterLowestVersion / (2 ^ 15))) & _
            ".0." & _
            CStr(CLng(objVers.ClusterLowestVersion And LOW16))

' Format and display the output string.
strVersion = objVers.Name & vbCrLf & _
             objVers.VendorID & " version " & _
             strOSVersion & vbCrLf & "Compatible with versions: " & _
             strLowest & " and " & strHighest & vbCrLf
WScript.Echo strVersion

Set objVers = Nothing
Set objClus = Nothing
```



## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                             |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/>             |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl> |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl> |
| IID<br/>                      | IID\_ISClusVersion is defined as F2E60716-2631-11D1-89F1-00A0C90D061E<br/>      |



## See also

<dl> <dt>

[Cluster Management Objects](cluster-management-objects.md)
</dt> </dl>

 

 





