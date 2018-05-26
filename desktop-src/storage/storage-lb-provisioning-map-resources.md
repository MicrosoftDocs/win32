---
title: STORAGE\_LB\_PROVISIONING\_MAP\_RESOURCES structure
description: The STORAGE\_LB\_PROVISIONING\_MAP\_RESOURCES structure contains, when valid, the count of available and used bytes mapped to a storage device. This structure is returned from an IOCTL\_STORAGE\_GET\_LB\_PROVISIONING\_MAP\_RESOURCES request.
ms.assetid: 6F7DE233-D002-4927-80FC-307A3A33653A
keywords:
- STORAGE_LB_PROVISIONING_MAP_RESOURCES structure Storage Devices
- PSTORAGE_LB_PROVISIONING_MAP_RESOURCES structure pointer Storage Devices
topic_type:
- apiref
api_name:
- STORAGE_LB_PROVISIONING_MAP_RESOURCES
api_location:
- Ntddstor.h
api_type:
- HeaderDef
ms.date: 05/31/2018
ms.topic: structure
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# STORAGE\_LB\_PROVISIONING\_MAP\_RESOURCES structure

The **STORAGE\_LB\_PROVISIONING\_MAP\_RESOURCES** structure contains, when valid, the count of available and used bytes mapped to a storage device. This structure is returned from an [**IOCTL\_STORAGE\_GET\_LB\_PROVISIONING\_MAP\_RESOURCES**](ioctl-storage-get-lb-provisioning-map-resources.md) request.

## Syntax


```C++
typedef struct _STORAGE_LB_PROVISIONING_MAP_RESOURCES {
  ULONG     Size;
  ULONG     Version;
  UCHAR     AvailableMappingResourcesValid  :1;
  UCHAR     UsedMappingResourcesValid  :1;
  UCHAR     Reserved0  :6;
  UCHAR     Reserved1[3];
  UCHAR     AvailableMappingResourcesScope  :2;
  UCHAR     UsedMappingResourcesScope  :2;
  UCHAR     Reserved2  :4;
  UCHAR     Reserved3[3];
  ULONGLONG AvailableMappingResources;
  ULONGLONG UsedMappingResources;
} STORAGE_LB_PROVISIONING_MAP_RESOURCES, *PSTORAGE_LB_PROVISIONING_MAP_RESOURCES;
```



## Members

<dl> <dt>

**Size**
</dt> <dd>

The size of this structure. This is set to **sizeof**(STORAGE\_LB\_PROVISIONING\_MAP\_RESOURCES).

</dd> <dt>

**Version**
</dt> <dd>

The version of this structure.

</dd> <dt>

**AvailableMappingResourcesValid**
</dt> <dd>

The validity of the **AvailableMappingResources** member.



| Value                                                                        | Meaning                                                |
|------------------------------------------------------------------------------|--------------------------------------------------------|
| <dl> <dt>0</dt> </dl> | **AvailableMappingResources** is not valid.<br/> |
| <dl> <dt>1</dt> </dl> | **AvailableMappingResources** is valid.<br/>     |



 

</dd> <dt>

**UsedMappingResourcesValid**
</dt> <dd>

The validity of the **UsedMappingResources** member.



| Value                                                                        | Meaning                                           |
|------------------------------------------------------------------------------|---------------------------------------------------|
| <dl> <dt>0</dt> </dl> | **UsedMappingResources** is not valid.<br/> |
| <dl> <dt>1</dt> </dl> | **UsedMappingResources** is valid.<br/>     |



 

</dd> <dt>

**Reserved0**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved1**
</dt> <dd>

Reserved.

</dd> <dt>

**AvailableMappingResourcesScope**
</dt> <dd>

Resources scope available to a LUN or a LUN pool.



| Value                                                                                                                                                                                                                                                                                                                                | Meaning                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_REPORTED"></span><span id="log_page_lbp_resource_scope_not_reported"></span><dl> <dt>**LOG\_PAGE\_LBP\_RESOURCE\_SCOPE\_NOT\_REPORTED**</dt> <dt>0</dt> </dl>                           | Mapping resources are not reported.<br/>        |
| <span id="LOG_PAGE_LBP_RESOURCE_SCOPE_DEDICATED_TO_LUN"></span><span id="log_page_lbp_resource_scope_dedicated_to_lun"></span><dl> <dt>**LOG\_PAGE\_LBP\_RESOURCE\_SCOPE\_DEDICATED\_TO\_LUN**</dt> <dt>1</dt> </dl>              | Mapping resources dedicated to a LUN.<br/>      |
| <span id="LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_DEDICATED_TO_LUN"></span><span id="log_page_lbp_resource_scope_not_dedicated_to_lun"></span><dl> <dt>**LOG\_PAGE\_LBP\_RESOURCE\_SCOPE\_NOT\_DEDICATED\_TO\_LUN**</dt> <dt>2</dt> </dl> | Mapping resources dedicated to a LUN pool.<br/> |



 

</dd> <dt>

**UsedMappingResourcesScope**
</dt> <dd>

Resources scope used by a LUN or LUN pool.



| Value                                                                                                                                                                                                                                                                                                                                | Meaning                                               |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------|
| <span id="LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_REPORTED"></span><span id="log_page_lbp_resource_scope_not_reported"></span><dl> <dt>**LOG\_PAGE\_LBP\_RESOURCE\_SCOPE\_NOT\_REPORTED**</dt> <dt>0</dt> </dl>                           | Mapping resources are not reported.<br/>        |
| <span id="LOG_PAGE_LBP_RESOURCE_SCOPE_DEDICATED_TO_LUN"></span><span id="log_page_lbp_resource_scope_dedicated_to_lun"></span><dl> <dt>**LOG\_PAGE\_LBP\_RESOURCE\_SCOPE\_DEDICATED\_TO\_LUN**</dt> <dt>1</dt> </dl>              | Mapping resources dedicated to a LUN.<br/>      |
| <span id="LOG_PAGE_LBP_RESOURCE_SCOPE_NOT_DEDICATED_TO_LUN"></span><span id="log_page_lbp_resource_scope_not_dedicated_to_lun"></span><dl> <dt>**LOG\_PAGE\_LBP\_RESOURCE\_SCOPE\_NOT\_DEDICATED\_TO\_LUN**</dt> <dt>2</dt> </dl> | Mapping resources dedicated to a LUN pool.<br/> |



 

</dd> <dt>

**Reserved2**
</dt> <dd>

Reserved.

</dd> <dt>

**Reserved3**
</dt> <dd>

Reserved.

</dd> <dt>

**AvailableMappingResources**
</dt> <dd>

The count, in bytes, of the available mapping resources for a disk.

</dd> <dt>

**UsedMappingResources**
</dt> <dd>

The count, in bytes, of the used mapping resources for a disk.

</dd> </dl>

## Remarks

As a managed storage element, resource usage for a thinly provisioned LUN is tracked. Resource allocation is logged for the device by the storage subsystem. A storage application can query for this resource usage information using the [**IOCTL\_STORAGE\_GET\_LB\_PROVISIONING\_MAP\_RESOURCES**](ioctl-storage-get-lb-provisioning-map-resources.md) request.

Logging of mapped resource counts is dependent on support from the storage device. The **AvailableMappingResources** and **UsedMappingResources** members contain resource counts when their respective validity fields are set.

Resource counts are in bytes instead of totals of blocks or slabs.

## Requirements



|                    |                                                                                                                      |
|--------------------|----------------------------------------------------------------------------------------------------------------------|
| Version<br/> | Available starting with Windows 8.<br/>                                                                        |
| Header<br/>  | <dl> <dt>Ntddstor.h (include Ntddstor.h or Scsi.h)</dt> </dl> |



## See also

<dl> <dt>

[**IOCTL\_STORAGE\_GET\_LB\_PROVISIONING\_MAP\_RESOURCES**](ioctl-storage-get-lb-provisioning-map-resources.md)
</dt> </dl>

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstorage\storage%5D:%20STORAGE_LB_PROVISIONING_MAP_RESOURCES%20structure%20%20RELEASE:%20%283/29/2018%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")






