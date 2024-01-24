---
title: Direct2D does not support rendering to rich metafiles in Internet Explorer 9
description: Direct2D does not support rendering to rich metafiles in Internet Explorer 9
ms.assetid: D106FBD6-F05E-41A6-B8F8-569EB9810E2C
ms.topic: article
ms.date: 05/31/2018
---

# Direct2D does not support rendering to rich metafiles in Internet Explorer 9

## Platforms

**Clients** – Windows Vista, Windows 7, Windows 8  
**Servers** – Windows Server 2008, Windows Server 2008 R2, Windows Server 2012  




## Description

Due to internal rendering changes in Internet Explorer 9, the [IHTMLElementRender::DrawToDC](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa752273(v=vs.85)) and [IViewObject::Draw](/windows/desktop/api/oleidl/nf-oleidl-iviewobject-draw) APIs will now create a metafile containing a single bitmap that represents the web content instead of a rich metafile containing text and vector info. This change was due to the move from GDI rendering to hardware-accelerated Direct2D (D2D) rendering.

This change affects apps that use these APIs and rely on text or vector info in the metafile.

## Manifestation

Depending on the app that is affected by this change, users might see broken or incorrect behavior in their apps.

## Mitigation

Apps that only need to extract text info from a web document (without positioning info) can use the [innerText](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa752299(v=vs.85)) property to extract text.

Apps that use IViewObject::Draw can use the [FEATURE\_IVIEWOBJECTDRAW\_DMLT9\_WITH\_GDI](/previous-versions/windows/internet-explorer/ie-developer/general-info/ee330732(v=vs.85)) feature control key to revert to GDI rendering if the document mode:

-   Is less or equal to 8
-   The FCK authorizes that host to use GDI
-   And a metafile DC is passed to the API

## Resources

-   [IHTMLElementRender::DrawToDC](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa752273(v=vs.85))
-   [IViewObject::Draw](/windows/win32/api/oleidl/nf-oleidl-iviewobject-draw)
-   [IHTMLElement::innerText Property](/previous-versions/windows/internet-explorer/ie-developer/platform-apis/aa752299(v=vs.85))
-   [Internet Feature Controls (I..L)](/previous-versions/windows/internet-explorer/ie-developer/general-info/ee330732(v=vs.85))

 

 