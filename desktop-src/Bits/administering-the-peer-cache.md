---
title: Administering the Peer Cache
description: Note  Starting with Windows 7, the Background Intelligent Transfer Service (BITS) 3.0 peer caching model is deprecated.
ms.assetid: 'a33a43e5-02f9-4902-ad3a-ec65b0d80520'
---

# Administering the Peer Cache

> [!Note]  
> Starting with Windows 7, the Background Intelligent Transfer Service (BITS) 3.0 peer caching model is deprecated. If BITS 4.0 is installed, the BITS 3.0 peer caching model is unavailable.

 

To improve download performance, BITS lets you download content from peer computers. To enable this feature, the administrator must enable the EnablePeerCaching group policy setting. If enabled, the peer can download content from peers and serve content to peers. The administrator can also use the DisablePeerCachingClient and DisablePeerCachingServer policy settings to prevent downloading content from a peer or serving content to peers, respectively.

If the group policy settings are not configured, an application can call the [**IBitsPeerCacheAdministration::SetConfigurationFlags**](ibitspeercacheadministration-setconfigurationflags.md) method to set the peer caching preference for the computer. Note that these preferences are overridden by the group policy settings if they are set later. To determine if the computer enables peer caching, call the [**IBitsPeerCacheAdministration::GetConfigurationFlags**](ibitspeercacheadministration-getconfigurationflags.md) method.

If peer caching is enabled, BITS will only cache the contents of a job if the job explicitly allows its content to be cached. BITS will also only download content from a peer if the job explicitly allows it. To enable peer caching for a job, call the [**IBackgroundCopyJob4::SetPeerCachingFlags**](ibackgroundcopyjob4-setpeercachingflags.md) method.

In addition to using Group Policy or the [**IBitsPeerCacheAdministration**](ibitspeercacheadministration.md) interface to enable peer caching, you can also use either method to change the default cache size and length of time that a non-accessed file remains in the cache. To change the defaults using the **IBitsPeerCacheAdministration** interface, call the [**SetMaximumCacheSize**](ibitspeercacheadministration-setmaximumcachesize.md) and [**SetMaximumContentAge**](ibitspeercacheadministration-setmaximumcontentage.md) methods. Since these methods set the preference settings, they are overridden by the group policy settings.

To list the peers from whom BITS will try to download content, call the [**IBitsPeerCacheAdministration::EnumPeers**](ibitspeercacheadministration-enumpeers.md) method.

To list the files in the cache that BITS will serve to peers, call the [**IBitsPeerCacheAdministration::EnumRecords**](ibitspeercacheadministration-enumrecords.md) method.

You should never have to manage the peer cache with regards to discovering peers or deleting cache records. This functionality was included in the [**IBitsPeerCacheAdministration**](ibitspeercacheadministration.md) interface for completeness.

 

 




