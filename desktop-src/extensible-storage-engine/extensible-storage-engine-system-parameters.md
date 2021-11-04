---
description: "Learn more about: Extensible Storage Engine System Parameters"
title: Extensible Storage Engine System Parameters
TOCTitle: Extensible Storage Engine System Parameters
ms:assetid: f95c2e87-b25e-4be5-8c17-8486ba37dad4
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294139(v=EXCHG.10)
ms:contentKeyID: 32765753
ms.date: 04/11/2016
ms.topic: reference
api_name: 
topic_type: 
- apiref
- kbArticle
api_type: 
- COM
api_location: 
ROBOTS: INDEX,FOLLOW

---

# Extensible Storage Engine System Parameters


_**Applies to:** Windows | Windows Server_

## Extensible Storage Engine System Parameters

The following constants are used as values for the *paramid* parameter of the [JetGetSystemParameter](./jetgetsystemparameter-function.md) and [JetSetSystemParameter](./jetsetsystemparameter-function.md) functions.

  - [Backup and Restore Parameters](./backup-and-restore-parameters.md)

  - [Callback Parameters](./callback-parameters.md)

  - [Database Parameters](./database-parameters.md)

  - [Database Cache Parameters](./database-cache-parameters.md)

  - [Error Handling Parameters](./error-handling-parameters.md)

  - [Event Log Parameters](./event-log-parameters.md)

  - [I/O Parameters](./i-o-parameters.md)

  - [Index Parameters](./index-parameters.md)

  - [Informational Parameters](./informational-parameters.md)

  - [Meta Parameters](./meta-parameters.md)

  - [Resource Parameters](./resource-parameters.md)

  - [Temporary Database Parameters](./temporary-database-parameters.md)

  - [Transaction Log Parameters](./transaction-log-parameters.md)

### System Parameter Description Format

Each system parameter will be described using the following format:

JET_paramX

Description of the JET_paramX system parameter.


| Label | Value |
|--------|-------|
| <p>Default Value:</p> | <p>The default value of the parameter.</p> | 
| <p>Type:</p> | <p>The data type of the parameter.</p> | 
| <p>Valid Range:</p> | <p>The legal values for the parameter.</p> | 
| <p>Scope:</p> | <p>Is the parameter Global or per Instance?</p> | 
| <p>Set After <a href="gg269354(v=exchg.10).md">JetCreateInstance</a>:</p> | <p>Can the parameter be set if any instances exist?</p> | 
| <p>Set after <a href="gg294068(v=exchg.10).md">JetInit</a>:</p> | <p>Can the parameter be set when initialized?</p> | 
| <p>Affects Physical Layout:</p> | <p>Does the parameter affect the files on disk?</p> | 
| <p>Affects Reliability:</p> | <p>Does the parameter affect engine reliability?</p> | 
| <p>Affects Performance:</p> | <p>Does the parameter affect engine performance?</p> | 
| <p>Affects Resources:</p> | <p>Does the parameter affect engine resources?</p> | 
| <p>Availability:</p> | <p>Releases of Windows that support the parameter.</p> | 

