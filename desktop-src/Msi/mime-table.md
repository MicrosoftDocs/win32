---
description: The MIME table associates a MIME content type with a file name extension or a CLSID to generate the extension or COM server information required for advertisement of the MIME (Multipurpose Internet Mail Extensions) content.
ms.assetid: 5d452b24-ae04-4c45-8b3b-48e81f13a21e
title: MIME Table
ms.topic: article
ms.date: 05/31/2018
---

# MIME Table

The MIME table associates a MIME content type with a file name extension or a CLSID to generate the extension or COM server information required for advertisement of the MIME (Multipurpose Internet Mail Extensions) content.

The MIME table has the following columns.



| Column      | Type             | Key | Nullable |
|-------------|------------------|-----|----------|
| ContentType | [Text](text.md) | Y   | N        |
| Extension\_ | [Text](text.md) | N   | N        |
| CLSID       | [GUID](guid.md) | N   | Y        |



 

## Columns

<dl> <dt>

<span id="ContentType"></span><span id="contenttype"></span><span id="CONTENTTYPE"></span>ContentType
</dt> <dd>

This column is an identifier for the MIME content. It is commonly written in the form of type/format.

</dd> <dt>

<span id="Extension_"></span><span id="extension_"></span><span id="EXTENSION_"></span>Extension\_
</dt> <dd>

This column contains the server extension that is to be associated with the MIME content, without the dot. This column is a foreign key into the [Extension table](extension-table.md). The Extension table contains file name extension server information which is used as a part of advertisement.

</dd> <dt>

<span id="CLSID"></span><span id="clsid"></span>CLSID
</dt> <dd>

This column contains the COM server CLSID that is to be associated with the MIME content. The CLSID in this column can be a foreign key into the [Class table](class-table.md) or it can be a CLSID that already exists on the user's machine. The Class table contains COM server-related information which is used as a part of advertisement.

</dd> </dl>

## Remarks

This table is referred to when the [RegisterMIMEInfo action](registermimeinfo-action.md) or the [UnregisterMIMEInfo action](unregistermimeinfo-action.md) is executed. In advertise mode, the RegisterMIMEInfo action registers all MIME information for servers from the MIME table for which the corresponding feature is enabled. Otherwise the action registers MIME information for servers from the MIME table for which the corresponding feature is currently selected to be installed. The [UnregisterMIMEInfo action](unregistermimeinfo-action.md) unregisters MIME-related registry information from the system. The action unregisters MIME information for servers from the MIME table for which the corresponding feature is currently selected to be uninstalled.

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE15](ice15.md)  
[ICE32](ice32.md)  
</dl>

 

 



