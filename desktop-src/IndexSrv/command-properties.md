---
title: Command Properties
description: Command Properties
ms.assetid: 05f20d75-283f-47c0-a780-c5f1eba6c324
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Command Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The properties of [**Command objects**](c72d0308-7e30-4250-b85e-557b8c399a3c) provide a way to pass on information that is necessary when the command is executing. Command properties for OLE DB objects usually identify properties that must be supported by the rowsets that are created as a result of executing the command text. In Indexing Service, the command properties specify where the query is to be executed: which machine name, catalog name, and the scope within the catalog to use. Other properties can be identified to further control the query resolution process. The additional properties include the following.

<dl> <dt>

<span id="DBPROP_USEEXTENDEDDBTYPES"></span><span id="dbprop_useextendeddbtypes"></span>DBPROP\_USEEXTENDEDDBTYPES
</dt> <dd>

Resulting rowsets should use [**PROPVARIANT**](_stg_propvariant) types.

</dd> <dt>

<span id="DBPROP_USECONTENTINDEX"></span><span id="dbprop_usecontentindex"></span>DBPROP\_USECONTENTINDEX
</dt> <dd>

Force use of content (and not property) index only.

</dd> </dl>

For other properties, see [Extended OLE DB Properties](extended-ole-db-properties.md).

Helper functions [**CICreateCommand**](/windows/desktop/api/Ntquery/nf-ntquery-cicreatecommand) and [**CIMakeICommand**](/windows/desktop/api/Ntquery/nf-ntquery-cimakeicommand) create [**Command**](c72d0308-7e30-4250-b85e-557b8c399a3c) objects and set their properties. The [Simple sample](simple-sample.md) (QSample) has additional examples of command property use.

 

 




