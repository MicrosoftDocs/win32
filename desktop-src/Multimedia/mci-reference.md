---
title: MCI Reference
description: MCI Reference
ms.assetid: e7cedfc2-ce01-481c-a431-c93c97d45baf
keywords:
- MCI reference,about
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# MCI Reference

\[The feature associated with this page, [MCI](/windows/win32/multimedia/mci), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer). **MediaPlayer** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** instead of **MCI**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

This section lists the MCI functions, structures, messages, macros, commands, and command strings, which are documented under [Multimedia Reference](multimedia-reference.md). These elements are grouped as follows.

## Notifications

-   [**MM\_MCINOTIFY**](mm-mcinotify.md)
-   [**MM\_MCISIGNAL**](mm-mcisignal.md)

## Getting Information

-   [**mciGetCreatorTask**](/previous-versions//dd757155(v=vs.85))
-   [**mciGetDeviceID**](/previous-versions//dd757156(v=vs.85))
-   [**mciGetDeviceIDFromElementID**](/previous-versions//dd757157(v=vs.85))
-   [**mciGetErrorString**](/previous-versions//dd757158(v=vs.85))

## Sending Commands

-   [**mciExecute**](/previous-versions//dd757154(v=vs.85))
-   [**mciSendCommand**](/previous-versions//dd757160(v=vs.85))
-   [**mciSendString**](/previous-versions//dd757161(v=vs.85))

## Time Formats

-   [**MCI\_HMS\_HOUR**](mci-hms-hour.md)
-   [**MCI\_HMS\_MINUTE**](mci-hms-minute.md)
-   [**MCI\_HMS\_SECOND**](mci-hms-second.md)
-   [**MCI\_MAKE\_HMS**](mci-make-hms.md)
-   [**MCI\_MAKE\_MSF**](mci-make-msf.md)
-   [**MCI\_MAKE\_TMSF**](mci-make-tmsf.md)
-   [**MCI\_MSF\_FRAME**](/previous-versions//dd743438(v=vs.85))
-   [**MCI\_MSF\_MINUTE**](mci-msf-minute.md)
-   [**MCI\_MSF\_SECOND**](mci-msf-second.md)
-   [**MCI\_TMSF\_FRAME**](mci-tmsf-frame.md)
-   [**MCI\_TMSF\_MINUTE**](mci-tmsf-minute.md)
-   [**MCI\_TMSF\_SECOND**](mci-tmsf-second.md)
-   [**MCI\_TMSF\_TRACK**](mci-tmsf-track.md)

## Yield Procedures

-   [**mciGetYieldProc**](/previous-versions//dd757159(v=vs.85))
-   [**mciSetYieldProc**](/previous-versions//dd757163(v=vs.85))

## Configuring a Device

-   [**break**](break.md)
-   [**configure**](configure.md)
-   [escape](escape.md)
-   [**index**](./windows-multimedia-start-page.md)
-   [**MCI\_BREAK**](mci-break.md)
-   [**MCI\_BREAK\_PARMS**](mci-break-parms.md)
-   [**MCI\_CONFIGURE**](mci-configure.md)
-   [**MCI\_DGV\_SET\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_set_parms)
-   [**MCI\_DGV\_SETAUDIO\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_setaudio_parmsa)
-   [**MCI\_DGV\_SETVIDEO\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_setvideo_parmsa)
-   [**MCI\_ESCAPE**](mci-escape.md)
-   [**MCI\_INDEX**](mci-index.md)
-   [**MCI\_SEQ\_SET\_PARMS**](mci-seq-set-parms.md)
-   [**MCI\_SET**](mci-set.md)
-   [**MCI\_SET\_PARMS**](mci-set-parms.md)
-   [**MCI\_SETAUDIO**](mci-setaudio.md)
-   [**MCI\_SETTIMECODE**](mci-settimecode.md)
-   [**MCI\_SETTUNER**](mci-settuner.md)
-   [**MCI\_SETVIDEO**](mci-setvideo.md)
-   [**MCI\_SPIN**](mci-spin.md)
-   [**MCI\_VCR\_SET\_PARMS**](mci-vcr-set-parms.md)
-   [**MCI\_VCR\_SETAUDIO\_PARMS**](mci-vcr-setaudio-parms.md)
-   [**MCI\_VCR\_SETTUNER\_PARMS**](mci-vcr-settuner-parms.md)
-   [**MCI\_VCR\_SETVIDEO\_PARMS**](mci-vcr-setvideo-parms.md)
-   [**MCI\_VD\_ESCAPE\_PARMS**](mci-vd-escape-parms.md)
-   [**MCI\_WAVE\_SET\_PARMS**](mci-wave-set-parms.md)
-   [**set**](set.md)
-   [**setaudio**](setaudio.md)
-   [**settimecode**](settimecode.md)
-   [**settuner**](settuner.md)
-   [**setvideo**](setvideo.md)
-   [**spin**](spin.md)

## Controlling Playback

-   [**freeze**](freeze.md)
-   [**load**](load.md)
-   [**MCI\_DGV\_FREEZE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_rect_parms)
-   [**MCI\_DGV\_LOAD\_PARMS**](/previous-versions//dd743391(v=vs.85))
-   [**MCI\_DGV\_PAUSE\_PARMS**](/previous-versions//dd743395(v=vs.85))
-   [**MCI\_DGV\_PLAY\_PARMS**](/previous-versions//dd743396(v=vs.85))
-   [**MCI\_DGV\_RESUME\_PARMS**](/previous-versions//dd743403(v=vs.85))
-   [**MCI\_DGV\_STOP\_PARMS**](/previous-versions//dd743411(v=vs.85))
-   [**MCI\_FREEZE**](mci-freeze.md)
-   [**MCI\_LOAD**](mci-load.md)
-   [**MCI\_LOAD\_PARMS**](mci-load-parms.md)
-   [**MCI\_OVLY\_LOAD\_PARMS**](mci-ovly-load-parms.md)
-   [**MCI\_PAUSE**](mci-pause.md)
-   [**MCI\_PLAY**](mci-play.md)
-   [**MCI\_PLAY\_PARMS**](mci-play-parms.md)
-   [**MCI\_RESUME**](mci-resume.md)
-   [**MCI\_STOP**](mci-stop.md)
-   [**MCI\_UNFREEZE**](mci-unfreeze.md)
-   [**MCI\_VCR\_PLAY\_PARMS**](mci-vcr-play-parms.md)
-   [**MCI\_VD\_PLAY\_PARMS**](mci-vd-play-parms.md)
-   [**pause**](pause.md)
-   [**play**](play.md)
-   [**resume**](resume.md)
-   [**stop**](stop.md)
-   [**unfreeze**](unfreeze.md)

## Controlling the Position

-   [**cue**](cue.md)
-   [**mark**](mark.md)
-   [**MCI\_CUE**](mci-cue.md)
-   [**MCI\_DGV\_CUE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_cue_parms)
-   [**MCI\_DGV\_SIGNAL\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_signal_parms)
-   [**MCI\_DGV\_STEP\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_step_parms)
-   [**MCI\_MARK**](mci-mark.md)
-   [**MCI\_SEEK**](mci-seek.md)
-   [**MCI\_SEEK\_PARMS**](mci-seek-parms.md)
-   [**MCI\_SIGNAL**](mci-signal.md)
-   [**MCI\_STEP**](mci-step.md)
-   [**MCI\_VCR\_CUE\_PARMS**](mci-vcr-cue-parms.md)
-   [**MCI\_VCR\_SEEK\_PARMS**](mci-vcr-seek-parms.md)
-   [**MCI\_VCR\_STEP\_PARMS**](mci-vcr-step-parms.md)
-   [**MCI\_VD\_STEP\_PARMS**](mci-vd-step-parms.md)
-   [**seek**](seek.md)
-   [**signal**](signal.md)
-   [**step**](step.md)

## Editing

-   [**copy**](copy.md)
-   [**cut**](cut.md)
-   [**delete**](delete.md)
-   [**MCI\_COPY**](mci-copy.md)
-   [**MCI\_CUT**](mci-cut.md)
-   [**MCI\_DELETE**](mci-delete.md)
-   [**MCI\_DGV\_COPY\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_copy_parms)
-   [**MCI\_DGV\_CUT\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_cut_parms)
-   [**MCI\_DGV\_DELETE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_delete_parms)
-   [**MCI\_DGV\_PASTE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_paste_parms)
-   [**MCI\_PASTE**](mci-paste.md)
-   [**MCI\_UNDO**](mci-undo.md)
-   [**MCI\_WAVE\_DELETE\_PARMS**](mci-wave-delete-parms.md)
-   [**paste**](paste.md)
-   [**undo**](undo.md)

## Miscellaneous

-   [**MCI\_GENERIC\_PARMS**](mci-generic-parms.md)

## Opening and Closing

-   [**close**](close.md)
-   [**MCI\_CLOSE**](mci-close.md)
-   [**MCI\_DGV\_OPEN\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_open_parmsa)
-   [**MCI\_OPEN**](mci-open.md)
-   [**MCI\_OPEN\_PARMS**](mci-open-parms.md)
-   [**MCI\_OVLY\_OPEN\_PARMS**](mci-ovly-open-parms.md)
-   [**MCI\_WAVE\_OPEN\_PARMS**](mci-wave-open-parms.md)
-   [**open**](open.md)

## Realizing a Palette

-   [**MCI\_REALIZE**](mci-realize.md)
-   [**realize**](realize.md)

## Repainting a Frame

-   [**MCI\_DGV\_UPDATE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_update_parms)
-   [**MCI\_UPDATE**](mci-update.md)
-   [**update**](update.md)

## Retrieving Information

-   [**capability**](capability.md)
-   [**info**](info.md)
-   [**list**](list.md)
-   [**MCI\_DGV\_INFO\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_info_parmsa)
-   [**MCI\_DGV\_LIST\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_list_parmsa)
-   [**MCI\_DGV\_STATUS\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_status_parmsa)
-   [**MCI\_GETDEVCAPS**](mci-getdevcaps.md)
-   [**MCI\_GETDEVCAPS\_PARMS**](mci-getdevcaps-parms.md)
-   [**MCI\_INFO**](mci-info.md)
-   [**MCI\_INFO\_PARMS**](mci-info-parms.md)
-   [**MCI\_LIST**](mci-list.md)
-   [**MCI\_STATUS**](mci-status.md)
-   [**MCI\_STATUS\_PARMS**](mci-status-parms.md)
-   [**MCI\_SYSINFO**](mci-sysinfo.md)
-   [**MCI\_SYSINFO\_PARMS**](mci-sysinfo-parms.md)
-   [**MCI\_VCR\_LIST\_PARMS**](mci-vcr-list-parms.md)
-   [**MCI\_VCR\_STATUS\_PARMS**](mci-vcr-status-parms.md)
-   [**status**](status.md)
-   [sysinfo](sysinfo.md)

## Saving

-   [**MCI\_DGV\_RECORD\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_record_parms)
-   [**MCI\_DGV\_SAVE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_save_parmsa)
-   [**MCI\_OVLY\_SAVE\_PARMS**](/previous-versions//dd743447(v=vs.85))
-   [**MCI\_RECORD**](mci-record.md)
-   [**MCI\_RECORD\_PARMS**](mci-record-parms.md)
-   [**MCI\_SAVE**](mci-save.md)
-   [**MCI\_SAVE\_PARMS**](mci-save-parms.md)
-   [**MCI\_VCR\_RECORD\_PARMS**](mci-vcr-record-parms.md)
-   [**record**](record.md)
-   [**save**](save.md)

## Video Control

-   [**capture**](capture.md)
-   [**MCI\_CAPTURE**](mci-capture.md)
-   [**MCI\_DGV\_MONITOR\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_monitor_parms)
-   [**MCI\_DGV\_QUALITY\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_quality_parmsa)
-   [**MCI\_DGV\_RESERVE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_reserve_parmsa)
-   [**MCI\_DGV\_RESTORE\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_restore_parmsa)
-   [**MCI\_MONITOR**](mci-monitor.md)
-   [**MCI\_QUALITY**](mci-quality.md)
-   [**MCI\_RESERVE**](mci-reserve.md)
-   [**MCI\_RESTORE**](mci-restore.md)
-   [**monitor**](monitor.md)
-   [**quality**](quality.md)
-   [**reserve**](reserve.md)
-   [**restore**](restore.md)

## Window or Display Rectangles

-   [**MCI\_DGV\_PUT\_PARMS**](/previous-versions//dd743397(v=vs.85))
-   [**MCI\_DGV\_RECT\_PARMS**](/windows/win32/api/digitalv/ns-digitalv-mci_dgv_rect_parms)
-   [**MCI\_DGV\_WINDOW\_PARMS**](/windows/desktop/api/Digitalv/ns-digitalv-mci_dgv_window_parmsa)
-   [**MCI\_OVLY\_RECT\_PARMS**](mci-ovly-rect-parms.md)
-   [**MCI\_OVLY\_WINDOW\_PARMS**](mci-ovly-window-parms.md)
-   [**MCI\_PUT**](mci-put.md)
-   [**MCI\_WHERE**](mci-where.md)
-   [**MCI\_WINDOW**](mci-window.md)
-   [**put**](put.md)
-   [**where**](where.md)
-   [**window**](window.md)

## Related topics

<dl> <dt>

[MCI](mci.md)
</dt> </dl>

 

 