---
Description: Indicates the location to be searched for an Active Directory certificate store.
ms.assetid: 56b9695e-7ab9-405b-9cae-d78c43071186
title: CAPICOM\_ACTIVE\_DIRECTORY\_SEARCH\_LOCATION enumeration
ms.date: 05/31/2018
ms.topic: enumeration
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# CAPICOM\_ACTIVE\_DIRECTORY\_SEARCH\_LOCATION enumeration

The **CAPICOM\_ACTIVE\_DIRECTORY\_SEARCH\_LOCATION** enumeration type indicates the location to be searched for an Active Directory [*certificate store*](security.c_gly#-security-certificate-store-gly).

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



|                            |                                                                                      |
|----------------------------|--------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                |
| Header<br/>          | <dl> <dt>Capicom.h</dt> </dl> |



 

 




