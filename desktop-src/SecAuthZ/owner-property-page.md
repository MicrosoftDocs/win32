---
Description: 'The access control editor can include an Owner property page that enables the user to change an object's owner. For more information about an object's owner, see Owner of a New Object and Taking Object Ownership in C++.'
ms.assetid: 'b0c421db-450e-4030-98e9-e062202e482c'
title: Owner Property Page
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Owner Property Page

The access control editor can include an Owner property page that enables the user to change an object's owner. For more information about an object's owner, see [Owner of a New Object](owner-of-a-new-object.md) and [Taking Object Ownership in C++](taking-object-ownership-in-c--.md).

The **Owner** property page is in the [advanced security property sheet](advanced-security-property-sheet.md) displayed when the user clicks the **Advanced** button on the [basic security property page](basic-security-property-page.md). To include the **Owner** property page, set the SI\_ADVANCED and SI\_EDIT\_OWNER flags in the [**SI\_OBJECT\_INFO**](/windows/desktop/api/Aclui/ns-aclui-_si_object_info) structure returned by your [**ISecurityInformation::GetObjectInformation**](/windows/desktop/api/Aclui/) implementation.

 

 



