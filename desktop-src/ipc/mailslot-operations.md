---
description: Descriptions of functions to use when working with mailslots, clients and servers.
ms.assetid: 40758d5e-8538-47d9-b8ca-8de5b053ee8b
title: Mailslot Operations
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
| [**DuplicateHandle**](/windows/desktop/api/handleapi/nf-handleapi-duplicatehandle)                      | Duplicates the mailslot handle.                     |
| [**ReadFile**](/windows/desktop/api/fileapi/nf-fileapi-readfile), [**ReadFileEx**](/windows/desktop/api/fileapi/nf-fileapi-readfileex) | Retrieves messages from a mailslot.                 |
| [**GetFileTime**](/windows/desktop/api/fileapi/nf-fileapi-getfiletime)                              | Retrieves the date and time a mailslot was created. |
| [**SetFileTime**](/windows/desktop/api/fileapi/nf-fileapi-setfiletime)                              | Sets the date and time a mailslot was created.      |
| [**GetHandleInformation**](/windows/desktop/api/handleapi/nf-handleapi-gethandleinformation)            | Retrieves properties of the mailslot handle.        |
| [**SetHandleInformation**](/windows/desktop/api/handleapi/nf-handleapi-sethandleinformation)            | Sets properties of the mailslot handle.             |



 

## Mailslot Client Functions

A client process uses the following functions when interacting with a mailslot.



| Function                                                             | Description                                     |
|----------------------------------------------------------------------|-------------------------------------------------|
| [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle)                                  | Closes a mailslot handle for a client process.  |
| [**CreateFile**](/windows/desktop/api/fileapi/nf-fileapi-createfilea)                                    | Creates a mailslot handle for a client process. |
| [**DuplicateHandle**](/windows/desktop/api/handleapi/nf-handleapi-duplicatehandle)                          | Duplicates a mailslot handle.                   |
| [**WriteFile**](/windows/desktop/api/fileapi/nf-fileapi-writefile), [**WriteFileEx**](/windows/desktop/api/fileapi/nf-fileapi-writefileex) | Writes data to a mailslot.                      |



 

 

 
