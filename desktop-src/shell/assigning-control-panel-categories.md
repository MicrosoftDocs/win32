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



<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Category ID</th>
<th>Category Name (Windows 7)</th>
<th>Category Name (Windows Vista)</th>
<th>Category Name (Windows XP)</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>0</td>
<td>&quot;All Control Panel Items&quot;</td>
<td>&quot;Additional Options&quot;
<blockquote>
[!Note]<br />
Any Control Panel item that does not specify a category ID appears in this category.
</blockquote>
<br/></td>
<td>&quot;Other Control Panel Options&quot;
<blockquote>
[!Note]<br />
Any Control Panel item that does not specify a category ID appears in this category.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>1</td>
<td>&quot;Appearance and Personalization&quot;</td>
<td>&quot;Appearance and Personalization&quot;</td>
<td>&quot;Appearance and Themes&quot;</td>
</tr>
<tr class="odd">
<td>2</td>
<td>&quot;Hardware and Sound&quot;</td>
<td>&quot;Hardware and Sound&quot;</td>
<td>&quot;Printers and Other Hardware&quot;</td>
</tr>
<tr class="even">
<td>3</td>
<td>&quot;Network and Internet&quot;</td>
<td>&quot;Network and Internet&quot;</td>
<td>&quot;Network and Internet Connections&quot;</td>
</tr>
<tr class="odd">
<td>4</td>
<td>No longer used. Any item that adds itself only to category 4 appears in category 2 (Hardware and Sound).</td>
<td>No longer used. Any item that adds itself only to category 4 appears in category 2 (Hardware and Sound).</td>
<td>&quot;Sounds, Speech, and Audio Devices&quot;</td>
</tr>
<tr class="even">
<td>5</td>
<td>&quot;System and Security&quot;</td>
<td>&quot;System and Maintenance&quot;</td>
<td>&quot;Performance and Maintenance&quot;</td>
</tr>
<tr class="odd">
<td>6</td>
<td>&quot;Clock, Language, and Region&quot;</td>
<td>&quot;Clock, Language, and Region&quot;</td>
<td>&quot;Date, Time, Language, and Regional Options&quot;</td>
</tr>
<tr class="even">
<td>7</td>
<td>&quot;Ease of Access&quot;</td>
<td>&quot;Ease of Access&quot;</td>
<td>&quot;Accessibility Options&quot;</td>
</tr>
<tr class="odd">
<td>8</td>
<td>&quot;Programs&quot;</td>
<td>&quot;Programs&quot;</td>
<td>&quot;Add or Remove Programs&quot;</td>
</tr>
<tr class="even">
<td>9</td>
<td>&quot;User Accounts&quot;
<blockquote>
[!Note]<br />
When not connected to a domain, this is called &quot;User Accounts and Family Safety&quot;.
</blockquote>
<br/></td>
<td>&quot;User Accounts&quot;
<blockquote>
[!Note]<br />
When not connected to a domain, this is called &quot;User Accounts and Family Safety&quot;.
</blockquote>
<br/></td>
<td>&quot;User Accounts&quot;</td>
</tr>
<tr class="odd">
<td>10</td>
<td>No longer used. Items registered in this category appear in category 5 (System and Security).</td>
<td>&quot;Security&quot;</td>
<td>&quot;Security Center&quot;
<blockquote>
[!Note]<br />
Available only in Windows XP Service Pack 2 (SP2) or later.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>11</td>
<td>No longer used. Items registered in this category appear in category 0 (All Control Panel Items).</td>
<td>&quot;Mobile PC&quot;
<blockquote>
[!Note]<br />
This category is only visible on mobile PCs.
</blockquote>
<br/></td>
<td>Not used.</td>
</tr>
</tbody>
</table>



 

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

 

 




