---
title: Getting Program Information
description: Getting Program Information
ms.assetid: '530ada66-9f62-4476-8ede-8e6b90b24f37'
---

# Getting Program Information

Custom guide store loaders need to get program information from the transport stream. There are several ways to do this:

-   Get information from the [BDA MPEG-2 Transport Information Filter](bda-mpeg-2-transport-information-filter.md) (TIF)
-   Get section data from the [**MPEG-2 Sections and Tables**](mpeg-2-sections-and-tables-filter.md) filter
-   Implement a custom filter that parses the raw PSI section packets.

You can combine any of these approaches within the same client.

To get program information from the TIF, implement the [**IGuideDataEvent**](iguidedataevent.md) interface in your component, and then set up a connection point with the TIF using the **IConnectionPoint** interface.

For information about using the MPEG-2 Sections and Tables filter, see [Getting MPEG-2 PSI Tables](getting-mpeg2-psi-tables.md).

The third option, implementing a custom filter, is not recommended because the MPEG-2 Sections and Tables filter already provides a much simpler way to get section data. If you do take this approach, you must create a list of default component types that includes an additional "CategoryOther" type, and set this list as the default preferred components list on the tuning space. This will cause the Network Provider filter to create an additional output pin on the MPEG-2 Demultiplexer filter, so that you can connect your filter to the graph. For more information about setting the default component types, see [Components](components.md).

When your filter connects, call the [**IBDA\_TIF\_REGISTRATION::RegisterTIFEx**](ibda-tif-registration-registertifex.md) method to register the filter with the Network Provider. This method returns a pointer to the [**IMPEG2PIDMap**](https://msdn.microsoft.com/library/windows/desktop/dd407132) interface; use that interface to map the desired PIDs to that pin. (Do not use the **IMPEG2PIDMap** interface on the MPEG-2 Demultiplexer, because the Network Provider must be notified of all PID mappings in a BDA graph. It forwards the call to the demux.) When your filter is disconnected, call the [**IBDA\_TIF\_REGISTRATION::UnregisterTIF**](ibda-tif-registration-unregistertif.md) method to unregister with the Network Provider.

## Related topics

<dl> <dt>

[The Microsoft Unified Tuning Model](the-microsoft-unified-tuning-model.md)
</dt> </dl>

 

 




