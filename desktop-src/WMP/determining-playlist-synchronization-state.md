---
title: Determining Playlist Synchronization State
description: Determining Playlist Synchronization State
ms.assetid: 634b659b-c3ae-4957-b17e-18fd92e915be
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
- portable devices,determining synchronization playlist state
- synchronization playlists,synchronization state
ms.topic: article
ms.date: 05/31/2018
---

# Determining Playlist Synchronization State

Windows Media Player 10 or later uses the **SyncState** attribute to contain information about whether a particular digital media file has been copied to a portable device and, in the case of a failure, whether copying failed because the device did not have enough memory.

The following example code creates a function that retrieves this information from a digital media file. The function takes the following parameters:

-   *pMedia*. Pointer to an **IWMPMedia** interface that represents the digital media file to inspect.
-   *lPsIndex*. Partnership index of the current device.
-   *pulOnDevice*. Pointer to a **long** variable that receives the value indicating whether the digital media file has been copied to the device.
-   *pulDidNotFit*. Pointer to a **long** variable that receives the value indicating whether the copy operation failed because the device did not have enough memory.

The information contained in the **SyncState** attribute is encoded in a bitwise fashion. You can see how this function is used in the example code in [Enumerating the Media Items](enumerating-the-media-items.md).


```C++
STDMETHODIMP CSyncSettings::GetPartnershipSyncState(IWMPMedia* pMedia, long lPsIndex, ULONG *pulOnDevice, ULONG *pulDidNotFit)
{
    ATLASSERT(pMedia); 
    ATLASSERT(lPsIndex > 0 && 
              lPsIndex < 17);
    ATLASSERT(pulOnDevice);
    ATLASSERT(pulDidNotFit);
  
    CComVariant varSyncStateVal;   
    CComPtr<IWMPMedia> spMedia(pMedia); 
    CComPtr<IWMPMedia3> spMedia3;     
    HRESULT hr = spMedia.QueryInterface(&spMedia3); 
    ULONG ulSyncState = 0; // Stores the ulVal member of varSyncStateVal. 
    ULONG lLSB = 0; // Represents least significant bit: Did the media fail to copy because it would not fit?
    ULONG lMSB = 0; // Represents most significant bit: Is the media on the device?

    // Calculate the bit shift required to isolate the partnership bit 
    // pair from the SyncState attribute.
    const int iRshift = (lPsIndex - 1) * 2;

    if(SUCCEEDED(hr) && spMedia3)
    {       
        hr = spMedia3->getItemInfoByType(CComBSTR("SyncState"), CComBSTR(""), 0, &varSyncStateVal);
    }

    if(SUCCEEDED(hr) && varSyncStateVal.vt == VT_UI4)
    {   
        // Get the value.
        ulSyncState = varSyncStateVal.ulVal;

        // Shift the bit pair to the rightmost position.
        ulSyncState >>= iRshift; 

        // Mask the rightmost bit pair.
        ulSyncState &= 3;

        // Get the LSB         
        lLSB = ulSyncState & ~2; // Sets the 2E1 bit to zero. 

        // Get the MSB
        ulSyncState >>= 1;
        lMSB = ulSyncState;       
    }

    // Return the bits.
    *pulOnDevice = lMSB;
    *pulDidNotFit = lLSB;

    return hr;
}
```



## Related topics

<dl> <dt>

[**IWMPMedia Interface**](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpmedia)
</dt> <dt>

[**IWMPMedia3::getItemInfoByType**](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpmedia3-getiteminfobytype)
</dt> <dt>

[**Managing Synchronization Playlists**](managing-synchronization-playlists.md)
</dt> <dt>

[**SyncState Attribute**](syncstate-attribute.md)
</dt> </dl>

 

 




