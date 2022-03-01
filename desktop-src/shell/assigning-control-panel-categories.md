---
description: As of Windows XP, Control Panel supports categorization of Control Panel items. Items are registered to appear in one or more category. New categories cannot be created.
title: Assigning Control Panel Categories
ms.topic: article
ms.date: 05/31/2018
ms.assetid: e189b57d-c066-4f28-b1d5-3e05d6c6eeb2
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Assigning Control Panel Categories

As of Windows XP, Control Panel supports categorization of Control Panel items. Items are registered to appear in one or more category. New categories cannot be created.

To register a Control Panel item in one or more categories, add values as explained in the [Executable Control Panel Item Registration](registering-control-panel-items.md) or [DLL Control Panel Item Registration](registering-control-panel-items.md) section of [Registering Control Panel Items](registering-control-panel-items.md), as appropriate.




| Category ID | Category Name (Windows 7) | Category Name (Windows Vista) | Category Name (Windows XP) | 
|-------------|---------------------------|-------------------------------|----------------------------|
| 0 | "All Control Panel Items" | "Additional Options"<blockquote>[!Note]<br />Any Control Panel item that does not specify a category ID appears in this category.</blockquote><br /> | "Other Control Panel Options"<blockquote>[!Note]<br />Any Control Panel item that does not specify a category ID appears in this category.</blockquote><br /> | 
| 1 | "Appearance and Personalization" | "Appearance and Personalization" | "Appearance and Themes" | 
| 2 | "Hardware and Sound" | "Hardware and Sound" | "Printers and Other Hardware" | 
| 3 | "Network and Internet" | "Network and Internet" | "Network and Internet Connections" | 
| 4 | No longer used. Any item that adds itself only to category 4 appears in category 2 (Hardware and Sound). | No longer used. Any item that adds itself only to category 4 appears in category 2 (Hardware and Sound). | "Sounds, Speech, and Audio Devices" | 
| 5 | "System and Security" | "System and Maintenance" | "Performance and Maintenance" | 
| 6 | "Clock, Language, and Region" | "Clock, Language, and Region" | "Date, Time, Language, and Regional Options" | 
| 7 | "Ease of Access" | "Ease of Access" | "Accessibility Options" | 
| 8 | "Programs" | "Programs" | "Add or Remove Programs" | 
| 9 | "User Accounts"<blockquote>[!Note]<br />When not connected to a domain, this is called "User Accounts and Family Safety".</blockquote><br /> | "User Accounts"<blockquote>[!Note]<br />When not connected to a domain, this is called "User Accounts and Family Safety".</blockquote><br /> | "User Accounts" | 
| 10 | No longer used. Items registered in this category appear in category 5 (System and Security). | "Security" | "Security Center"<blockquote>[!Note]<br />Available only in Windows XP Service Pack 2 (SP2) or later.</blockquote><br /> | 
| 11 | No longer used. Items registered in this category appear in category 0 (All Control Panel Items). | "Mobile PC"<blockquote>[!Note]<br />This category is only visible on mobile PCs.</blockquote><br /> | Not used. | 




 

In Windows XP, the categories **Add or Remove Programs** and **User Accounts** work somewhat differently from other categories in Control Panel. When one or more items are added to one of these two categories, the associated link in Control Panel opens a category page. The registered items appear in the lower portion of the page under the heading "or Pick a Control Panel icon". When no items are registered for one of these categories, the associated link in Control Panel directly invokes the standard Windows item for that category. In Windows Vista and later, the **Programs** category and the **User Accounts** category do not have this property.

The **Security Center** category, available only in Windows XP SP2, is also somewhat non-standard. Clicking this category opens the **Security Center** page in a new window. Items registered for **Security Center** appear in the lower portion of that page under the heading **Manage security settings for:**. Clicking an icon opens the Control Panel item.

## Related topics

<dl> <dt>

[Control Panel Items](control-panel-applications.md)
</dt> <dt>

[User Experience Guidelines](user-experience-guidelines.md)
</dt> <dt>

[Registering Control Panel Items](registering-control-panel-items.md)
</dt> <dt>

[Using CPLApplet](using-cplapplet.md)
</dt> <dt>

[Control Panel Message Processing](message-processing.md)
</dt> <dt>

[Executing Control Panel Items](executing-control-panel-items.md)
</dt> <dt>

[Extending System Control Panel Items](extending-system-control-panel-items.md)
</dt> <dt>

[Creating Searchable Task Links for a Control Panel Item](creating-searchable-task-links.md)
</dt> <dt>

[Accessing the Control Panel in Safe Mode under Windows Vista](accessing-the-cp-in-safe-mode-under-vista.md)
</dt> </dl>

 

 
