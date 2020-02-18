---
title: ALE Flow Customization
description: Network filtering at the Application Layer Enforcement (ALE) layers of the Windows Filtering Platform (WFP) can be customized by adding filters with specific classify options.
ms.assetid: 123af237-cf42-410b-8a2f-c011cb5f4f19
ms.topic: article
ms.date: 05/31/2018
---

# ALE Flow Customization

Network filtering at the Application Layer Enforcement (ALE) layers of the Windows Filtering Platform (WFP) can be customized by adding filters with specific classify options.

## Multicast/Broadcast Traffic

To block inbound traffic based on outbound multicast or broadcast states, add a filter that authorizes outbound multicast and broadcast traffic and that has the [**FWP\_CLASSIFY\_OPTION\_MULTICAST\_STATE**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_classify_option0) option set to **FWP\_OPTION\_VALUE\_DENY\_MULTICAST\_STATE**.

## Remote Peers

To add response packets from different peers to the same ALE flow, add a filter that has the [**FWP\_CLASSIFY\_OPTION\_LOOSE\_SOURCE\_MAPPING**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_classify_option0) option set to **FWP\_OPTION\_VALUE\_ENABLE\_LOOSE\_SOURCE\_MAPPING**.

See [Using Classify Options](using-classify-options.md) for code sample.

## ALE Flow Lifetime

To modify the idle timeout values for an ALE flow, add a filter that has the [**FWP\_CLASSIFY\_OPTION\_MCAST\_BCAST\_LIFETIME**](/windows/desktop/api/Fwpmtypes/ns-fwpmtypes-fwpm_classify_option0) option and/or the **FWP\_CLASSIFY\_OPTION\_UNICAST\_LIFETIME** option set to the desired idle timeout value.

See [Using Classify Options](using-classify-options.md) for a code sample.

## Related topics

<dl> <dt>

[Application Layer Enforcement (ALE)](application-layer-enforcement--ale-.md)
</dt> <dt>

[ALE Layers](ale-layers.md)
</dt> <dt>

[ALE Stateful Filtering](ale-stateful-filtering.md)
</dt> <dt>

[ALE Multicast/Broadcast Traffic](ale-multicast-broadcast-traffic.md)
</dt> <dt>

[ALE Reauthorization](ale-re-authorization.md)
</dt> <dt>

[Using Classify Options](using-classify-options.md)
</dt> </dl>

 

 




