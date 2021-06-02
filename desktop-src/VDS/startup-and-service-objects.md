---
description: VDS provides objects for performing service-related activities. This topic describes each object.
ms.assetid: ae4d18f2-4d50-480c-bc7a-4eec0334707d
title: Startup and Service Objects
ms.topic: article
ms.date: 05/31/2018
---

# Startup and Service Objects

\[Beginning with Windows 8 and Windows Server 2012, the [Virtual Disk Service](virtual-disk-service-portal.md) COM interface is superseded by the [Windows Storage Management API](/previous-versions/windows/desktop/stormgmt/windows-storage-management-api-portal).\]

VDS provides objects for performing service-related activities. This topic describes each object.

## Service Loader Object

The service loader object provides the methods that are used by applications to load and initialize VDS. To prepare VDS for use, an application must perform the following operations:

-   Create an instance of the service loader object, which returns the [**IVdsServiceLoader**](/windows/desktop/api/Vds/nn-vds-ivdsserviceloader) interface.
-   Call the [**IVdsServiceLoader::LoadService**](/windows/desktop/api/Vds/nf-vds-ivdsserviceloader-loadservice) method to load the service.

For a code example, see [Loading VDS](loading-vds.md).

Always allow the service to initialize completely before calling the methods that are exposed by the service object. Use the [**IVdsService::IsServiceReady**](/windows/desktop/api/Vds/nf-vds-ivdsservice-isserviceready) method to determine the status of the load process. Use the [**IVdsService::WaitForServiceReady**](/windows/desktop/api/Vds/nf-vds-ivdsservice-waitforserviceready) method to block calls to VDS objects until the initialization completes.

The following table lists related interfaces, enumerations, and structures.

| Type                                              | Element                                         |
|---------------------------------------------------|-------------------------------------------------|
| Interfaces that are always exposed by this object | [**IVdsServiceLoader**](/windows/desktop/api/Vds/nn-vds-ivdsserviceloader). |
| Associated enumerations                           | None.                                           |
| Associated structures                             | None.                                           |



 

## Service Object

The service object is a multifunctional object that is central to all VDS applications. With this object, a caller can perform the following operations:

-   Determine the status of the service initialization.
-   Retrieve all hardware or software providers registered with VDS.
-   Report on unallocated disks.
-   Return the file system type and drive letter associated with volumes on a disk.
-   Remove unused user-mode paths and mounted folders from the registry and refresh disks.
-   Receive VDS notifications.
-   Reboot the host.
-   Retrieve Fibre Channel HBA ports or iSCSI initiator adapters on the local computer.
-   Safely prepare LUNs exposed as disks on the local computer for removal.

VDS notification structures pass object GUIDs to all applications that are registered with VDS to receive notifications. Use the [**IVdsService::GetObject**](/windows/desktop/api/Vds/nf-vds-ivdsservice-getobject) method to convert an object GUID to an object pointer. For a more complete description of the notification model, see [VDS Notifications](vds-notification-model.md).

The following table lists related interfaces, enumerations, and structures. 

| Type                                                                   | Element                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object                      | [**IVdsService**](/windows/desktop/api/Vds/nn-vds-ivdsservice), [**IVdsServiceHba**](/windows/desktop/api/Vds/nn-vds-ivdsservicehba)\*, [**IVdsServiceIscsi**](/windows/desktop/api/Vds/nn-vds-ivdsserviceiscsi)\*, [**IVdsServiceUninstallDisk**](/windows/desktop/api/Vds/nn-vds-ivdsserviceuninstalldisk)\*.                                                                                                                                                                                                           |
| Interfaces that are always implemented but not exposed to applications | [**IVdsAdmin**](/windows/desktop/api/VdsHwPrv/nn-vdshwprv-ivdsadmin)                                                                                                                                                                                                                                                                                                                                                                            |
| Associated enumerations                                                | [**VDS\_QUERY\_PROVIDER\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_query_provider_flag), [**VDS\_OBJECT\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_object_type), [**VDS\_SERVICE\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_service_flag), [**VDS\_DRIVE\_LETTER\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_drive_letter_flag), [**VDS\_FILE\_SYSTEM\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_file_system_flag), [**VDS\_FILE\_SYSTEM\_PROP\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_file_system_prop_flag).                                                      |
| Associated structures                                                  | [**VDS\_SERVICE\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_service_prop), [**VDS\_FILE\_SYSTEM\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_file_system_prop), [**VDS\_FILE\_SYSTEM\_TYPE\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_file_system_type_prop), [**VDS\_DRIVE\_LETTER\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_drive_letter_notification), [**VDS\_FILE\_SYSTEM\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_file_system_notification), [**VDS\_MOUNT\_POINT\_NOTIFICATION**](/windows/desktop/api/Vds/ns-vds-vds_mount_point_notification). |



 

**\*Windows Server 2003:** These interfaces are not supported until Windows Server 2003 R2.

## Initiator Adapter Object

An initiator adapter object models an iSCSI initiator adapter on the host machine of the VDS service. The VDS service can only view initiator adapters on the local machine. The role of an initiator adapter object is for managing login sessions from the local computer to iSCSI targets.

The following table lists related interfaces, enumerations, and structures. 

| Type                                              | Element                                                                                                                                                                  |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object | [**IVdsIscsiInitiatorAdapter**](/windows/desktop/api/Vds/nn-vds-ivdsiscsiinitiatoradapter)\*.                                                                                                        |
| Associated enumerations                           | [**VDS\_ISCSI\_LOGIN\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_iscsi_login_type). [**VDS\_ISCSI\_LOGIN\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_iscsi_login_flag), [**VDS\_ISCSI\_AUTH\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_iscsi_auth_type). |
| Associated structures                             | [**VDS\_ISCSI\_INITIATOR\_ADAPTER\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_iscsi_initiator_adapter_prop).                                                                                        |



 

**\*Windows Server 2003:** This interface is not supported until Windows Server 2003 R2.

## Initiator Portal Object

An initiator portal object models an iSCSI initiator portal on an iSCSI initiator. An initiator portal is the combination of an IP address and port through which a host computer connects to a portal on an iSCSI subsystem. The role of an initiator portal object is to serve as one of the endpoints of an MPIO path and to configure IPSEC security settings.

The following table lists the related interfaces, enumerations, and structures. 

| Type                                              | Element                                                                                                                                                                         |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object | [**IVdsIscsiInitiatorPortal**](/windows/desktop/api/Vds/nn-vds-ivdsiscsiinitiatorportal)\*.                                                                                                                 |
| Associated enumerations                           | [**VDS\_ISCSI\_IPSEC\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_iscsi_ipsec_flag).                                                                                                                        |
| Associated structures                             | [**VDS\_ISCSI\_INITIATOR\_PORTAL\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_iscsi_initiator_portal_prop), [**VDS\_ISCSI\_IPSEC\_KEY**](/windows/desktop/api/Vds/ns-vds-vds_iscsi_ipsec_key), [**VDS\_IPADDRESS**](/windows/desktop/api/Vds/ns-vds-vds_ipaddress). |



 

**\*Windows Server 2003:** This interface is not supported until Windows Server 2003 R2.

## HBA Port Object

The HBA port object models a Fibre Channel host bus adapter (HBA) port.

Use the [**IVdsServiceHba::QueryHbaPorts**](/windows/desktop/api/Vds/nf-vds-ivdsservicehba-queryhbaports) method to determine the HBA ports that are known to VDS on the local computer.

The following table lists the related interfaces, enumerations, and structures.

| Type                                              | Element                                                                                                                                                          |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Interfaces that are always exposed by this object | [**IVdsHbaPort**](/windows/desktop/api/Vds/nn-vds-ivdshbaport)\*.                                                                                                                            |
| Associated enumerations                           | [**VDS\_HBAPORT\_TYPE**](/windows/desktop/api/Vds/ne-vds-vds_hbaport_type), [**VDS\_HBAPORT\_STATUS**](/windows/desktop/api/Vds/ne-vds-vds_hbaport_status), [**VDS\_HBAPORT\_SPEED\_FLAG**](/windows/desktop/api/Vds/ne-vds-vds_hbaport_speed_flag). |
| Associated structures                             | [**VDS\_HBAPORT\_PROP**](/windows/desktop/api/Vds/ns-vds-vds_hbaport_prop).                                                                                                                  |



 

**\*Windows Server 2003:** This interface is not supported until Windows Server 2003 R2.

## Related topics

<dl> <dt>

[VDS Object Model](vds-object-model.md)
</dt> <dt>

[**IVdsServiceLoader::LoadService**](/windows/desktop/api/Vds/nf-vds-ivdsserviceloader-loadservice)
</dt> <dt>

[Loading VDS](loading-vds.md)
</dt> <dt>

[**IVdsService::GetObject**](/windows/desktop/api/Vds/nf-vds-ivdsservice-getobject)
</dt> <dt>

[VDS Notifications](vds-notification-model.md)
</dt> </dl>

 

 
