---
title: Delivery Optimization Structures and Unions
description: The Delivery Optimization interfaces use the following structures.
ms.assetid: 58A5361E-871A-4911-85BD-83F18CB9A2F5
ms.topic: article
ms.date: 07/03/2019
---

# Delivery Optimization Structures and Unions

The Delivery Optimization [interfaces](do-interfaces.md) use the following structures.

## In this section

| Topic | Description |
|-|-|
| [**BG_FILE_PROGRESS**](bg-file-progress.md) | The **BG_FILE_PROGRESS** structure provides file-related progress information, such as the number of bytes transferred. |
| [**BG_FILE_RANGE**](bg-file-range.md) | The **BG_FILE_RANGE** structure identifies a range of bytes to download from a file. |
| [**BG_JOB_PROGRESS**](bg-job-progress.md) | The **BG_JOB_PROGRESS** structure provides job-related progress information, such as the number of bytes and files transferred. For upload jobs, the progress applies to the upload file, not the reply file.  |
| [**BG_JOB_TIMES**](bg-job-times.md) | The **BG_JOB_TIMES** structure provides job-related time stamps. |
| [**BITS_FILE_PROPERTY_VALUE**](bits-file-property-value.md) | The **BITS_FILE_PROPERTY_VALUE** union provides the property value of the Delivery Optimization file based on a value from the [**BITS_FILE_PROPERTY_ID**](bits-file-property-id-.md) enumeration. |
| [**BITS_JOB_PROPERTY_VALUE**](bits-job-property-value-.md) | The **BITS_JOB_PROPERTY_VALUE** union provides the property value of the Delivery Optimization job based on the value of the [**BITS_JOB_PROPERTY_ID**](bits-job-property-id.md) enumeration. |
| [**DO_DOWNLOAD_ENUM_CATEGORY**](./do/ns-do-do_download_enum_category.md) | Used by **IDOManager::EnumDownloads** to filter the downloads enumeration by the specific property's value. |
| [**DO_DOWNLOAD_RANGE**](./deliveryoptimizationdownloadtypes/ns-deliveryoptimizationdownloadtypes-do_download_range.md) | Identifies a single range of bytes to download from a file. |
| [**DO_DOWNLOAD_RANGE_INFO**](./do/ns-do-do_download_range_info.md) | Identifies an array of ranges of bytes to download from a file. |
| [**DO_DOWNLOAD_STATUS**](./do/ns-do-do_download_status.md) | Used to obtain the status of a specific download. |
| [**DOSwarmStats**](doswarmstats.md) | Contains fields for download and upload statistics for a file. |