---
title: Music Catalog
description: Music Catalog
ms.assetid: d7ebf37f-00ae-4978-a63d-9d13741724f5
keywords:
- Windows Media Player online stores,music catalogs
- online stores,music catalogs
- type 1 online stores,music catalogs
- Windows Media Player online stores,catalog compiler
- online stores,catalog compiler
- type 1 online stores,catalog compiler
- music catalogs
- catalog compiler
ms.topic: article
ms.date: 05/31/2018
---

# Music Catalog

A type 1 online store creates its music catalog as a set of tab-separated-value (TSV) files. Then the online store uses Microsoft's [catalog compiler](catalog-compiler-for-type-1-online-stores.md) to compile the TSV files into a compressed catalog that can be downloaded by Windows Media Player. Windows Media Player can download full catalog files or catalog update files. Catalog updates contain only the catalog information that has changed since the last catalog update. It is up to the content partner plug-in to determine whether to download a full catalog or an update. In either case, Windows Media Player applies the changes to the current catalog upon notification from the plug-in.

If the online store has a new catalog prepared, the plug-in can notify the Player by calling [IWMPContentPartnerCallback::Notify](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartnercallback-notify) and passing wmpcnNewCatalogAvailable as the value for the *type* parameter.

When Windows Media Player is ready to download a catalog or update, the Player calls [IWMPContentPartner::GetCatalogURL](/previous-versions/windows/desktop/api/contentpartner/nf-contentpartner-iwmpcontentpartner-getcatalogurl). This method provides the plug-in with information about the current catalog, such as the catalog version and locale identifier. The plug-in responds by supplying the uniform resource locator (URL) of the correct full catalog or update, as well as an updated version number and expiration date. Windows Media Player will periodically request catalog updates based upon the information provided by the plug-in in **GetCatalogURL**.

## Related topics

<dl> <dt>

[**About Type 1 Online Stores**](about-type-1-online-stores.md)
</dt> <dt>

[**Catalog Compiler for Type 1 Online Stores**](catalog-compiler-for-type-1-online-stores.md)
</dt> <dt>

[**IWMPContentPartner Interface**](/previous-versions/windows/desktop/api/contentpartner/nn-contentpartner-iwmpcontentpartner)
</dt> </dl>

 

 




