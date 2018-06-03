---
title: CFSTR\_DSOBJECTNAMES clipboard format
description: The snap-ins for Active Directory Users and Computers, the Active Directory Sites and Services, and the Active Directory Domains and Trusts support the CFSTR\_DSOBJECTNAMES clipboard format.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9be96d2a-6545-4986-b47b-1eab6a02ac26
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CFSTR_DSOBJECTNAMES clipboard format MMC
topic_type:
- apiref
api_name:
- CFSTR_DSOBJECTNAMES
api_location:
- DsClient.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CFSTR\_DSOBJECTNAMES clipboard format

The snap-ins for Active Directory Users and Computers, the Active Directory Sites and Services, and the Active Directory Domains and Trusts support the **CFSTR\_DSOBJECTNAMES** clipboard format. The **CFSTR\_DSOBJECTNAMES** clipboard format provides the list of objects that are selected when a property page or context menu is invoked by an Active Directory administrative snap-in.

## Data Format

The data is returned as an **HGLOBAL** type that points to a [**DSOBJECTNAMES**](https://msdn.microsoft.com/library/ms676011) structure. The structure contains the count of items in the selection and a pointer to an array of [**DSOBJECT**](https://msdn.microsoft.com/library/ms676010) structures that represent each selected item. The **DSOBJECT** structure contains the ADsPath, class name, and flags that indicate whether the page should be read-only and whether the object is a container. If it is necessary to read or modify properties on the object, the ADsPath can be used to bind to the object and perform the necessary operations.

## Remarks

An extension snap-in uses this format by calling the **GetData** member on the [**IDataObject**](https://msdn.microsoft.com/library/windows/desktop/ms688421) interface pointer that it receives from the Active Directory Users and Computers snap-in.

## Requirements



|                   |                                                                                       |
|-------------------|---------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>DsClient.h</dt> </dl> |



 

 





