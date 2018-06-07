---
Description: Descriptions of functions to use when working with mailslots, clients and servers.
ms.assetid: 40758d5e-8538-47d9-b8ca-8de5b053ee8b
title: Mailslot Operations
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Mailslot Operations

When working with mailslots, clients and servers should use only the functions discussed in the following tables. Do not use other functions, even if they accept file handles or file names as parameters, as they are not designed to work with mailslots.

## Mailslot Server Functions

Mailslot servers have exclusive use of three functions, as shown in the following table.



| Function                                   | Description                                                                                                                                                                                                  |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateMailslot**](/windows/desktop/api/Winbase/nf-winbase-createmailslota)   | Creates a mailslot and returns a mailslot handle.                                                                                                                                                            |
| [**GetMailslotInfo**](/windows/desktop/api/Winbase/nf-winbase-getmailslotinfo) | Retrieves the maximum message size, the mailslot size, the size of the next message in the mailslot, the number of messages in the mailslot, and the amount of time a read operation can wait for a message. |
| [**SetMailslotInfo**](/windows/desktop/api/Winbase/nf-winbase-setmailslotinfo) | Changes the read time-out for a mailslot.                                                                                                                                                                    |



 

The following functions are also used by mailslot servers.



| Function                                                         | Description                                         |
|------------------------------------------------------------------|-----------------------------------------------------|
| [**DuplicateHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724251)                      | Duplicates the mailslot handle.                     |
| [**ReadFile**](https://msdn.microsoft.com/library/windows/desktop/aa365467), [**ReadFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365468) | Retrieves messages from a mailslot.                 |
| [**GetFileTime**](https://msdn.microsoft.com/library/windows/desktop/ms724320)                              | Retrieves the date and time a mailslot was created. |
| [**SetFileTime**](https://msdn.microsoft.com/library/windows/desktop/ms724933)                              | Sets the date and time a mailslot was created.      |
| [**GetHandleInformation**](https://msdn.microsoft.com/library/windows/desktop/ms724329)            | Retrieves properties of the mailslot handle.        |
| [**SetHandleInformation**](https://msdn.microsoft.com/library/windows/desktop/ms724935)            | Sets properties of the mailslot handle.             |



 

## Mailslot Client Functions

A client process uses the following functions when interacting with a mailslot.



| Function                                                             | Description                                     |
|----------------------------------------------------------------------|-------------------------------------------------|
| [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211)                                  | Closes a mailslot handle for a client process.  |
| [**CreateFile**](https://msdn.microsoft.com/library/windows/desktop/aa363858)                                    | Creates a mailslot handle for a client process. |
| [**DuplicateHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724251)                          | Duplicates a mailslot handle.                   |
| [**WriteFile**](https://msdn.microsoft.com/library/windows/desktop/aa365747), [**WriteFileEx**](https://msdn.microsoft.com/library/windows/desktop/aa365748) | Writes data to a mailslot.                      |



 

 

 



