---
title: Appendix D Notes for Visual Basic Developers
description: This section provides information about Microsoft Active Accessibility for Microsoft Visual Basic developers.
ms.assetid: 82a016a2-872d-4ba6-ac93-78b59f7ec639
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Appendix D: Notes for Visual Basic Developers

This section provides information about Microsoft Active Accessibility for Microsoft Visual Basic developers.

Applications written in Visual Basic are Microsoft Active Accessibility clients. They do not provide information about their custom user interface elements because they do not implement [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) or any other Component Object Model (COM) interface.

This documentation uses the C/C++ names for the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties; however, the Visual Basic names are similar. For example, the [**IAccessible::get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master) property would be called **accName** in a Visual Basic application.

## In this section

-   [Visual Basic Method Notes: accName](visual-basic-method-notes--accname.md)
-   [Visual Basic Method Notes: accValue](visual-basic-method-notes--accvalue.md)
-   [Visual Basic Sample Programs](visual-basic-sample-programs.md)

 

 




