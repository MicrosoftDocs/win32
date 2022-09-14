---
description: The DuplicateHandle function creates a duplicate handle that can be used by another specified process.
ms.assetid: b79d2b8f-931e-4cab-9bbe-9ead1b102132
title: Object Duplication
ms.topic: article
ms.date: 05/31/2018
---

# Object Duplication

The [**DuplicateHandle**](/windows/win32/api/handleapi/nf-handleapi-duplicatehandle) function creates a duplicate handle that can be used by another specified process. This method of sharing object handles is more complex than using named objects or inheritance. It requires communication between the creating process and the process into which the handle is duplicated. The necessary information (the handle value and process identifier) can be communicated by any of the interprocess communication methods, such as named pipes or named shared memory.

 

 
