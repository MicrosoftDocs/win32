---
title: CCF\_COLUMN\_SET\_ID clipboard format
description: The CCF\_COLUMN\_SET\_ID clipboard format is introduced in MMC 1.2.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'e4fc2b5f-2736-4a5b-adaa-f1c87d55f0b8'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["CCF_COLUMN_SET_ID clipboard format MMC"]
topic_type:
- apiref
api_name:
- CCF_COLUMN_SET_ID
api_location:
- Mmc.h
api_type:
- HeaderDef
---

# CCF\_COLUMN\_SET\_ID clipboard format

The **CCF\_COLUMN\_SET\_ID** clipboard format is introduced in MMC 1.2.

The **CCF\_COLUMN\_SET\_ID** clipboard format enables a snap-in to specify a unique ID for a column set.

By default, when the user changes the column configuration data of a column set, MMC propagates the changes to other scope items with the same column set ID.

For more information about how **CCF\_COLUMN\_SET\_ID** is used in column persistence, see [Using Column Persistence](using-column-persistence.md).

## Data Format

The **CCF\_COLUMN\_SET\_ID** clipboard format uses the [**SColumnSetID**](scolumnsetid.md) structure. The **dwFlags** member is reserved for future use. The id member holds the start of a byte array of length **cBytes**, which acts as the column set ID.

## Remarks

Supporting the **CCF\_COLUMN\_SET\_ID** format is optional. A snap-in that supports this format must do so in its [**IDataObject::GetData**](https://msdn.microsoft.com/library/windows/desktop/ms678431) implementation.

If a snap-in does not support the format, MMC will use the **nodetypeGUID** of the scope item associated with the column set for that identifies the column set.

For more information about column persistence, see [Using Column Persistence](using-column-persistence.md).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[Using Column Persistence](using-column-persistence.md)
</dt> </dl>

 

 





