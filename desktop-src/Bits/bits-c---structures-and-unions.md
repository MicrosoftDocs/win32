---
title: BITS Structures and Unions
description: The Background Intelligent Transfer Service (BITS) interfaces use the following structures.
ms.assetid: a1b8b4a1-77d6-46ac-96d5-6a0c99cfc643
ms.topic: article
ms.date: 05/31/2018
---

# BITS Structures and Unions

The Background Intelligent Transfer Service (BITS) [interfaces](bits-interfaces.md) use the following structures.

## In this section



| Topic                                                                        | Description                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BG\_AUTH\_CREDENTIALS**](/windows/desktop/api/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0005)<br/>              | The [**BG\_AUTH\_CREDENTIALS**](/windows/desktop/api/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0005) structure identifies the target (proxy or server), authentication scheme, and the user's credentials to use for user authentication requests. The structure is passed to the [**IBackgroundCopyJob2::SetCredentials**](/windows/desktop/api/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials) method.<br/>                  |
| [**BG\_AUTH\_CREDENTIALS\_UNION**](/windows/desktop/api/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0004)<br/> | The [**BG\_AUTH\_CREDENTIALS\_UNION**](/windows/desktop/api/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0004) union identifies the credentials to use for the authentication scheme specified in the [**BG\_AUTH\_CREDENTIALS**](/windows/desktop/api/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0005) structure.<br/>                                                                                                                     |
| [**BG\_BASIC\_CREDENTIALS**](/windows/desktop/api/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0003)<br/>            | The [**BG\_BASIC\_CREDENTIALS**](/windows/desktop/api/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0003) structure identifies the user name and password to authenticate.<br/>                                                                                                                                                                                                                      |
| [**BG\_FILE\_INFO**](/windows/desktop/api/Bits/ns-bits-_bg_file_info)<br/>                            | The [**BG\_FILE\_INFO**](/windows/desktop/api/Bits/ns-bits-_bg_file_info) structure provides the local and remote names of the file to transfer.<br/>                                                                                                                                                                                                                                |
| [**BG\_FILE\_PROGRESS**](/windows/desktop/api/Bits/ns-bits-_bg_file_progress)<br/>                    | The [**BG\_FILE\_PROGRESS**](/windows/desktop/api/Bits/ns-bits-_bg_file_progress) structure provides file-related progress information, such as the number of bytes transferred.<br/>                                                                                                                                                                                                |
| [**BG\_FILE\_RANGE**](/windows/desktop/api/Bits2_0/ns-bits2_0-_bg_file_range)<br/>                          | The [**BG\_FILE\_RANGE**](/windows/desktop/api/Bits2_0/ns-bits2_0-_bg_file_range) structure identifies a range of bytes to download from a file.<br/>                                                                                                                                                                                                                                      |
| [**BG\_JOB\_PROGRESS**](/windows/desktop/api/Bits/ns-bits-_bg_job_progress)<br/>                      | The [**BG\_JOB\_PROGRESS**](/windows/desktop/api/Bits/ns-bits-_bg_job_progress) structure provides job-related progress information, such as the number of bytes and files transferred. For upload jobs, the progress applies to the upload file, not the reply file. To view reply file progress, see the [**BG\_JOB\_REPLY\_PROGRESS**](/windows/desktop/api/Bits1_5/ns-bits1_5-_bg_job_reply_progress) structure.<br/> |
| [**BG\_JOB\_REPLY\_PROGRESS**](/windows/desktop/api/Bits1_5/ns-bits1_5-_bg_job_reply_progress)<br/>         | The [**BG\_JOB\_REPLY\_PROGRESS**](/windows/desktop/api/Bits1_5/ns-bits1_5-_bg_job_reply_progress) structure provides progress information related to the reply portion of an upload-reply job.<br/>                                                                                                                                                                                       |
| [**BG\_JOB\_TIMES**](/windows/desktop/api/Bits/ns-bits-_bg_job_times)<br/>                            | The [**BG\_JOB\_TIMES**](/windows/desktop/api/Bits/ns-bits-_bg_job_times) structure provides job-related time stamps.<br/>                                                                                                                                                                                                                                                           |
| [**BITS\_FILE\_PROPERTY\_VALUE**](/windows/desktop/api/Bits5_0/ns-bits5_0-__midl___midl_itf_bits5_0_0000_0000_0005)<br/>   | Provides the property value of a BITS file.<br/>                                                                                                                                                                                                                                                                                                      |
| [**BITS\_JOB\_PROPERTY\_VALUE**](/windows/desktop/api/Bits5_0/ns-bits5_0-__midl___midl_itf_bits5_0_0000_0000_0003)<br/>     | Provides the property value of the BITS job based on the value of the [**BITS\_JOB\_PROPERTY\_ID**](/windows/desktop/api/Bits5_0/ne-bits5_0-__midl___midl_itf_bits5_0_0000_0000_0002) enumeration.<br/>                                                                                                                                                                                                       |



 

 

 





