---
title: Column Object object
description: The Column object is used to manage a column in the result pane.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 9005ab58-ec89-4168-ac7c-aeaa25c2c778
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- Column Object object MMC
- Column Object object MMC , described
topic_type:
- apiref
api_name:
- Column Object
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# Column Object object

The **Column** object is used to manage a column in the result pane.

## Members

The **Column Object** object has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **Column Object** object has these methods.



| Method                                            | Description                                                       |
|:--------------------------------------------------|:------------------------------------------------------------------|
| [**IsSortColumn**](column-issortcolumn.md)       | Determines if the column is the sort column.<br/>           |
| [**Name**](column-name.md)                       | The name of the column.<br/>                                |
| [**SetAsSortColumn**](column-setassortcolumn.md) | A value that specifies this column as the sort column.<br/> |



 

### Properties

The **Column Object** object has these properties.



| Property                                                     | Access type           | Description                                                                           |
|:-------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------|
| [**DisplayPosition**](column-displayposition.md)<br/> | Read/write<br/> | Sets the display position of the column in reference to the other columns.<br/> |
| [**Hidden**](column-hidden.md)<br/>                   | Read/write<br/> | A value that specifies whether the column is hidden.<br/>                       |
| [**Width**](column-width.md)<br/>                     | Read/write<br/> | A value that specifies the width of the column.<br/>                            |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |
| IID<br/>                      | IID\_Column is defined as FD1C5F63-2B16-4D06-9AB3-F45350B940AB<br/>               |



 

 





