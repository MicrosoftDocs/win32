---
title: MMCListPadInfo object
description: The MMCListPadInfo object represents a label and a button for the ListPad control to be added to the taskpad page. It should be used on list view taskpads only.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '523f20cf-ab35-404b-ae06-34d7c78412ee'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["MMCListPadInfo object MMC", "MMCListPadInfo object MMC , described"]
topic_type:
- apiref
api_name:
- MMCListPadInfo
api_location:
- MmcNdMgr.dll
api_type:
- COM
---

# MMCListPadInfo object

The MMCListPadInfo object represents a label and a button for the ListPad control to be added to the taskpad page. It should be used on list view taskpads only.

An MMCListPadInfo object is returned by the GetListPadInfo method of the MMCCtrl control. The MMCListPadInfo object's properties represent the members of the MMC\_LISTPAD\_INFO structure passed in the [**IExtendTaskPad::GetListPadInfo**](iextendtaskpad-getlistpadinfo.md) method that MMC called when it retrieved the information for that task during the setup of the taskpad. The MMCListPadInfo object also has one additional property that represents the snap-in CLSID.

The MMC list view taskpad templates use the MMCListPadInfo object. To create a custom list view taskpad that has a label and button specified for the snap-in, the taskpad's HTML page should use the [**GetListPadInfo**](getlistpadinfo.md) method to retrieve the MMCListPadInfo object and add the label and button to the page.

## Members

The **MMCListPadInfo** object has these types of members:

-   [Properties](#properties)

### Properties

The **MMCListPadInfo** object has these properties.



| Property                                                        | Access type          | Description                                                                                 |
|:----------------------------------------------------------------|:---------------------|:--------------------------------------------------------------------------------------------|
| [**Clsid**](mmclistpadinfo-object-clsid.md)<br/>         | Read-only<br/> | CLSID of the snap-in that created the list view taskpad and owns it.<br/>             |
| [**HasButton**](mmclistpadinfo-object-hasbutton.md)<br/> | Read-only<br/> | Indicates whether the listpad button should be displayed.<br/>                        |
| [**NotifyID**](mmclistpadinfo-object-notifyid.md)<br/>   | Read-only<br/> | The command ID returned to the snap-in when the user clicks the optional button.<br/> |
| [**Text**](mmclistpadinfo-object-text.md)<br/>           | Read-only<br/> | Text for an optional button.<br/>                                                     |
| [**Title**](mmclistpadinfo-object-title.md)<br/>         | Read-only<br/> | Title text for the list control.<br/>                                                 |



 

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                          |
| Header<br/>                   | <dl> <dt>MMCObj.h</dt> </dl>     |
| IDL<br/>                      | <dl> <dt>MMCObj.idl</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MmcNdMgr.dll</dt> </dl> |



 

 





