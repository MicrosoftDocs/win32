---
description: Message tables are special string resources used when displaying error messages. They are declared in a resource file using the MESSAGETABLE resource-definition statement. To access the message strings, use the FormatMessage function.
ms.assetid: db84f190-1d1e-4192-8dba-baaee0a3e3ea
title: Message Tables
ms.topic: article
ms.date: 05/31/2018
---

# Message Tables

Message tables are special string resources used when displaying error messages. They are declared in a resource file using the [MESSAGETABLE](../menurc/messagetable-resource.md) resource-definition statement. To access the message strings, use the [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) function.

The system provides a message table for the [system error codes](system-error-codes.md). To retrieve the string that corresponds to the error code, call [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag.

To provide a message table for your application, follow the instructions in [Message Text Files](../eventlog/message-text-files.md). To retrieve strings from your message table, call [**FormatMessage**](/windows/desktop/api/WinBase/nf-winbase-formatmessage) with the FORMAT\_MESSAGE\_FROM\_HMODULE flag.

 

 
