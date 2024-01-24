---
title: PLAYLIST Element
description: PLAYLIST Element
ms.assetid: de568529-81f2-476b-ad1b-bb53f7e97b13
keywords:
- Windows Media Player skins,PLAYLIST element
- skins,PLAYLIST element
- PLAYLIST element
- reference for skins,PLAYLIST element
- elements,PLAYLIST
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# PLAYLIST Element

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The **PLAYLIST** element provides a way to organize media items in a list for easy manipulation using the following attributes and methods. Predefined **PLAYLIST** elements are also provided for convenience. Customized columns can be specified for a playlist by including **COLUMN** elements as children of the **PLAYLIST** element.

The **PLAYLIST** element supports the following attributes.



| Attribute                                                                                 | Description                                                                                                                                |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| [allowColumnSorting](playlist-allowcolumnsorting.md)                                     | Specifies or retrieves a value indicating whether sorting on column headers is allowed.                                                    |
| [allowItemEditing](playlist-allowitemediting.md)                                         | Specifies or retrieves a value indicating whether items in a playlist support in-place editing.                                            |
| [backgroundColor](playlist-backgroundcolor.md)                                           | Specifies or retrieves the background color.                                                                                               |
| [backgroundImage](playlist-backgroundimage.md)                                           | Specifies or retrieves the background image.                                                                                               |
| [checkboxesVisible](playlist-checkboxesvisible.md)                                       | Specifies or retrieves a value indicating whether checkboxes are visible.                                                                  |
| [columnCount](playlist-columncount.md)                                                   | Retrieves the number of columns shown.                                                                                                     |
| [columnOrder](playlist-columnorder.md)                                                   | Specifies or retrieves the order of the playlist columns.                                                                                  |
| [columns](playlist-columns.md)                                                           | Defines the columns that appear in the **PLAYLIST** element.                                                                               |
| [columnsVisible](playlist-columnsvisible.md)                                             | Specifies or retrieves a value indicating whether columns are shown.                                                                       |
| [copying](playlist-copying.md)                                                           | Retrieves a value indicating whether the **PLAYLIST** element is in the act of copying.                                                    |
| [disabledItemColor](playlist-disableditemcolor.md)                                       | Specifies or retrieves the color of a disabled CD track or of online content when offline.                                                 |
| [dropDownBackgroundImage](playlist-dropdownbackgroundimage.md)                           | Specifies or retrieves the name of the image that displays in the background of the drop-down list.                                        |
| [dropDownImage](playlist-dropdownimage.md)                                               | Specifies or retrieves the name of the image used for the drop-down list button that is displayed at the right edge of the drop-down list. |
| [dropDownList](playlist-dropdownlist.md)                                                 | Specifies or retrieves a value indicating which elements show up in the drop-down list for a given instance of the **PLAYLIST** element.   |
| [dropDownToolTip](playlist-dropdowntooltip.md)                                           | Specifies or retrieves the ToolTip shown when the user hovers over the **PLAYLIST** element drop-down menu.                                |
| [dropDownVisible](playlist-dropdownvisible.md)                                           | Specifies or retrieves a value indicating whether the **PLAYLIST** element drop-down selector is visible.                                  |
| [editButtonVisible](playlist-editbuttonvisible.md)                                       | Specifies or retrieves a value indicating whether the **PLAYLIST** element edit button is visible.                                         |
| [foregroundColor](playlist-foregroundcolor.md)                                           | Specifies or retrieves the foreground color.                                                                                               |
| [hueShift](playlist-hueshift.md)                                                         | Specifies or retrieves the amount by which the hue of the drop-down images is shifted.                                                     |
| [itemCount](playlist-itemcount.md)                                                       | Retrieves the number of items currently displayed in the **PLAYLIST** element.                                                             |
| [itemErrorColor](playlist-itemerrorcolor.md)                                             | Specifies or retrieves the highlight color that indicates a playlist item that has an error condition.                                     |
| [itemMedia](playlist-itemmedia.md)                                                       | Retrieves the **Media** object corresponding to the given index in the **PLAYLIST** element.                                               |
| [itemPlayingBackgroundColor](playlist-itemplayingbackgroundcolor.md)                     | Specifies or retrieves the background color of the currently playing playlist item.                                                        |
| [itemPlayingColor](playlist-itemplayingcolor.md)                                         | Specifies or retrieves the highlight color that indicates the currently playing item in the playlist.                                      |
| [itemPlaylist](playlist-itemplaylist.md)                                                 | Retrieves the playlist for the media item that is displayed at the given index in the **PLAYLIST** element.                                |
| [itemSelectedBackgroundColor](playlist-itemselectedbackgroundcolor.md)                   | Specifies or retrieves a value indicating the background color of a selected item in the playlist.                                         |
| [itemSelectedBackgroundFocusLostColor](playlist-itemselectedbackgroundfocuslostcolor.md) | Specifies or retrieves a value indicating the text color of a selected item in the playlist.                                               |
| [itemSelectedColor](playlist-itemselectedcolor.md)                                       | Specifies or retrieves a value indicating the text color of a selected item in the playlist.                                               |
| [itemSelectedFocusLostColor](playlist-itemselectedfocuslostcolor.md)                     | Specifies or retrieves a value indicating the text color of a selected item in the playlist when the playlist loses focus.                 |
| [leftStatus](playlist-leftstatus.md)                                                     | Specifies or retrieves the status text that is displayed on the left side and bottom of the **PLAYLIST** element.                          |
| [playlist](playlist-playlist.md)                                                         | Specifies or retrieves the **Playlist** object to which the **PLAYLIST** element provides an interface.                                    |
| [playlistItemsVisible](playlist-playlistitemsvisible.md)                                 | Specifies or retrieves a value indicating whether items in the playlist are visible.                                                       |
| [rightStatus](playlist-rightstatus.md)                                                   | Specifies or retrieves the status text that is displayed on the right side and bottom of the **PLAYLIST** element.                         |
| [saturation](playlist-saturation.md)                                                     | Specifies or retrieves the saturation value of the drop-down images.                                                                       |
| [statusColor](playlist-statuscolor.md)                                                   | Specifies or retrieves the color of the status line in the **PLAYLIST** element.                                                           |
| [statusTextColor](playlist-statustextcolor.md)                                           | Specifies or retrieves a value indicating the color of the status text.                                                                    |
| [toolbarVisible](playlist-toolbarvisible.md)                                             | Specifies or retrieves a value indicating whether the playlist toolbar displays.                                                           |



 

The **PLAYLIST** element supports the following methods.



| Method                                                              | Description                                                                                                               |
|---------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| [abortCopy](playlist-abortcopy.md)                                 | Cancels a copy operation.                                                                                                 |
| [addSelectedToPlaylist](playlist-addselectedtoplaylist.md)         | Adds the selected item to the playlist.                                                                                   |
| [copy](playlist-copy.md)                                           | Begins a copy operation from the CD.                                                                                      |
| [deleteSelected](playlist-deleteselected.md)                       | Deletes the selected item from the playlist.                                                                              |
| [deleteSelectedFromLibrary](playlist-deleteselectedfromlibrary.md) | Deletes the selected item from the playlist and from the library.                                                         |
| [getNextCheckedItem](playlist-getnextcheckeditem.md)               | Retrieves the index of the next checked item in the playlist following the specified index.                               |
| [getNextCheckedItem2](playlist-getnextcheckeditem2.md)             | Retrieves the index of the next checked item in the playlist following the specified index. Works with nested playlists.  |
| [getNextSelectedItem](playlist-getnextselecteditem.md)             | Retrieves the index of the next selected item in the playlist following the specified index.                              |
| [getNextSelectedItem2](playlist-getnextselecteditem2.md)           | Retrieves the index of the next selected item in the playlist following the specified index. Works with nested playlists. |
| [moveSelectedDown](playlist-moveselecteddown.md)                   | Moves the selected item down one position in the list.                                                                    |
| [moveSelectedUp](playlist-moveselectedup.md)                       | Moves the selected item up one position in the list.                                                                      |
| [setCheckedState](playlist-setcheckedstate.md)                     | Specifies that the indexed item in the playlist is checked.                                                               |
| [setCheckedState2](playlist-setcheckedstate2.md)                   | Sets the checked state of the item with the specified index in the **PLAYLIST** element. Works with nested playlists.     |
| [setColumnResizeMode](playlist-setcolumnresizemode.md)             | Specifies how the indexed column sizes itself.                                                                            |
| [setColumnWidth](playlist-setcolumnwidth.md)                       | Specifies the column width and changes the resize mode of the column to "wmpcrmFixed".                                    |
| [setSelectedState](playlist-setselectedstate.md)                   | Specifies that the indexed item in the playlist is selected.                                                              |
| [setSelectedState2](playlist-setselectedstate2.md)                 | Sets the selected state of the item with the specified index in the **PLAYLIST** element. Works with nested playlists.    |
| [sortColumn](playlist-sortcolumn.md)                               | Sorts the data in the specified column.                                                                                   |



 

The **PLAYLIST** element supports the ambient attributes and can implement the ambient event handlers, except where noted. For more information, see [Ambient Attributes](ambient-attributes.md) and [Ambient Event Handlers](ambient-event-handlers.md).

Predefined playlists are normal **PLAYLIST** elements with various common attribute settings specified by default. The following predefined playlists are available.



| Predefined PLAYLIST                      | Description                                                       |
|------------------------------------------|-------------------------------------------------------------------|
| [DROPDOWNPLAYLIST](dropdownplaylist.md) | A drop-down **PLAYLIST** with no items visible.                   |
| [ITEMSPLAYLIST](itemsplaylist.md)       | A drop-down **PLAYLIST** with no items or column headers visible. |



 

## Related topics

<dl> <dt>

[**Skin Programming Reference**](skin-programming-reference.md)
</dt> </dl>

 

 




