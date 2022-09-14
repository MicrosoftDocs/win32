---
title: IResultsViewer interface (WdsSharedIDL.h)
description: Exposes methods and properties for the results view.
ms.assetid: 4d476511-d65c-4417-8073-337cfbae621d
keywords:
- IResultsViewer interface Legacy Windows Environment Features
- IResultsViewer interface Legacy Windows Environment Features , described
topic_type:
- apiref
api_name:
- IResultsViewer
api_location:
- WdsSharedIDL.h
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IResultsViewer interface

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use the [Windows Search API](../search/-search-reference-entry-page.md) instead. 

Exposes methods and properties for the results view.

## Members

The **IResultsViewer** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IResultsViewer** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IResultsViewer** interface has these methods.



| Method                                                   | Description                                                                            |
|:---------------------------------------------------------|:---------------------------------------------------------------------------------------|
| [**GoBack**](-search-2x-iresultsviewer-goback.md)       | Not implemented.<br/>                                                            |
| [**GoForward**](-search-2x-iresultsviewer-goforward.md) | Not implemented.<br/>                                                            |
| [**Refresh**](-search-2x-iresultsviewer-refresh.md)     | Not implemented.<br/>                                                            |
| [**Stop**](-search-2x-iresultsviewer-stop.md)           | Not implemented.<br/>                                                            |
| [**Update**](-search-2x-iresultsviewer-update.md)       | Applies any query changes and navigates the view to the new set of results.<br/> |



 

### Properties

The **IResultsViewer** interface has these properties.



| Property                                                                            | Access type           | Description                                                                                      |
|:------------------------------------------------------------------------------------|:----------------------|:-------------------------------------------------------------------------------------------------|
| [**Contents**](-search-2x-iresultsviewer-contents.md)<br/>                   | Write-only<br/> | This property tracks the type of the content being displayed in the results view. <br/>    |
| [**DisplayName**](-search-2x-iresultsviewer-displayname.md)<br/>             | Read-only<br/>  | Localized display name of the type.<br/>                                                   |
| [**EnumSelectedItems**](-search-2x-iresultsviewer-enumselecteditems.md)<br/> | Write-only<br/> | Not implemented.<br/>                                                                      |
| [**FilterType**](-search-2x-iresultsviewer-filtertype.md)<br/>               | Read/write<br/> | This property will set or return the name of the preceived type to filter results by.<br/> |
| [**HeaderStyle**](-search-2x-iresultsviewer-headerstyle.md)<br/>             | Read/write<br/> | The style of header displayed in the view.<br/>                                            |
| [**IsUpdateNeeded**](-search-2x-iresultsviewer-isupdateneeded.md)<br/>       | Write-only<br/> | This returns TRUE if the views query has been modified and needs updating. <br/>           |
| [**ItemStore**](-search-2x-iresultsviewer-itemstore.md)<br/>                 | Read/write<br/> | This property will set or return the name of the store to filter results by.<br/>          |
| [**PreviewStyle**](-search-2x-iresultsviewer-previewstyle.md)<br/>           | Read/write<br/> | Controls the preview pane's display mode.<br/>                                             |
| [**PropertyFilters**](-search-2x-iresultsviewer-propertyfilters.md)<br/>     | Write-only<br/> | When calling the property filter collection it will return the following:<br/>             |
| [**QueryText**](-search-2x-iresultsviewer-querytext.md)<br/>                 | Read/write<br/> | Gets or sets the current query text.<br/>                                                  |
| [**ResultsStyle**](-search-2x-iresultsviewer-resultsstyle.md)<br/>           | Write-only<br/> | Not implemented.<br/>                                                                      |
| [**SortOrderProperty**](-search-2x-iresultsviewer-sortorderproperty.md)<br/> | Read/write<br/> | This property will set or return the order of columns to sort results by. <br/>            |
| [**SortProperty**](-search-2x-iresultsviewer-sortproperty.md)<br/>           | Read/write<br/> | This property will set or return the IndexColumn of the property to sort results by. <br/> |



 

## Remarks

These methods and properties are used to manipulate the information viewed.

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP with SP2 \[desktop apps only\]<br/>                                      |
| Minimum supported server<br/> | Windows Server 2003 with SP1 \[desktop apps only\]<br/>                             |
| Redistributable<br/>          | Windows Desktop Search (WDS) 3.0<br/>                                               |
| Header<br/>                   | <dl> <dt>WdsSharedIDL.h</dt> </dl> |



 

