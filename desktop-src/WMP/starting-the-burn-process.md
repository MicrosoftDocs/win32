---
title: Starting the Burn Process
description: Starting the Burn Process
ms.assetid: 91442bd2-1a68-465c-b865-63d309f33d55
keywords:
- Windows Media Player,CD burning
- Windows Media Player object model,CD burning
- object model,CD burning
- Windows Media Player ActiveX control,CD burning
- ActiveX control,CD burning
- Windows Media Player Mobile ActiveX control,CD burning
- Windows Media Player Mobile,CD burning
- CD burning,starting burn process
- burning CDs,starting burn process
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Starting the Burn Process

\[The feature associated with this page, [Windows Media Player SDK](/windows/win32/wmp/windows-media-player-sdk), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **Windows Media Player SDK**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Before burning can begin, you must assign a playlist to be burned. Use [IWMPCdromBurn::put\_burnPlaylist](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-put_burnplaylist) to specify a playlist for burning.


```C++
HRESULT CMainDlg::PutPlaylist (void)
{
    // Specify the burn playlist.   
    HRESULT hr = m_spCdromBurn->put_burnPlaylist(m_spPlaylist);

    // Update the status information.
    if (SUCCEEDED(hr))
    {
        hr = m_spCdromBurn->refreshStatus();
    }

    return hr;
}

```



For information about using playlists, see [IWMPPlaylist](/previous-versions/windows/desktop/api/wmp/nn-wmp-iwmpplaylist).

To start the burning operation, call [IWMPCdromBurn::startBurn](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-startburn).


```C++
// Start burning.
hr = m_spCdromBurn->startBurn();

```



You can stop the burning operation by calling [IWMPCdromBurn::stopBurn](/previous-versions/windows/desktop/api/wmp/nf-wmp-iwmpcdromburn-stopburn).


```C++
// Stop burning.
hr = m_spCdromBurn->stopBurn();

```



## Related topics

<dl> <dt>

[**Burning a CD**](burning-a-cd.md)
</dt> <dt>

[**Retrieving the CD Burning Interface**](retrieving-the-cd-burning-interface.md)
</dt> <dt>

[**Erasing a Rewritable CD**](erasing-a-rewritable-cd.md)
</dt> <dt>

[**Retrieving the Drive and Disc Status**](retrieving-the-drive-and-disc-status.md)
</dt> <dt>

[**Retrieving the Burn Status**](retrieving-the-burn-status.md)
</dt> </dl>

 

 




