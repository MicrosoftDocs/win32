---
description: AAUX Source Control (ASC) Pack
ms.assetid: 3df80895-81e1-42a4-a095-913e77b199e5
title: AAUX Source Control (ASC) Pack
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# AAUX Source Control (ASC) Pack

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer), [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine), and [Audio/Video Capture in Media Foundation](windows/win32/medfound/audio-video-capture-in-media-foundation). Those features have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer**, **IMFMediaEngine** and **Audio/Video Capture in Media Foundation** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following tables list the values used by the MSDV driver to fill in the **dwDVAAuxCtl** and

**dwDVAAuxCtl1** members of the [**DVINFO**](/windows/desktop/api/strmif/ns-strmif-dvinfo) structure. For more information, see [DVINFO Field Settings in the MSDV Driver](dvinfo-field-settings-in-the-msdv-driver.md).

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

CGMS (2)

00

00

00

00

ISR (2)

11

11

11

11

CMP (2)

11

11

11

11

SS (2)

11

11

11

11

REC ST (1)

1

1

1

1

REC END (1)

1

1

1

1

REC MODE (3)

001

001

001

001

INSERT CH (3)

111

111

111

111

DRF (1)

1

1

1

1

SPEED (7)

010:0000

010:0000

010:0000

010:0000

Reserved (1)

1

1

1

1

GENRE (7)

111:1111

111:1111

111:1111

111:1111

ASC Pack (both audio blocks)\*

0xFFA0CF3F

0xFFA0CF3F

0xFFA0CF3F

0xFFA0CF3F



 

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

CGMS (2)

00

00

00

00

Reserved (4)

1111

1111

1111

1111

EFC (2)

00

00

00

00

REC ST (1)

1

1

1

1

REC END (1)

1

1

1

1

FADE ST (1)

1

1

1

1

FADE END (1)

1

1

1

1

Reserved (4)

1111

1111

1111

1111

DRF (1)

1

1

1

1

SPEED (7)

111:1000

110:0100

111:1000

110:0100

Reserved (8)

1111:1111

1111:1111

1111:1111

1111:1111

ASC Pack (both audio blocks)\*

0xFFA0CF3F

0xFFA0CF3F

0xFFA0CF3F

0xFFA0CF3F



 

\* The *DVINFO* structure contains two AAUX AS packs, for audio blocks 1 and 2. DV50 has four audio blocks; blocks 3 and 4 are not represented in the *DVINFO* structure.

DVCR 100 Settings (Planned)



DV Standard

DVCPRO 100 — Planned

FOURCC

dvh1

System

1080-60i

720-60p

1080-50i

CGMS (2)

00

00

00

Reserved (4)

1111

1111

1111

EFC (2)

00

00

00

REC ST (1)

1

1

1

REC END (1)

1

1

1

FADE ST (1)

1

1

1

FADE END (1)

1

1

1

Reserved (4)

1111

1111

1111

DRF (1)

1

1

1

SPEED (7)

111:1000

111:1000

110:0100

Reserved (8)

1111:1111

1111:1111

1111:1111

ASC Pack (both audio blocks)\*

0xFFF8FF3C

0xFFF8FF3C

0xFFE4FF3C



 

\* DVCPRO 100 has 8 audio blocks; blocks 3 through 8 are not represented in the *DVINFO* structure.

## Remarks

The following field codes are of interest:

-   **CGMS**: Copy generation management system. 0 = copying permitted without restriction.

    The actual ASC packs in the DV stream may contain different values.

<!-- -->

-   **REC MODE**: Recording mode. 1 = Original
-   **SPEED**: VTR playback speed.

    IEC 61834 definition:

    -   010:0000 = normal speed, 525-60 or 625-50

    SMPTE 314M definition:

    -   111:1000 = normal speed, 525-60
    -   110:0100 = normal speed, 625-50

## Related topics

<dl> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> <dt>

[DVINFO Field Settings in the MSDV Driver](dvinfo-field-settings-in-the-msdv-driver.md)
</dt> </dl>

 

 



