---
description: "Learn more about: User Defined Columns"
title: User Defined Columns
TOCTitle: User Defined Columns
ms:assetid: cccfc97c-acde-4328-a87f-ee7dcc54203c
ms:mtpsurl: https://msdn.microsoft.com/library/Gg294091(v=EXCHG.10)
ms:contentKeyID: 32765706
ms.date: 04/11/2016
ms.topic: article
---

# User Defined Columns


_**Applies to:** Windows | Windows Server_

## User Defined Columns

User defined columns are columns whose default values are provided by a callback function. These columns are always tagged and set to the value computed by the callback function. This value must be stable for each row in the table. The callback function is only used when either the application or the database engine itself needs to read the value of the column for a given row. The application has the option to override the default value and set a specific value in the column. When the default value is overridden in the columns, it uses space in the row, otherwise user defined default columns do not use space in the record.

User defined defaults option is set in the **grbit** member of the [JET_COLUMNDEF](./jet-columndef-structure.md) structure in the call to [JetAddColumn](./jetaddcolumn-function.md). The *pvDefault* parameter of the [JetAddColumn](./jetaddcolumn-function.md) function points to a [JET_USERDEFINEDDEFAULT](./jet-userdefineddefault-structure.md) structure, that contains the name of the callback function in the **szCallback** member, and the data that is passed to the callback in the **pbUserData** member.
