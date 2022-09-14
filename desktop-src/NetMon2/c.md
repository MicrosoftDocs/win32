---
description: Glossary of Network Monitor terms that begin with the letter C.
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: '9e0b9f77-8a47-4724-b08c-fac3b6e23afc'
title: C (Network Monitor)
ms.topic: article
ms.date: 05/31/2018
---

# C (Network Monitor)

<dl> <dt>

<span id="_netmon_capture_gly"></span><span id="_NETMON_CAPTURE_GLY"></span>**capture**
</dt> <dd>

Network traffic data that is collected in frames. A network packet provider (NPP) performs a capture. See also [*delayed capture*](d.md), and *real-time capture*

</dd> <dt>

<span id="_netmon_capture_file_gly"></span><span id="_NETMON_CAPTURE_FILE_GLY"></span>**capture file**
</dt> <dd>

A file that Network Monitor creates to store captured data. The .cap file name extension identifies a capture file. Network Monitor randomly generates a capture file name, but you can change the file name when you save the capture file.

Network Monitor creates a capture file each time the capture process starts, and then keeps the file open during the capture process. You cannot access the contents of a capture file until the capture process is stopped and the capture file is closed.

</dd> <dt>

<span id="_netmon_capture_filter_gly"></span><span id="_NETMON_CAPTURE_FILTER_GLY"></span>**capture filter**
</dt> <dd>

A set of Network Monitor functions used to restrict incoming frames that a network packet provider (NPP) application uses.

</dd> <dt>

<span id="_netmon_capture_trigger_gly"></span><span id="_NETMON_CAPTURE_TRIGGER_GLY"></span>**capture trigger**
</dt> <dd>

A trigger event that is set to stop the capture process. The capture trigger event can be a temporary capture file that is directed to a specific level or data pattern that occurs in a captured frame.

</dd> <dt>

<span id="_netmon_captured_data_gly"></span><span id="_NETMON_CAPTURED_DATA_GLY"></span>**captured data**
</dt> <dd>

Frames that have a defined set of criteria. The data frames are contained in a temporary capture file.

</dd> <dt>

<span id="_netmon_conversation_statistics_gly"></span><span id="_NETMON_CONVERSATION_STATISTICS_GLY"></span>**conversation statistics**
</dt> <dd>

Statistics of network traffic saved during a capture. These statistics include station and session information beginning when the capture process starts, and ending when the capture stops. If you pause the capture process, Network Monitor continues to add statistics when you resume the process. To retrieve conversation statistics, call the **GetConversationStatistics** method for the interface you are using.

</dd> </dl>

 

 



