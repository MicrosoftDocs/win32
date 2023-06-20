---
description: VAUX Source Control (VSC) Pack
ms.assetid: 9d5dd89e-9084-409d-86c0-30b57645d33d
title: VAUX Source Control (VSC) Pack
ms.topic: article
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# VAUX Source Control (VSC) Pack

\[The feature associated with this page, [DirectShow](/windows/win32/directshow/directshow), is a legacy feature. It has been superseded by [MediaPlayer](/uwp/api/Windows.Media.Playback.MediaPlayer) and [IMFMediaEngine](/windows/win32/api/mfmediaengine/nn-mfmediaengine-imfmediaengine). **MediaPlayer** and **IMFMediaEngine** have been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **MediaPlayer** and **IMFMediaEngine** instead of **DirectShow**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

The following tables list the values used by the MSDV driver to fill in the **dwDVVAuxCtl** member of the [**DVINFO**](/windows/desktop/api/strmif/ns-strmif-dvinfo) structure. For more information, see [DVINFO Field Settings in the MSDV Driver](dvinfo-field-settings-in-the-msdv-driver.md).

**DVCR Settings**



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

Reserved (1)

1

1

1

1

REC MODE (2)

00

00

00

00

Reserved (1)

1

1

1

1

DISP (3)

000

000

000

000

FF (1)

1

1

1

1

FS (1)

1

1

1

1

FC (1)

1

1

1

1

IL (1)

1

1

1

1

ST (1)

1

1

1

1

SC (1)

1

1

1

1

BCSYS (2)

00

01

00

01

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

VSC Pack

0xFFFCC83F

0xFFFDC83F

0xFFFCC83F

0xFFFDC83F



 

**DVCPRO 25 and DVCPRO 50 Settings (Planned)**



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

Reserved (6)

11:1111

11:1111

11:1111

11:1111

Reserved (2)

11

11

11

11

Reserved (2)

00

00

00

00

Reserved (1)

1

1

1

1

DISP (3)

000

000

000

000

FF (1)

1

1

1

1

FS (1)

1

1

1

1

FC (1)

1

1

1

1

IL (1)

1

1

1

1

Reserved (2)

11

11

11

11

Reserved (2)

00

00

00

00

Reserved (8)

1111:1111

1111:1111

1111:1111

1111:1111

VSC Pack

0xFFFCC83F

0xFFFCC83F

0xFFFCC83F

0xFFFCC83F



 

**DVCPRO 100 Settings (Planned)**



DV Standard

DVCPRO 100 — Planned

FOURCC

dvh1

System

1080-60i

720p-60p

1080-50i

CGMS (2)

00

00

00

Reserved (6)

11:1111

11:1111

11:1111

Reserved (2)

11

11

11

Reserved (2)

00

00

00

Reserved (1)

1

1

1

DISP (3)

010

010

010

FF (1)

1

1

1

FS (1)

1

1

1

FC (1)

1

1

1

IL (1)

1

1

1

Reserved (2)

11

11

11

Reserved (2)

00

00

00

Reserved (8)

1111:1111

1111:1111

1111:1111

VSC Pack

0xFFFCCA3F

0xFFFCCA3F

0xFFFCCA3F



 

## Remarks

The following field codes are of interest:

-   **CGMS**: Copy generation management system. 0 = copying permitted without restriction.

    The actual VSC packs in the DV stream may contain different values.

<!-- -->

-   **REC MODE**: Recording mode. 1 = Original.
-   **DISP**: Display select mode. 000 = 4:3 aspect ratio, full format; 010 = 16:9 aspect ratio.
-   **BCSYS**: Broadcast system. This field defines the type of wide screen signaling information.
    -   0 = type 0 (see IEC 61880)
    -   1 = type 1 (see ETSI EN 300 294)

## Related topics

<dl> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> <dt>

[DVINFO Field Settings in the MSDV Driver](dvinfo-field-settings-in-the-msdv-driver.md)
</dt> </dl>

 

 



