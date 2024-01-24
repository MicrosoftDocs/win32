---
title: Volume management structures
description: Structures used in volume management (fileio.h).
ms.assetid: bbde9dfb-c205-4432-be71-250d73b881f1
ms.topic: article
ms.date: 02/09/2023
---

# Volume management structures

Structures used in volume management.

## In this section

| Topic | Description |
|--------|--------|
| [**BOOT\_AREA\_INFO**](/windows/win32/api/WinIoCtl/ns-winioctl-boot_area_info) | Contains the output for the [**FSCTL\_GET\_BOOT\_AREA\_INFO**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_boot_area_info) control code. |
| [**CREATE\_USN\_JOURNAL\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-create_usn_journal_data) | Contains information that describes an update sequence number (USN) change journal. |
| [**CSV\_IS\_OWNED\_BY\_CSVFS**](/windows/win32/api/WinIoCtl/ns-winioctl-csv_is_owned_by_csvfs) | Contains the output for the [**FSCTL\_IS\_VOLUME\_OWNED\_BYCSVFS**](/windows/win32/api/winioctl/ni-winioctl-fsctl_is_volume_owned_bycsvfs) control code that determines whether a volume is owned by CSVFS. |
| [**CSV\_NAMESPACE\_INFO**](/windows/win32/api/WinIoCtl/ns-winioctl-csv_namespace_info) | Contains the output for the [**FSCTL\_IS\_CSV\_FILE**](/windows/win32/api/winioctl/ni-winioctl-fsctl_is_csv_file) control code that retrieves namespace information for a file. |
| [**CSV\_QUERY\_VETO\_FILE\_DIRECT\_IO\_OUTPUT**](/windows/win32/api/WinIoCtl/ns-winioctl-csv_query_veto_file_direct_io_output) | Contains troubleshooting information about why a volume is in redirected mode. |
| [**DELETE\_USN\_JOURNAL\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-delete_usn_journal_data) | Contains information on the deletion of an update sequence number (USN) change journal using the [**FSCTL\_DELETE\_USN\_JOURNAL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_delete_usn_journal) control code. |
| [**FILE\_STORAGE\_TIER**](/windows/win32/api/WinIoctl/ns-winioctl-file_storage_tier) | Represents an identifier for the storage tier relative to the volume. |
| [**FILE\_STORAGE\_TIER\_REGION**](/windows/win32/api/WinIoctl/ns-winioctl-file_storage_tier_region) | Describes a single storage tier region. |
| [**FILE\_SYSTEM\_RECOGNITION\_INFORMATION**](/windows/win32/api/WinIoCtl/ns-winioctl-file_system_recognition_information) | Contains file system recognition information retrieved by the [**FSCTL\_QUERY\_FILE\_SYSTEM\_RECOGNITION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_file_system_recognition) control code. |
| [**FILE\_SYSTEM\_RECOGNITION\_STRUCTURE**](file-system-recognition-structure.md) | Contains the on-disk file system recognition information stored in the volume's boot sector (logical disk sector zero). |
| [**FSCTL\_GET\_INTEGRITY\_INFORMATION\_BUFFER**](/windows/win32/api/WinIoCtl/ns-winioctl-fsctl_get_integrity_information_buffer) | Contains the integrity information for a file or directory. |
| [**FSCTL\_QUERY\_REGION\_INFO\_INPUT**](/windows/win32/api/WinIoctl/ns-winioctl-fsctl_query_region_info_input) | Contains the storage tier regions from the storage stack for a particular volume. |
| [**FSCTL\_QUERY\_REGION\_INFO\_OUTPUT**](/windows/win32/api/WinIoctl/ns-winioctl-fsctl_query_region_info_output) | Contains information for one or more regions. |
| [**FSCTL\_QUERY\_STORAGE\_CLASSES\_OUTPUT**](/windows/win32/api/WinIoctl/ns-winioctl-fsctl_query_storage_classes_output) | Contains information for all tiers of a specific volume. |
| [**FSCTL\_SET\_INTEGRITY\_INFORMATION\_BUFFER**](/windows/win32/api/WinIoCtl/ns-winioctl-fsctl_set_integrity_information_buffer) | Input buffer passed with the [**FSCTL\_SET\_INTEGRITY\_INFORMATION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_set_integrity_information) control code. |
| [**LOOKUP\_STREAM\_FROM\_CLUSTER\_ENTRY**](/windows/win32/api/WinIoCtl/ns-winioctl-lookup_stream_from_cluster_entry) | Returned from the [**FSCTL\_LOOKUP\_STREAM\_FROM\_CLUSTER**](/windows/win32/api/winioctl/ni-winioctl-fsctl_lookup_stream_from_cluster) control code. |
| [**LOOKUP\_STREAM\_FROM\_CLUSTER\_INPUT**](/windows/win32/api/WinIoCtl/ns-winioctl-lookup_stream_from_cluster_input) | Passed as input to the [**FSCTL\_LOOKUP\_STREAM\_FROM\_CLUSTER**](/windows/win32/api/winioctl/ni-winioctl-fsctl_lookup_stream_from_cluster) control code. |
| [**LOOKUP\_STREAM\_FROM\_CLUSTER\_OUTPUT**](/windows/win32/api/WinIoCtl/ns-winioctl-lookup_stream_from_cluster_output) | Received as output from the [**FSCTL\_LOOKUP\_STREAM\_FROM\_CLUSTER**](/windows/win32/api/winioctl/ni-winioctl-fsctl_lookup_stream_from_cluster) control code. |
| [**MARK\_HANDLE\_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-mark_handle_info) | Contains information that is used to mark a specified file or directory, and its update sequence number (USN) change journal record with data about changes. |
| [**MARK\_HANDLE\_INFO32**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-mark_handle_info32) | Contains information that is used to mark a specified file or directory, and its update sequence number (USN) change journal record with data about changes. This is only defined for 64-bit code and exists to interpret [**MARK\_HANDLE\_INFO**](/windows-hardware/drivers/ddi/ntifs/ns-ntifs-mark_handle_info) structures sent by 32-bit code. |
| [**MFT\_ENUM\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-mft_enum_data_v0) | Contains information defining the boundaries for and starting place of an enumeration of update sequence number (USN) change journal records. |
| [**MFT\_ENUM\_DATA\_V1**](/windows/win32/api/WinIoCtl/ns-winioctl-mft_enum_data_v1) | Contains information defining the boundaries for and starting place of an enumeration of update sequence number (USN) change journal records for ReFS volumes. |
| [**MOVE\_FILE\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-move_file_data) | Contains input data for the [**FSCTL\_MOVE\_FILE**](/windows/win32/api/winioctl/ni-winioctl-fsctl_move_file) control code. |
| [**NTFS\_VOLUME\_DATA\_BUFFER**](/windows/win32/api/WinIoCtl/ns-winioctl-ntfs_extended_volume_data) | Represents volume data. |
| [**PLEX\_READ\_DATA\_REQUEST**](/windows/win32/api/WinIoCtl/ns-winioctl-plex_read_data_request) | Indicates the range of the read operation to perform and the plex from which to read. |
| [**READ\_FILE\_USN\_DATA**](/windows/win32/api/WinIoCtl/ns-winioctl-read_file_usn_data) | Specifies the versions of the update sequence number (USN) change journal supported by the application. |
| [**READ\_USN\_JOURNAL\_DATA\_V0**](/windows/win32/api/WinIoCtl/ns-winioctl-read_usn_journal_data_v0) | Contains information defining a set of update sequence number (USN) change journal records to return to the calling process. |
| [**READ\_USN\_JOURNAL\_DATA\_V1**](/previous-versions/windows/desktop/legacy/hh802706(v=vs.85)) | Contains information defining a set of update sequence number (USN) change journal records to return to the calling process. |
| [**REPAIR\_COPIES\_INPUT**](/windows/win32/api/WinIoCtl/ns-winioctl-repair_copies_input) | Input structure for the [**FSCTL\_REPAIR\_COPIES**](/windows/win32/api/winioctl/ni-winioctl-fsctl_repair_copies) control code. |
| [**REPAIR\_COPIES\_OUTPUT**](/windows/win32/api/WinIoCtl/ns-winioctl-repair_copies_output) | Contains output of a repair copies operation returned from the [**FSCTL\_REPAIR\_COPIES**](/windows/win32/api/winioctl/ni-winioctl-fsctl_repair_copies) control code. |
| [**RETRIEVAL\_POINTER\_BASE**](/windows/win32/api/WinIoCtl/ns-winioctl-retrieval_pointer_base) | Contains the output for the [**FSCTL\_GET\_RETRIEVAL\_POINTER\_BASE**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_retrieval_pointer_base) control code. |
| [**RETRIEVAL\_POINTERS\_BUFFER**](/windows/win32/api/WinIoCtl/ns-winioctl-retrieval_pointers_buffer) | Contains the output for the [**FSCTL\_GET\_RETRIEVAL\_POINTERS**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_retrieval_pointers) control code. |
| [**SHRINK\_VOLUME\_INFORMATION**](/windows/win32/api/WinIoCtl/ns-winioctl-shrink_volume_information) | Specifies the volume shrink operation to perform. |
| [**STARTING\_LCN\_INPUT\_BUFFER**](/windows/win32/api/WinIoCtl/ns-winioctl-starting_lcn_input_buffer) | Contains the starting LCN to the [**FSCTL\_GET\_VOLUME\_BITMAP**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_volume_bitmap) control code. |
| [**STARTING\_VCN\_INPUT\_BUFFER**](/windows/win32/api/WinIoCtl/ns-winioctl-starting_vcn_input_buffer) | Contains the starting VCN to the [**FSCTL\_GET\_RETRIEVAL\_POINTERS**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_retrieval_pointers) control code. |
| [**USN\_JOURNAL\_DATA\_V0**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_journal_data_v0) | Represents an update sequence number (USN) change journal, its records, and its capacity. |
| [**USN\_JOURNAL\_DATA\_V1**](/previous-versions/windows/desktop/legacy/hh802707(v=vs.85)) | Represents an update sequence number (USN) change journal, its records, and its capacity. |
| [**USN\_JOURNAL\_DATA\_V2**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_journal_data_v2) | Represents an update sequence number (USN) change journal, its records, and its capacity. This structure is the output buffer for the [**FSCTL\_QUERY\_USN\_JOURNAL**](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_usn_journal) control code. |
| [**USN\_RANGE\_TRACK\_OUTPUT**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_range_track_output) | Contains returned update sequence number (USN) from [**FSCTL\_USN\_TRACK\_MODIFIED\_RANGES**](/windows/win32/api/winioctl/ni-winioctl-fsctl_usn_track_modified_ranges) control code. |
| [**USN\_RECORD\_COMMON\_HEADER**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_common_header) | Contains the information for an update sequence number (USN) common header which is common through [**USN\_RECORD\_V2**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_v2), [**USN\_RECORD\_V3**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_v3) and [**USN\_RECORD\_V4**](/windows/win32/api/winioctl/ns-winioctl-usn_record_extent). |
| [**USN\_RECORD\_EXTENT**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_extent) | Contains the offset and length for an update sequence number (USN) record extent. |
| [**USN\_RECORD\_V2**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_v2) | Contains the information for an update sequence number (USN) change journal version 2.0 record. |
| [**USN\_RECORD\_V3**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_v3) | Contains the information for an update sequence number (USN) change journal version 3.0 record. |
| [**USN\_RECORD\_V4**](/windows/win32/api/winioctl/ns-winioctl-usn_record_extent) | Contains the information for an update sequence number (USN) change journal version 4.0 record. The version 2.0 and 3.0 records are defined by the [**USN\_RECORD\_V2**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_v2) (also called **USN\_RECORD**) and [**USN\_RECORD\_V3**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_record_v3) structures respectively. |
| [**USN\_TRACK\_MODIFIED\_RANGES**](/windows/win32/api/WinIoCtl/ns-winioctl-usn_track_modified_ranges) | Contains information on range tracking parameters for an update sequence number (USN) change journal using the [**FSCTL\_USN\_TRACK\_MODIFIED\_RANGES**](/windows/win32/api/winioctl/ni-winioctl-fsctl_usn_track_modified_ranges) control code. |
| [**VOLUME\_BITMAP\_BUFFER**](/windows/win32/api/WinIoCtl/ns-winioctl-volume_bitmap_buffer) | Represents the occupied and available clusters on a disk. |
| [**VOLUME\_DISK\_EXTENTS**](/windows/win32/api/WinIoCtl/ns-winioctl-volume_disk_extents) | Represents a physical location on a disk. |
| [**VOLUME\_GET\_GPT\_ATTRIBUTES\_INFORMATION**](/windows/win32/api/WinIoCtl/ns-winioctl-volume_get_gpt_attributes_information) | Contains volume attributes retrieved with the [**IOCTL\_VOLUME\_GET\_GPT\_ATTRIBUTES**](/windows/win32/api/WinIoCtl/ni-winioctl-ioctl_volume_get_gpt_attributes) control code. |
