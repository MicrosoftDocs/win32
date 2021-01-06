---
description: Contains a single object that corresponds to the computer whose catalog you are accessing. This object holds computer level settings information.
ms.assetid: 75f14cad-9cd5-44a6-9afa-2c8ad1e87027
title: LocalComputer collection
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- LocalComputer
api_type: 
- COM
api_location: 
---

# LocalComputer collection

Contains a single object that corresponds to the computer whose catalog you are accessing. This object holds computer level settings information. If you call the [**Connect**](/windows/desktop/api/ComAdmin/nf-comadmin-icomadmincatalog-connect) method on an object created from the [**COMAdminCatalog**](comadmincatalog.md) class, the object in the **LocalComputer** collection contains information about the remote computer whose catalog you are accessing.

This collection does not support the [**Add**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-add) and [**Remove**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogcollection-remove) methods of the [**COMAdminCatalogCollection**](comadmincatalogcollection.md) object.

## Members

The **LocalComputer** collection inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface but does not have additional members.

## Related Collections

You can navigate from this collection to any of the following collections:

-   [**ErrorInfo**](errorinfo.md)
-   [**PropertyInfo**](propertyinfo.md)
-   [**RelatedCollectionInfo**](relatedcollectioninfo.md)

You can navigate to this collection from the following collections:

-   [**Root**](root.md)

## Properties

The following properties are supported by the [**COMAdminCatalogObject**](comadmincatalogobject.md) object within the collection:

-   [ApplicationProxyRSN](#applicationproxyrsn)
-   [CISEnabled](#cisenabled)
-   [DCOMEnabled](#dcomenabled)
-   [DefaultAuthenticationLevel](#defaultauthenticationlevel)
-   [DefaultImpersonationLevel](#defaultimpersonationlevel)
-   [DefaultToInternetPorts](#defaulttointernetports)
-   [Description](#description)
-   [DSPartitionLookupEnabled](#dspartitionlookupenabled)
-   [InternetPortsListed](#internetportslisted)
-   [IsRouter](#isrouter)
-   [LoadBalancingCLSID](#loadbalancingclsid)
-   [LocalPartitionLookupEnabled](#localpartitionlookupenabled)
-   [Name](#name)
-   [OperatingSystem](#operatingsystem)
-   [PartitionsEnabled](#partitionsenabled)
-   [Ports](#defaulttointernetports)
-   [ResourcePoolingEnabled](#resourcepoolingenabled)
-   [RPCProxyEnabled](#rpcproxyenabled)
-   [SecureReferencesEnabled](#securereferencesenabled)
-   [SecurityTrackingEnabled](#securitytrackingenabled)
-   [SRPActivateAsActivatorChecks](#srpactivateasactivatorchecks)
-   [SRPRunningObjectChecks](#srprunningobjectchecks)
-   [TransactionTimeout](#transactiontimeout)

### ApplicationProxyRSN



| Entry | Value |
|----------------|------------------------------------------------------------|
| Description    | Remote server name used by application proxies by default. |
| Access         | ReadWrite                                                  |
| Type           | String                                                     |
| Default        | ""                                                         |
| Minimum system | Windows 2000                                               |



 

### CISEnabled



| Entry | Value |
|----------------|-----------------------------------------------------|
| Description    | Indicates whether COM Internet Services is enabled. |
| Access         | ReadWrite                                           |
| Type           | Bool                                                |
| Default        | False                                               |
| Minimum system | Windows 2000                                        |



 

### DCOMEnabled



| Entry | Value |
|----------------|---------------------------------------------|
| Description    | Set to True to enable DCOM on the computer. |
| Access         | ReadWrite                                   |
| Type           | Bool                                        |
| Default        | True                                        |
| Minimum system | Windows 2000                                |



 

### DefaultAuthenticationLevel



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Authentication level used by applications that have Authentication set to Default. Values correspond to the Remote Procedure Call (RPC) authentication settings.                                                                                         |
| Access         | ReadWrite                                                                                                                                                                                                                                                |
| Type           | Long Possible values:COMAdminAuthenticationDefault (0)COMAdminAuthenticationNone (1) COMAdminAuthenticationConnect (2)COMAdminAuthenticationCall (3)COMAdminAuthenticationPacket (4)COMAdminAuthenticationIntegrity (5)COMAdminAuthenticationPrivacy (6) |
| Default        | COMAdminAuthenticationConnect (2)                                                                                                                                                                                                                        |
| Minimum system | Windows 2000                                                                                                                                                                                                                                             |



 

> [!Note]  
> COMAdminAuthenticationDefault is mapped to COMAdminAuthenticationConnect when COM calls [**CoInitializeSecurity**](/windows/desktop/api/combaseapi/nf-combaseapi-coinitializesecurity). It is recommended that you use the constants in the enumeration and not the numeric values.

 

### DefaultImpersonationLevel



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Impersonation level to allow if one is not set.                                                                                                               |
| Access         | ReadWrite                                                                                                                                                     |
| Type           | Long Possible values:COMAdminImpersonationAnonymous (1)COMAdminImpersonationIdentify (2)COMAdminImpersonationImpersonate (3)COMAdminImpersonationDelegate (4) |
| Default        | COMAdminImpersonationIdentify (2)                                                                                                                             |
| Minimum system | Windows 2000                                                                                                                                                  |



 

> [!Note]  
> It is recommended that you use the constants in the enumeration, and not the numeric values.

 

### DefaultToInternetPorts



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------|
| Description    | Determines whether the default type of port provided should be Internet (True) or intranet (False). |
| Access         | ReadWrite                                                                                           |
| Type           | Bool                                                                                                |
| Default        | False                                                                                               |
| Minimum system | Windows 2000                                                                                        |



 

### Description



| Entry | Value |
|----------------|--------------------------------|
| Description    | A description of the computer. |
| Access         | ReadWrite                      |
| Type           | String                         |
| Default        | ""                             |
| Minimum system | Windows 2000                   |



 

### DSPartitionLookupEnabled



| Entry | Value |
|----------------|----------------------------------------------------------------------------------------|
| Description    | Indicates whether the user of the partition mappings is checked into the domain store. |
| Access         | ReadWrite                                                                              |
| Type           | Bool                                                                                   |
| Default        | True                                                                                   |
| Minimum system | Windows Server 2003                                                                    |



 

### InternetPortsListed



| Entry | Value |
|----------------|-----------------------------------------------------------------------------------------------------------------------|
| Description    | Determines whether the ports listed in the Ports property are to be used for Internet (True) or for intranet (False). |
| Access         | ReadWrite                                                                                                             |
| Type           | Bool                                                                                                                  |
| Default        | False                                                                                                                 |
| Minimum system | Windows 2000                                                                                                          |



 

### IsRouter



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Set to True if the computer is a router for the component load balancing (CLB) service. This property can be set to True only if the component load balancing service is currently installed on the computer; otherwise, it errors with COMADMIN\_E\_REQUIRES\_DIFFERENT\_PLATFORM. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                           |
| Type           | Bool                                                                                                                                                                                                                                                                                |
| Default        | False                                                                                                                                                                                                                                                                               |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                        |



 

If this property is set to True, the CLB server is configured and starts at startup. The server is added to the ApplicationCluster collection if it is not already present.

### LoadBalancingCLSID



| Entry | Value |
|----------------|-------------------------------------|
| Description    | The CLSID of the object to balance. |
| Access         | ReadWrite                           |
| Type           | String                              |
| Default        | NULL                                |
| Minimum system | Windows XP                          |



 

### LocalPartitionLookupEnabled



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------|
| Description    | Indicates whether the user of the partition mappings is checked into the local store. |
| Access         | ReadWrite                                                                             |
| Type           | Bool                                                                                  |
| Default        | True                                                                                  |
| Minimum system | Windows Server 2003                                                                   |



 

### Name



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The name of the computer. Extra spaces at the beginning and end of the string are stripped out. This property is returned when the [**Key**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_key) or [**Name**](/windows/desktop/api/ComAdmin/nf-comadmin-icatalogobject-get_name) property method is called on an object of this collection. |
| Access         | WriteOnce                                                                                                                                                                                                                                                              |
| Type           | String                                                                                                                                                                                                                                                                 |
| Default        | "My Computer"                                                                                                                                                                                                                                                          |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                           |



 

### OperatingSystem



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | The operating system installed on the local computer.                                                                                                                                                                                                                                                                                                                                                                                                |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Type           | Long Possible values:COMAdminOSNotInitialized (0)COMAdminOSWindows3\_1(1)COMAdminOSWindows9x (2)COMAdminOSWindows2000 (3)COMAdminOSWindows2000AdvancedServer (4)COMAdminOSWindows2000Unknown (5)COMAdminOSUnknown (6)COMAdminOSWindowsXPPersonal (11)COMAdminOSWindowsXPProfessional (12)COMAdminOSWindowsNETStandardServer (13)COMAdminOSWindowsNETEnterpriseServer (14)COMAdminOSWindowsNETDatacenterServer (15)COMAdminOSWindowsNETWebServer (16) |
| Default        | COMAdminOSNotInitialized (0)                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                                                                                                                         |



 

### PartitionsEnabled



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Indicates whether COM+ partitions can be used on the local computer. If this property is False, any attempt to use COM+ partitions results in an error. |
| Access         | ReadWrite                                                                                                                                               |
| Type           | Bool                                                                                                                                                    |
| Default        | False                                                                                                                                                   |
| Minimum system | Windows Server 2003                                                                                                                                     |



 

### Ports



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | A string describing ports that are for either Internet or intranet use, depending on the InternetPortsListed property; for example, "500-599: 600-800". |
| Access         | ReadWrite                                                                                                                                               |
| Type           | String                                                                                                                                                  |
| Default        | ""                                                                                                                                                      |
| Minimum system | Windows 2000                                                                                                                                            |



 

### ResourcePoolingEnabled



| Entry | Value |
|----------------|-------------------------------------|
| Description    | Enables use of resource dispensers. |
| Access         | ReadWrite                           |
| Type           | Bool                                |
| Default        | True                                |
| Minimum system | Windows 2000                        |



 

### RPCProxyEnabled



| Entry | Value |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Controls whether the RPC IIS proxy is enabled. The RPC IIS proxy is used in conjunction with IIS to forward calls to the RPC mechanism from IIS and is one of the core pieces of COM Internet Services, which is enabled by setting CISEnabled to True. For more information on RPCProxyEnabled, see [HTTP RPC Security](/windows/desktop/Rpc/rpc-over-http-security). |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                             |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                                  |
| Default        | False                                                                                                                                                                                                                                                                                                                                                 |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                          |



 

### SecureReferencesEnabled



| Entry | Value |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Enforces in DCOM computers that cross-process calls to [**IUnknown::AddRef**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-addref) and [**IUnknown::Release**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-release) methods are secured. |
| Access         | ReadWrite                                                                                                                                                                 |
| Type           | Bool                                                                                                                                                                      |
| Default        | False                                                                                                                                                                     |
| Minimum system | Windows 2000                                                                                                                                                              |



 

### SecurityTrackingEnabled



| Entry | Value |
|----------------|---------------------------------------------------------|
| Description    | Set to True if security tracking is enabled on objects. |
| Access         | ReadWrite                                               |
| Type           | Bool                                                    |
| Default        | True                                                    |
| Minimum system | Windows 2000                                            |



 

### SRPActivateAsActivatorChecks



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines how the software restriction policy (SRP) handles activate-as-activator connections. If set to True, the SRP trust level that is configured for the server object is compared with the SRP trust level of the client object and the higher (more stringent) trust level is used to run the server object. If set to False, the server object runs with the SRP trust level of the client object, regardless of the SRP trust level with which the server is configured. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Default        | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |



 

### SRPRunningObjectChecks



| Entry | Value |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Determines how the software restriction policy (SRP) handles attempted connections to existing processes. If set to False, attempts to connect to running objects are not checked for appropriate SRP trust levels. If set to True, the running object must have an equal or higher (more stringent) SRP trust level than the client object. For example, a client object with an Unrestricted SRP trust level cannot connect to a running object with a Disallowed SRP trust level. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Type           | Bool                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Default        | True                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| Minimum system | Windows XP                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |



 

### TransactionTimeout



| Entry | Value |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Should be set to a sufficient value in seconds if you are doing numerous operations within a transaction. The default time-out period is 60 seconds, and the maximum time-out period is 3600 seconds (1 hour). Setting this property to 0 disables transaction time-outs. This property can be overridden by individual components by using the ComponentTransactionTimeout property of the [**Components**](components.md) collection. |
| Access         | ReadWrite                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Type           | Long (0-3600)                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Default        | 60                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Minimum system | Windows 2000                                                                                                                                                                                                                                                                                                                                                                                                                             |



 

## Example

The following Microsoft Visual Basic example demonstrates how to connect to a remote computer and get its SecurityTrackingEnabled property by using the **LocalComputer** collection of the remote computer. To use this example, add the COM+ Admin Type Library as a reference to your Visual Basic project.


```VB
Function RemoteComputerConnect(strComputer As String _
) As Boolean  ' Return False if any errors occur.
    
    RemoteComputerConnect = False   ' Initialize the function.
    On Error GoTo My_Error_Handler  ' Initialize error handling.

    Dim boolSTE As Boolean
    Dim objCatalog As COMAdminCatalog
    Dim objRemoteRootColl As COMAdminCatalogCollection
    Dim objRemoteComputerColl As COMAdminCatalogCollection
    Dim objRemoteComputerItem As COMAdminCatalogObject
    
    Set objCatalog = CreateObject("COMAdmin.COMAdminCatalog")
    Set objRemoteRootColl = objCatalog.Connect(strComputer)
    Set objRemoteComputerColl = objRemoteRootColl.GetCollection( _
      "LocalComputer", objRemoteRootColl.Name)
    objRemoteComputerColl.Populate
    Set objRemoteComputerItem = objRemoteComputerColl.Item(0)
    boolSTE = objRemoteComputerItem.Value("SecurityTrackingEnabled")
    If boolSTE Then
        MsgBox "Security Tracking is enabled on " & strComputer
    Else
        MsgBox "Security Tracking is NOT enabled on " & strComputer
    End If

    Set objRemoteComputerItem = Nothing
    Set objRemoteComputerColl = Nothing
    Set objRemoteRootColl = Nothing
    Set objCatalog = Nothing
    RemoteComputerConnect = True  ' Successful end to procedure
    Exit Function

My_Error_Handler:  ' Replace with specific error handling.
    MsgBox "Error # " & Err.Number & " (Hex: " & Hex(Err.Number) _
      & ")" & vbNewLine & Err.Description
    Set objRemoteComputerItem = Nothing
    Set objRemoteComputerColl = Nothing
    Set objRemoteRootColl = Nothing
    Set objCatalog = Nothing
End Function


```



To use the function, provide a string value for the name of the remote computer. The following Visual Basic code shows how to connect to the computer named "RemoteComputerName".


```VB
Sub Main()
    If Not RemoteComputerConnect("RemoteComputerName") Then
        MsgBox "RemoteComputerConnect failed."
    End If
End Sub

```



## See also

<dl> <dt>

[COM+ Administration Collections](com--administration-collections.md)
</dt> </dl>

 

 
