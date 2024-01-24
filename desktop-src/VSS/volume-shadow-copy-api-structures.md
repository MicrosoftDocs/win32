---
description: The following structures are defined in the Volume Shadow Copy API.
ms.assetid: 20cf12e4-4611-4e39-9f6f-e29f15e58b36
title: Volume Shadow Copy API Structures
ms.topic: article
ms.date: 05/31/2018
---

# Volume Shadow Copy API Structures

The following structures are defined in the Volume Shadow Copy API.



| Structure                                                           | Description                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VSS\_COMPONENTINFO**](/windows/desktop/api/VsBackup/ns-vsbackup-vss_componentinfo)                     | Contains information about a given component.                                                                                                                                                                                                                       |
| [**VSS\_DIFF\_AREA\_PROP**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_diff_area_prop)                 | Describes associations between source volumes containing the original file data and volumes containing the shadow copy storage area.                                                                                                                                |
| [**VSS\_DIFF\_VOLUME\_PROP**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_diff_volume_prop)             | Describes a shadow copy storage area volume.                                                                                                                                                                                                                        |
| [**VSS\_MGMT\_OBJECT\_PROP**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_mgmt_object_prop)             | Describes the properties of a volume, shadow copy storage volume, or a shadow copy storage area.                                                                                                                                                                    |
| [**VSS\_MGMT\_OBJECT\_UNION**](/openspecs/windows_protocols/ms-scmp/63b53947-2649-4eac-a883-498f77361396)           | A union of [**VSS\_VOLUME\_PROP**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_volume_prop), [**VSS\_DIFF\_VOLUME\_PROP**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_diff_volume_prop), and [**VSS\_DIFF\_AREA\_PROP**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_diff_area_prop) structures used by the [**VSS\_MGMT\_OBJECT\_PROP**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_mgmt_object_prop) structure. |
| [**VSS\_OBJECT\_PROP**](/windows/desktop/api/Vss/ns-vss-vss_object_prop)                        | Describes the properties of a provider, volume, shadow copy, or shadow copy set.                                                                                                                                                                                    |
| [**VSS\_OBJECT\_UNION**](/openspecs/windows_protocols/ms-scmp/f63af19f-bc5c-4a20-afaf-4f6e0f7c1045)                      | A union of [**VSS\_SNAPSHOT\_PROP**](/windows/desktop/api/Vss/ns-vss-vss_snapshot_prop) and [**VSS\_PROVIDER\_PROP**](/windows/desktop/api/Vss/ns-vss-vss_provider_prop) structures, used by the [**VSS\_OBJECT\_PROP**](/windows/desktop/api/Vss/ns-vss-vss_object_prop) structure.                                                                    |
| [**VSS\_PROVIDER\_PROP**](/windows/desktop/api/Vss/ns-vss-vss_provider_prop)                    | Specifies shadow copy provider properties.                                                                                                                                                                                                                          |
| [**VSS\_SNAPSHOT\_PROP**](/windows/desktop/api/Vss/ns-vss-vss_snapshot_prop)                    | Contains the properties of a shadow copy or shadow copy set.                                                                                                                                                                                                        |
| [**VSS\_VOLUME\_PROP**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_volume_prop)                        | Describes the properties of a shadow copy source volume.                                                                                                                                                                                                            |
| [**VSS\_VOLUME\_PROTECTION\_INFO**](/windows/desktop/api/VsMgmt/ns-vsmgmt-vss_volume_protection_info) | Contains information about a volume's shadow copy protection level.                                                                                                                                                                                                 |



 

 

 



