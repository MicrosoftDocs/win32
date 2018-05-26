---
Description: The following structures are defined in the Volume Shadow Copy API.
ms.assetid: 20cf12e4-4611-4e39-9f6f-e29f15e58b36
title: Volume Shadow Copy API Structures
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Volume Shadow Copy API Structures

The following structures are defined in the Volume Shadow Copy API.



| Structure                                                           | Description                                                                                                                                                                                                                                                         |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**VSS\_COMPONENTINFO**](/windows/win32/VsBackup/ns-vsbackup-_vss_componentinfo?branch=master)                     | Contains information about a given component.                                                                                                                                                                                                                       |
| [**VSS\_DIFF\_AREA\_PROP**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_diff_area_prop?branch=master)                 | Describes associations between source volumes containing the original file data and volumes containing the shadow copy storage area.                                                                                                                                |
| [**VSS\_DIFF\_VOLUME\_PROP**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_diff_volume_prop?branch=master)             | Describes a shadow copy storage area volume.                                                                                                                                                                                                                        |
| [**VSS\_MGMT\_OBJECT\_PROP**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_mgmt_object_prop?branch=master)             | Describes the properties of a volume, shadow copy storage volume, or a shadow copy storage area.                                                                                                                                                                    |
| [**VSS\_MGMT\_OBJECT\_UNION**](/windows/win32/VsMgmt/ns-vsmgmt-__midl___midl_itf_vsmgmt_0000_0000_0001?branch=master)           | A union of [**VSS\_VOLUME\_PROP**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_volume_prop?branch=master), [**VSS\_DIFF\_VOLUME\_PROP**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_diff_volume_prop?branch=master), and [**VSS\_DIFF\_AREA\_PROP**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_diff_area_prop?branch=master) structures used by the [**VSS\_MGMT\_OBJECT\_PROP**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_mgmt_object_prop?branch=master) structure. |
| [**VSS\_OBJECT\_PROP**](/windows/win32/Vss/ns-vss-_vss_object_prop?branch=master)                        | Describes the properties of a provider, volume, shadow copy, or shadow copy set.                                                                                                                                                                                    |
| [**VSS\_OBJECT\_UNION**](/windows/win32/Vss/ns-vss-__midl___midl_itf_vss_0000_0000_0001?branch=master)                      | A union of [**VSS\_SNAPSHOT\_PROP**](/windows/win32/Vss/ns-vss-_vss_snapshot_prop?branch=master) and [**VSS\_PROVIDER\_PROP**](/windows/win32/Vss/ns-vss-_vss_provider_prop?branch=master) structures, used by the [**VSS\_OBJECT\_PROP**](/windows/win32/Vss/ns-vss-_vss_object_prop?branch=master) structure.                                                                    |
| [**VSS\_PROVIDER\_PROP**](/windows/win32/Vss/ns-vss-_vss_provider_prop?branch=master)                    | Specifies shadow copy provider properties.                                                                                                                                                                                                                          |
| [**VSS\_SNAPSHOT\_PROP**](/windows/win32/Vss/ns-vss-_vss_snapshot_prop?branch=master)                    | Contains the properties of a shadow copy or shadow copy set.                                                                                                                                                                                                        |
| [**VSS\_VOLUME\_PROP**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_volume_prop?branch=master)                        | Describes the properties of a shadow copy source volume.                                                                                                                                                                                                            |
| [**VSS\_VOLUME\_PROTECTION\_INFO**](/windows/win32/VsMgmt/ns-vsmgmt-_vss_volume_protection_info?branch=master) | Contains information about a volume's shadow copy protection level.                                                                                                                                                                                                 |



 

 

 



