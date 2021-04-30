---
description: Used with the Store.Open method to indicate how a certificate store is to be opened.
ms.assetid: 6ec87b8c-9431-4ecc-bd90-943cfe2df1c2
title: CAPICOM_STORE_OPEN_MODE enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_STORE_OPEN_MODE
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_STORE\_OPEN\_MODE enumeration

The CAPICOM\_STORE\_OPEN\_MODE enumeration type is used with the [**Store.Open**](store-open.md) method to indicate how a certificate store is to be opened.

## Members



| Member                                      | Description                                                                                                                                                              | Value |
|---------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|
| **CAPICOM\_STORE\_OPEN\_READ\_ONLY**        | Open the store in read-only mode.<br/>                                                                                                                             | 0     |
| **CAPICOM\_STORE\_OPEN\_READ\_WRITE**       | Open the store in read/write mode.<br/>                                                                                                                            | 1     |
| **CAPICOM\_STORE\_OPEN\_MAXIMUM\_ALLOWED**  | Open the store in read/write mode if the user has read/write permissions. If the user does not have read/write permissions, open the store in read-only mode.<br/> | 2     |
| **CAPICOM\_STORE\_OPEN\_EXISTING\_ONLY**    | Open existing stores only; do not create a new store. Introduced by CAPICOM 2.0.<br/>                                                                              | 128   |
| **CAPICOM\_STORE\_OPEN\_INCLUDE\_ARCHIVED** | Include archived certificates when using the store. Introduced by CAPICOM 2.0.<br/>                                                                                | 256   |



## Remarks

When using the CAPICOM\_STORE\_OPEN\_MODE enumeration, only one of the following settings can be used.

-   CAPICOM\_STORE\_OPEN\_READ\_ONLY
-   CAPICOM\_STORE\_OPEN\_READ\_WRITE
-   CAPICOM\_STORE\_OPEN\_MAXIMUM\_ALLOWED

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



## See also

<dl> <dt>

[**Store.Open**](store-open.md)
</dt> </dl>

 

 




