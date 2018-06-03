---
title: CCF\_DESCRIPTION clipboard format
description: Introduced in MMC 2.0, the CCF\_DESCRIPTION clipboard format is provided by snap-ins using the Extended View extension. A node that supports this clipboard format will have a text-string displayed in the Extended View description area.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: eff5b42b-662a-49b0-bc32-9522e7c12704
ms.prod: windows-server-dev
ms.technology: microsoft-management-console
ms.tgt_platform: multiple
keywords:
- CCF_DESCRIPTION clipboard format MMC
topic_type:
- apiref
api_name:
- CCF_DESCRIPTION
api_location:
- Mmc.h
api_type:
- HeaderDef
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CCF\_DESCRIPTION clipboard format

Introduced in MMC 2.0, the CCF\_DESCRIPTION clipboard format is provided by snap-ins using the [Extended View extension](using-the-extended-view-extension.md). A node that supports this clipboard format will have a text-string displayed in the Extended View description area.

Be aware that CCF\_DESCRIPTION is also the name of a property recognized by the Extended View extension. Instead of supporting CCF\_DESCRIPTION as a clipboard format, a snap-in can support the CCF\_DESCRIPTION property by implementing the [**INodeProperties**](/windows/desktop/api/Mmc/nn-mmc-inodeproperties) interface.

## Data Format

A string that represents text appearing in the Extended View description area. The data must be plain text and should represent a description of the item selected. Be aware that the Extended View extension automatically provides the name of the selected item, so the text your snap-in provides for CCF\_DESCRIPTION does not require a name.

If the Extended View is unable to retrieve the CCF\_DESCRIPTION property using the [**INodeProperties**](/windows/desktop/api/Mmc/nn-mmc-inodeproperties) interface, then the Extended View queries for the CCF\_DESCRIPTION clipboard format using the HGLOBAL medium in a call to [**IDataObject::GetDataHere**](https://www.bing.com/search?q=**IDataObject::GetDataHere**). If this medium is not supported, then the Extended View will query for the CCF\_DESCRIPTION clipboard format using the IStream medium in a call to **IDataObject::GetDataHere**.

## Remarks

If the snap-in supports the CCF\_DESCRIPTION property or clipboard format, the Extended View extension will display the returned string text beneath "Description:" text in the description area. If the [**CCF\_HTML\_DETAILS**](ccf-html-details.md) property or clipboard format is supported, the description area will appear below the HTML details area (the user may need to scroll to see the description area).

## Requirements



|                                     |                                                                                  |
|-------------------------------------|----------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                   |
| Header<br/>                   | <dl> <dt>Mmc.h</dt> </dl> |



## See also

<dl> <dt>

[Using the Extended View Extension](using-the-extended-view-extension.md)
</dt> <dt>

[**CCF\_HTML\_DETAILS**](ccf-html-details.md)
</dt> </dl>

 

 





