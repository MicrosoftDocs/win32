---
description: Sets or retrieves the Active Directory search location.
ms.assetid: 43320799-1c01-4e09-bed9-f3576baadcce
title: Settings.ActiveDirectorySearchLocation property
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- Settings.ActiveDirectorySearchLocation
api_type: 
- COM
api_location: 
- Capicom.dll
---

# Settings.ActiveDirectorySearchLocation property

\[The **ActiveDirectorySearchLocation** property is available for use in the operating systems specified in the Requirements section.\]

The **ActiveDirectorySearchLocation** property sets or retrieves the Active Directory search location.

## Syntax


```VB
Settings.ActiveDirectorySearchLocation As CAPICOM_ACTIVE_DIRECTORY_SEARCH_LOCATION
```



## Property value

A value of the [**CAPICOM\_ACTIVE\_DIRECTORY\_SEARCH\_LOCATION**](capicom-active-directory-search-location.md) enumeration that specifies the search location. The default value is CAPICOM\_SEARCH\_ANY. The following table shows the possible values.



| Value                                                                                                                                                                                                           | Meaning                                    |
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| <span id="CAPICOM_SEARCH_ANY"></span><span id="capicom_search_any"></span><dl> <dt>**CAPICOM\_SEARCH\_ANY**</dt> </dl>                                   | Search all available locations.<br/> |
| <span id="CAPICOM_SEARCH_DEFAULT_DOMAIN"></span><span id="capicom_search_default_domain"></span><dl> <dt>**CAPICOM\_SEARCH\_DEFAULT\_DOMAIN**</dt> </dl> | Search only the default domain.<br/> |
| <span id="CAPICOM_SEARCH_GLOBAL_CATALOG"></span><span id="capicom_search_global_catalog"></span><dl> <dt>**CAPICOM\_SEARCH\_GLOBAL\_CATALOG**</dt> </dl> | Search only the global catalog.<br/> |



 

## Requirements



| Requirement | Value |
|----------------------------|----------------------------------------------------------------------------------------|
| Redistributable<br/> | CAPICOM 2.0 or later on Windows Server 2003 and Windows XP<br/>                  |
| DLL<br/>             | <dl> <dt>Capicom.dll</dt> </dl> |



## See also

<dl> <dt>

[**Settings**](settings.md)
</dt> </dl>

 

 




