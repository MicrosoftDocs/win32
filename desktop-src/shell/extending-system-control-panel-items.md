---
description: Some of the system items found in the Control Panel are extensible. To install a Control Panel extension, register your Shell extension as follows, where name is the predefined name of the system item (see table below).
title: Extending System Control Panel Items
ms.topic: article
ms.date: 05/31/2018
ms.assetid: b8b18b71-c95f-4c71-8df4-fe9342ce0165
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Extending System Control Panel Items

Some of the system items found in the Control Panel are extensible. To install a Control Panel extension, register your Shell extension as follows, where *name* is the predefined name of the system item (see table below).

```
HKEY_LOCAL_MACHINE
   Software
      Microsoft
         Windows
            CurrentVersion
               Controls Folder
                  name
                     shellex
                        PropertySheetHandlers
```

This is similar to the way you would register an extension for a predefined Shell object. Because the only Shell extensions supported by Control Panel items are property sheets, the registration must be under the **shellex**\\**PropertySheetHandlers** subkey.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Control Panel item</th>
<th><em>name</em></th>
<th>Remarks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Display</td>
<td>Desk</td>
<td>Also supports replacement of the <strong>Desktop</strong> page.
<blockquote>
[!Note]<br />
This is no longer supported under Windows Vista.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Display Settings Advanced</td>
<td>Device</td>
<td>Nonhardware-specific advanced properties.
<blockquote>
[!Note]<br />
This is no longer supported under Windows Vista.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td>Display Settings Advanced</td>
<td>Display</td>
<td>Hardware-specific advanced properties.
<blockquote>
[!Note]<br />
This is no longer supported under Windows Vista.
</blockquote>
<br/></td>
</tr>
<tr class="even">
<td>Internet Options</td>
<td>Internet</td>
<td>The maximum number of extension pages is 18.</td>
</tr>
<tr class="odd">
<td>Keyboard</td>
<td>Keyboard</td>
<td>The maximum number of extension pages is 30.</td>
</tr>
<tr class="even">
<td>Mouse</td>
<td>Mouse</td>
<td>Also supports replacement of standard pages. The maximum number of extension pages is 8.</td>
</tr>
<tr class="odd">
<td>Power Options</td>
<td>Power</td>
<td>The maximum number of pages, including standard pages, is 18.</td>
</tr>
<tr class="even">
<td>System</td>
<td>System</td>
<td>The maximum number of extension pages is 8.
<blockquote>
[!Note]<br />
This is no longer supported under Windows Vista.
</blockquote>
<br/></td>
</tr>
</tbody>
</table>



 

The **Add or Remove Programs** item in the Windows XP Control Panel is not a property sheet and therefore cannot be extended by the methods discussed here. Instead, its content is obtained from application publishers. For more information on adding content to **Add or Remove Programs**, see [**IAppPublisher**](/windows/desktop/api/Shappmgr/nn-shappmgr-iapppublisher), [**IEnumPublishedApps**](/windows/desktop/api/Shappmgr/nn-shappmgr-ienumpublishedapps), and [**IPublishedApp**](/windows/desktop/api/Shappmgr/nn-shappmgr-ipublishedapp).

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

[Assigning Control Panel Categories](assigning-control-panel-categories.md)
</dt> <dt>

[Creating Searchable Task Links for a Control Panel Item](creating-searchable-task-links.md)
</dt> <dt>

[Accessing the Control Panel in Safe Mode under Windows Vista](accessing-the-cp-in-safe-mode-under-vista.md)
</dt> </dl>

 

 




