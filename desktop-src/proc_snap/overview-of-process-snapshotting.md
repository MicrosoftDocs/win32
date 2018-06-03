---
title: Overview of Process Snapshotting
description: With process snapshotting, you can capture and analyze data about running processes. The data is typically used for diagnostic purposes.
ms.assetid: 86FE968A-D34B-401B-8077-51A4C0895D27
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Overview of Process Snapshotting

With process snapshotting, you can capture and analyze data about running processes. The data is typically used for diagnostic purposes. Various types of data are available, including data about threads, handles, virtual spaces and process performance.

The Process Snapshotting functions are in kernel32.dll, and are installed as part of Windows.

-   [Capturing a snapshot](#capturing-a-snapshot)
-   [Getting data](#getting-data)
    -   [Getting single-instance data](#getting-single-instance-data)
    -   [Getting multi-instance data](#getting-multi-instance-data)

## Capturing a snapshot

To capture process data, you call the [**PssCaptureSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psscapturesnapshot) function, providing a handle to the process. The data that **PssCaptureSnapshot** captures is called a snapshot.

A snapshot can contain more than one type of data. You specify the types you want by setting the appropriate flags in the *CaptureFlags* parameter. The flags are members of the [**PSS\_CAPTURE\_FLAGS**](/previous-versions/windows/desktop/api/processsnapshot/ne-processsnapshot-pss_capture_flags) enumeration.

Though [**PssCaptureSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psscapturesnapshot) captures the snapshot, it does not provide the snapshot data to you. Instead it returns a snapshot handle. To get data you call other functions, as described below.

## Getting data

There are two functions that provide snapshot data to you. [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot) provides types of data for which there is only a single instance in the snapshot, and [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot) provides multi-instance data.

### Getting single-instance data

The [**PSS\_QUERY\_INFORMATION\_CLASS**](/previous-versions/windows/desktop/api/processsnapshot/ne-processsnapshot-pss_query_information_class) enumeration lists the types of single-instance data that [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot) provides. When you call **PssQuerySnapshot**, you set the *InformationClass* parameter to specify the type of data you want. You can only get one type per call.

The *Buffer* parameter is a pointer to a structure that receives the data. The type of structure that you provide depends on the type of data you request with the *InformationClass* parameter. The [**PSS\_QUERY\_INFORMATION\_CLASS**](/previous-versions/windows/desktop/api/processsnapshot/ne-processsnapshot-pss_query_information_class) topic tells you what type of structure to provide for each type of data.

### Getting multi-instance data

The [**PSS\_WALK\_INFORMATION\_CLASS**](/previous-versions/windows/desktop/api/processsnapshot/ne-processsnapshot-pss_walk_information_class) enumeration lists the types of multi-instance data that [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot) provides. For these types there are a variable number of instances in a snapshot. You retrieve the instances one at a time, one per call to **PssWalkSnapshot**. You can call [**PssQuerySnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-pssquerysnapshot) to determine the number of instances available.

Before you call [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot) for the first time, you call [**PssWalkMarkerCreate**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkercreate) to create a walk marker. Each time you call **PssWalkSnapshot**, you pass the walk marker, which indicates to **PssWalkSnapshot** what instance to return. Before **PssWalkSnapshot** returns, it advances the marker to the next instance. You can create any number of walk markers for a snapshot.

You can call [**PssWalkMarkerGetPosition**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkergetposition) to get a marker position, and [**PssWalkMarkerSetPosition**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkersetposition) to set a marker to a position that **PssWalkMarkerGetPosition** provided. You call [**PssWalkMarkerSeekToBeginning**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkerseektobeginning) to set the marker back to the beginning position (the position indicated by a newly-created walk marker).

When you call [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot), the *Buffer* parameter is a pointer to a structure that receives the data. The type of structure that you provide depends on the type of data you request with the *InformationClass* parameter. The [**PSS\_WALK\_INFORMATION\_CLASS**](/previous-versions/windows/desktop/api/processsnapshot/ne-processsnapshot-pss_walk_information_class) topic tells you what type of structure to provide for each type of data.

Use the following steps to capture and process all instances of multi-instance data.

1.  Call [**PssCaptureSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psscapturesnapshot) to capture a snapshot. You specify the types of data to capture with the *CaptureFlags* parameter. **PssCaptureSnapshot** returns a snapshot handle.
2.  Call [**PssWalkMarkerCreate**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkercreate) to create a walk marker. **PssWalkMarkerCreate** returns a walk marker handle.
3.  Call [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot), passing parameters as follows:

    -   The *SnapshotHandle* parameter is set to the snapshot handle that [**PssCaptureSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psscapturesnapshot) returned.
    -   The *InformationClass* parameter is set to one of the members of [**PSS\_WALK\_INFORMATION\_CLASS**](/previous-versions/windows/desktop/api/processsnapshot/ne-processsnapshot-pss_walk_information_class) to specify the type of data to provide.
    -   The *WalkMarkerHandle* is set to the walk marker handle that [**PssWalkMarkerCreate**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalkmarkercreate) returned.
    -   The *Buffer* parameter is a pointer to a structure that receives the data. The structure must be the proper type for the type of data being received.
    -   The *BufferLength* parameter is set to the length of the receiving structure that *Buffer* points to. You can use `sizeof` to get this; for example, `sizeof(PSS_HANDLE_ENTRY)`.

    These parameters can remain the same every time you call [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot) to get another instance, unless your processing requires a different buffer for each call.

4.  Handle the return value from [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot) as follows:
    -   If the return value is **ERROR\_SUCCESS**, the call succeeded, and you have data in your buffer. Process the data, then go back to step 3 to call [**PssWalkSnapshot**](/previous-versions/windows/desktop/api/processsnapshot/nf-processsnapshot-psswalksnapshot) again. Before **PssWalkSnapshot** returned, it advanced the walk marker to point to the next instance.
    -   If the return value is **ERROR\_NO\_MORE\_ITEMS**, you got and processed every instance. You are done.
    -   If the return value is anything else, there is an error, and you must stop short of processing all the instances.

 

 




