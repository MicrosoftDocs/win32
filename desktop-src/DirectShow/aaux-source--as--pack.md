---
description: AAUX Source (AS) Pack
ms.assetid: 0e173fe5-0b9d-48e8-bcbd-403614d51558
title: AAUX Source (AS) Pack
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AAUX Source (AS) Pack

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following tables list the values used by the MSDV driver to fill in the **dwDVAAuxSrc** and **dwDVAAuxSrc1** members of the [**DVINFO**](/windows/desktop/api/strmif/ns-strmif-dvinfo) structure. For more information, see [DVINFO Field Settings in the MSDV Driver](dvinfo-field-settings-in-the-msdv-driver.md).

DVCR Settings



DV Standard

DVCR (IEC 61834)

FOURCC

dvsl

dvsd

System

525-60

625-50

525-60

625-50

LF (1)

1

1

1

1

Reserved (1)

1

1

1

1

AF SIZE (6)

00:1111

01:0000

00:1111

01:0000

SM (1)

0

0

0

0

CHN (2)

01

01

01

01

PA (1)

1

1

1

1

AUDIO MODE (4)

    Audio Block 1\*

0000

0000

0000

0000

    Audio Block 2\*

0000

0000

1111

1111

Reserved (1)

1

1

1

1

ML (1)

1

1

1

1

50/60 (1)

0

1

0

1

STYPE (5)

0:0001

0:0001

0:0000

0:0000

EF (1)

1

1

1

1

TC (1)

1

1

1

1

SMP (3)

010

010

010

010

QU (3)

001

001

001

001

AS Pack

    Audio Block 1\*

0xD1C130CF

0xD1E130D0

0xD1C030CF

0xD1E030D0

    Audio Block 2\*

0x00000000

0x00000000

0xD1C03FCF

0xD1E03FD0



 

DVCR 25 and DVCPRO 50 Settings (Planned)



DV Standard

DVCPRO (SMPTE 314M) — Planned

FOURCC

dv25

dv50

System

525-60

625-50

525-60

625-50

LF (1)

0

0

0

0

Reserved (1)

1

1

1

1

AF SIZE (6)

01:0110

01:1000

01:0110

01:1000

Reserved (1)

0

0

0

0

CHN (2)

00

00

00

00

Reserved (1)

1

1

1

1

AUDIO MODE (4)

    Audio Block 1\*

0000

0000

0000

0000

    Audio Block 2\*

0001

0001

0001

0001

Reserved (2)

11

11

11

11

50/60 (1)

0

1

0

1

STYPE (5)

0:0000

0:0000

0:0010

0:0010

Reserved (2)

11

11

11

11

SMP (3)

000

000

000

000

QU (3)

000

000

000

000

AS Pack

    Audio Block 1\*

0xC0C01056

0xC0E01058

0xC0C21056

0xC0E21058

    Audio Block 2\*

0xC0C01156

0xC0E01158

0xC0C21156

0xC0E21158



 

> [!Note]  
> \* The [**DVINFO**](/windows/desktop/api/strmif/ns-strmif-dvinfo) structure contains two AAUX AS packs, for audio blocks 1 and 2. DV50 has four audio blocks; blocks 3 and 4 are not represented in the **DVINFO** structure.

 

DVCR 100 Settings (Planned)



DV Standard

DVCPRO 100 — Planned

FOURCC

dvh1

System

1080-60i

720-60p

1080-50i

LF (1)

0

0

0

Reserved (1)

1

1

1

AF SIZE (6)

01:0110

01:0110

01:1000

Reserved (1)

0

0

0

CHN (2)

00

00

00

Reserved (1)

1

1

1

AUDIO MODE (4)

    Audio Block 1\*

0000

0000

0000

    Audio Block 2\*

0001

0001

0001

Reserved (2)

11

11

11

50/60 (1)

0

0

1

STYPE (5)

0:0011

0:0011

0:0011

Reserved (2)

11

11

11

SMP (3)

000

000

000

QU (3)

000

000

000

AS Pack

    Audio Block 1\*

0xC0C31056

0xC0C31056

0xC0D31058

    Audio Block 2\*

0xC0C31156

0xC0C31156

0xC0D31158



 

> [!Note]  
> \* DVCPRO 100 has 8 audio blocks; blocks 3 through 8 are not represented in the [DVINFO](dvinfo-field-settings-in-the-msdv-driver.md) structure.

 

## Remarks

The following field codes are of interest:

-   LF: Locked mode flag. Indicates whether the audio is locked.
    -   0 = Locked
    -   1 = Unlocked
-   AF SIZE: Audio frame size. Specifies the number of audio samples per frame.

    IEC 61834 definition:

    -   00:1111 = 1068 samples per frame
    -   01:0000 = 1280 samples per frame

    SMPTE 314M definition:

    -   01:0110 = 1602 samples per frame
    -   01:1000 = 1920 samples per frame

    Depending on the frame rate, the exact number of samples in a frame might vary. For example, NTSC is 30000/1001 frames per second (29.97 fps). With 32-kHz audio, there are about 1067.73 audio samples per frame. Thus, the nominal rate is 1068, but the actual number varies per frame. Also, with unlocked audio, the number of audio samples per frame is allowed to vary within a certain range over time.

<!-- -->

-   SM: Stereo mode.
    -   0 = Stereo
    -   1 = Mono
-   CHN: Number of audio channels per audio block.
    -   0 = One channel per audio block
    -   1 = Two channels per audio block
-   AUDIO MODE: Indicates the contents of the audio signal on each channel. The interpretation of this field depends on what values are placed in the SM and CHN fields. The definitions given below are for the values used by MSDV; refer to the specifications for more information.

    IEC 61834 definition:

    -   0000 = Ch a/c/e/g is left channel, Ch b/d/f/h is right channel
    -   1111 = no audio data

    SMPTE 314M definition:

    -   0000 = CH1 (CH3)
    -   0001 = CH2 (CH4)

-   50/60: Number of fields.
    -   0 = 60 fields
    -   1 = 50 fields
-   STYPE: System type.

    IEC 61834 definition:

    -   00000 = 525-60 or 625-50, dvsd
    -   00001 = 525-60 or 625-50, dvsl (see IEC 61883-5)

    SMPTE 314M/SPMTE 370 definition:

    -   00000 = 2 audio blocks per video frame
    -   00010 = 4 audio blocks per video frame
    -   00011 = 8 audio blocks per video frame

-   SMP: Sampling frequency.
    -   000 = 48 kHz
    -   010 = 32 kHz
-   QU: Quantization.
    -   0 = 16 bits linear
    -   1 = 12 bits non-linear

## Related topics

<dl> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> <dt>

[DVINFO Field Settings in the MSDV Driver](dvinfo-field-settings-in-the-msdv-driver.md)
</dt> </dl>

 

 



