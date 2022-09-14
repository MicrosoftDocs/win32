---
description: The following constants specify the Windows Image Acquisition (WIA) item type.
ms.assetid: 7961f692-088a-4f3b-84e9-5fabb0373c3c
title: WIA Item Type Flags (Wiadef.h)
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- WiaItemTypeAnalyze
- WiaItemTypeAudio
- WiaItemTypeBurst
- WiaItemTypeDeleted
- WiaItemTypeDevice
- WiaItemTypeDisconnected
- WiaItemTypeDocument
- WiaItemTypeFile
- WiaItemTypeFolder
- WiaItemTypeFree
- WiaItemTypeGenerated
- WiaItemTypeHasAttachments
- WiaItemTypeHPanorama
- WiaItemTypeImage
- WiaItemTypeProgrammableDataSource
- WiaItemTypeRemoved
- WiaItemTypeRoot
- WiaItemTypeStorage
- WiaItemTypeTransfer
- WiaItemTypeTwainCapabilityPassThrough
- WiaItemTypeVideo
- WiaItemTypeVPanorama
api_type: 
- HeaderDef
api_location: 
- wiadef.h
---

# WIA Item Type Flags

The following constants specify the Windows Image Acquisition (WIA) item type.



| Constant                                                                                                                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                       |
|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="WiaItemTypeAnalyze"></span><span id="wiaitemtypeanalyze"></span><span id="WIAITEMTYPEANALYZE"></span><dl> <dt>**WiaItemTypeAnalyze**</dt> </dl>                                                                             | This item supports the [**IWiaItem::AnalyzeItem**](/windows/desktop/api/wia_xp/nf-wia_xp-iwiaitem-analyzeitem) method. *This constant is not supported by* Windows Vista *and later.*<br/>                                                                                                                               |
| <span id="WiaItemTypeAudio"></span><span id="wiaitemtypeaudio"></span><span id="WIAITEMTYPEAUDIO"></span><dl> <dt>**WiaItemTypeAudio**</dt> </dl>                                                                                     | The item is an audio file. Only valid for items that also have the **WiaItemTypeFile** attribute. <br/>                                                                                                                                                                                     |
| <span id="WiaItemTypeBurst"></span><span id="wiaitemtypeburst"></span><span id="WIAITEMTYPEBURST"></span><dl> <dt>**WiaItemTypeBurst**</dt> </dl>                                                                                     | For folders only. Images in this folder were taken in a continuous time sequence. *This constant is not supported by* Windows Vista *and later.*<br/>                                                                                                                                       |
| <span id="WiaItemTypeDeleted"></span><span id="wiaitemtypedeleted"></span><span id="WIAITEMTYPEDELETED"></span><dl> <dt>**WiaItemTypeDeleted**</dt> </dl>                                                                             | The item is marked as deleted from the tree. <br/>                                                                                                                                                                                                                                          |
| <span id="WiaItemTypeDevice"></span><span id="wiaitemtypedevice"></span><span id="WIAITEMTYPEDEVICE"></span><dl> <dt>**WiaItemTypeDevice**</dt> </dl>                                                                                 | The item represents a connected device. <br/>                                                                                                                                                                                                                                               |
| <span id="WiaItemTypeDisconnected"></span><span id="wiaitemtypedisconnected"></span><span id="WIAITEMTYPEDISCONNECTED"></span><dl> <dt>**WiaItemTypeDisconnected**</dt> </dl>                                                         | The item represents a disconnected device. <br/>                                                                                                                                                                                                                                            |
| <span id="WiaItemTypeDocument"></span><span id="wiaitemtypedocument"></span><span id="WIAITEMTYPEDOCUMENT"></span><dl> <dt>**WiaItemTypeDocument**</dt> </dl>                                                                         | The item represents a document. *This constant is supported only by* Windows Vista *and later.*<br/>                                                                                                                                                                                        |
| <span id="WiaItemTypeFile"></span><span id="wiaitemtypefile"></span><span id="WIAITEMTYPEFILE"></span><dl> <dt>**WiaItemTypeFile**</dt> </dl>                                                                                         | The item is a file. <br/>                                                                                                                                                                                                                                                                   |
| <span id="WiaItemTypeFolder"></span><span id="wiaitemtypefolder"></span><span id="WIAITEMTYPEFOLDER"></span><dl> <dt>**WiaItemTypeFolder**</dt> </dl>                                                                                 | The item is a folder. <br/>                                                                                                                                                                                                                                                                 |
| <span id="WiaItemTypeFree"></span><span id="wiaitemtypefree"></span><span id="WIAITEMTYPEFREE"></span><dl> <dt>**WiaItemTypeFree**</dt> </dl>                                                                                         | The item is uninitialized or has been deleted. <br/>                                                                                                                                                                                                                                        |
| <span id="WiaItemTypeGenerated"></span><span id="wiaitemtypegenerated"></span><span id="WIAITEMTYPEGENERATED"></span><dl> <dt>**WiaItemTypeGenerated**</dt> </dl>                                                                     | This item was created by the application or the driver, and does not have a corresponding item in the driver item tree. <br/>                                                                                                                                                               |
| <span id="WiaItemTypeHasAttachments"></span><span id="wiaitemtypehasattachments"></span><span id="WIAITEMTYPEHASATTACHMENTS"></span><dl> <dt>**WiaItemTypeHasAttachments**</dt> </dl>                                                 | The item has file attachments. *This constant is not supported by* Windows Vista *and later.*<br/>                                                                                                                                                                                          |
| <span id="WiaItemTypeHPanorama"></span><span id="wiaitemtypehpanorama"></span><span id="WIAITEMTYPEHPANORAMA"></span><dl> <dt>**WiaItemTypeHPanorama**</dt> </dl>                                                                     | The item represents a horizontal panoramic image. *This constant is not supported by* Windows Vista *and later.*<br/>                                                                                                                                                                       |
| <span id="WiaItemTypeImage"></span><span id="wiaitemtypeimage"></span><span id="WIAITEMTYPEIMAGE"></span><dl> <dt>**WiaItemTypeImage**</dt> </dl>                                                                                     | The item is an image file. Only valid for items that also have the **WiaItemTypeFile** attribute. <br/>                                                                                                                                                                                     |
| <span id="WiaItemTypeProgrammableDataSource"></span><span id="wiaitemtypeprogrammabledatasource"></span><span id="WIAITEMTYPEPROGRAMMABLEDATASOURCE"></span><dl> <dt>**WiaItemTypeProgrammableDataSource**</dt> </dl>                 | The item represents a programmable data source. *This constant is supported only by* Windows Vista *and later.*<br/>                                                                                                                                                                        |
| <span id="WiaItemTypeRemoved"></span><span id="wiaitemtyperemoved"></span><span id="WIAITEMTYPEREMOVED"></span><dl> <dt>**WiaItemTypeRemoved**</dt> </dl>                                                                             | The item has been removed from the device. <br/>                                                                                                                                                                                                                                            |
| <span id="WiaItemTypeRoot"></span><span id="wiaitemtyperoot"></span><span id="WIAITEMTYPEROOT"></span><dl> <dt>**WiaItemTypeRoot**</dt> </dl>                                                                                         | Identifies the root item in the device's tree of item objects. *This constant is supported only by* Windows Vista *and later.*<br/>                                                                                                                                                         |
| <span id="WiaItemTypeStorage"></span><span id="wiaitemtypestorage"></span><span id="WIAITEMTYPESTORAGE"></span><dl> <dt>**WiaItemTypeStorage**</dt> </dl>                                                                             | The item represents a storage medium. <br/>                                                                                                                                                                                                                                                 |
| <span id="WiaItemTypeTransfer"></span><span id="wiaitemtypetransfer"></span><span id="WIAITEMTYPETRANSFER"></span><dl> <dt>**WiaItemTypeTransfer**</dt> </dl>                                                                         | The item can be transferred. <br/>                                                                                                                                                                                                                                                          |
| <span id="WiaItemTypeTwainCapabilityPassThrough"></span><span id="wiaitemtypetwaincapabilitypassthrough"></span><span id="WIAITEMTYPETWAINCAPABILITYPASSTHROUGH"></span><dl> <dt>**WiaItemTypeTwainCapabilityPassThrough**</dt> </dl> | This type indicates that the WIA device is capable of receiving TWAIN capability data from the TWAIN compatibility layer. If this type is set, any TWAIN capability that isn't understood by the TWAIN compatibility layer, during a TWAIN session, will be passed to the WIA driver. <br/> |
| <span id="WiaItemTypeVideo"></span><span id="wiaitemtypevideo"></span><span id="WIAITEMTYPEVIDEO"></span><dl> <dt>**WiaItemTypeVideo**</dt> </dl>                                                                                     | The item represents streaming video. *This constant is not supported by either* Windows Server 2003*,* Windows Vista*, or later.*<br/>                                                                                                                                                      |
| <span id="WiaItemTypeVPanorama"></span><span id="wiaitemtypevpanorama"></span><span id="WIAITEMTYPEVPANORAMA"></span><dl> <dt>**WiaItemTypeVPanorama**</dt> </dl>                                                                     | The item represents a vertical panoramic image. *This constant is not supported by* Windows Vista *and later.*<br/>                                                                                                                                                                         |



## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional, Windows XP \[desktop apps only\]<br/>              |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>Wiadef.h</dt> </dl> |



 

 




