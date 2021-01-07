---
description: VAUX Source (VS) Pack
ms.assetid: 5ffd2883-0e56-459f-b229-cc014b894237
title: VAUX Source (VS) Pack
ms.topic: article
ms.date: 05/31/2018
---

# VAUX Source (VS) Pack

The following tables list the values used by the MSDV driver to fill in the **dwDVVAuxSrc** member of the [**DVINFO**](/windows/desktop/api/strmif/ns-strmif-dvinfo) structure. For more information, see [DVINFO Field Settings in the MSDV Driver](dvinfo-field-settings-in-the-msdv-driver.md).

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

TV CHANNEL (8)

1111:1111

1111:1111

1111:1111

1111:1111

B/W (1)

1

1

1

1

EN (1)

1

1

1

1

CLF (2)

11

11

11

11

TV CHANNEL (4)

1111

1111

1111

1111

SOURCE CODE (2)

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

0:0001

0:0001

0:0000

0:0000

TUNER CATEGORY (8)

1111:1111

1111:1111

1111:1111

1111:1111

VS Pack

0xFFC1FFFF

0xFFE1FFFF

0xFFC0FFFF

0xFFE0FFFF



 

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

Reserved (8)

1111:1111

1111:1111

1111:1111

1111:1111

B/W (1)

1

1

1

1

EN (1)

1

1

1

1

CLF (2)

11

11

11

11

Reserved (4)

1111

1111

1111

1111

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

0:0100

0:0100

VISC (8)

1111:1111

1111:1111

1111:1111

1111:1111

VS Pack

0x7FC0FFFF

0x7FE0FFFF

0x7FC4FFFF

0x7FE4FFFF



 

**DVCR 100 Settings (Planned)**



DV Standard

DVCPRO 100 — Planned

FOURCC

dvh1

System

1080-60i

720-60p

1080-50i

Reserved (8)

1111:1111

1111:1111

1111:1111

B/W (1)

1

1

1

EN (1)

1

1

1

CLF (2)

11

11

11

Reserved (4)

1111

1111

1111

Reserved (2)

11

11

11

50/60 (1)

0

0

1

STYPE (5)

1:0100

1:1000

1:0100

VISC (8)

1111:1111

1111:1111

1111:1111

VS Pack

0x7FD4FFFF

0x7FD8FFFF

0x7FF4FFFF



 

## Remarks

The following field codes are of interest:

-   **B/W**: Black and white flag. 1 = color.
-   **50/60**: Number of fields.
    -   0 = 60 fields
    -   1 = 50 fields
-   **STYPE**: Signal type.

    IEC 61834 definition:

    -   0:0000 = 525-60 or 625-50, dvsd
    -   0:0001 = 525-60 or 625-50, dvsl (as defined in IEC 61883-5)

    SMPTE 314M definition:

    -   0:0000 = 4:1:1 compression
    -   0:0100 = 4:2:2 compression

    SMPTE 370 definition:

    -   1:0100 = 1080/60i (60 Hz) or 1080/50i (50 Hz)
    -   1:1000 = 720/60p

## Related topics

<dl> <dt>

[Digital Video in DirectShow](digital-video-in-directshow.md)
</dt> <dt>

[DVINFO Field Settings in the MSDV Driver](dvinfo-field-settings-in-the-msdv-driver.md)
</dt> </dl>

 

 



