---
description: Logging and Error Reporting
ms.assetid: 162ce34b-cc82-40bb-8422-a639152aee25
title: Logging and Error Reporting
ms.topic: article
ms.date: 05/31/2018
---

# Logging and Error Reporting

## Log file

COMREPL generates a log file containing status and error messages. This file is stored on the computer where COMREPL was launched in %systemdir%\\com\\replication\\ComRepl.log.

This log file is cleared when a copy phase is started. Subsequent installation on targets will append to the file.

## Error handling

Errors are noted in the log file described above. Detailed error information may also be found in the event log on source or target computers.

## Related topics

<dl> <dt>

[File Management](file-management.md)
</dt> <dt>

[Replication Phases](replication-phases.md)
</dt> <dt>

[Using COMREPL](using-comrepl.md)
</dt> <dt>

[What Gets Replicated](what-gets-replicated.md)
</dt> </dl>

 

 



