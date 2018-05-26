---
title: Examples on Capturing Snapshots Using Trace Profiles
description: Examples on Capturing Snapshots Using Trace Profiles
ms.assetid: 3d49b74e-5a55-44ac-b42d-ddd2d422ae81
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Examples on Capturing Snapshots Using Trace Profiles

The following examples turn on several ETW sessions and merge them into a single trace file as needed.

### Memory-based trace profile

For an in-memory repeated snapshots trace profile, run the following command:


```
xperf -start perf!GeneralProfiles.InBuffer
```



Run some scenario, and then issue the following command:


```
xperf -save perf!GeneralProfiles.InBuffer snapshot1.etl
```



You can, optionally, continue saving additional snapshots, and then stop the trace capturing with the following command:


```
xperf -cancel perf!GeneralProfiles.InBuffer.InBuffer
```



### File-based trace profile

For a file-based trace profile, use following command:


```
xperf -start perf!RegistryProfiles.InSequentialFile
```



Run some scenario, and then issue the following command to stop trace capturing:


```
xperf -stop perf!RegistryProfiles.InSequentialFile trace.etl
```



### Extending Profile Definitions

Profile definitions can be extended and composed using a script-based inheritance model, as explained earlier in this document, as well as immediately using the command line. For example, to add ReadyThread stacks to the perf!FileIOProfiles.InSequentialFile, run the following command:


```
xperf -start perf!FileIOProfiles.InSequentialFile -stackwalk ReadyThread
```



 

 




