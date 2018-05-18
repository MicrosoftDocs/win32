---
Description: 'Restart records mark a last-known good state of application data.'
ms.assetid: 'f6c97136-fd43-4387-810d-0205d04c6133'
title: Restart Records
---

# Restart Records

Restart records mark a last-known good state of application data. This allows an application to optimize the recreation of its active state at startup, without reading the entire log. When you write a restart record, you can also move the base tail in an atomic operation because all records prior to the restart record may make up the last known good state.

Restart records are stored as a chain of records within a log stream. This allows the application to read multiple restart records in order to restore their state.

 

 



