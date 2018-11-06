---
title: Managing Synchronization Playlists
description: Managing Synchronization Playlists
ms.assetid: 5891ada0-37a6-4256-9885-8aa9dbe98b7c
keywords:
- Windows Media Player,portable devices
- Windows Media Player object model,portable devices
- object model,portable devices
- Windows Media Player ActiveX control,portable devices
- ActiveX control,portable devices
- Windows Media Player Mobile ActiveX control,portable devices
- Windows Media Player Mobile,portable devices
- portable devices,managing synchronization playlists
- device synchronization,playlists
- synchronizing devices,playlists
- Windows Media Player,synchronization playlists
- Windows Media Player object model,synchronization playlists
- object model,synchronization playlists
- Windows Media Player Mobile,synchronization playlists
- Windows Media Player ActiveX control,synchronization playlists
- Windows Media Player Mobile ActiveX control,synchronization playlists
- ActiveX control,synchronization playlists
- playlists,synchronization
- metafile playlists,synchronization
- Windows Media metafile playlists,synchronization
- synchronization playlists,managing
ms.topic: article
ms.date: 05/31/2018
---

# Managing Synchronization Playlists

Windows Media Player 10 or later uses playlists to synchronize digital media files with portable devices. This section explains how to work with synchronization playlists.

The example code in this section uses two ListView controls to display information. The first ListView control (IDC\_PLVIEW) displays all of the playlists in the Windows Media Player library, with synchronization playlists appearing first. Synchronization playlists for the currently selected device are marked with a check mark and are sorted in synchronization priority order. All other playlists are unchecked. The ListView control was configured for single selection. The order of playlists in the ListView control determines their synchronization priority. The checked state of an individual playlist determines whether it is a synchronization playlist for the currently selected device.

The second ListView control (IDC\_MEDIAVIEW) displays the media items in the selected playlist. Two additional columns display text indicating whether the digital media file was copied to the device and, in the case of a failure, whether the copy failed because the digital media file did not fit.

The following example code shows how the ListView controls are initialized:


```C++
STDMETHODIMP CSyncSettings::InitListView()
{
    m_hPlView = GetDlgItem(IDC_PLVIEW);
    m_hMediaView = GetDlgItem(IDC_MEDIAVIEW); 

    ATLASSERT(m_hPlView);
    ATLASSERT(m_hMediaView);

    // Sync playlist information.
    // Selection highlights all rows.
    // Show checkboxes.
    ListView_SetExtendedListViewStyleEx(m_hPlView, 0, LVS_EX_CHECKBOXES | LVS_EX_FULLROWSELECT);
   
    // Add headers.
    LVCOLUMN lvc;
    ZeroMemory(&lvc, sizeof(LVCOLUMN));
    lvc.mask = LVCF_WIDTH | LVCF_TEXT | LVCF_SUBITEM; 
    lvc.iSubItem = 0;
    
    lvc.pszText = _T("Sync");
    lvc.cx = 40;
    ListView_InsertColumn(m_hPlView, lvc.iSubItem, &lvc);

    lvc.iSubItem++;
    lvc.pszText = _T("Playlist Name");
    lvc.cx = 300;
    ListView_InsertColumn(m_hPlView, lvc.iSubItem, &lvc); 

    // Media information.
    // Selection highlights all rows.
    ListView_SetExtendedListViewStyleEx(m_hMediaView, 0, LVS_EX_FULLROWSELECT);

    // Add headers
    ZeroMemory(&lvc, sizeof(LVCOLUMN));
    lvc.mask = LVCF_WIDTH | LVCF_TEXT | LVCF_SUBITEM; 
    lvc.iSubItem = 0;
    
    lvc.pszText = _T("Media name");
    lvc.cx = 150;
    ListView_InsertColumn(m_hMediaView, lvc.iSubItem, &lvc);

    lvc.iSubItem++;
    lvc.pszText = _T("On Device");
    lvc.cx = 69;
    ListView_InsertColumn(m_hMediaView, lvc.iSubItem, &lvc);  

    lvc.iSubItem++;
    lvc.pszText = _T("Fit?");
    lvc.cx = 40;
    ListView_InsertColumn(m_hMediaView, lvc.iSubItem, &lvc);  
   
    return S_OK;
}
```



The following array of strings contains the names of the synchronization attributes used in the examples:


```C++
static const TCHAR *g_szSyncAttributeNames[17] = {
        _T("Not used"), // Do not access this one.
        _T("Sync01"),
        _T("Sync02"),
        _T("Sync03"),
        _T("Sync04"),
        _T("Sync05"),
        _T("Sync06"),
        _T("Sync07"),
        _T("Sync08"),
        _T("Sync09"),
        _T("Sync10"),
        _T("Sync11"),
        _T("Sync12"),
        _T("Sync13"),
        _T("Sync14"),
        _T("Sync15"),
        _T("Sync16")};
```



The following member variable contains a playlist containing all playlists in the Windows Media Player library. Each playlist is represented as a media item.


```C++
CComPtr<IWMPPlaylist> m_spPlaylist;
```



The following sections provide example code:

-   [Enumerating Synchronization Playlists](enumerating-synchronization-playlists.md)
-   [Sorting Playlists by Synchronization Priority](sorting-playlists-by-synchronization-priority.md)
-   [Enumerating the Media Items](enumerating-the-media-items.md)
-   [Determining Playlist Synchronization State](determining-playlist-synchronization-state.md)
-   [Changing Synchronization Priority](changing-synchronization-priority.md)

## Related topics

<dl> <dt>

[**Working with Portable Devices**](working-with-portable-devices.md)
</dt> </dl>

 

 




