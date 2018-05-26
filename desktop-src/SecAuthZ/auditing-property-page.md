---
Description: The access control editor can include an Auditing property page that enables the user to view and edit the access control entries (ACEs) in an objects system access control list (SACL). For more information about SACLs, see Access Control Lists (ACLs).
ms.assetid: 2a9152b7-c72d-4f03-bc3f-b75927fb4b6c
title: Auditing Property Page
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Auditing Property Page

The access control editor can include an **Auditing** property page that enables the user to view and edit the [*access control entries*](https://msdn.microsoft.com/library/windows/desktop/ms721532#-security-access-control-entry-gly) (ACEs) in an object's [*system access control list*](https://msdn.microsoft.com/library/windows/desktop/ms721625#-security-system-access-control-list-gly) (SACL). For more information about SACLs, see [Access Control Lists](access-control-lists.md) (ACLs).

**To view the Auditing property page**

-   On the [basic security property page](basic-security-property-page.md), click **Advanced**. The **Auditing** property page is in the [advanced security property sheet](advanced-security-property-sheet.md).

To include the **Auditing** property page, set the **SI\_ADVANCED** and **SI\_EDIT\_AUDITS** flags in the [**SI\_OBJECT\_INFO**](/windows/win32/Aclui/ns-aclui-_si_object_info?branch=master) structure returned by your [**ISecurityInformation::GetObjectInformation**](/windows/win32/Aclui/?branch=master) implementation.

 

 



