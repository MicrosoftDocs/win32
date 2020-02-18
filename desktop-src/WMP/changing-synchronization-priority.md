---
title: Changing Synchronization Priority
description: Changing Synchronization Priority
ms.assetid: 992781cb-5018-4b88-aa93-2f8a86468a42
keywords:
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
- portable devices,changing synchronization playlist priorities
- synchronization playlists,priorities
ms.topic: article
ms.date: 05/31/2018
---

# Changing Synchronization Priority

The following example code specifies a priority value for each item in the ListView control identified by IDC\_PLVIEW. Items that are marked with a check mark are assigned a priority value based on their order in the list. Items that are not checked are assigned a priority value of zero.


```C++
void CSyncSettings::SetPriorities()
{
    ATLASSERT(m_spPlaylist.p);
    
    long lCount = 0;
    CComBSTR bstrAttribute(g_szSyncAttributeNames[m_lCurrentPSIndex]); 
    long lPriorityCount = 0; // Tracks the next priority value to be assigned.
    long lNewPriority = 0; // Contains the new priority value for the playlist.

    HRESULT hr = m_spPlaylist->get_count(&lCount);

    if(SUCCEEDED(hr) && lCount > 0)
    {
        HCURSOR hCursor = LoadCursor(NULL, IDC_WAIT);
        HCURSOR hCursorOld = SetCursor(hCursor);

        // Walk the list.
        for(long i = 0; i < lCount; i++)
        {
            CComPtr<IWMPMedia> spMedia;
            BOOL bChecked = ListView_GetCheckState(m_hPlView, i);

            if(TRUE == bChecked)
            {
                // Assign a priority value.
                lNewPriority = ++lPriorityCount;
            }
            else
            {
                // Not a sync playlist.
                lNewPriority = 0;
            }

            // Set the attribute on the playlist.
            hr = m_spPlaylist->get_item(i, &spMedia);

            if(SUCCEEDED(hr))
            {     
                WCHAR buffer[30];
                _ltow(lNewPriority, buffer, 10);
                CComBSTR bstrPriority(buffer);
                hr = spMedia->setItemInfo(bstrAttribute, bstrPriority);
            }
        }
        SetCursor(hCursorOld);
    }       
}
```



## Related topics

<dl> <dt>

[**IWMPMedia Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia)
</dt> <dt>

[**IWMPPlaylist Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylist)
</dt> <dt>

[**Managing Synchronization Playlists**](managing-synchronization-playlists.md)
</dt> </dl>

 

 




