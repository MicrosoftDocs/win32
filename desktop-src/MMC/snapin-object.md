---
title: SnapIn Object object
description: The SnapIn object encapsulates a single MMC snap-in. A SnapIn object is always a primary standalone snap-in.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 94a9c623-8778-4010-bb69-6ac0d7ae5ca9
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- SnapIn Object object MMC
- SnapIn Object object MMC , described
topic_type:
- apiref
api_name:
- SnapIn Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# SnapIn Object object

The **SnapIn** object encapsulates a single MMC snap-in. A **SnapIn** object is always a primary standalone snap-in.

## Members

The **SnapIn Object** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **SnapIn Object** object has these methods.



| Method                                                    | Description                                                                      |
|:----------------------------------------------------------|:---------------------------------------------------------------------------------|
| [**EnableAllExtensions**](snapin-enableallextensions.md) | Determines whether or not all extensions for the snap-in are enabled.<br/> |



 

### Properties

The **SnapIn Object** object has these properties.



| Property                                             | Access type          | Description                                                                                    |
|:-----------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------|
| [**Extensions**](snapin-extensions.md)<br/>   | Read-only<br/> | Returns the [**Extensions**](extensions-collection.md) collection for the snap-in.<br/> |
| [**Name**](snapin-name.md)<br/>               | Read-only<br/> | Returns the name of the snap-in.<br/>                                                    |
| [**Properties**](snapin-properties.md)<br/>   | Read-only<br/> | Returns the [**Properties**](properties-collection.md) collection for the snap-in.<br/> |
| [**SnapinCLSID**](snapin-snapinclsid.md)<br/> | Read-only<br/> | Returns the CLSID of the snap-in.<br/>                                                   |
| [**Vendor**](snapin-vendor.md)<br/>           | Read-only<br/> | Returns the name of the snap-in vendor.<br/>                                             |
| [**Version**](snapin-version.md)<br/>         | Read-only<br/> | Returns the version of the snap-in.<br/>                                                 |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_SnapIn is defined as 3BE910F6-3459-49C6-A1BB-41E6BE9DF3EA<br/>               |



 

 





