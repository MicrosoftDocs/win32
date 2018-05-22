---
Description: 'Message tables are special string resources used when displaying error messages. They are declared in a resource file using the MESSAGETABLE resource-definition statement. To access the message strings, use the FormatMessage function.'
ms.assetid: 'db84f190-1d1e-4192-8dba-baaee0a3e3ea'
title: Message Tables
---

# Message Tables

Message tables are special string resources used when displaying error messages. They are declared in a resource file using the [MESSAGETABLE](tools.messagetable_resource) resource-definition statement. To access the message strings, use the [**FormatMessage**](formatmessage.md) function.

The system provides a message table for the [system error codes](system-error-codes.md). To retrieve the string that corresponds to the error code, call [**FormatMessage**](formatmessage.md) with the FORMAT\_MESSAGE\_FROM\_SYSTEM flag.

To provide a message table for your application, follow the instructions in [Message Text Files](base.message_text_files). To retrieve strings from your message table, call [**FormatMessage**](formatmessage.md) with the FORMAT\_MESSAGE\_FROM\_HMODULE flag.

 

 



