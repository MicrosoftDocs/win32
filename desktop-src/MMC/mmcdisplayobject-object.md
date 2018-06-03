---
title: MMCDisplayObject object
description: The MMCDisplayObject object specifies the type of image and all the data required to use that image to display a task or the background on a taskpad.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 2b250453-b1b1-4db4-8a50-f9b6bc957618
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- MMCDisplayObject object MMC
- MMCDisplayObject object MMC , described
topic_type:
- apiref
api_name:
- MMCDisplayObject
api_location:
- MmcNdMgr.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: interface
ms.date: 05/31/2018
---

# MMCDisplayObject object

The **MMCDisplayObject** object specifies the type of image and all the data required to use that image to display a task or the background on a taskpad.

## Members

The **MMCDisplayObject** object has these types of members:

-   [Properties](#properties)

### Properties

The **MMCDisplayObject** object has these properties.



| Property                                                  | Description                                                                                                                                                                                          |
|:----------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DisplayObjectType**](displayobjecttype.md)<br/> | Returns the type of image displayed for a task or as the background in a taskpad.<br/>                                                                                                         |
| [**FontFamilyName**](fontfamilyname.md)<br/>       | Returns a null-terminated string that contains the font family name of the symbol displayed in a taskpad.<br/>                                                                                 |
| [**MouseOffBitmap**](mouseoffbitmap.md)<br/>       | Returns a null-terminated string that contains the resource path to the image file for the image displayed for the task when the mouse is not in the task's image or text area.<br/>           |
| [**MouseOverBitmap**](mouseoverbitmap.md)<br/>     | Returns a null-terminated string that contains the resource path to the image file for the image displayed for the task when the user moves the mouse over the task's image or text area.<br/> |
| [**SymbolString**](symbolstring.md)<br/>           | Returns a null-terminated string that contains the character or characters displayed in the symbol.<br/>                                                                                       |
| [**URLtoEOT**](urltoeot.md)<br/>                   | Returns a null-terminated string that contains the resource path to the EOT (embedded OpenType) file that contains the font for the symbol being displayed in a taskpad.<br/>                  |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |



 

 





