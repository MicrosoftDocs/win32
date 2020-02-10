---
title: ProjFS callback functions
description: The following callback functions are declared in projectedfslib.h.
ms.assetid: <GUID-GOES-HERE>
ms.date: 01/17/2020
ms.topic: article
---

# Callback functions

The following callback functions are declared in projectedfslib.h.

## In this section

| Topic | Description |
|-|-|
| [**PRJ_CANCEL_COMMAND_CB**](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_cancel_command_cb) | Notifies the provider that an operation by an earlier invocation of a callback should be canceled. |
| [**PRJ_END_DIRECTORY_ENUMERATION_CB**](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_end_directory_enumeration_cb) | Informs the provider that a directory enumeration is over. |
| [**PRJ_GET_DIRECTORY_ENUMERATION_CB**](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_get_directory_enumeration_cb) | Requests directory enumeration information from the provider.
| [**PRJ_GET_FILE_DATA_CB**](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_get_file_data_cb) | Requests the contents of a file's primary data stream.
| [**PRJ_GET_PLACEHOLDER_INFO_CB**](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_get_placeholder_info_cb) | Requests information for a file or directory from the provider.
| [**PRJ_NOTIFICATION_CB**](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_notification_cb) | Delivers notifications to the provider about file system operations.
| [**PRJ_QUERY_FILE_NAME_CB**](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_query_file_name_cb) | Determines whether a given file path exists in the provider's backing store.
| [**PRJ_START_DIRECTORY_ENUMERATION_CB**](/windows/win32/api/projectedfslib/nc-projectedfslib-prj_start_directory_enumeration_cb) | Informs the provider that a directory enumeration is starting.