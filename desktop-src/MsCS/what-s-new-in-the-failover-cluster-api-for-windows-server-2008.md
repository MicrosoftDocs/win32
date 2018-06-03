---
title: What's New in the Failover Cluster API for Windows Server 2008
description: This summarizes the changes in the Failover Cluster APIs for Windows Server 2008.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3F828899-EF24-4628-BF3B-8BF761E41BCA
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# What's New in the Failover Cluster API for Windows Server 2008

This summarizes the changes in the Failover Cluster APIs for Windows Server 2008.

## New programming elements introduced in Windows Server 2008:

New functions added in Windows Server 2008:

-   [**AddClusterNode**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_add_cluster_node)
-   [**ClusterRegBatchAddCommand**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_batch_add_command)
-   [**ClusterRegBatchCloseNotification**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_batch_close_notification)
-   [**ClusterRegBatchReadCommand**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_get_batch_notification)
-   [**ClusterRegCloseBatch**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_close_batch)
-   [**ClusterRegCloseBatchNotifyPort**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_close_batch_notify_port)
-   [**ClusterRegCreateBatch**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterregcreatebatch)
-   [**ClusterRegCreateBatchNotifyPort**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_reg_create_batch_notify_port)
-   [**ClusterRegGetBatchNotification**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusterreggetbatchnotification)
-   [**CreateCluster**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_create_cluster)
-   [**DestroyCluster**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_destroy_cluster)
-   [**DestroyClusterGroup**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_destroy_cluster_group)
-   [**GetClusterResourceDependencyExpression**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_get_cluster_resource_dependency_expression)
-   [**ResUtilFindFileTimeProperty**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_find_filetime_property)
-   [**ResUtilGetClusterRoleState**](/previous-versions/windows/desktop/api/ResApi/nf-resapi-resutilgetclusterrolestate)
-   [**ResUtilGetFileTimeProperty**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_filetime_property)
-   [**ResUtilGetLongProperty**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_long_property)
-   [**ResUtilGetQwordValue**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_get_qword_value)
-   [**ResUtilSetQwordValue**](/previous-versions/windows/desktop/api/ResApi/nc-resapi-presutil_set_qword_value)
-   [**SetClusterResourceDependencyExpression**](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pclusapi_set_cluster_resource_dependency_expression)

New callback functions added in Windows Server 2008:

-   [*ResourceCallback*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-lpresource_callback)
-   [*ResourceCallbackEx*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-lpresource_callback_ex)
-   [*PCLUSTERpclu\_SETUP\_PROGRESS\_CALLBACK*](/previous-versions/windows/desktop/api/ClusAPI/nc-clusapi-pcluster_setup_progress_callback)
-   [*WorkerStartRoutine*](/previous-versions/windows/desktop/api/ResApi/nc-resapi-pworker_start_routine)

New methods added in Windows Server 2008:

-   [**AddToCluster**](https://msdn.microsoft.com/library/cc512204)
-   [**AddNode**](https://msdn.microsoft.com/library/cc512211)
-   [**CreateCluster**](https://msdn.microsoft.com/library/cc512205)
-   [**DestroyCluster**](https://msdn.microsoft.com/library/cc512206)
-   [**EvictNode**](https://msdn.microsoft.com/library/cc512212)
-   [**ExecuteClusterControl**](https://msdn.microsoft.com/library/cc512207)
-   [**ForceCleanup**](https://msdn.microsoft.com/library/cc512208)
-   [**SetDiskQuorum**](https://msdn.microsoft.com/library/cc512209)
-   [**SetMajorityQuorum**](https://msdn.microsoft.com/library/cc512213)
-   [**SetNodeMajorityQuorum**](https://msdn.microsoft.com/library/cc512210)
-   [**ExecuteNetworkControl**](https://msdn.microsoft.com/library/cc512215)
-   [**ExecuteNetworkInterfaceControl**](https://msdn.microsoft.com/library/cc512214)
-   [**ExecuteNodeControl**](https://msdn.microsoft.com/library/cc512216)
-   [**AddPossibleOwner**](https://msdn.microsoft.com/library/cc512234)
-   [**ExecuteResourceControl**](https://msdn.microsoft.com/library/cc512235)
-   [**GetDependencies**](https://msdn.microsoft.com/library/cc512237)
-   [**ReleaseAddress**](https://msdn.microsoft.com/library/cc512239)
-   [**RemovePossibleOwner**](https://msdn.microsoft.com/library/cc512241)
-   [**RenewAddress**](https://msdn.microsoft.com/library/cc512242)
-   [**SetDependencies**](https://msdn.microsoft.com/library/cc512243)
-   [**DestroyGroup**](https://msdn.microsoft.com/library/cc512219)
-   [**ExecuteGroupControl**](https://msdn.microsoft.com/library/cc512232)
-   [**GetGroupType**](https://msdn.microsoft.com/library/cc512230)
-   [**SetGroupType**](https://msdn.microsoft.com/library/cc512231)
-   [**SetPreferredOwners**](https://msdn.microsoft.com/library/cc512233)
-   [**ExecuteResourceTypeControl**](https://msdn.microsoft.com/library/cc512240)
-   [**Start**](https://msdn.microsoft.com/library/cc512245)
-   [**Stop**](https://msdn.microsoft.com/library/cc512244)

New control codes added in Windows Server 2008:

-   [CLUSCTL\_CLUSTER\_CHECK\_VOTER\_EVICT](clusctl-cluster-check-voter-evict.md)
-   [CLUSCTL\_CLUSTER\_SHUTDOWN](clusctl-cluster-shutdown.md)
-   [CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_32BIT](clusctl-resource-add-registry-checkpoint-32bit.md)
-   [CLUSCTL\_RESOURCE\_ADD\_REGISTRY\_CHECKPOINT\_64BIT](clusctl-resource-add-registry-checkpoint-64bit.md)
-   [CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_ADD](clusctl-resource-fileserver-share-add.md)
-   [CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_DEL](clusctl-resource-fileserver-share-del.md)
-   [CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_MODIFY](clusctl-resource-fileserver-share-modify.md)
-   [CLUSCTL\_RESOURCE\_FILESERVER\_SHARE\_REPORT](clusctl-resource-fileserver-share-report.md)
-   [CLUSCTL\_RESOURCE\_FSWITNESS\_GET\_EPOCH\_INFO](clusctl-resource-fswitness-get-epoch-info.md)
-   [CLUSCTL\_RESOURCE\_FSWITNESS\_RELEASE\_LOCK](clusctl-resource-fswitness-release-lock.md)
-   [CLUSCTL\_RESOURCE\_FSWITNESS\_SET\_EPOCH\_INFO](clusctl-resource-fswitness-set-epoch-info.md)
-   [CLUSCTL\_RESOURCE\_GET\_DNS\_NAME](clusctl-resource-get-dns-name.md)
-   [CLUSCTL\_RESOURCE\_IPADDRESS\_RELEASE\_LEASE](clusctl-resource-ipaddress-release-lease.md)
-   [CLUSCTL\_RESOURCE\_IPADDRESS\_RENEW\_LEASE](clusctl-resource-ipaddress-renew-lease.md)
-   [CLUSCTL\_RESOURCE\_JOINING\_GROUP](clusctl-resource-joining-group.md)
-   [CLUSCTL\_RESOURCE\_LEAVING\_GROUP](clusctl-resource-leaving-group.md)
-   [CLUSCTL\_RESOURCE\_NETNAME\_CREDS\_UPDATED](clusctl-resource-netname-creds-updated.md)
-   [CLUSCTL\_RESOURCE\_NETNAME\_DELETE\_CO](clusctl-resource-netname-delete-co.md)
-   [CLUSCTL\_RESOURCE\_NETNAME\_GET\_VIRTUAL\_SERVER\_TOKEN](clusctl-resource-netname-get-virtual-server-token.md)
-   [CLUSCTL\_RESOURCE\_NETNAME\_REGISTER\_DNS\_RECORDS](clusctl-resource-netname-register-dns-records.md)
-   [CLUSCTL\_RESOURCE\_NETNAME\_RESET\_VCO](clusctl-resource-netname-reset-vco.md)
-   [CLUSCTL\_RESOURCE\_NETNAME\_SET\_PWD\_INFO](clusctl-resource-netname-set-pwd-info.md)
-   [CLUSCTL\_RESOURCE\_NETNAME\_VALIDATE\_VCO](clusctl-resource-netname-validate-vco.md)
-   [CLUSCTL\_RESOURCE\_PROVIDER\_STATE\_CHANGE](clusctl-resource-provider-state-change.md)
-   [CLUSCTL\_RESOURCE\_STORAGE\_CLUSTER\_DISK](clusctl-resource-storage-cluster-disk.md)
-   [CLUSCTL\_RESOURCE\_STORAGE\_GET\_DISK\_INFO\_EX](clusctl-resource-storage-get-disk-info-ex.md)
-   [CLUSCTL\_RESOURCE\_STORAGE\_SET\_DRIVELETTER](clusctl-resource-storage-set-driveletter.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_GEN\_APP\_VALIDATE\_DIRECTORY](clusctl-resource-type-gen-app-validate-directory.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_GEN\_APP\_VALIDATE\_PATH](clusctl-resource-type-gen-app-validate-path.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_GEN\_SCRIPT\_VALIDATE\_PATH](clusctl-resource-type-gen-script-validate-path.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_NETNAME\_VALIDATE\_NETNAME](clusctl-resource-type-netname-validate-netname.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_AVAILABLE\_DISKS\_EX](clusctl-resource-type-storage-get-available-disks-ex.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_DISKID](clusctl-resource-type-storage-get-diskid.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_GET\_DRIVELETTERS](clusctl-resource-type-storage-get-driveletters.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_IS\_CLUSTERABLE](clusctl-resource-type-storage-is-clusterable.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_REMAP\_DRIVELETTER](clusctl-resource-type-storage-remap-driveletter.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_REMOVE\_VM\_OWNERSHIP](clusctl-resource-type-storage-remove-vm-ownership.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_STORAGE\_SYNC\_CLUSDISK\_DB](clusctl-resource-type-storage-sync-clusdisk-db.md)
-   [CLUSCTL\_RESOURCE\_TYPE\_WITNESS\_VALIDATE\_PATH](clusctl-resource-type-witness-validate-path.md)
-   [CLUSCTL\_RESOURCE\_VM\_CONFIG\_UPDATE](clusctl-resource-vm-config-update.md)

New enumerations added in Windows Server 2008:

-   [**CLUSCTL\_CLUSTER\_CODES**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clusctl_cluster_codes)
-   [**CLUSCTL\_GROUP\_CODES**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clusctl_group_codes)
-   [**CLUSCTL\_NETINTERFACE\_CODES**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clusctl_netinterface_codes)
-   [**CLUSCTL\_NETWORK\_CODES**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clusctl_network_codes)
-   [**CLUSCTL\_NODE\_CODES**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-clusctl_node_codes)
-   [**CLUSTER\_GROUP\_STATE**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_group_state)
-   [**CLUSTER\_QUORUM\_TYPE**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_quorum_type)
-   [**CLUSTER\_REG\_COMMAND**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-_cluster_reg_command)
-   [**CLUSTER\_RESOURCE\_CLASS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_resource_class)
-   [**CLUSTER\_RESOURCE\_CREATE\_FLAGS**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-cluster_resource_create_flags)
-   [**CLUSTER\_ROLE**](/previous-versions/windows/desktop/api/ResApi/ne-resapi-_cluster_role)
-   [**CLUSTER\_ROLE\_STATE**](/previous-versions/windows/desktop/api/ResApi/ne-resapi-_cluster_role_state)
-   [**FILESHARE\_CHANGE\_ENUM**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-_fileshare_change_enum)
-   [**MAINTENANCE\_MODE\_TYPE\_ENUM**](/previous-versions/windows/desktop/api/ClusAPI/ne-clusapi-_maintenance_mode_type_enum)
-   [**RESOURCE\_MONITOR\_STATE**](/previous-versions/windows/desktop/api/ResApi/ne-resapi-resource_monitor_state)

New MOF classes added in Windows Server 2008:

-   [**MSCluster\_AvailableDisk**](https://msdn.microsoft.com/library/cc325745)
-   [**MSCluster\_ClusterToAvailableDisk**](https://msdn.microsoft.com/library/cc325744)
-   [**MSCluster\_Disk**](https://msdn.microsoft.com/library/aa965285)
-   [**MSCluster\_DiskPartition**](https://msdn.microsoft.com/library/aa965286)
-   [**MSCluster\_DiskToDiskPartition**](https://msdn.microsoft.com/library/aa965287)
-   [**MSCluster\_EventClusterCallback**](https://msdn.microsoft.com/library/cc325746)
-   [**MSCluster\_EventRegistryChange**](https://msdn.microsoft.com/library/aa965288)
-   [**MSCluster\_ResourceToDisk**](https://msdn.microsoft.com/library/aa965289)

New properties added in Windows Server 2008:

-   [**AdapterId**](adapterid.md)
-   [**Address**](address.md)
-   [**ApplicationName**](applicationname.md)
-   [**ApplicationParams**](applicationparams.md)
-   [**BackupInProgress**](backupinprogress.md)
-   [**CurrentDirectory**](currentdirectory.md)
-   [**DeadlockTimeout**](deadlocktimeout.md)
-   [**DeadlockTimeout**](deadlocktimeout-restypprop.md)
-   [**DhcpAddress**](dhcpaddress.md)
-   [**DhcpEnabled**](dhcpenabled.md)
-   [**DhcpServer**](dhcpserver.md)
-   [**DhcpSubnetMask**](dhcpsubnetmask.md)
-   [**DiskArbInterval**](diskarbinterval.md)
-   [**DiskIdGuid**](diskidguid.md)
-   [**DiskIdType**](diskidtype.md)
-   [**DiskPath**](diskpath.md)
-   [**DiskReload**](diskreload.md)
-   [**DiskRunChkDsk**](diskrunchkdsk.md)
-   [**DiskSignature**](disksignature.md)
-   [**DiskVolumeInfo**](diskvolumeinfo.md)
-   [**MaxUsers**](distributed-file-system-maxusers.md)
-   [**Path**](distributed-file-system-path.md)
-   [**Remark**](distributed-file-system-remark.md)
-   [**Security Descriptor**](distributed-file-system-security-descriptor.md)
-   [**ShareFlags**](distributed-file-system-shareflags.md)
-   [**ShareName**](distributed-file-system-sharename.md)
-   [**DnsName**](dnsname.md)
-   [**EnableDhcp**](enabledhcp.md)
-   [**CommandLine**](generic-scripts-commandline.md)
-   [**CurrentDirectory**](generic-scripts-currentdirectory.md)
-   [**InteractWithDesktop**](generic-scripts-interactwithdesktop.md)
-   [**UseNetworkName**](generic-scripts-usenetworkname.md)
-   [**HostRecordTTL**](hostrecordttl.md)
-   [**IPv4Addresses**](ipv4addresses.md)
-   [**IPv4Addresses**](ipv4addresses-netifprop.md)
-   [**IPv4PrefixLengths**](ipv4prefixlengths.md)
-   [**IPv6Addresses**](ipv6addresses.md)
-   [**IPv6Addresses**](ipv6addresses-netifprop.md)
-   [**IPv6PrefixLengths**](ipv6prefixlengths.md)
-   [**DatabaseStorage**](isns-databasestorage.md)
-   [**LastDNSUpdateTime**](lastdnsupdatetime.md)
-   [**LeaseExpiresTime**](leaseexpirestime.md)
-   [**LeaseObtainedTime**](leaseobtainedtime.md)
-   [**MaintenanceMode**](maintenancemode.md)
-   [**MonitorProcessId**](monitorprocessid.md)
-   [**TimerCallbackAdditionalThreshold**](network-names-timercallbackadditionalthreshold.md)
-   [**Network**](network-prop.md)
-   [**ObjectGUID**](objectguid.md)
-   [**OverrideAddressMatch**](overrideaddressmatch.md)
-   [**PendingTimeout**](pendingtimeout.md)
-   [**PrefixLength**](prefixlength.md)
-   [**BeepEnabled**](print-spoolers-beepenabled.md)
-   [**ClusterDriverDirectory**](print-spoolers-clusterdriverdirectory.md)
-   [**GMTAdjustedForDST**](print-spoolers-gmtadjustedfordst.md)
-   [**PublishPTRRecords**](publishptrrecords.md)
-   [**RegisterAllProvidersIP**](registerallprovidersip.md)
-   [**RequestReplyTimeout**](requestreplytimeout.md)
-   [**ResourceSpecificStatus**](resources-resourcespecificstatus.md)
-   [**SharePath**](sharepath.md)
-   [**StatusDNS**](statusdns.md)
-   [**StatusKerberos**](statuskerberos.md)
-   [**StatusNetBIOS**](statusnetbios.md)
-   [**TriggerArray**](triggerarray.md)
-   [**TunnelType**](tunneltype.md)
-   [**VmId**](virtual-machine-configurations-vmid.md)
-   [**VmPhysicalDisks**](virtual-machine-configurations-vmphysicaldisks.md)
-   [**VmStoreRootPath**](virtual-machine-configurations-vmstorerootpath.md)
-   [**VmSwitchPorts**](virtual-machine-configurations-vmswitchports.md)
-   [**OfflineAction**](virtual-machines-offlineaction.md)
-   [**VmId**](virtual-machines-vmid.md)
-   [**WitnessRestartInterval**](witnessrestartinterval.md)

New structures added in Windows Server 2008:

-   [**CLUS\_MAINTENANCE\_MODE\_INFOEX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_maintenance_mode_infoex)
-   [**CLUS\_NETNAME\_PWD\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_netname_pwd_info)
-   [**CLUS\_NETNAME\_VS\_TOKEN\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_netname_vs_token_info)
-   [**CLUS\_PARTITION\_INFO\_EX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clus_partition_info_ex)
-   [**CLUS\_PROVIDER\_STATE\_CHANGE\_INFO**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_provider_state_change_info)
-   [**CLUS\_STORAGE\_GET\_AVAILABLE\_DRIVELETTERS**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_storage_get_available_driveletters)
-   [**CLUS\_STORAGE\_REMAP\_DRIVELETTER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_storage_remap_driveletter)
-   [**CLUS\_STORAGE\_SET\_DRIVELETTER**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_clus_storage_set_driveletter)
-   [**CLUSPROP\_FILETIME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_filetime)
-   [**CLUSPROP\_PARTITION\_INFO\_EX**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_partition_info_ex)
-   [**CLUSTER\_BATCH\_COMMAND**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_cluster_batch_command)
-   [**CLUSTER\_IP\_ENTRY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_cluster_ip_entry)
-   [**CLUSTER\_VALIDATE\_DIRECTORY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_cluster_validate_directory)
-   [**CLUSTER\_VALIDATE\_NETNAME**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_cluster_validate_netname)
-   [**CLUSTER\_VALIDATE\_PATH**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_cluster_validate_path)
-   [**CREATE\_CLUSTER\_CONFIG**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_create_cluster_config)
-   [**FILESHARE\_CHANGE**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_fileshare_change)
-   [**FILESHARE\_CHANGE\_LIST**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-_fileshare_change_list)
-   [**MONITOR\_STATE**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-monitor_state)
-   [**RESUTIL\_FILETIME\_DATA**](/previous-versions/windows/desktop/api/ResApi/ns-resapi-resutil_filetime_data)

## Related topics

<dl> <dt>

[Failover Cluster APIs](failover-cluster-apis-portal.md)
</dt> </dl>

 

 




