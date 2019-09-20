---
title: BITS structures and unions
description: The Background Intelligent Transfer Service (BITS) interfaces use the following structures.
ms.assetid: a1b8b4a1-77d6-46ac-96d5-6a0c99cfc643
ms.topic: article
ms.date: 02/21/2019
---

# BITS structures and unions

The Background Intelligent Transfer Service (BITS) [interfaces](bits-interfaces.md) use the following structures.

## In this section

| Topic | Description |
|-|-|
| [**BG_AUTH_CREDENTIALS**](/windows/win32/api/bits1_5/ns-bits1_5-bg_auth_credentials) | Identifies the target (proxy or server), authentication scheme, and the user's credentials to use for user authentication requests. The structure is passed to the [IBackgroundCopyJob2::SetCredentials method](/windows/win32/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials). |
| [**BG_AUTH_CREDENTIALS_UNION**](/windows/win32/api/bits1_5/ns-bits1_5-bg_auth_credentials_union) | Identifies the credentials to use for the authentication scheme specified in the [BG_AUTH_CREDENTIALS structure](/windows/win32/api/bits1_5/ns-bits1_5-bg_auth_credentials). |
| [**BG_BASIC_CREDENTIALS**](/windows/win32/api/bits1_5/ns-bits1_5-bg_basic_credentials) | Identifies the user name and password to authenticate. |
| [**BG_FILE_INFO**](/windows/win32/api/bits/ns-bits-bg_file_info) | Provides the local and remote names of the file to transfer. |
| [**BG_FILE_PROGRESS**](/windows/win32/api/bits/ns-bits-bg_file_progress) | Provides file-related progress information, such as the number of bytes transferred. |
| [**BG_FILE_RANGE**](/windows/win32/api/bits2_0/ns-bits2_0-bg_file_range) | Identifies a range of bytes to download from a file. |
| [**BG_JOB_PROGRESS**](/windows/win32/api/bits/ns-bits-bg_job_progress) | Provides job-related progress information, such as the number of bytes and files transferred. For upload jobs, the progress applies to the upload file, not the reply file. To view reply file progress, see the [BG_JOB_REPLY_PROGRESS structure](/windows/win32/api/bits1_5/ns-bits1_5-bg_job_reply_progress). |
| [**BG_JOB_REPLY_PROGRESS**](/windows/win32/api/bits1_5/ns-bits1_5-bg_job_reply_progress) | Provides progress information related to the reply portion of an upload-reply job. |
| [**BG_JOB_TIMES**](/windows/win32/api/bits/ns-bits-bg_job_times) | Provides job-related time stamps. |
| [**BITS_FILE_PROPERTY_VALUE union**](/windows/win32/api/bits5_0/ns-bits5_0-bits_file_property_value) | Provides the property value of a BITS file. |
| [**BITS_JOB_PROPERTY_VALUE**](/windows/win32/api/bits5_0/ns-bits5_0-bits_file_property_value) | Provides the property value of the BITS job based on the value of the [BITS_JOB_PROPERTY_ID enumeration](/windows/win32/api/bits5_0/ne-bits5_0-bits_job_property_id). |
