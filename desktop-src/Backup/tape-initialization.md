---
title: Tape Initialization
description: An application must use the CreateFile function to create a handle of a tape device. This handle is used in subsequent operations on the tape in the device.
ms.assetid: 5e7eddd2-8137-4e79-b1ee-c371bc4c7f75
keywords:
- tape initialization Backup
ms.topic: article
ms.date: 05/31/2018
---

# Tape Initialization

An application must use the [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea) function to create a handle of a tape device. This handle is used in subsequent operations on the tape in the device.

Before an application writes to a tape, the tape must be formatted according to the needs of the application and the capabilities of the tape drive being used. The [**CreateTapePartition**](/windows/desktop/api/Winbase/nf-winbase-createtapepartition) function reformats a tape, creating on it a given number of partitions of a specified size.

The [**PrepareTape**](/windows/desktop/api/Winbase/nf-winbase-preparetape) function prepares a tape to be accessed or removed. This function can load, unload, lock, or unlock a tape. This function can also tension the tape by moving the tape to the end of the tape and back to the beginning.

To retrieve and set information about a tape and tape drive, an application uses the [**GetTapeParameters**](/windows/desktop/api/Winbase/nf-winbase-gettapeparameters), [**SetTapeParameters**](/windows/desktop/api/Winbase/nf-winbase-settapeparameters), and [**GetTapeStatus**](/windows/desktop/api/Winbase/nf-winbase-gettapestatus) functions.

[**GetTapeParameters**](/windows/desktop/api/Winbase/nf-winbase-gettapeparameters) retrieves information that describes a tape or a tape drive. The tape information includes the tape's type, density, and block size; the number of partitions on the tape; the amount of tape remaining; and so on. The tape drive information includes the drive's default block size, the maximum partition count, and the features that are supported.

[**SetTapeParameters**](/windows/desktop/api/Winbase/nf-winbase-settapeparameters) either sets the tape block size or sets the tape drive flags that indicate whether the drive supports hardware error correction, data compression, data padding, or any combination of the three.

[**GetTapeStatus**](/windows/desktop/api/Winbase/nf-winbase-gettapestatus) indicates whether the tape drive is ready to process tape commands.

 

 