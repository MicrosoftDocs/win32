---
title: MCIERR Return Values
description: MCIERR Return Values
ms.assetid: 61f7b128-b4f7-4385-9daf-e2bc9fb36e24
keywords:
- Windows multimedia,MCIERR return values
- multimedia,MCIERR return values
- multimedia reference,MCIERR return values
- reference for multimedia,MCIERR return values
- MCIERR return values,about
- mciSendCommand function
- mciSendString function
- Windows multimedia,errors
- multimedia,errors
- multimedia reference,errors
- reference for multimedia,errors
- Media Control Interface (MCI),MCIERR return values
- MCI (Media Control Interface),MCIERR return values
- reference for MCI,MCIERR return values
- MCI reference,MCIERR return values
- Media Control Interface (MCI),errors
- MCI (Media Control Interface),errors
- reference for MCI,errors
- MCI reference,errors
ms.topic: article
ms.date: 05/31/2018
---

# MCIERR Return Values

The [**mciSendCommand**](https://msdn.microsoft.com/library/Dd757160(v=VS.85).aspx) and [**mciSendString**](https://msdn.microsoft.com/library/Dd757161(v=VS.85).aspx) functions return zero if they are successful; otherwise, they return a **DWORD** value that contains one of the following error values in the low word.

-   [General MCI Errors](general-mci-errors.md)
-   [mciSendString Errors](mcisendstring-errors.md)
-   [Digital-Video Errors](digital-video-errors.md)
-   [Sequencer Errors](sequencer-errors.md)
-   [Waveform-Audio Errors](waveform-audio-errors.md)

You can obtain a description of individual return values by passing the return values to the [**mciGetErrorString**](https://msdn.microsoft.com/library/Dd757158(v=VS.85).aspx) function.

 

 




