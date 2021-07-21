---
description: After you assess your property strategy, you must determine what properties to show in the Windows Explorer UI, and where.
ms.assetid: b7af0491-2ece-42b5-8eea-32643854632f
title: Using Property Lists
ms.topic: article
ms.date: 05/31/2018
---

# Using Property Lists

After you assess your property strategy, you must determine what properties to show in the Windows Explorer UI, and where. There are various locations where properties are displayed in a read-only manner. Property editing, on the other hand, is enabled only in the **Properties** dialog box. That dialog box can be invoked through either the **Edit Properties** link in the **Preview Pane** or the shortcut menu of an item.

The property lists are semi-colon delimited strings that have the following form.


```
Prop:[flags]PropertyCanonicalName;[flags]PropertyCanonicalName;
```



The only flag currently available is shown in the following table.



| Flag | Description                                                                                                                                                                                   |
|------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| \*   | Do not show the property in the **Preview Pane** as instructed in the **PreviewDetails** registry key value. See the example that follows the next table if that property's value is not set. |



 

After you define a property list, you can store that string in the registry through the standard [Shell file association](../shell/fa-file-types.md) system under **HKEY\_CLASSES\_ROOT.** The following table summarizes the values for the property lists that can be assigned under the registry key for a particular file name extension.



<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FullDetails</td>
<td>Properties are displayed on the <strong>Details</strong> tab of the <strong>Properties</strong> dialog box. This is the complete list of properties that the file type supports.</td>
</tr>
<tr class="even">
<td>PreviewDetails</td>
<td>Properties are displayed in the <strong>Preview Pane</strong>.</td>
</tr>
<tr class="odd">
<td>PreviewTitle</td>
<td>Properties are displayed in the title area of the <strong>Preview Pane</strong> next to the thumbnail for the item. The maximum number of entries is 3. If the property list contains more than the maximum allowable number, the rest of the entries are ignored.</td>
</tr>
<tr class="even">
<td>TileInfo</td>
<td>Properties are displayed when the list view is in <strong>Tiles</strong> view mode. The maximum number of entries is 3. If the property list contains more than the maximum allowable number, the rest of the entries are ignored.
<blockquote>
[!Note]<br />
This value was present in Windows XP.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>ExtendedTileInfo</td>
<td>Properties are displayed for an item when the list view is in <strong>Extended Tile</strong> view mode.</td>
</tr>
<tr class="even">
<td>InfoTip</td>
<td>Properties are displayed in an infotip when a user hovers over an item.
<blockquote>
[!Note]<br />
This value was present in Windows XP.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>QuickTip</td>
<td>Properties are displayed when it is difficult to retrieve properties directly from an item, such as when the item must be accessed over a slow network connection. It is recommended that the properties named here, such as Type or Size, do not require opening the file stream to determine their value.
<blockquote>
[!Note]<br />
This value was present in Windows XP.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

The example below defines the PreviewDetails value for a .recipe file type, using a ProgID of **RecipeKey**.

```
HKEY_CLASSES_ROOT
   .recipe
      (Default) = Recipe File
   RecipeFile
      PreviewDetails = prop:*System.Title;*System.Author
```

As explained in the [Shell file association](../shell/fa-file-types.md) topic, file associations can be described for the most specific to the most general form. The most specific form is the single file name extension and the most generic form is a key that applies to all files and file folders. Between those two extremes, you can also define a [PROGID](../shell/fa-progids.md) that groups a set of file name extensions together (for instance, .jpg and .jpeg types grouped as **jpegfile**). When you define property lists, you should define them for ProgIDs or, in some cases, specific file name extensions. Avoid relying on broad entries such as the **AllFileSystemObjects** key.

## Related topics

<dl> <dt>

[Understanding Property Handlers](./building-property-handlers-properties.md)
</dt> <dt>

[Using Kind Names](./building-property-handlers-user-friendly-kind-names.md)
</dt> <dt>

[Initializing Property Handlers](./building-property-handlers-property-handlers.md)
</dt> <dt>

[Registering and Distributing Property Handlers](./prophand-reg-dist.md)
</dt> <dt>

[Property Handler Best Practices and FAQ](./prophand-bestprac-faq.yml)
</dt> </dl>

 

 
