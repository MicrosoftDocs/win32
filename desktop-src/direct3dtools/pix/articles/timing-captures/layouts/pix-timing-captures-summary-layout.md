---
title: "Timing Captures Summary Layout"
description: "Describes the Summary layout in PIX Timing Captures."
ms.topic: concept-article
ms.date: 10/14/2025
---

# The Summary layout 

When a [Timing Capture](..\pix-timing-captures.md) is opened, PIX performs an initial analysis that produces capture statistics and a set of potential candidates for additional performance analysis.  The analysis is grouped into several sections.  The Summary layout consists of three views: the **Capture Details** view, the **Summary** view and the **Checklist** view.

<a id="summary_view"></a>

## Capture Details view

The Capture Details view provides a set of capture statistics, including the capture length, the version of PIX that capture was taken with, and a description of the PC the capture was taken on.

![The Capture Details view](../../../images/pix_timing_capture_summary_capture_details.png)

## Summary View

The following sections make up the summary view.

* **Longest Top-Level PIX Events.** A table listing the [PIX events](../../general/pix-instrumenting.md) that have the longest durations in the capture.  The longest instances are recorded for each event.  Clicking on an event name in the table graphs the event in the [Metrics layout](pix-metrics-layout.md).  Clicking on an event instance in the table navigates to that instance in the [Timeline layout](pix-timing-captures-timeline-layout.md).

![The Longest Top-Level PIX Events section of the Summary view](../../../images/pix_timing_capture_summary_view_longest_pix_events.png)

* **Bookmarks**. A list of the bookmarks in the capture.

![The Bookmarks section of the Summary view](../../../images/pix_timing_capture_summary_view_bookmarks.png)

* **Top PIX Events by Count.** The PIX events that occurred most frequently in the capture.  Clicking on a hyperlink in the name column graphs the event in the [Metrics layout](pix-metrics-layout.md).

![The Top PIX Events by Count section of the Summary view](../../../images/pix_timing_capture_summary_view_top_pix_events.png)

* **Top PIX Markers by Count.** The [PIX markers](../../general/pix-instrumenting.md) that occurred most frequently in the capture.

![The Top PIX Markers by Count section of the Summary view](../../../images/pix_timing_capture_summary_view_top_pix_markers.png)

* **CPU Utilization %.** The utilization of each CPU as determined by CPU sampling.

![The CPU Utilization % section of the Summary view](../../../images/pix_timing_capture_summary_view_cpu_utilization.png)

* **Largest API Objects Allocated.** A table listing the largest D3D API Objects sorted by size.  Clicking on the name of a resource in the table navigates to that instance in the **Range Details** view in the [Timeline layout](pix-timing-captures-timeline-layout.md).

![The Largest API Objects Allocated section of the Summary view](../../../images/pix_timing_capture_summary_view_cpu_d3d_objects.png)

* **CPU Thread and Core Usage.** A table listing the utilization of each CPU and thread as determined by CPU sampling.

![The CPU Thread and Core Usage section of the Summary view](../../../images/pix_timing_capture_summary_view_cpu_thread_core.png)

<a id="checklist_view"></a>

## Checklist View

The Checklist view provides a set of requirements that must be met or best practices that, if followed, will maximize the performance of your title.  The set of Checklist items is built into PIX.

For each checklist item that does not pass, the list of specific violations can be found by expanding the checklist item.  

Use the **Filter** bar to control the individual checklist items and violations displayed in the view.

![The Checklist view in the Summary layout](../../../images/pix_timing_capture_checklist_view.png)

