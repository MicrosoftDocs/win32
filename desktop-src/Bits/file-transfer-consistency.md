---
title: File Transfer Consistency
description: BITS guarantees that the version of the file it transfers is consistent based on the file size and time stamp, not content (BITS does not protect against man-in-the-middle attacks).
ms.assetid: ba82f172-a3ac-49d6-bccd-7d0b68ba66de
ms.topic: article
ms.date: 05/31/2018
---

# File Transfer Consistency

BITS guarantees that the version of the file it transfers is consistent based on the file size and time stamp, not content (BITS does not protect against man-in-the-middle attacks). To verify the contents yourself, you can use the [**IBackgroundCopyFile3::GetTemporaryName**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyfile3-gettemporaryname) method to get the name of the file that contains the downloaded content, verify the contents using your own mechanism, and then call the [**IBackgroundCopyFile3::SetValidationState**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyfile3-setvalidationstate) method to indicate to BITS if the contents of the file is valid. If you set the validation state to **FALSE** and the content is from the origin server, the job goes into the error state. If the content is from a peer, BITS downloads the file from the origin server.

For downloads, if the file size or time stamp changes while BITS is transferring the file, BITS restarts the transfer of that file only. For example, if the download job contains two files and the files are updated on the server while BITS is transferring the second file, BITS restarts the transfer of the second file only. The first file, which already transferred successfully, is not updated to reflect the new changes.

Note that if you own the file being downloaded from the server, you should create a new URL for each new version of the file. If you use the same URL for new versions of the file, some proxy servers may serve stale data from their cache because they do not verify with the original server if the file is stale.

For uploads, if the file size or time stamp changes during the file transfer, BITS generates an error and the job is placed in the BG\_JOB\_STATE\_ERROR state.

BITS does not synchronize transfer requests when one or more users request that the same file be transferred to the same location. BITS transfers the file for each request separately.

 

 




