---
title: MMC 2.0 Clipboard Formats
description: Each data object must support these four clipboard formats in its implementation of the IDataObject GetDataHere method
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '8e113c1b-1b03-45d7-af3a-172b5eb2dabf'
ms.prod: 'windows-server-dev'
ms.technology: 'microsoft-management-console'
ms.tgt_platform: multiple
keywords: ["clipboard formats MMC 2.0"]
---

# MMC 2.0 Clipboard Formats

Each data object must support these four clipboard formats in its implementation of the **IDataObject::GetDataHere** method:

-   [**CCF\_DISPLAY\_NAME**](ccf-display-name.md)
-   [**CCF\_NODETYPE**](ccf-nodetype.md)
-   [**CCF\_SNAPIN\_CLASSID**](ccf-snapin-classid.md)
-   [**CCF\_SZNODETYPE**](ccf-sznodetype.md)

The data object's **IDataObject::GetDataHere** implementation can also support the following formats, depending on the snap-in's needs:

-   [**CCF\_COLUMN\_SET\_ID**](ccf-column-set-id.md)
-   [**CCF\_DESCRIPTION**](ccf-description.md)
-   [**CCF\_HTML\_DETAILS**](ccf-html-details.md)
-   [**CCF\_MMC\_DYNAMIC\_EXTENSIONS**](ccf-mmc-dynamic-extensions.md)
-   [**CCF\_SNAPIN\_PRELOADS**](ccf-snapin-preloads.md)
-   [**CCF\_WINDOW\_TITLE**](ccf-window-title.md)

The data object's **IDataObject::GetData** implementation can support the following formats, depending on the snap-in's needs:

[**CCF\_MULTI\_SELECT\_SNAPINS**](ccf-multi-select-snapins.md)

[**CCF\_NODEID**](ccf-nodeid.md)

[**CCF\_NODEID2**](ccf-nodeid2.md)

The data object can also support its own custom clipboard formats. To enable other snap-ins to request data using a custom clipboard format, you can publish your snap-in's clipboard formats in the MMC snap-in gallery website.

MMC also passes data to the snap-in for some multiselection operations using the following format:

[**CCF\_MMC\_MULTISELECT\_DATAOBJECT**](ccf-mmc-multiselect-dataobject.md)

 

 




