---
title: GUID attribute
description: Traffic control uses GUIDs to convey information about the status of packet shaper interfaces, to report errors, and to provide statistics.
ms.assetid: 57b803e5-0fa8-43ed-99f1-95152dedab2b
keywords:
- GUID attribute QOS
topic_type:
- apiref
api_name:
- GUID
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# GUID attribute

Traffic control uses GUIDs to convey information about the status of packet shaper interfaces, to report errors, and to provide statistics.

The GUID\_QOS\_STATISTICS\_BUFFER structure is actually an array of [**PS\_COMPONENT\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_component_stats?branch=master) structures, which in turn serve as a container structure, holding one of the five following structures in its **Stats** member:

-   [**PS\_ADAPTER\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_adapter_stats?branch=master)
-   [**PS\_FLOW\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_flow_stats?branch=master)
-   [**PS\_CONFORMER\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_conformer_stats?branch=master)
-   [**PS\_SHAPER\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_shaper_stats?branch=master)
-   [**PS\_DRRSEQ\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_drrseq_stats?branch=master)

The following table lists GUIDs used with packet shaper on QOS-enabled computers. In the scope column, P/I indicates that the GUID is based per-interface, and P/F indicates it is based per-flow.



| GUID                                  | Size               | Scope    | Settable? | Notification? | Description                                                                                                                                                                                                                                    |
|---------------------------------------|--------------------|----------|-----------|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GUID\_QOS\_REMAINING\_BANDWIDTH       | ULONG              | P/I      | No        | Yes           | The remaining amount of reservable bandwidth on this interface.                                                                                                                                                                                |
| GUID\_QOS\_BESTEFFORT\_BANDWIDTH      | ULONG              | P/I      | No        | No            | The remaining amount of bandwidth.                                                                                                                                                                                                             |
| GUID\_QOS\_LATENCY                    | ULONG              | P/I      | No        | No            | The latency of this interface.                                                                                                                                                                                                                 |
| GUID\_QOS\_FLOW\_COUNT                | ULONG              | P/I      | No        | Yes           | Number of active flows.                                                                                                                                                                                                                        |
| GUID\_QOS\_NON\_BESTEFFORT\_LIMIT     | ULONG              | P/I      | No        | No            | The total amount of reservable bandwidth.                                                                                                                                                                                                      |
| GUID\_QOS\_MAX\_OUTSTANDING\_SENDS    | ULONG              | P/I      | No        | No            | Maximum number of sends that can be outstanding on this interface.                                                                                                                                                                             |
| GUID\_QOS\_STATISTICS\_BUFFER         | See the following. | P/I, P/F | Yes       | No            | Statistics collected for flow or interface. The GUID\_QOS\_STATISTICS\_BUFFER structure is actually an array of [**PS\_COMPONENT\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_component_stats?branch=master) structures, as described in the preceding.                                  |
| GUID\_QOS\_FLOW\_MODE                 | ULONG              | P/I      | Yes       | No            | Mode of operation for the interface: ADAPTER\_FLOW\_MODE\_STANDARD or ADAPTER\_FLOW\_MODE\_DIFFSERV. Note that you must specify the constants rather than Standard or Diffserv when using this GUID. These constants are defined in ntddpsch.h |
| GUID\_QOS\_ISSLOW\_FLOW               | ULONG              | P/F      | No        | No            | Indicates an ISSLOW flow.                                                                                                                                                                                                                      |
| GUID\_QOS\_TIMER\_RESOLUTION          | ULONG              | none     | No        | No            | Timer resolution, in microseconds.                                                                                                                                                                                                             |
| GUID\_QOS\_FLOW\_IP\_CONFORMING       | ULONG              | P/F      | No        | No            | The conforming DSCP value for this flow.                                                                                                                                                                                                       |
| GUID\_QOS\_FLOW\_IP\_NONCONFORMING    | ULONG              | P/F      | No        | No            | The nonconforming SCP value for this flow.                                                                                                                                                                                                     |
| GUID\_QOS\_FLOW\_8021P\_CONFORMING    | ULONG              | P/F      | No        | No            | The conforming 802.1p value for this flow                                                                                                                                                                                                      |
| GUID\_QOS\_FLOW\_8021P\_NONCONFORMING | ULONG              | P/F      | No        | No            | The nonconforming 802.1p value for this flow.                                                                                                                                                                                                  |
| GUID\_QOS\_ENABLE\_AVG\_STATS         | ULONG              | P/I, P/F | Yes       | No            | Enables averaging statistics in the Packet Scheduler (provides the average number of packets in the shaper).                                                                                                                                   |
| GUID\_QOS\_ENABLE\_WINDOW\_ADJUSTMENT | ULONG              | P/I      | Yes       | No            | Enables TCP window size adjustment for TCP connections on a slow ling, running ICS.                                                                                                                                                            |



 

## Remarks

In the GUID\_QOS\_STATISTICS\_BUFFER GUID described in the table above, you must pass in a buffer that is large enough to hold all returned [**PS\_COMPONENT\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_component_stats?branch=master) structures.

## See also

<dl> <dt>

[**FLOWSPEC**](/windows/previous-versions/Qos/ns-qos-_flowspec?branch=master)
</dt> <dt>

[**PS\_ADAPTER\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_adapter_stats?branch=master)
</dt> <dt>

[**PS\_FLOW\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_flow_stats?branch=master)
</dt> <dt>

[**PS\_CONFORMER\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_conformer_stats?branch=master)
</dt> <dt>

[**PS\_SHAPER\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_shaper_stats?branch=master)
</dt> <dt>

[**PS\_DRRSEQ\_STATS**](/windows/previous-versions/Ntddpsch/ns-ntddpsch-_ps_drrseq_stats?branch=master)
</dt> </dl>

 

 




