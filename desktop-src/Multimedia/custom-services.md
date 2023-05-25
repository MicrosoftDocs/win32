---
title: Custom Services
description: Custom Services
ms.assetid: 98b68205-3a34-4406-84de-bf2c8a5ed5b0
keywords:
- multimedia file I/O,custom services
- file I/O,custom services
- input and output (I/O),custom services
- I/O (input and output),custom services
- custom I/O
- mmioInstallIOProc function
- mmioOpen function
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Custom Services

\[The feature associated with this page, [Multimedia File I/O](/windows/win32/multimedia/multimedia-file-i-o), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **Multimedia File I/O**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Multimedia file I/O services use I/O procedures to handle the physical input and output associated with reading and writing to different types of storage systems, such as file-archival systems and database-storage systems. Predefined I/O procedures exist for the standard file systems and for memory files, but you can supply a custom I/O procedure for accessing a unique storage system by using the [**mmioInstallIOProc**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioinstallioproc) function.

To open a file by using a custom I/O procedure, use the [**mmioOpen**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioopen) function. Include a plus sign (+) or the CFSEPCHAR constant in the filename to separate the name of the physical file from the name of the element of the file you want to open. The following example opens a file element named "element" from a file named FILENAME.ARC:


```C++
mmioOpen("filename.arc+element", NULL, MMIO_READ); 
```



When the file I/O manager encounters a plus sign in a filename, it examines the filename extension to determine which I/O procedure to associate with the file. In the previous example, the file I/O manager would attempt to use the I/O procedure associated with the .ARC filename extension; this I/O procedure would have been installed by using [**mmioInstallIOProc**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioinstallioproc). If no I/O procedure is installed, [**mmioOpen**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioopen) returns an error.

I/O procedures must respond to the following messages:

-   [**MMIOM\_CLOSE**](mmiom-close.md)
-   [**MMIOM\_OPEN**](mmiom-open.md)
-   [**MMIOM\_READ**](mmiom-read.md)
-   [**MMIOM\_WRITE**](mmiom-write.md)
-   [**MMIOM\_SEEK**](mmiom-seek.md)
-   [**MMIOM\_RENAME**](mmiom-rename.md)
-   [**MMIOM\_WRITEFLUSH**](mmiom-writeflush.md)

You can also create custom messages and send them to your I/O procedure by using the [**mmioSendMessage**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmiosendmessage) function. If you define your own messages, make sure they are defined at or above the value defined by the MMIOM\_USER constant.

In addition to processing messages, an I/O procedure must maintain the **lDiskOffset** member of the [**MMIOINFO**](/previous-versions//dd757322(v=vs.85)) structure (pointed to by the *lpmmioinfo* parameter of the **mmioOpen** function). The **lDiskOffset** member must always contain the file offset to the location that the next MMIOM\_READ or MMIOM\_WRITE message will access. The offset is specified in bytes and is relative to the beginning of the file. The I/O procedure can use the **adwInfo** member to maintain any required state information. The I/O procedure should not modify any other members in the **MMIOINFO** structure.

 

 