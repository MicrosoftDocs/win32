---
description: Indicates the location to be searched for an Active Directory certificate store.
ms.assetid: 56b9695e-7ab9-405b-9cae-d78c43071186
title: CAPICOM_ACTIVE_DIRECTORY_SEARCH_LOCATION enumeration (Capicom.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- CAPICOM_ACTIVE_DIRECTORY_SEARCH_LOCATION
api_type: 
- HeaderDef
api_location: 
- Capicom.h
---

# CAPICOM\_ACTIVE\_DIRECTORY\_SEARCH\_LOCATION enumeration

The **CAPICOM\_ACTIVE\_DIRECTORY\_SEARCH\_LOCATION** enumeration type indicates the location to be searched for an Active Directory [*certificate store*](../secgloss/c-gly.md).

## Members



| Member                               | Description                                  | Value |
|--------------------------------------|----------------------------------------------|-------|
| **CAPICOM\_SEARCH\_ANY**             | Searches all available locations.<br/> | 0     |
| **CAPICOM\_SEARCH\_GLOBAL\_CATALOG** | Searches only the global catalog.<br/> | 1     |
| **CAPICOM\_SEARCH\_DEFAULT\_DOMAIN** | Searches only the default domain.<br/> | 2     |



## Remarks

This enumeration type is used by the following property:

-   [**Settings.ActiveDirectorySearchLocation**](settings-activedirectorysearchlocation.md)

## Requirements



| Requirement | Value |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 
