---
title: MCI_LIST command (Mmsystem.h)
description: The MCI\_LIST command obtains information about the number and types of inputs available to the device. Digital-video and VCR devices recognize this command.
ms.assetid: 1977fbfa-cae4-4afe-9fc5-ac68177574ca
keywords:
- MCI_LIST command Windows Multimedia
topic_type:
- apiref
api_name:
- MCI_LIST
api_location:
- Mmsystem.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# MCI\_LIST command

The MCI\_LIST command obtains information about the number and types of inputs available to the device. Digital-video and VCR devices recognize this command.

To send this command, call the [**mciSendCommand**](/previous-versions//dd757160(v=vs.85)) function with the following parameters.


```C++
MCIERROR mciSendCommand(
  MCIDEVICEID wDeviceID, 
  MCI_LIST, 
  DWORD dwFlags, 
  (DWORD) (LPMCI_GENERIC_PARMS) lpList
);
```



## Parameters

<dl> <dt>

<span id="wDeviceID"></span><span id="wdeviceid"></span><span id="WDEVICEID"></span>*wDeviceID*
</dt> <dd>

Device identifier of the MCI device that is to receive the command message.

</dd> <dt>

<span id="dwFlags"></span><span id="dwflags"></span><span id="DWFLAGS"></span>*dwFlags*
</dt> <dd>

MCI\_NOTIFY, MCI\_WAIT, or MCI\_TEST. For information about these flags, see [The Wait, Notify, and Test Flags](the-wait-notify-and-test-flags.md).

</dd> <dt>

<span id="lpList"></span><span id="lplist"></span><span id="LPLIST"></span>*lpList*
</dt> <dd>

Pointer to an [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md) structure. (Devices with extended command sets might replace this structure with a device-specific structure.)

</dd> </dl>

## Return Value

Returns zero if successful or an error otherwise.

## Remarks

The following additional flags apply to the **digitalvideo** device type:

<dl> <dt>

<span id="MCI_DGV_LIST_ALG"></span><span id="mci_dgv_list_alg"></span>MCI\_DGV\_LIST\_ALG
</dt> <dd>

The **lpstrAlgorithm** member of the structure identified by *lpList* contains an address of a buffer containing the name of an algorithm. The name is used to retrieve the types of quality descriptors associated with an algorithm.

</dd> <dt>

<span id="MCI_DGV_LIST_COUNT"></span><span id="mci_dgv_list_count"></span>MCI\_DGV\_LIST\_COUNT
</dt> <dd>

Returns the number of options of the specified type.

</dd> <dt>

<span id="MCI_DGV_LIST_ITEM"></span><span id="mci_dgv_list_item"></span>MCI\_DGV\_LIST\_ITEM
</dt> <dd>

A constant indicating the list type is included in the **dwItem** member of the structure identified by *lpList*. This flag is required. Use one of the following constants to indicate the list type:

</dd> <dt>

<span id="MCI_DGV_LIST_AUDIO_ALG"></span><span id="mci_dgv_list_audio_alg"></span>MCI\_DGV\_LIST\_AUDIO\_ALG
</dt> <dd>

The command should retrieve names of audio algorithms.

</dd> <dt>

<span id="MCI_DGV_LIST_AUDIO_QUALITY"></span><span id="mci_dgv_list_audio_quality"></span>MCI\_DGV\_LIST\_AUDIO\_QUALITY
</dt> <dd>

The command should retrieve audio quality levels. The levels returned are associated with the algorithm referenced by the **lpstrAlgorithm** member of the structure identified by *lpList*. If that member is specified using the string "current", then the qualities associated with the current algorithm are returned.

</dd> <dt>

<span id="MCI_DGV_LIST_AUDIO_STREAM"></span><span id="mci_dgv_list_audio_stream"></span>MCI\_DGV\_LIST\_AUDIO\_STREAM
</dt> <dd>

The command should retrieve names of audio streams.

</dd> <dt>

<span id="MCI_DGV_LIST_STILL_AL"></span><span id="mci_dgv_list_still_al"></span>MCI\_DGV\_LIST\_STILL\_AL
</dt> <dd>

The command should retrieve names of still algorithms.

</dd> <dt>

<span id="MCI_DGV_LIST_STILL_QUALITY"></span><span id="mci_dgv_list_still_quality"></span>MCI\_DGV\_LIST\_STILL\_QUALITY
</dt> <dd>

The command should retrieve quality levels. The levels returned are associated with the algorithm referenced by the **lpstrAlgorithm** member of the structure identified by *lpList*. If that member is specified using the string "current", then the qualities associated with the current algorithm are returned.

</dd> <dt>

<span id="MCI_DGV_LIST_VIDEO_ALG"></span><span id="mci_dgv_list_video_alg"></span>MCI\_DGV\_LIST\_VIDEO\_ALG
</dt> <dd>

The command should retrieve names of video algorithms.

</dd> <dt>

<span id="MCI_DGV_LIST_VIDEO_QUALITY"></span><span id="mci_dgv_list_video_quality"></span>MCI\_DGV\_LIST\_VIDEO\_QUALITY
</dt> <dd>

The command should retrieve video quality levels. The levels returned are associated with the algorithm referenced by the **lpstrAlgorithm** member of the structure identified by *lpList*. If that member is specified using the string "current", then the qualities associated with the current algorithm are returned.

</dd> <dt>

<span id="MCI_DGV_LIST_VIDEO_SOURCE"></span><span id="mci_dgv_list_video_source"></span>MCI\_DGV\_LIST\_VIDEO\_SOURCE
</dt> <dd>

The command should return information about the video sources. When used with MCI\_DGV\_LIST\_COUNT, the command returns the number of video sources. When used with MCI\_DGV\_LIST\_NUMBER, the command returns the type of a video source. MCI defines the following types:

-   MCI\_DGV\_SETVIDEO\_SRC\_GENERIC
-   MCI\_DGV\_SETVIDEO\_SRC\_NTSC
-   MCI\_DGV\_SETVIDEO\_SRC\_PAL
-   MCI\_DGV\_SETVIDEO\_SRC\_RGB
-   MCI\_DGV\_SETVIDEO\_SRC\_SECAM
-   MCI\_DGV\_SETVIDEO\_SRC\_SVIDEO

There might be more than one source of each type returned. The generic source type is used when more then one type of signal is allowed for that connector.

</dd> <dt>

<span id="MCI_DGV_LIST_VIDEO_STREAM"></span><span id="mci_dgv_list_video_stream"></span>MCI\_DGV\_LIST\_VIDEO\_STREAM
</dt> <dd>

The command should retrieve names of video streams.

</dd> <dt>

<span id="MCI_DGV_LIST_NUMBER"></span><span id="mci_dgv_list_number"></span>MCI\_DGV\_LIST\_NUMBER
</dt> <dd>

An index is specified in the **dwNumber** member of the structure identified by *lpList*. The index must be an integer between 1 and the value returned for the MCI\_DGV\_LIST\_COUNT flag.

</dd> </dl>

For digital-video devices, *lpList* points to an [**MCI\_DGV\_LIST\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_list_parmsa) structure.

The following additional flags apply to the **vcr** device type:

<dl> <dt>

<span id="MCI_VCR_LIST_AUDIO_SOURCE"></span><span id="mci_vcr_list_audio_source"></span>MCI\_VCR\_LIST\_AUDIO\_SOURCE
</dt> <dd>

List audio inputs or types.

</dd> <dt>

<span id="MCI_VCR_LIST_COUNT"></span><span id="mci_vcr_list_count"></span>MCI\_VCR\_LIST\_COUNT
</dt> <dd>

Sets the **dwReturn** member of the structure identified by *lpList* to the total number of video or audio inputs.

</dd> <dt>

<span id="MCI_VCR_LIST_NUMBER"></span><span id="mci_vcr_list_number"></span>MCI\_VCR\_LIST\_NUMBER
</dt> <dd>

Sets the **dwReturn** member of the structure identified by *lpList* to the type of the video or audio input specified by the **dwNumber** member.

</dd> <dt>

<span id="MCI_VCR_LIST_VIDEO_SOURCE"></span><span id="mci_vcr_list_video_source"></span>MCI\_VCR\_LIST\_VIDEO\_SOURCE
</dt> <dd>

List video inputs or types.

</dd> </dl>

For VCR devices, *lpList* points to an [**MCI\_VCR\_LIST\_PARMS**](mci-vcr-list-parms.md) structure.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                                      |
| Header<br/>                   | <dl> <dt>Mmsystem.h (include Windows.h)</dt> </dl> |



## See also

<dl> <dt>

[MCI](mci.md)
</dt> <dt>

[MCI Commands](mci-commands.md)
</dt> </dl>

 

