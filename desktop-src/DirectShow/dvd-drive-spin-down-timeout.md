---
description: DVD Drive Spin Down Timeout
ms.assetid: 2295253d-0199-41b4-95a8-cda049ca93c7
title: DVD Drive Spin Down Timeout
ms.topic: article
ms.date: 05/31/2018
---

# DVD Drive Spin Down Timeout

On laptop computers, to conserve battery life it may be desirable to reduce the length of time that a DVD drive will continue to spin after the user has paused playback. By default, the DVD Navigator keeps the disc spinning for two minutes. This value can be modified in the Windows Registry under this key:


```C++
DWORD HKLM\SOFTWARE\Microsoft\DVDNavigator\DriveSpindown 
[Sec]
```



where


```
Sec
```



is the spin down time in seconds.

## Related topics

<dl> <dt>

[Appendixes](appendixes.md)
</dt> </dl>

 

 



