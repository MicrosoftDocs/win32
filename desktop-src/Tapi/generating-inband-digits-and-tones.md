---
description: After a call is in the connected state, information can be transmitted over it.
ms.assetid: a2afa7e9-c625-48ec-920b-0ae8c3e1b395
title: Generating Inband Digits and Tones
ms.topic: article
ms.date: 05/31/2018
---

# Generating Inband Digits and Tones

After a call is in the *connected* state, information can be transmitted over it. Two functions are provided that allow end-to-end inband signaling between the application and remote station equipment such as an answering machine. One function is [**lineGenerateDigits**](/windows/desktop/api/Tapi/nf-tapi-linegeneratedigits), which generates inband digits on a call, signaling them over the voice channel. Digits can be signaled as either rotary/pulse sequences or as DTMF tones. The other function is [**lineGenerateTone**](/windows/desktop/api/Tapi/nf-tapi-linegeneratetone), which enables the application to generate one of a variety of multifrequency tones inband (over the media stream). This generates telephony tones, such as ringback, beep, and busy, as well as arbitrary multifrequency, multicadenced tones.

Only one digit or tone generation can be in progress on a call at any one time. When digit or tone generation completes, a [**LINE\_GENERATE**](line-generate.md) message is sent to the application that requested the generation. In the case where multiple digits are generated, only a single message is sent back after all digits have been generated. Calling [**lineGenerateDigits**](/windows/desktop/api/Tapi/nf-tapi-linegeneratedigits) or [**lineGenerateTone**](/windows/desktop/api/Tapi/nf-tapi-linegeneratetone) while digit or tone generation is in progress will abort the generation currently in progress and send the LINE\_GENERATE message to the application whose generation was aborted with a cancel indication.

 

 



