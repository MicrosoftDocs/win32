---
title: Administering the Peer Cache
description: Note  Starting with Windows 7, the Background Intelligent Transfer Service (BITS) 3.0 peer caching model is deprecated.
ms.assetid: a33a43e5-02f9-4902-ad3a-ec65b0d80520
ms.topic: article
ms.date: 05/31/2018
---

# Administering the Peer Cache

> [!Note]  
> Starting with Windows 7, the Background Intelligent Transfer Service (BITS) 3.0 peer caching model is deprecated. If BITS 4.0 is installed, the BITS 3.0 peer caching model is unavailable.

 

To improve download performance, BITS lets you download content from peer computers. To enable this feature, the administrator must enable the EnablePeerCaching group policy setting. If enabled, the peer can download content from peers and serve content to peers. The administrator can also use the DisablePeerCachingClient and DisablePeerCachingServer policy settings to prevent downloading content from a peer or serving content to peers, respectively.

If the group policy settings are not configured, an application can call the [**IBitsPeerCacheAdministration::SetConfigurationFlags**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-setconfigurationflags) method to set the peer caching preference for the computer. Note that these preferences are overridden by the group policy settings if they are set later. To determine if the computer enables peer caching, call the [**IBitsPeerCacheAdministration::GetConfigurationFlags**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-getconfigurationflags) method.

If peer caching is enabled, BITS will only cache the contents of a job if the job explicitly allows its content to be cached. BITS will also only download content from a peer if the job explicitly allows it. To enable peer caching for a job, call the [**IBackgroundCopyJob4::SetPeerCachingFlags**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibackgroundcopyjob4-setpeercachingflags) method.

In addition to using Group Policy or the [**IBitsPeerCacheAdministration**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibitspeercacheadministration) interface to enable peer caching, you can also use either method to change the default cache size and length of time that a non-accessed file remains in the cache. To change the defaults using the **IBitsPeerCacheAdministration** interface, call the [**SetMaximumCacheSize**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-setmaximumcachesize) and [**SetMaximumContentAge**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-setmaximumcontentage) methods. Since these methods set the preference settings, they are overridden by the group policy settings.

To list the peers from whom BITS will try to download content, call the [**IBitsPeerCacheAdministration::EnumPeers**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-enumpeers) method.

To list the files in the cache that BITS will serve to peers, call the [**IBitsPeerCacheAdministration::EnumRecords**](/windows/desktop/api/Bits3_0/nf-bits3_0-ibitspeercacheadministration-enumrecords) method.

You should never have to manage the peer cache with regards to discovering peers or deleting cache records. This functionality was included in the [**IBitsPeerCacheAdministration**](/windows/desktop/api/Bits3_0/nn-bits3_0-ibitspeercacheadministration) interface for completeness.

 

 




