---
description: Windows Image Acquisition (WIA) 2.0 items are grouped into categories that define how a IWiaItem2 is to be treated or used.
ms.assetid: 927f4957-aedf-4eef-8892-91cf9b56e1a2
title: WIA 2.0 Item Category GUIDs (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WIA_CATEGORY_AUTO
- WIA_CATEGORY_FEEDER
- WIA_CATEGORY_FEEDER_BACK
- WIA_CATEGORY_FEEDER_FRONT
- WIA_CATEGORY_FILM
- WIA_CATEGORY_FINISHED_FILE
- WIA_CATEGORY_FLATBED
- WIA_CATEGORY_FOLDER
- WIA_CATEGORY_ROOT
api_type: 
- HeaderDef
api_location: 
- wiadef.h
---

# WIA 2.0 Item Category GUIDs

Windows Image Acquisition (WIA) 2.0 items are grouped into categories that define how a [**IWiaItem2**](-wia-iwiaitem2.md) is to be treated or used. For example, if the item represents a feeder, then the application should expect it to contain the required document feeder properties and operate like a document feeder. If the item represents a finished file, then a WIA 2.0 application should treat it that way, assuming that the data is static and located on the device. (The rules for each item will be defined in their individual specification documents.) Each category has a GUID type constant.



| Constant                                                                                                                                                                                               | Description                                                                                                                                                                    |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WIA_CATEGORY_AUTO"></span><span id="wia_category_auto"></span><dl> <dt>**WIA\_CATEGORY\_AUTO**</dt> </dl>                             | An item that represents the automatic configuration settings for a WIA 2.0 scanner device that supports auto-configured scanning.<br/>                                   |
| <span id="WIA_CATEGORY_FEEDER"></span><span id="wia_category_feeder"></span><dl> <dt>**WIA\_CATEGORY\_FEEDER**</dt> </dl>                       | A feeder item that is a programmable data source and follows the standard rules and property sets required to support document feeders.<br/>                             |
| <span id="WIA_CATEGORY_FEEDER_BACK"></span><span id="wia_category_feeder_back"></span><dl> <dt>**WIA\_CATEGORY\_FEEDER\_BACK**</dt> </dl>       | A programmable data source describing the back side data source of a duplex base feeder item.<br/>                                                                       |
| <span id="WIA_CATEGORY_FEEDER_FRONT"></span><span id="wia_category_feeder_front"></span><dl> <dt>**WIA\_CATEGORY\_FEEDER\_FRONT**</dt> </dl>    | A programmable data source describing the front side data source of a duplex base feeder item.<br/>                                                                      |
| <span id="WIA_CATEGORY_FILM"></span><span id="wia_category_film"></span><dl> <dt>**WIA\_CATEGORY\_FILM**</dt> </dl>                             | A film item that is a programmable data source and follows the standard rules and property sets required to support film scanning units.<br/>                            |
| <span id="WIA_CATEGORY_FINISHED_FILE"></span><span id="wia_category_finished_file"></span><dl> <dt>**WIA\_CATEGORY\_FINISHED\_FILE**</dt> </dl> | An item that is not a programmable data source, or an item that provides data in a finished file format, or a folder item that contains finished file format items.<br/> |
| <span id="WIA_CATEGORY_FLATBED"></span><span id="wia_category_flatbed"></span><dl> <dt>**WIA\_CATEGORY\_FLATBED**</dt> </dl>                    | A flatbed item that is a programmable data source and follows the standard rules and property sets required to support flatbed platen scanning.<br/>                     |
| <span id="WIA_CATEGORY_FOLDER"></span><span id="wia_category_folder"></span><dl> <dt>**WIA\_CATEGORY\_FOLDER**</dt> </dl>                       | A folder storage item (not a programmable data source) containing other folder items or finished files or both.<br/>                                                     |
| <span id="WIA_CATEGORY_ROOT"></span><span id="wia_category_root"></span><dl> <dt>**WIA\_CATEGORY\_ROOT**</dt> </dl>                             | The root item for the device. <br/>                                                                                                                                      |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2008 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 




