---
title: Overview of Process Snapshotting
description: With process snapshotting, you can capture and analyze data about running processes. The data is typically used for diagnostic purposes.
ms.assetid: '86FE968A-D34B-401B-8077-51A4C0895D27'
---

# Overview of Process Snapshotting

With process snapshotting, you can capture and analyze data about running processes. The data is typically used for diagnostic purposes. Various types of data are available, including data about threads, handles, virtual spaces and process performance.

The Process Snapshotting functions are in kernel32.dll, and are installed as part of Windows.

-   [Capturing a snapshot](#capturing-a-snapshot)
-   [Getting data](#getting-data)
    -   [Getting single-instance data](#getting-single-instance-data)
    -   [Getting multi-instance data](#getting-multi-instance-data)

## Capturing a snapshot

To capture process data, you call the [**PssCaptureSnapshot**](psscapturesnapshot.md) function, providing a handle to the process. The data that **PssCaptureSnapshot** captures is called a snapshot.

A snapshot can contain more than one type of data. You specify the types you want by setting the appropriate flags in the *CaptureFlags* parameter. The flags are members of the [**PSS\_CAPTURE\_FLAGS**](pss-capture-flags.md) enumeration.

Though [**PssCaptureSnapshot**](psscapturesnapshot.md) captures the snapshot, it does not provide the snapshot data to you. Instead it returns a snapshot handle. To get data you call other functions, as described below.

## Getting data

There are two functions that provide snapshot data to you. [**PssQuerySnapshot**](pssquerysnapshot.md) provides types of data for which there is only a single instance in the snapshot, and [**PssWalkSnapshot**](psswalksnapshot.md) provides multi-instance data.

### Getting single-instance data

The [**PSS\_QUERY\_INFORMATION\_CLASS**](pss-query-information-class.md) enumeration lists the types of single-instance data that [**PssQuerySnapshot**](pssquerysnapshot.md) provides. When you call **PssQuerySnapshot**, you set the *InformationClass* parameter to specify the type of data you want. You can only get one type per call.

The *Buffer* parameter is a pointer to a structure that receives the data. The type of structure that you provide depends on the type of data you request with the *InformationClass* parameter. The [**PSS\_QUERY\_INFORMATION\_CLASS**](pss-query-information-class.md) topic tells you what type of structure to provide for each type of data.

### Getting multi-instance data

The [**PSS\_WALK\_INFORMATION\_CLASS**](pss-walk-information-class.md) enumeration lists the types of multi-instance data that [**PssWalkSnapshot**](psswalksnapshot.md) provides. For these types there are a variable number of instances in a snapshot. You retrieve the instances one at a time, one per call to **PssWalkSnapshot**. You can call [**PssQuerySnapshot**](pssquerysnapshot.md) to determine the number of instances available.

Before you call [**PssWalkSnapshot**](psswalksnapshot.md) for the first time, you call [**PssWalkMarkerCreate**](psswalkmarkercreate.md) to create a walk marker. Each time you call **PssWalkSnapshot**, you pass the walk marker, which indicates to **PssWalkSnapshot** what instance to return. Before **PssWalkSnapshot** returns, it advances the marker to the next instance. You can create any number of walk markers for a snapshot.

You can call [**PssWalkMarkerGetPosition**](psswalkmarkergetposition.md) to get a marker position, and [**PssWalkMarkerSetPosition**](psswalkmarkersetposition.md) to set a marker to a position that **PssWalkMarkerGetPosition** provided. You call [**PssWalkMarkerSeekToBeginning**](psswalkmarkerseektobeginning.md) to set the marker back to the beginning position (the position indicated by a newly-created walk marker).

When you call [**PssWalkSnapshot**](psswalksnapshot.md), the *Buffer* parameter is a pointer to a structure that receives the data. The type of structure that you provide depends on the type of data you request with the *InformationClass* parameter. The [**PSS\_WALK\_INFORMATION\_CLASS**](pss-walk-information-class.md) topic tells you what type of structure to provide for each type of data.

Use the following steps to capture and process all instances of multi-instance data.

1.  Call [**PssCaptureSnapshot**](psscapturesnapshot.md) to capture a snapshot. You specify the types of data to capture with the *CaptureFlags* parameter. **PssCaptureSnapshot** returns a snapshot handle.
2.  Call [**PssWalkMarkerCreate**](psswalkmarkercreate.md) to create a walk marker. **PssWalkMarkerCreate** returns a walk marker handle.
3.  Call [**PssWalkSnapshot**](psswalksnapshot.md), passing parameters as follows:

    -   The *SnapshotHandle* parameter is set to the snapshot handle that [**PssCaptureSnapshot**](psscapturesnapshot.md) returned.
    -   The *InformationClass* parameter is set to one of the members of [**PSS\_WALK\_INFORMATION\_CLASS**](pss-walk-information-class.md) to specify the type of data to provide.
    -   The *WalkMarkerHandle* is set to the walk marker handle that [**PssWalkMarkerCreate**](psswalkmarkercreate.md) returned.
    -   The *Buffer* parameter is a pointer to a structure that receives the data. The structure must be the proper type for the type of data being received.
    -   The *BufferLength* parameter is set to the length of the receiving structure that *Buffer* points to. You can use `sizeof` to get this; for example, `sizeof(PSS_HANDLE_ENTRY)`.

    These parameters can remain the same every time you call [**PssWalkSnapshot**](psswalksnapshot.md) to get another instance, unless your processing requires a different buffer for each call.

4.  Handle the return value from [**PssWalkSnapshot**](psswalksnapshot.md) as follows:
    -   If the return value is **ERROR\_SUCCESS**, the call succeeded, and you have data in your buffer. Process the data, then go back to step 3 to call [**PssWalkSnapshot**](psswalksnapshot.md) again. Before **PssWalkSnapshot** returned, it advanced the walk marker to point to the next instance.
    -   If the return value is **ERROR\_NO\_MORE\_ITEMS**, you got and processed every instance. You are done.
    -   If the return value is anything else, there is an error, and you must stop short of processing all the instances.

 

 




