---
title: Time Controls
description: Time Controls
ms.assetid: 1799ec80-8e99-4ab7-8ff9-40e80e25f270
keywords:
- audio mixers,controls
- audio mixers,time controls
- mixers,controls
- mixers,time controls
- time controls
- microsecond control
- millisecond control
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Time Controls

\[The feature associated with this page, [Audio Mixers](/windows/win32/multimedia/audio-mixers), is a legacy feature. It has been superseded by [Volume Controls](/windows/win32/coreaudio/volume-controls). **Volume Controls** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Volume Controls** instead of **Audio Mixers**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The time controls allow the user to enter timing-related data, such as an echo delay or reverberation. The time data is expressed as positive integers. Types of time controls include the following:



| Control     | Description                                                                                            |
|-------------|--------------------------------------------------------------------------------------------------------|
| Microsecond | Supports timing data expressed in microseconds. The range of acceptable values is 0 through (232 – 1). |
| Millisecond | Supports timing data expressed in milliseconds. The range of acceptable values is 0 through (232 – 1). |



 

 

 




