---
title: Configuring Web Streams
description: Configuring Web Streams
ms.assetid: 1eeb6243-5095-4dba-994c-2083beda7b78
keywords:
- streams,configuring Web streams
- codecs,configuring Web streams
- Web streams,configuring
ms.topic: article
ms.date: 05/31/2018
---

# Configuring Web Streams

Web streams are a specialized type of file transfer stream used to deliver the files associated with a Web site in a single stream. Web stream configuration is summarized in the following table.



| Setting                                            | Description                                                                       |
|----------------------------------------------------|-----------------------------------------------------------------------------------|
| **WM\_MEDIA\_TYPE.majortype**                      | Set to WMMEDIATYPE\_FileTransfer.                                                 |
| **WM\_MEDIA\_TYPE.subtype**                        | Set to WMMEDIASUBTYPE\_WebStream.                                                 |
| **WM\_MEDIA\_TYPE.bFixedSizeSamples**              | Set to False.                                                                     |
| **WM\_MEDIA\_TYPE.bTemporalCompression**           | Set to True.                                                                      |
| **WM\_MEDIA\_TYPE.lSampleSize**                    | Set to 0.                                                                         |
| **WM\_MEDIA\_TYPE.formattype**                     | Set to WMFORMAT\_WebStream.                                                       |
| **WM\_MEDIA\_TYPE.pUnk**                           | Set to **NULL**.                                                                  |
| **WM\_MEDIA\_TYPE.cbFormat**                       | Set to `sizeof(WMT_WEBSTREAM_FORMAT)`.                                            |
| **WM\_MEDIA\_TYPE.pbFormat**                       | Set to the address of a properly configured **WMT\_WEBSTREAM\_FORMAT** structure. |
| **WMT\_WEBSTREAM\_FORMAT.cbSampleHeaderFixedData** | Set to `sizeof(WMT_WEBSTREAM_SAMPLE_HEADER)`.                                     |
| **WMT\_WEBSTREAM\_FORMAT.wVersion**                | Set to 1.                                                                         |
| **WMT\_WEBSTREAM\_FORMAT.wreserved**               | Set to 0.                                                                         |



 

## Related topics

<dl> <dt>

[**Configuration Common to All Streams**](configuration-common-to-all-streams.md)
</dt> <dt>

[**Configuring Arbitrary Stream Types**](configuring-arbitrary-stream-types.md)
</dt> <dt>

[**Web Streams**](web-streams.md)
</dt> </dl>

 

 




