---
title: BITS Structures and Unions
description: The Background Intelligent Transfer Service (BITS) interfaces use the following structures.
ms.assetid: a1b8b4a1-77d6-46ac-96d5-6a0c99cfc643
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# BITS Structures and Unions

The Background Intelligent Transfer Service (BITS) [interfaces](bits-interfaces.md) use the following structures.

## In this section



| Topic                                                                        | Description                                                                                                                                                                                                                                                                                                                                                 |
|------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**BG\_AUTH\_CREDENTIALS**](/windows/win32/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0005?branch=master)<br/>              | The [**BG\_AUTH\_CREDENTIALS**](/windows/win32/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0005?branch=master) structure identifies the target (proxy or server), authentication scheme, and the user's credentials to use for user authentication requests. The structure is passed to the [**IBackgroundCopyJob2::SetCredentials**](/windows/win32/Bits1_5/nf-bits1_5-ibackgroundcopyjob2-setcredentials?branch=master) method.<br/>                  |
| [**BG\_AUTH\_CREDENTIALS\_UNION**](/windows/win32/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0004?branch=master)<br/> | The [**BG\_AUTH\_CREDENTIALS\_UNION**](/windows/win32/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0004?branch=master) union identifies the credentials to use for the authentication scheme specified in the [**BG\_AUTH\_CREDENTIALS**](/windows/win32/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0005?branch=master) structure.<br/>                                                                                                                     |
| [**BG\_BASIC\_CREDENTIALS**](/windows/win32/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0003?branch=master)<br/>            | The [**BG\_BASIC\_CREDENTIALS**](/windows/win32/Bits1_5/ns-bits1_5-__midl_ibackgroundcopyjob2_0003?branch=master) structure identifies the user name and password to authenticate.<br/>                                                                                                                                                                                                                      |
| [**BG\_FILE\_INFO**](/windows/win32/Bits/ns-bits-_bg_file_info?branch=master)<br/>                            | The [**BG\_FILE\_INFO**](/windows/win32/Bits/ns-bits-_bg_file_info?branch=master) structure provides the local and remote names of the file to transfer.<br/>                                                                                                                                                                                                                                |
| [**BG\_FILE\_PROGRESS**](/windows/win32/Bits/ns-bits-_bg_file_progress?branch=master)<br/>                    | The [**BG\_FILE\_PROGRESS**](/windows/win32/Bits/ns-bits-_bg_file_progress?branch=master) structure provides file-related progress information, such as the number of bytes transferred.<br/>                                                                                                                                                                                                |
| [**BG\_FILE\_RANGE**](/windows/win32/Bits2_0/ns-bits2_0-_bg_file_range?branch=master)<br/>                          | The [**BG\_FILE\_RANGE**](/windows/win32/Bits2_0/ns-bits2_0-_bg_file_range?branch=master) structure identifies a range of bytes to download from a file.<br/>                                                                                                                                                                                                                                      |
| [**BG\_JOB\_PROGRESS**](/windows/win32/Bits/ns-bits-_bg_job_progress?branch=master)<br/>                      | The [**BG\_JOB\_PROGRESS**](/windows/win32/Bits/ns-bits-_bg_job_progress?branch=master) structure provides job-related progress information, such as the number of bytes and files transferred. For upload jobs, the progress applies to the upload file, not the reply file. To view reply file progress, see the [**BG\_JOB\_REPLY\_PROGRESS**](/windows/win32/Bits1_5/ns-bits1_5-_bg_job_reply_progress?branch=master) structure.<br/> |
| [**BG\_JOB\_REPLY\_PROGRESS**](/windows/win32/Bits1_5/ns-bits1_5-_bg_job_reply_progress?branch=master)<br/>         | The [**BG\_JOB\_REPLY\_PROGRESS**](/windows/win32/Bits1_5/ns-bits1_5-_bg_job_reply_progress?branch=master) structure provides progress information related to the reply portion of an upload-reply job.<br/>                                                                                                                                                                                       |
| [**BG\_JOB\_TIMES**](/windows/win32/Bits/ns-bits-_bg_job_times?branch=master)<br/>                            | The [**BG\_JOB\_TIMES**](/windows/win32/Bits/ns-bits-_bg_job_times?branch=master) structure provides job-related time stamps.<br/>                                                                                                                                                                                                                                                           |
| [**BITS\_FILE\_PROPERTY\_VALUE**](/windows/win32/Bits5_0/ns-bits5_0-__midl___midl_itf_bits5_0_0000_0000_0005?branch=master)<br/>   | Provides the property value of a BITS file.<br/>                                                                                                                                                                                                                                                                                                      |
| [**BITS\_JOB\_PROPERTY\_VALUE**](/windows/win32/Bits5_0/ns-bits5_0-__midl___midl_itf_bits5_0_0000_0000_0003?branch=master)<br/>     | Provides the property value of the BITS job based on the value of the [**BITS\_JOB\_PROPERTY\_ID**](/windows/win32/Bits5_0/ne-bits5_0-__midl___midl_itf_bits5_0_0000_0000_0002?branch=master) enumeration.<br/>                                                                                                                                                                                                       |



 

 

 





