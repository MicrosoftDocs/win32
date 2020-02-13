---
title: Sorting Playlists by Synchronization Priority
description: Sorting Playlists by Synchronization Priority
ms.assetid: 0f7f1ed3-0639-47bf-bf8e-52ae0a1d7ab2
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
- portable devices,sorting synchronization playlists
- synchronization playlists,sorting
- synchronization playlists,priorities
ms.topic: article
ms.date: 05/31/2018
---

# Sorting Playlists by Synchronization Priority

The following code performs a simple sort of playlists. You can see how this function is used in the example code in [Enumerating Synchronization Playlists](enumerating-synchronization-playlists.md). The function takes the following parameters:

-   *pPlaylist*. The pointer to the Windows Media Player playlist to sort. The media items in the playlist must point to other playlists, not individual digital media files.
-   *bstrSyncAttribute*. A BSTR containing the name of the synchronization partnership attribute for the current device ("Sync01", "Sync02", and so on).
-   *plSelected*. Pointer to a **long** variable that receives the count of synchronization playlists.

The function inspects the synchronization partnership attribute for each media item (representing a playlist) in the playlist specified by *pPlaylist*. If the attribute has a nonzero value, the code moves the media item to the beginning of the playlist and inserts it in priority order.

When finished, the function returns the count of media items (synchronization playlists) that had a nonzero value for the synchronization partnership attribute.


```C++
STDMETHODIMP CSyncSettings::SortPlaylist(IWMPPlaylist *pPlaylist, BSTR bstrSyncAttribute, long *plSelected)
{
    HRESULT hr = S_OK;
    long lSyncItemCount = 0;

    ATLASSERT (pPlaylist);
    ATLASSERT (plSelected);

    // Local copies of the parameters.
    CComPtr<IWMPPlaylist> spPlaylist(pPlaylist);
    CComBSTR bstrAttribute(bstrSyncAttribute);

    ATLASSERT (bstrAttribute.Length());

    // Get the count of playlist media items.
    long lCount = 0;
    spPlaylist->get_count(&lCount);

    // Walk the playlist.
    for(long i = 0; i < lCount; i++)
    {
        CComPtr<IWMPMedia> spMedia;                 
        CComBSTR bstrVal;            
        long lPriority = 0;
        
        hr = spPlaylist->get_item(i, &spMedia);

        if(SUCCEEDED(hr) && spMedia)
        {      
            // Get the sync priority value as a string.
            hr = spMedia->getItemInfo(bstrAttribute, &bstrVal);
        }

        if(SUCCEEDED(hr) && spMedia)
        {
            // Convert sync priority to a long number.
            lPriority = _wtol(bstrVal);
        }

        // Sort the playlist.
        // Only move the current item if it has a
        // sync priority value.
        if(lPriority > 0)
        {
            lSyncItemCount++;

            // Walk down the list and insert the item
            // in ascending order.
            for(long j = 0; j < lCount; j++)
            {
                CComPtr<IWMPMedia> spMediaCompare;
                CComBSTR bstrValCompare;
                long lPriorityTest = 0;

                hr = spPlaylist->get_item(j, &spMediaCompare);

                if(SUCCEEDED(hr) && spMediaCompare.p)
                {
                    hr = spMediaCompare->getItemInfo(bstrAttribute, &bstrValCompare);
                }
                if(SUCCEEDED(hr) && spMediaCompare.p)
                {
                    lPriorityTest = _wtol(bstrValCompare);
                    
                    if(lPriority <= lPriorityTest || 
                        0 == lPriorityTest)
                    {
                        hr = spPlaylist->moveItem(i, j);
                        break;                            
                    }                        
                } 
            } // for j                       
        } // if(lPriority > 0)          
    } // for i  
  
    // Return the sync item count.
    *plSelected = lSyncItemCount;

    return hr;
}
```



## Related topics

<dl> <dt>

[**IWMPMedia::getItemInfo**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpmedia-getiteminfo)
</dt> <dt>

[**IWMPPlaylist::get\_item**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplaylist-get_item)
</dt> <dt>

[**IWMPPlaylist::moveItem**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpplaylist-moveitem)
</dt> <dt>

[**Managing Synchronization Playlists**](managing-synchronization-playlists.md)
</dt> <dt>

[**Sync Attributes**](sync-attributes.md)
</dt> </dl>

 

 




